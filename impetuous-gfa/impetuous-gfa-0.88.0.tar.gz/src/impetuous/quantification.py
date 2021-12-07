"""
Copyright 2021 RICHARD TJÖRNHAMMAR

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import numpy as np
import pandas as pd
from impetuous.convert import create_synonyms , flatten_dict
from scipy.stats import rankdata
from scipy.stats import ttest_rel , ttest_ind , mannwhitneyu
from scipy.stats.mstats import kruskalwallis as kruskwall
from sklearn.decomposition import PCA
import itertools
import typing

def SubArraysOf ( Array,Array_=None ) :
    if Array_ == None :
        Array_ = Array[:-1]
    if Array == [] :
        if Array_ == [] :
            return ( [] )
        return( SubArraysOf(Array_,Array_[:-1]) )
    return([Array]+SubArraysOf(Array[1:],Array_))

def permuter( inputs , n ) :
    # permuter( inputs = ['T2D','NGT','Female','Male'] , n = 2 )
    return( [p[0] for p in zip(itertools.permutations(inputs,n))] )

def grouper ( inputs, n ) :
    iters = [iter(inputs)] * n
    return zip ( *iters )

def whiten_data ( Xdf ) :
    # REMEMBER BOYS AND GIRLS THIS IS SOMETHING YOU MIGHT NOT WANT TO DO :)
    mean_center = lambda x: x-np.mean(x,0)
    X = Xdf.values
    u , s , v = np.linalg.svd( mean_center(X),full_matrices=False )
    X_white = np.dot(X,np.dot( np.diag(s**-1),np.abs(v) )) # we don't know the sign
    return ( pd.DataFrame( X_white,index=Xdf.index.values,columns=Xdf.columns ) )

def threshold ( E , A ) :
    if not 'pandas' in str(type(A)) or not 'pandas' in str(type(E)):
        print ( "ERROR MUST SUPPLY TWO PANDAS DATAFRAMES" )
        return ( -1 )
    thresholds_df = pd .DataFrame ( np.dot( E,A.T ) ,
                          columns = A .index ,
                          index   = E .index ) .apply ( lambda x:x/np.sum(E,1) )
    return ( thresholds_df )

def solve ( C = pd.DataFrame([ [10,1],[3,5] ]) ,
            E = pd.DataFrame([ [25],[31] ]) ):
    if not 'pandas' in str(type(C)) or not 'pandas' in str(type(E)):
        print ( "ERROR MUST SUPPLY TWO PANDAS DATAFRAMES" )
        return ( -1 )
    recover = lambda U,S,Vt : np.dot(U*S,Vt)
    cU, cS, cVt = np.linalg.svd(C, full_matrices=False )
    cST   = 1/cS
    psuedo_inverse = pd.DataFrame( recover(cVt.T,cST,cU.T) , index=C.columns ,columns=C.index )
    identity  = np.dot(C,psuedo_inverse)
    TOLERANCE = np.max( np.sqrt( ( identity * ( ( 1-np.eye(len(np.diag(identity)))) ) )**2 ))
    return ( np.dot( psuedo_inverse,E),TOLERANCE )

import re
def find_category_variables( istr ) :
    return ( re.findall( r'C\((.*?)\)', istr ) )

def encode_categorical( G = ['Male','Male','Female'] ):
    #
    # CREATES AN BINARY ENCODING MATRIX FROM THE SUPPLIED LIST
    # USES A PANDAS DATAFRAME AS INTERMEDIATE FOR ERROR CHECKING
    # THIS PUTS THE O IN OPLS (ORTHOGONAL)
    #
    ugl = list(set(G)) ; n = len(ugl) ; m = len(G)
    lgu = { u:j for u,j in zip(ugl,range(n)) }
    enc_d = pd.DataFrame( np.zeros(m*n).reshape(-1,n),columns=ugl )
    for i in range ( m ) :
        j = lgu[G[i]]
        enc_d.iloc[i,j] = 1
    return ( enc_d )

def create_encoding_journal( use_categories, journal_df ) :
    encoding_df = None
    for category in use_categories :
        catvals = journal_df.loc[category].to_list()
        cat_encoding = encode_categorical( catvals )
        cat_encoding.index = journal_df.columns.values
        if encoding_df is None :
            encoding_df = cat_encoding.T
        else :
            encoding_df = pd.concat([encoding_df,cat_encoding.T])
    return ( encoding_df )

def quantify_density_probability ( rpoints , cutoff = None ) :
    #
    # DETERMINE P VALUES
    loc_pdf = lambda X,mean,variance : [ 1./np.sqrt(2.*np.pi*variance)*np.exp(-((x-mean)/(2.*variance))**2) for x in X ]
    from scipy.special import erf as erf_
    loc_cdf = lambda X,mean,variance : [      0.5*( 1. + erf_(  (x-mean)/np.sqrt( 2.*variance ) ) ) for x in X ]
    loc_Q   = lambda X,mean,variance : [ 1. - 0.5*( 1. + erf_(  (x-mean)/np.sqrt( 2.*variance ) ) ) for x in X ]
    M_,Var_ = np.mean(rpoints),np.std(rpoints)**2
    #
    # INSTEAD OF THE PROBABILTY DENSITY WE RETURN THE FRACTIONAL RANKS
    # SINCE THIS ALLOWS US TO CALCULATE RANK STATISTICS FOR THE PROJECTION
    corresponding_density = rankdata (rpoints,'average') / len(rpoints) # loc_pdf( rpoints,M_,Var_ )
    corresponding_pvalue  = loc_Q  ( rpoints,M_,Var_ )
    #
    # HERE WE MIGHT BE DONE
    if not cutoff is None :
        resolution = 10. ; nbins = 100.
        #
        # ONLY FOR ASSESING
        h1,h2      = np.histogram(rpoints,bins=int(np.ceil(len(rpoints)/resolution)))
        bin_radius = 0.5 * ( h2[1:] + h2[:-1] )
        radial_density = np.cumsum( h1 )/np.sum( h1 ) # lt
        #
        # NOW RETRIEVE ALL DENSITIES OF THE RADII
        tol = 1./nbins
        corresponding_radius = np.min( bin_radius[radial_density > cutoff/nbins] )
        return ( corresponding_pvalue , corresponding_density, corresponding_radius )
    return ( corresponding_pvalue , corresponding_density )

def find_category_interactions ( istr ) :
    all_cats = re.findall( r'C\((.*?)\)', istr )
    interacting = [ ':' in c for c in istr.split(')') ][ 0:len(all_cats) ]
    interacting_categories = [ [all_cats[i-1],all_cats[i]] for i in range(1,len(interacting)) if interacting[i] ]
    return ( interacting_categories )

def create_encoding_data_frame ( journal_df , formula , bVerbose = False ) :
    #
    # THE JOURNAL_DF IS THE COARSE GRAINED DATA (THE MODEL)
    # THE FORMULA IS THE SEMANTIC DESCRIPTION OF THE PROBLEM
    #
    interaction_pairs = find_category_interactions ( formula.split('~')[1] )
    add_pairs = []
    sjdf = set(journal_df.index)
    if len( interaction_pairs ) > 0 :
        for pair in interaction_pairs :
            cpair = [ 'C('+p+')' for p in pair ]
            upair = [ pp*(pp in sjdf)+cp*(cp in sjdf and not pp in sjdf) for (pp,cp) in zip( pair,cpair) ]
            journal_df.loc[ ':'.join(upair) ] = [ p[0]+'-'+p[1] for p in journal_df.loc[ upair,: ].T.values ]
            add_pairs.append(':'.join(upair))
    use_categories = list(set(find_category_variables(formula.split('~')[1])))
    cusecats = [ 'C('+p+')' for p in use_categories ]
    use_categories = [ u*( u in sjdf) + cu *( cu in sjdf ) for (u,cu) in zip(use_categories,cusecats) ]
    use_categories = [ *use_categories,*add_pairs ]
    #
    if len( use_categories )>0 :
        encoding_df = create_encoding_journal ( use_categories , journal_df ).T
    else :
        encoding_df = None
    #
    if bVerbose :
        print ( [ v for v in encoding_df.columns.values ] )
        print ( 'ADD IN ANY LINEAR TERMS AS THEIR OWN AXIS' )
    #
    # THIS TURNS THE MODEL INTO A MIXED LINEAR MODEL
    add_df = journal_df.loc[ [c.replace(' ','') for c in formula.split('~')[1].split('+') if not 'C('in c],: ]
    if len(add_df)>0 :
        if encoding_df is None :
            encoding_df = add_df.T
        else :
            encoding_df = pd.concat([ encoding_df.T ,
                            journal_df.loc[ [ c.replace(' ','') for c in formula.split('~')[1].split('+') if not 'C(' in c] , : ] ]).T
    return ( encoding_df.apply(pd.to_numeric) )


def interpret_problem ( analyte_df , journal_df , formula , bVerbose=False ) :
    #
    # THE JOURNAL_DF IS THE COARSE GRAINED DATA (THE MODEL)
    # THE ANALYTE_DF IS THE   FINE GRAINED DATA  (THE DATA)
    # THE FORMULA IS THE SEMANTIC DESCRIPTION OF THE PROBLEM
    #
    interaction_pairs = find_category_interactions ( formula.split('~')[1] )
    add_pairs = []
    if len( interaction_pairs )>0 :
        for pair in interaction_pairs :
            journal_df.loc[ ':'.join(pair) ] = [ p[0]+'-'+p[1] for p in journal_df.loc[ pair,: ].T.values ]
            add_pairs.append(':'.join(pair))
    use_categories = list(set(find_category_variables(formula.split('~')[1])))
    use_categories =  [u for u in use_categories if 'C('+u+')' in set(formula.replace(' ','').split('~')[1].split('+'))]
    use_categories = [ *use_categories,*add_pairs ]
    #
    if len( use_categories )>0 :
        encoding_df = create_encoding_journal ( use_categories , journal_df ).T
    else :
        encoding_df = None
    #
    if bVerbose :
        print ( [ v for v in encoding_df.columns.values ] )
        print ( 'ADD IN ANY LINEAR TERMS AS THEIR OWN AXIS' )
    #
    # THIS TURNS THE MODEL INTO A MIXED LINEAR MODEL
    add_df = journal_df.loc[ [c.replace(' ','') for c in formula.split('~')[1].split('+') if not 'C('in c],: ]
    if len(add_df)>0 :
        if encoding_df is None :
            encoding_df = add_df.T
        else :
            encoding_df = pd.concat([ encoding_df.T ,
                            journal_df.loc[ [ c.replace(' ','') for c in formula.split('~')[1].split('+') if not 'C(' in c] , : ] ]).T
    return ( encoding_df )


def calculate_alignment_properties ( encoding_df , quantx, quanty, scorex,
                                     analyte_df = None , journal_df = None ,
                                     bVerbose = False , synonyms = None ,
                                     blur_cutoff = 99.8 , exclude_labels_from_centroids = [''] ,
                                     study_axii = None , owner_by = 'tesselation' ):
    if bVerbose :
        print ( np.shape(encoding_df) )
        print ( np.shape(analyte_df)  )
        print ( 'qx:',np.shape(quantx) )
        print ( 'qy:',np.shape(quanty) )
        print ( 'sx:',np.shape(scorex) )
        print ( 'WILL ASSIGN OWNER BY PROXIMITY TO CATEGORICALS' )

    if analyte_df is None or journal_df is None:
        print ( 'USER MUST SUPPLY ANALYTE AND JOURNAL DATA FRAMES' )
        exit(1)
    #
    # THESE ARE THE CATEGORICAL DESCRIPTORS
    use_centroid_indices = [ i for i in range(len(encoding_df.columns.values)) if (
                             encoding_df.columns.values[i] not in set( exclude_labels_from_centroids )
                           ) ]
    #
    use_centroids = list(  quanty[use_centroid_indices]  )
    use_labels    = list( encoding_df.columns.values[use_centroid_indices] )
    #
    if owner_by == 'tesselation' :
        transcript_owner = [ use_labels[ np.argmin([ np.sum((xw-cent)**2) for cent in use_centroids ])] for xw in quantx ]
        sample_owner     = [ use_labels[ np.argmin([ np.sum((yw-cent)**2) for cent in use_centroids ])] for yw in scorex ]
    #
    if owner_by == 'angle' :
        angular_proximity = lambda B,A : 1 - np.dot(A,B) / ( np.sqrt(np.dot(A,A))*np.sqrt(np.dot(B,B)) )
        transcript_owner = [ use_labels[ np.argmin([ angular_proximity(xw,cent) for cent in use_centroids ])] for xw in quantx ]
        sample_owner = [ use_labels[ np.argmin([ angular_proximity(yw,cent) for cent in use_centroids ])] for yw in scorex ]
    #
    # print ( 'PLS WEIGHT RADIUS' )
    radius  = lambda vector:np.sqrt(np.sum((vector)**2)) # radii
    #
    # print ( 'ESTABLISH LENGTH SCALES' )
    xi_l    = np.max(np.abs(quantx),0)
    #
    rpoints = np.array( [ radius( v/xi_l )    for v in quantx ] ) # HERE WE MERGE THE AXES
    xpoints = np.array( [ radius((v/xi_l)[0]) for v in quantx ] ) # HERE WE USE THE X AXES
    ypoints = np.array( [ radius((v/xi_l)[1]) for v in quantx ] ) # HERE WE USE THE Y AXES
    #
    # print ( 'ESTABLISH PROJECTION OF THE WEIGHTS ONTO THEIR AXES' )
    proj = lambda B,A : np.dot(A,B) / np.sqrt( np.dot(A,A) )
    #
    # ADDING IN ADDITIONAL DIRECTIONS
    # THAT WE MIGHT BE INTERESTED IN
    if 'list' in str( type( study_axii ) ):
        for ax in study_axii :
            if len( set( ax ) - set( use_labels ) ) == 0 and len(ax)==2 :
                axsel = np.array([ use_centroids[i]  for i in range(len(use_labels)) if use_labels[i] in set(ax)  ])
                axis_direction = axsel[0]-axsel[1]
                use_labels .append( '-'.join(ax) )
                use_centroids .append( np.array(axis_direction) )

    proj_df = pd.DataFrame( [ [ np.abs(proj(P/xi_l,R/xi_l)) for P in quantx ] for R in use_centroids ] ,
                  index = use_labels , columns=analyte_df.index.values )
    #
    # print ( 'P VALUES ALIGNED TO PLS AXES' )
    for idx in proj_df.index :
        proj_p,proj_rho = quantify_density_probability ( proj_df.loc[idx,:].values )
        proj_df = proj_df.rename( index = {idx:idx+',r'} )
        proj_df.loc[idx+',p']   = proj_p
        proj_df.loc[idx+',rho'] = proj_rho
    #
    # print ( 'THE EQUIDISTANT 1D STATS' )
    corresponding_pvalue , corresponding_density , corresponding_radius = quantify_density_probability ( rpoints , cutoff = blur_cutoff )
    #
    # print ( 'THE TWO XY 1D STATS' )
    corr_pvalue_0 , corr_density_0 = quantify_density_probability ( xpoints )
    corr_pvalue_1 , corr_density_1 = quantify_density_probability ( ypoints )
    #
    bOrderedAlphas = False
    if True :
        # DO ALPHA LEVELS BASED ON DENSITY
        bOrderedAlphas = True
        use_points = rpoints > corresponding_radius
        ordered_alphas = [ float(int(u))*0.5 + 0.01 for u in use_points ]

    result_dfs = []
    #
    # print ( 'COMPILE RESULTS FRAME' )
    for ( lookat,I_ ) in [ ( quantx , 0 ) ,
                           ( scorex  , 1 ) ] :
        lookat = [ [ l[0],l[1] ] for l in lookat ]
        if I_ == 1 :
            aidx = journal_df.columns.values
        else :
            aidx = analyte_df.index.values
        qdf = pd.DataFrame( [v[0] for v in lookat] , index=aidx , columns = ['x']  )
        qdf['y'] = [ v[1] for v in lookat ]
        names = aidx
        if I_ == 0 :
            qdf[ 'owner' ] = transcript_owner
            qdf['Corr,p' ] = corresponding_pvalue
            qdf['Corr,r' ] = corresponding_density
            qdf['Corr0,p'] = corr_pvalue_0
            qdf['Corr0,r'] = corr_density_0
            qdf['Corr1,p'] = corr_pvalue_1
            qdf['Corr1,r'] = corr_density_1
            qdf = pd.concat([qdf.T,proj_df]).T
            if bOrderedAlphas :
                qdf[ 'alpha' ] = ordered_alphas
            else :
                qdf['alpha'] = [ '0.3' for a in transcript_owner ]
        else :
            qdf['owner'] = sample_owner # The default should be the aligned projection weight
            qdf['alpha'] = [ '0.2' for n in names ]
        if synonyms is None :
            qdf['name'] = names
        else :
            qdf['name'] = [ synonyms[v] if v in synonyms else v for v in names ]
        result_dfs.append(qdf.copy())
    return ( result_dfs )


def run_rpls_regression ( analyte_df , journal_df , formula ,
                          bVerbose = False , synonyms = None , blur_cutoff = 99.8 ,
                          exclude_labels_from_centroids = [''] , pls_components = 2,
                          bDeveloperTesting = False ,
                          study_axii = None , owner_by = 'tesselation'
                        ) :

    encoding_df = interpret_problem ( analyte_df , journal_df , formula , bVerbose = bVerbose )
    from sklearn.cross_decomposition import PLSRegression as PLS

    if not bDeveloperTesting :
        pls_components = 2

    rpls     = PLS( pls_components )
    rpls_res = rpls.fit( X = analyte_df.T.values ,
                         Y = encoding_df .values )
    quantx,quanty = rpls_res.x_weights_ , rpls_res.y_weights_
    scorex = rpls_res.x_scores_

    res_df = calculate_alignment_properties ( encoding_df , quantx, quanty, scorex,
                       journal_df = journal_df, analyte_df = analyte_df , blur_cutoff = blur_cutoff ,
                       bVerbose = bVerbose, exclude_labels_from_centroids = exclude_labels_from_centroids ,
                       study_axii = study_axii , owner_by = owner_by )

    return ( res_df )

import impetuous.fit as ifit
import impetuous.clustering as icluster
def run_shape_alignment_clustering ( analyte_df , journal_df , formula, bVerbose = False ) :
        NOTE_ = "This is just a kmeans in arbitrary dimensions that start out with centroids that have been shape aligned"
        encoding_df = interpret_problem ( analyte_df , journal_df , formula , bVerbose = bVerbose )

        Q = encoding_df.T.apply( lambda x:(rankdata(x,'average')-0.5)/len(x) ).values
        P = analyte_df   .apply( lambda x:(rankdata(x,'average')-0.5)/len(x) ).values

        centroids = ifit.ShapeAlignment( P, Q ,
                        bReturnTransform = False ,
                        bShiftModel = True ,
                        bUnrestricted = True )
        #
        # FOR DIAGNOSTIC PURPOSES
        centroids_df = pd.DataFrame ( centroids ,
                        index = encoding_df.columns ,
                        columns = encoding_df.index )
        lookup_ = {i:n for n,i in zip( centroids_df.index,range(len(centroids_df.index)) ) }

        labels , centroids = icluster.seeded_kmeans( P , centroids )

        res_df = pd.DataFrame( [labels] , columns=analyte_df.index , index=['cluster index'] )
        nam_df = pd.DataFrame( [ lookup_[l] for l in labels ] ,
                     columns = ['cluster name'] , index = analyte_df.index ).T

        res_df = pd.concat( [ res_df , nam_df ] )
        clusters_df = pd.concat( [ centroids_df, pd.DataFrame( res_df.T.groupby('cluster name').apply(len),columns=['size']) ] ,axis=1 )

        return ( res_df , clusters_df )


def kmeans_clustering_alignment ( P, Q , bHighDim = False ) :
    return ( knn_clustering_alignment( P , Q , bHighDim = bHighDim ) )

def knn_clustering_alignment( P , Q , bHighDim=False ) : # ITS A SEEDED KMEANS THE NAME KNN IS A MISNOMER

    NOTE_ = "This is just a standard kmeans in arbitrary dimensions that start out with centroids that have been shape aligned"
    ispanda = lambda P: 'pandas' in str(type(P)).lower()
    BustedPanda = lambda R : R.values if ispanda(R) else R
    P_ = BustedPanda ( P )
    Q_ = BustedPanda ( Q )


    if bHighDim :
        centroids = ifit .HighDimensionalAlignment ( P_ , Q_ )
    else :
        centroids = ifit .ShapeAlignment ( P_ , Q_ ,
                    bReturnTransform = False ,
                    bShiftModel      = True  ,
                    bUnrestricted    = True  )

    if ispanda ( Q ) :
        #
        # FOR DIAGNOSTIC PURPOSES
        centroids_df = pd.DataFrame ( centroids ,
        index = Q.index ,
        columns = Q.columns )
        lookup_ = {i:n for n,i in zip( centroids_df.index,range(len(centroids_df.index)) ) }

    labels , centroids = icluster.seeded_kmeans( P_ , centroids )

    if ispanda ( Q ) and ispanda ( P ) :
        #
        # MORE DIAGNOSTICS
        res_df = pd.DataFrame( [labels] , columns=P.index , index=['cluster index'] )
        res_df .loc[ 'cluster name' ] = [ lookup_[l] for l in res_df.loc['cluster index'].values ]
        print ( res_df )

    return ( np.array(labels), np.array(centroids) )

def tol_check( val, TOL=1E-10 ):
    if val > TOL :
        print ( "WARNING: DATA ENTROPY HIGH (SNR LOW)", val )

ispanda = lambda P : 'pandas' in str(type(P)).lower()

def multifactor_solution ( analyte_df , journal_df , formula ,
                           bLegacy = False ) :
    A , J , f = analyte_df , journal_df , formula
    if bLegacy :
        encoding_df = interpret_problem ( analyte_df = A , journal_df = J , formula = f ).T
    else :
        encoding_df = create_encoding_data_frame ( journal_df = J , formula = f ).T

    solution_ =  solve ( A.T, encoding_df.T )
    tol_check ( solution_[1] )
    beta_df  = pd.DataFrame ( solution_[0] , index=A.index , columns=encoding_df.index )
    U, S, VT = np.linalg.svd ( beta_df.values,full_matrices=False )
    P = pd.DataFrame( U.T , index = [ 'Comp'+str(r) for r in range(len(U.T))] , columns = A.index )
    W = pd.DataFrame(  VT , index = [ 'Comp'+str(r) for r in range(len(U.T))] , columns = encoding_df.index )
    Z = threshold ( encoding_df.T , S*W ) .T
    return ( P.T , W.T , Z.T , encoding_df.T , beta_df )


def multifactor_evaluation (  analyte_df , journal_df , formula ) :
    #
    # ALTOUGH A GOOD METHOD IT IS STILL NOT SUFFICIENT
    #
    P, W, Z, encoding_df , beta_df = multifactor_solution ( analyte_df , journal_df , formula )
    eval_df = beta_df.apply(lambda x:x**2)
    all = [beta_df]
    for c in eval_df.columns :
        all.append ( pd.DataFrame ( quantify_density_probability ( eval_df.loc[:,c].values ),
                index = [c+',p',c+',r'], columns=eval_df.index ).T)
    res_df = pd.concat( all,1 )
    for c in res_df.columns:
        if ',p' in c:
            q = [ qv[0] for qv in qvalues(res_df.loc[:,c].values) ]
            res_df.loc[:,c.split(',p')[0]+',q'] = q
    return ( res_df )

def regression_assessment ( model , X , y , bLog = False ) :
    desc_ = """
     ALTERNATIVE NAIVE MODEL ASSESSMENT FOR A REGRESSION MODEL
     !PRVT2D1701CM5487!
    """
    y_    = y
    coefs = model.coef_
    mstat = dict()

    if bLog :
        X  = np.array( [ [ np.log(x) for x in xx ] for xx in X ])
        yp = np.exp(np.dot( coefs, X ) + model.intercept_ )
    else :
        yp =       (np.dot( coefs, X ) + model.intercept_ )
    #
    n   = len ( y_ ) ; p = len(coefs)
    ym  = np.mean( y_ ) # CRITICAL DIMENSION ...
    #
    # BZ FORMS
    TSS = np.array([ np.sum((  y_ - ym  ) ** 2, axis=0) ])[0]; dof_tss = n-1 ; mstat['TSS'] = TSS
    RSS = np.array([ np.sum((  y_ - yp  ) ** 2, axis=0) ])[0]; dof_rss = n-p ; mstat['RSS'] = RSS
    ESS = np.array([ np.sum((  yp - ym  ) ** 2, axis=0) ])[0]; dof_ess = p-1 ; mstat['ESS'] = ESS
    mstat['dof_tss'] = dof_tss ; mstat['dof_rss'] = dof_rss ; mstat['dof_ess'] = dof_ess
    #
    TMS = TSS / dof_tss ; mstat['TMS'] = TMS
    RMS = RSS / dof_rss ; mstat['RMS'] = RMS
    EMS = ESS / dof_ess ; mstat['EMS'] = EMS
    #
    #   F-TEST
    dof_numerator   = dof_rss
    dof_denominator = dof_ess
    from scipy.stats import f
    fdist = f( dof_numerator , dof_denominator )
    f0    = EMS / RMS
    #
    mstat['dof_numerator']   = dof_numerator
    mstat['dof_denominator'] = dof_denominator
    mstat['p-value']         = 1 - fdist.cdf(f0)
    mstat['f0']              = f0
    mstat['yp']              = yp
    mstat['model']           = model
    #
    return ( mstat )



def proj_c ( P ) :
    # P CONTAINS MUTUTALLY ORTHOGONAL COMPONENTS ALONG THE COLUMNS
    # THE CS CALCULATION MIGHT SEEM STRANGE BUT FULLFILS THE PURPOSE
    if not ispanda(P) : # ispandor är coola
        print ( "FUNCTION REQUIRES A SAIGA OR PANDA DATA FRAME" )
    CS  = P.T.apply( lambda x: pd.Series( [x[0],x[1]]/np.sqrt(np.sum(x**2)),index=['cos','sin']) ).T
    RHO = P.T.apply( lambda x: np.sqrt(np.sum(x**2)) )
    CYL = pd.concat( [RHO*CS['cos'],RHO*CS['sin']],1 )
    CYL.columns = ['X','Y']
    return ( CYL )


def multivariate_factorisation ( analyte_df , journal_df , formula ,
                          bVerbose = False , synonyms = None , blur_cutoff = 99.8 ,
                          exclude_labels_from_centroids = [''] ,
                          bDeveloperTesting = False , bReturnAll = False ,
                          study_axii = None , owner_by = 'angle' ,
                          bDoRecast = False , bUseThresholds = False ) :

    P, W, Z, encoding_df , beta_df = multifactor_solution ( analyte_df , journal_df , formula )
    #
    # USE THE INFLATION PROJECTION AS DEFAULT
    if not bUseThresholds :
        aA = np.linalg.svd ( analyte_df - np.mean(np.mean(analyte_df))   , full_matrices=False )
        aE = np.linalg.svd ( encoding_df.T , full_matrices=False )
        Z  = pd.DataFrame ( np.dot( np.dot( W.T , aE[-1] ), aA[-1]) ,
                        columns = encoding_df.T.columns ,
                        index= [ 'mComp' + str(r) for r in range(len(aE[-1]))]
                      ).T
    if bDoRecast :
        print ( "WARNING: THROWING AWAY INFORMATION IN ORDER TO DELIVER A" )
        print ( "         VISUALLY MORE PLEASING POINT CLOUD ... ")
        P = proj_c( P )
        W = proj_c( W )
        Z = proj_c( Z )

    res_df = calculate_alignment_properties ( encoding_df ,
                        quantx = P.values , quanty = W.values , scorex = Z.values ,
                        journal_df = journal_df , analyte_df = analyte_df ,
                        blur_cutoff = blur_cutoff , bVerbose = bVerbose ,
                        exclude_labels_from_centroids = exclude_labels_from_centroids ,
                        study_axii = study_axii , owner_by = owner_by )
    if bReturnAll :
        return ( { 'Mutlivariate Solutions' : res_df ,
                   'Feature Scores' : P , 'Encoding Weights'   : W ,
                   'Sample Scores'  : Z , 'Encoding DataFrame' : encoding_df })
    else :
        return ( res_df )


def associations ( M , W = None , bRanked = True ) :
    ispanda = lambda P : 'pandas' in str(type(P)).lower()
    if not ispanda( M ) :
        print ( "FUNCTION ",'recast_alignments'," REQUIRES ", 'M'," TO BE A PANDAS DATAFRAME" )
    bValid = False
    if not W is None :
        if not len(W.columns.values) == len(M.columns.values):
            W = M
        else:
            bValid = True
    else :
        W = M
    if bRanked :
        from scipy.stats import rankdata
        M = ( M.T.apply(lambda x:rankdata(x,'average')).T-0.5 )/len(M.columns)
        W = ( W.T.apply(lambda x:rankdata(x,'average')).T-0.5 )/len(W.columns)
    rho1 = M.T.apply( lambda x:np.sqrt( np.dot( x,x ) ) )
    rho2 = rho1
    if bValid :
        rho2 = W.T.apply( lambda x:np.sqrt( np.dot( x,x ) ) )
    R2  = pd.DataFrame( np.array([np.array([r]) for r in rho1.values])*[rho2.values] ,
                        index = rho1.index, columns = rho2.index )
    PQ  = pd.DataFrame( np.dot( M,W.T ), index = rho1.index, columns = rho2.index )
    res = PQ/R2
    return ( res )


crop = lambda x,W:x[:,:W]
def run_shape_alignment_regression( analyte_df , journal_df , formula ,
                          bVerbose = False , synonyms = None , blur_cutoff = 99.8 ,
                          exclude_labels_from_centroids = [''] ,
                          study_axii = None , owner_by = 'tesselation' ,
                          transform = crop ) :

        print ( 'WARNING: STILL UNDER DEVELOPMENT' )
        print ( 'WARNING: DEFAULT IS TO CROP ALIGNED FACTORS!!')

        encoding_df = interpret_problem ( analyte_df , journal_df , formula , bVerbose = bVerbose )

        Q = encoding_df.T.apply( lambda x:(rankdata(x,'average')-0.5)/len(x) ).copy().values
        P = analyte_df   .apply( lambda x:(rankdata(x,'average')-0.5)/len(x) ).copy().values

        centroids = ifit.ShapeAlignment( P, Q ,
                        bReturnTransform = False ,
                        bShiftModel = True ,
                        bUnrestricted = True )
        #
        # FOR DIAGNOSTIC PURPOSES
        centroids_df = pd.DataFrame ( centroids ,
                            index = encoding_df.columns ,
                            columns = encoding_df.index )

        xws = ifit.WeightsAndScoresOf( P )
        yws = ifit.WeightsAndScoresOf( centroids )

        W = np.min( [*np.shape(xws[0]),*np.shape(yws[0])] )

        quantx = transform( xws[0],W )
        quanty = transform( yws[0],W )
        scorex = transform( xws[1],W )

        res_df = calculate_alignment_properties ( encoding_df , quantx, quanty, scorex,
                    analyte_df = analyte_df.copy() , journal_df = journal_df.copy() ,
                    blur_cutoff = blur_cutoff , bVerbose = bVerbose,
                    exclude_labels_from_centroids = exclude_labels_from_centroids ,
                    study_axii = study_axii , owner_by = owner_by, synonyms=synonyms )
        return ( res_df )


def add_foldchanges ( df, information_df , group='', fc_type=0 , foldchange_indentifier = 'FC,') :
    all_vals = list(set(information_df.loc[group].values))
    pair_values = [all_vals[i] for i in range(len(all_vals)) if i<2 ]
    group1 = df.iloc[:,[n in pair_values[0] for n in information_df.loc[group].values] ].T
    group2 = df.iloc[:,[n in pair_values[1] for n in information_df.loc[group].values] ].T
    if fc_type == 0:
        FC = np.mean(group1.values,0) - np.mean(group2.values,0)
    if fc_type == 1:
        FC = np.log2( np.mean(group1.values,0) - np.mean(group2.values,0) )
    FCdf = pd.DataFrame(FC,index=df.index,columns=[foldchange_indentifier+'-'.join(pair_values) ] )
    df = pd.concat([df.T,FCdf.T]).T
    return ( df )


from statsmodels.stats.multitest import multipletests
def adjust_p ( pvalue_list , method = 'fdr_bh' , alpha = 0.05,
               check_r_bh = False , is_sorted = False ,
               returnsorted = False
             ) :
    """  WRAPPER FOR MULTIPLE HYPOTHESIS TESTING
    pvalue_list = [0.00001,0.01,0.0002,0.00005,0.01,0.1,0.2,0.4,0.5,0.6,0.7,0.8,0.9,0.99,0.0114,0.15,0.23,0.20]
    """
    available_methods = set( [ 'bonferroni' , 'sidak',
           'holm-sidak' , 'holm' , 'simes-hochberg' ,
           'hommel' , 'fdr_bh' , 'fdr_by' , 'fdr_tsbh' ,
           'fdr_tsbky' ] )
    if method not in available_methods :
        print ( available_methods )
    r_equiv = { 'fdr_bh':'BH' }
    if check_r_bh and method in r_equiv :
        from rpy2.robjects.packages import importr
        from rpy2.robjects.vectors import FloatVector
        r_stats = importr('stats')
        p_adjust = r_stats.p_adjust ( FloatVector(pvalue_list), method = r_equiv[method] )
    else :
        p_adjust_results = multipletests ( pvalue_list, alpha=alpha, method=method, 
                       is_sorted = is_sorted , returnsorted = returnsorted )
        p_adjust = [ p_adj for p_adj in p_adjust_results[1] ]
    return ( p_adjust )

def qvalues ( p_values_in , pi0 = None ) :
    p_s = p_values_in
    if pi0 is None :
        pi0 = 1.
    qs_ = []
    m = float(len(p_s)) ; itype = str( type( p_s[0] ) ) ; added_info = False
    if 'list' in itype or 'tuple' in itype :
        added_info = True
        ps = [ p[0] for p in p_s ]
    else :
        ps = p_s
    frp_ = rankdata( ps,method='ordinal' )/m
    ifrp_ = [ ( (p<=f)*f + p*(p>f) ) for p,f in zip(ps,frp_) ]
    for ip in range(len(ps)) :
        p_ = ps[ ip ] ; f_ = frp_[ip]
        q_ = pi0 * p_ / ifrp_[ip]
        qs_.append( (q_,p_) )
    if added_info :
        q   = [ tuple( [qvs[0]]+list(pinf) ) for ( qvs,pinf ) in zip(qs_,p_s) ]
        qs_ = q
    return qs_



class Qvalues ( object ) :
    def __init__( self, pvalues:np.array , method:str = "UNIQUE" , pi0:np.array = None ) :
        from scipy.stats import rankdata
        self.rankdata = rankdata
        self.method   : str      = method
        self.pvalues  : np.array = pvalues
        self.qvalues  : np.array = None
        self.qpres    : np.array = None
        if method == "FDR-BH" :
            self.qpres = self.qvaluesFDRBH  ( self.pvalues )
        if method == "QVALS"  :
            self.qpres = self.qvaluesFDRBH  ( self.pvalues , pi0 )
        if method == "UNIQUE" :
            self.qpres = self.qvaluesUNIQUE ( self.pvalues , pi0 )

    def __str__ ( self ) :
        return ( self.info() )

    def __repr__( self ) :
        return ( self.info() )

    def help ( self ) :
        desc__ = "\n\nRANK CORRECTION FOR P-VALUES\nVIABLE METHODS ARE method = FDR-BH , QVALS , UNIQUE\n\n EMPLOYED METHOD: " + self.method
        return ( desc__ )

    def info ( self ) :
        desc__ = "\nMETHOD:"+self.method+"\n   q-values       \t     p-values\n"
        return ( desc__+'\n'.join( [ ' \t '.join(["%10.10e"%z for z in s]) for s in self.qpres ] ) )

    def get ( self ) :
        return ( self.qpres )

    def qvaluesFDRBH ( self , p_values_in:np.array = None , pi0:np.array = None ) :
        p_s = p_values_in
        if p_s is None :
            p_s = self.pvalues
        m = int(len(p_s))
        if pi0 is None :
            pi0 = np.array([1. for i in range(m)])
        qs_ = []
        ps = p_s
        frp_ = (self.rankdata( ps,method='ordinal' )-0.5)/m
        ifrp_ = [ ( (p<=f)*f + p*(p>f) ) for p,f in zip(ps,frp_) ]
        for ip,p0 in zip(range(m),pi0) :
            p_ = ps[ ip ] ; f_ = frp_[ip]
            q_ = p0 * p_ / ifrp_[ip]
            qs_.append( (q_,p_) )
        self.qvalues = np.array([q[0] for q in qs_])
        return np.array(qs_)

    def qvaluesUNIQUE ( self , p_values_in = None , pi0 = None ) :
        p_s = p_values_in
        if p_s is None :
            p_s = self.pvalues
        m = int(len(set(p_s)))
        n = int(len(p_s))
        if pi0 is None :
            pi0 = np.array([1. for i in range(n)])
        qs_ = []
        ps  = p_s
        frp_  = (self.rankdata( ps,method='average' )-0.5)/m
        ifrp_ = [ ( (p<=f)*f + p*(p>f) ) for p,f in zip(ps,frp_) ]
        for ip,p0 in zip( range(n),pi0 ) :
            p_ = ps[ ip ] ; f_ = frp_[ip]
            q_ = p0 * p_ / ifrp_[ip]
            qs_.append( (q_,p_) )
        self.qvalues = np.array([q[0] for q in qs_])
        return np.array(qs_)



class MultiFactorAnalysis ( object ) :
    def __init__( self, analyte_df, journal_df, formula ) :
        #super(MultiFactorAnalysis,self).__init__()
        self.rankdata = rankdata
        self.A   = analyte_df
        self.J   = journal_df
        self.f   = formula
        self.E   = None
        self.C   = None
        self.B   = None
        self.R   = None
        self.TOL = None
        self.multifactor_evaluation ( self.A , self.J , self.f )
        #print ( self.predict(self.A.iloc[:,0],'male') )

    def fit(self, analyte_df, journal_df, formula) :
        self.__init__( analyte_df, journal_df, formula )

    def tol_check ( self, val, TOL=1E-10 ):
        if val > TOL :
            print ( "WARNING: DATA ENTROPY HIGH (SNR LOW)", val )

    def recover ( self, U, S, Vt ):
        return ( np.dot(U*S,Vt) )

    def qvalues ( self, p_values_in , pi0 = None ) :
        p_s = p_values_in
        if pi0 is None :
            pi0 = 1.
        qs_ = []
        m = float(len(p_s)) ; itype = str( type( p_s[0] ) ) ; added_info = False
        if 'list' in itype or 'tuple' in itype :
            added_info = True
            ps = [ p[0] for p in p_s ]
        else :
            ps = p_s
        frp_ = rankdata( ps,method='ordinal' )/m
        ifrp_ = [ ( (p<=f)*f + p*(p>f) ) for p,f in zip(ps,frp_) ]
        for ip in range(len(ps)) :
            p_ = ps[ ip ] ; f_ = frp_[ip]
            q_ = pi0 * p_ / ifrp_[ip]
            qs_.append( (q_,p_) )
        if added_info :
            q   = [ tuple( [qvs[0]]+list(pinf) ) for ( qvs,pinf ) in zip(qs_,p_s) ]
            qs_ = q
        return qs_

    def solve ( self , C=None , E=None ) :
        if C is None :
            C = self.C
        if E is None :
            E = self.E
        if not 'pandas' in str(type(C)) or not 'pandas' in str(type(E)):
            print ( "ERROR MUST SUPPLY TWO PANDAS DATAFRAMES" )
            return ( -1 )

        cU, cS, cVt    = np.linalg.svd(C, full_matrices=False )
        cST            = 1/cS
        psuedo_inverse = pd.DataFrame( self.recover(cVt.T,cST,cU.T) , index=C.columns ,columns=C.index )
        identity       = np.dot( C , psuedo_inverse )
        TOLERANCE      = np.max( np.sqrt( ( identity * ( ( 1-np.eye(len(np.diag(identity)))) ) )**2 ))
        self.B         = np.dot( psuedo_inverse,E )
        self.TOL       = TOLERANCE
        return ( self.B , self.TOL )

    def encode_categorical ( self , G = ['A','B'] ):
        #
        # CREATES AN BINARY ENCODING MATRIX FROM THE SUPPLIED LIST
        # USES A PANDAS DATAFRAME AS INTERMEDIATE FOR ERROR CHECKING
        #
        ugl = list(set(G)) ; n = len(ugl) ; m = len(G)
        lgu = { u:j for u,j in zip(ugl,range(n)) }
        enc_d = pd.DataFrame( np.zeros(m*n).reshape(-1,n),columns=ugl )
        for i in range ( m ) :
            j = lgu[G[i]]
            enc_d.iloc[i,j] = 1
        return ( enc_d )

    def create_encoding_journal ( self , use_categories, journal_df ) :
        encoding_df = None
        for category in use_categories :
            catvals = journal_df.loc[category].to_list()
            cat_encoding = self.encode_categorical( catvals )
            cat_encoding.index = journal_df.columns.values
            if encoding_df is None :
                encoding_df = cat_encoding.T
            else :
                encoding_df = pd.concat([encoding_df,cat_encoding.T])
        return ( encoding_df )

    def find_category_interactions ( self , istr ) :
        all_cats = re.findall( r'C\((.*?)\)', istr )
        interacting = [ ':' in c for c in istr.split(')') ][ 0:len(all_cats) ]
        interacting_categories = [ [all_cats[i-1],all_cats[i]] for i in range(1,len(interacting)) if interacting[i] ]
        return ( interacting_categories )

    def create_encoding_data_frame ( self, journal_df=None , formula=None , bVerbose = False ) :
        #
        # THE JOURNAL_DF IS THE COARSE GRAINED DATA (THE MODEL)
        # THE FORMULA IS THE SEMANTIC DESCRIPTION OF THE PROBLEM
        #
        if journal_df is None :
            journal_df = self.J
        if formula is None :
            formula    = self.f

        interaction_pairs = self.find_category_interactions ( formula.split('~')[1] )
        add_pairs = []
        sjdf = set(journal_df.index)
        if len( interaction_pairs ) > 0 :
            for pair in interaction_pairs :
                cpair = [ 'C('+p+')' for p in pair ]
                upair = [ pp*(pp in sjdf)+cp*(cp in sjdf and not pp in sjdf) for (pp,cp) in zip( pair,cpair) ]
                journal_df.loc[ ':'.join(upair) ] = [ p[0]+'-'+p[1] for p in journal_df.loc[ upair,: ].T.values ]
                add_pairs.append(':'.join(upair))
        use_categories = list(set(find_category_variables(formula.split('~')[1])))
        cusecats = [ 'C('+p+')' for p in use_categories ]
        use_categories = [ u*( u in sjdf) + cu *( cu in sjdf ) for (u,cu) in zip(use_categories,cusecats) ]
        use_categories = [ *use_categories,*add_pairs ]
        #
        if len( use_categories ) > 0 :
            encoding_df = self.create_encoding_journal ( use_categories , journal_df ).T
        else :
            encoding_df = None
        #
        if bVerbose :
            print ( [ v for v in encoding_df.columns.values ] )
            print ( 'ADD IN ANY LINEAR TERMS AS THEIR OWN AXIS' )
        #
        # THIS TURNS THE MODEL INTO A MIXED LINEAR MODEL
        add_df = journal_df.loc[ [c.replace(' ','') for c in formula.split('~')[1].split('+') if not 'C('in c],: ]
        if len(add_df)>0 :
            if encoding_df is None :
                encoding_df = add_df.T
            else :
                encoding_df = pd.concat([ encoding_df.T ,
                            journal_df.loc[ [ c.replace(' ','') for c in formula.split('~')[1].split('+') if not 'C(' in c] , : ] ]).T
        self.E = encoding_df.apply(pd.to_numeric)
        return ( self.E )

    def threshold ( self, E , A ) :
        if not 'pandas' in str(type(A)) or not 'pandas' in str(type(E)):
            print ( "ERROR MUST SUPPLY TWO PANDAS DATAFRAMES" )
            return ( -1 )
        thresholds_df = pd .DataFrame ( np.dot( E,A.T ) ,
                          columns = A .index ,
                          index   = E .index ) .apply ( lambda x:x/np.sum(E,1) )
        return ( thresholds_df )

    def multifactor_solution ( self , analyte_df=None , journal_df=None ,
                               formula=None , bLegacy = False ) :
        A , J , f = analyte_df , journal_df , formula
        if A is None :
            A = self.A
        if J is None :
            J = self.J
        if f is None :
            f = self.f

        encoding_df = self.create_encoding_data_frame ( journal_df = J , formula = f ).T
        encoding_df.loc['NormFinder'] = np.array([1 for i in range(len(encoding_df.columns))])
        self.E      = encoding_df

        solution_   = self.solve ( A.T, encoding_df.T )
        self.tol_check ( solution_[1] )
        beta_df = pd.DataFrame ( solution_[0] , index=A.index , columns=encoding_df.index )
        self.B  = beta_df
        return ( encoding_df.T , beta_df )

    def quantify_density_probability ( self , rpoints , cutoff = None ) :
        #
        # DETERMINE P VALUES
        loc_pdf = lambda X,mean,variance : [ 1./np.sqrt(2.*np.pi*variance)*np.exp(-((x-mean)/(2.*variance))**2) for x in X ]
        from scipy.special import erf as erf_
        loc_cdf = lambda X,mean,variance : [      0.5*( 1. + erf_(  (x-mean)/np.sqrt( 2.*variance ) ) ) for x in X ]
        loc_Q   = lambda X,mean,variance : [ 1. - 0.5*( 1. + erf_(  (x-mean)/np.sqrt( 2.*variance ) ) ) for x in X ]
        M_,Var_ = np.mean(rpoints),np.std(rpoints)**2
        #
        # INSTEAD OF THE PROBABILTY DENSITY WE RETURN THE FRACTIONAL RANKS
        # SINCE THIS ALLOWS US TO CALCULATE RANK STATISTICS FOR THE PROJECTION
        corresponding_density = ( self.rankdata (rpoints,'average')-0.5 ) / len( set(rpoints) )
        corresponding_pvalue  = loc_Q  ( rpoints,M_,Var_ )
        return ( corresponding_pvalue , corresponding_density )

    def predict ( self, X, name ) :
        desc__=""" print ( self.predict(X.iloc[:,0],'male') ) """
        if len( X ) == len(self.A.iloc[:,0].values) and name in set(self.B.columns) :
            coefs = self.B.loc[:,name].values
            return ( name , np.dot( coefs,X )>self.TOL  )
        else :
            print ( "CANNOT PREDICT" )

    def regression_assessment ( self ) :
        desc_ = """
         ALTERNATIVE NAIVE MODEL ASSESSMENT FOR A REGRESSION MODEL
         !PRVT2D1701CM5487!
         NO CV; NOT YET INFORMATIVE
        """
        X     = self.A
        coefs = self.B.T
        yp    = np.dot( coefs,X )
        y_    = self.E.values
        #
        # NORMFINDER IS INTERCEPT
        mstat = dict()
        #
        n     = len ( y_ ); p = len(coefs); q = len ( coefs.T )
        if q>n :
            print ( "OVER DETERMINED SYSTEM OF EQUATIONS " )
        ym  = np.mean( y_ , axis=0 )
        #
        # BZ FORMS
        TSS = np.array([ np.sum((  y_ - ym  ) ** 2, axis=1) ])[0]; dof_tss = np.abs(n-1) ; mstat['TSS'] = TSS
        RSS = np.array([ np.sum((  y_ - yp  ) ** 2, axis=1) ])[0]; dof_rss = np.abs(n-q) ; mstat['RSS'] = RSS
        ESS = np.array([ np.sum((  yp - ym  ) ** 2, axis=1) ])[0]; dof_ess = np.abs(p-1) ; mstat['ESS'] = ESS
        mstat['dof_tss'] = dof_tss ; mstat['dof_rss'] = dof_rss ; mstat['dof_ess'] = dof_ess
        #
        TMS = TSS / dof_tss ; mstat['TMS'] = TMS
        RMS = RSS / dof_rss ; mstat['RMS'] = RMS
        EMS = ESS / dof_ess ; mstat['EMS'] = EMS
        #
        #   F-TEST
        dof_numerator   = dof_rss
        dof_denominator = dof_ess
        from scipy.stats import f
        fdist = f( dof_numerator , dof_denominator )
        f0    = EMS / RMS
        #
        #
        mstat['dof_numerator']   = dof_numerator
        mstat['dof_denominator'] = dof_denominator
        mstat['p-value']         = 1 - fdist.cdf(f0)
        mstat['f0']              = f0
        mstat['yp']              = yp
        mstat['model']           = model
        return ( mstat )

    def multifactor_evaluation (  self, analyte_df=None , journal_df=None , formula=None ) :
        #
        if analyte_df is None :
            analyte_df = self.A
        if journal_df is None :
            journal_df = self.J
        if formula is None :
            formula = self.f

        encoding_df , beta_df = self.multifactor_solution ( analyte_df , journal_df , formula )
        eval_df = beta_df.apply(lambda x:x**2)
        all     = [ beta_df ]
        for c in eval_df.columns :
            all.append ( pd.DataFrame ( self.quantify_density_probability ( eval_df.loc[:,c].values ),
                    index = [c+',p',c+',r'], columns=eval_df.index ).T)
        res_df = pd.concat( all , axis=1 )
        for c in res_df.columns :
            if ',p' in c :
                q = [ qv[0] for qv in self.qvalues(res_df.loc[:,c].values) ]
                res_df.loc[:,c.split(',p')[0]+',q'] = q
        self.R = res_df
        return ( self.R )


from scipy import stats
from statsmodels.stats.anova import anova_lm as anova
import statsmodels.api as sm
import patsy
def anova_test ( formula, group_expression_df, journal_df, test_type = 'random' ) :
    type_d = { 'paired':1 , 'random':2 , 'fixed':1 }
    formula = formula.replace(' ','')
    tmp_df = pd.concat([ journal_df, group_expression_df ])
    gname = tmp_df.index.tolist()[-1]
    formula_l = formula.split('~')
    rename = { gname:formula_l[0] }
    tmp_df.rename( index=rename, inplace=True )
    tdf = tmp_df.T.iloc[ :,[ col in formula for col in tmp_df.T.columns] ].apply( pd.to_numeric )
    y, X = patsy.dmatrices( formula, tdf, return_type='dataframe')
    model = sm.OLS(endog=y,exog=X).fit()
    model .model.data.design_info = X.design_info
    table = sm.stats.anova_lm(model,typ=type_d[test_type])
    return table.iloc[ [(idx in formula) for idx in table.index],-1]


def glm_test (  formula , df , jdf , distribution='Gaussian' ) :
    tmp_df = pd.concat([ jdf, df ])
    family_description = """
        Family(link, variance) # The parent class for one-parameter exponential families.
        Binomial([link]) # Binomial exponential family distribution.
        Gamma([link]) # Gamma exponential family distribution.
        Gaussian([link]) # Gaussian exponential family distribution.
        InverseGaussian([link]) # InverseGaussian exponential family.
        NegativeBinomial([link, alpha]) # Negative Binomial exponential family.
        Poisson([link]) # Poisson exponential family.
        Tweedie([link, var_power, eql]) # Tweedie family.
    """
    if distribution == 'Gaussian' :
        family = sm.families.Gaussian()
    if distribution == 'Binomial' :
        family = sm.families.Binomial()
    if distribution == 'Gamma' :
        family = sm.families.Gamma()
    if distribution == 'InverseGaussian' :
        family = sm.families.InverseGaussian()
    if distribution == 'NegativeBinomial' :
        family = sm.families.NegativeBinomial()
    if distribution == 'Poisson' :
        family = sm.families.Poisson()

    formula = formula.replace( ' ','' )
    gname = tmp_df.index.tolist()[-1]
    formula_l = formula.split('~')
    rename = { gname:formula_l[0] }
    tmp_df .rename( index=rename, inplace=True )

    tdf = tmp_df.T.iloc[ :,[ col in formula for col in tmp_df.T.columns] ].apply( pd.to_numeric )
    y , X = patsy.dmatrices( formula, tdf, return_type='dataframe')
    distribution_model = sm.GLM( y, X, family=family )
    glm_results = distribution_model.fit()
    if False:
        print('Parameters: ', glm_results.params  )
        print('T-values  : ', glm_results.tvalues )
        print('p-values  : ', glm_results.pvalues )
    table = glm_results.pvalues

    return table.iloc[ [( idx.split('[')[0] in formula) for idx in table.index]]

def t_test ( df , endogen = 'expression' , group = 'disease' ,
             pair_values = ('Sick','Healthy') , test_type = 'independent',
             equal_var = False , alternative = 'greater' ) :

    group1 = df.iloc[:,[n in pair_values[0] for n in df.loc[group,:].values] ].loc[endogen,:].astype(float)
    group2 = df.iloc[:,[n in pair_values[1] for n in df.loc[group,:].values] ].loc[endogen,:].astype(float)

    if test_type == 'independent' :
        pv = ttest_ind ( group1, group2 , equal_var = equal_var )
    if test_type == 'related' :
        pv = ttest_rel ( group1, group2 )
    try :
        p_mannu = mannwhitneyu( group1, group2, alternative=alternative )[1]
    except ValueError as err:
        print(err.args)
        p_mannu = 1.0
    pvalue = pv[1] ; statistic=pv[0]
    return ( pvalue , p_mannu, statistic )

def mycov( x , full_matrices=0 ):
    x = x - x.mean( axis=0 )
    U, s, V = np.linalg.svd( x , full_matrices = full_matrices )
    C = np.dot(np.dot(V.T,np.diag(s**2)),V)
    return C / (x.shape[0]-1)

from scipy.special import chdtrc as chi2_cdf
def p_value_merger ( pvalues_df , p_label=',p' , axis = 0 ) :
    #
    print( " REQUIRED READING: doi: 10.1093/bioinformatics/btw438" )
    print( " ALSO MAKE SURE TO ADD THAT ARTICLE AS ADDITIONAL CITATION" )
    print( " IF THIS METHOD IS EMPLOYED" )
    print( " READ ABOVE ! " )
    print( " YOU CALLED A FUNCTION FOR MERGING P-VALUES" )
    print( " THIS METHOD IS NO LONGER SUPPORTED " )
    print( " FOR IMPETUOUS VERSIONS > 0.84.0 " )
    print( " THE METHOD merge_significance COULD BE EMPLOYED INSTEAD ")
    print( " BUT IT IS NOT RECOMMENDED " )
    print( " FATAL : WILL TERMINATE NOW " )
    exit(1)

def parse_test ( statistical_formula, group_expression_df , journal_df , test_type = 'random' ) :
    #
    # THE FALLBACK IS A TYPE2 ANOVA
    ident = False
    if 'glm' in statistical_formula.lower() :
        if not test_type in set(['Gaussian','Binomial','Gamma','InverseGaussian','NegativeBinomial','Poisson']):
            test_type = 'Gaussian'
            print('ONLY GAUSSIAN TESTS ARE SUPPORTED')
        print('THIS TEST IS NO LONGER SUPPORTED')
        result = glm_test( statistical_formula, group_expression_df , journal_df , distribution = test_type )
        ident = True

    if 'ttest' in statistical_formula.lower() :
        ident = True ; result = None
        #
        # WE CONDUCT SEPARATE TESTS FOR ALL THE UNIQUE PAIR LABELS PRESENT
        check = [ idx for idx in journal_df.index if idx in statistical_formula ]
        df = pd.concat( [journal_df,group_expression_df],axis=0 ).T
        for c in check :
            if test_type in set([ 'related' , 'fixed' , 'paired' ]):
                test_type = 'related'
            else :
                test_type = 'independent'

            for pair in permuter( list(set(journal_df.loc[c].values)),2) :
                result_ = t_test( df, endogen = df.columns.values[-1], group = c,
                                  pair_values = pair, test_type = test_type, equal_var = False )
                hdr = ' '.join( [c,' '.join([str(p) for p in pair])] )
                tdf = pd.Series( result_, index = [ hdr, hdr+' mwu', hdr+' stat,s' ] )
                if result is None :
                    result = tdf
                else :
                    result = pd.concat([result,tdf])
                result.name = 'PR>t'

    if not ident :
        result = anova_test( statistical_formula, group_expression_df , journal_df , test_type=test_type )

    return ( result )

def prune_journal ( journal_df , remove_units_on = '_' ) :
    journal_df = journal_df.loc[ [ 'label' in idx.lower() or '[' in idx for idx in journal_df.index.values] , : ].copy()
    bSel = [ ('label' in idx.lower() ) for idx in journal_df.index.values]
    bool_dict = { False:0 , True:1 , 'False':0 , 'True':1 }
    str_journal = journal_df.iloc[ bSel ]
    journal_df = journal_df.replace({'ND':np.nan})
    nmr_journal = journal_df.iloc[ [ not b for b in bSel ] ].replace(bool_dict).apply( pd.to_numeric )
    if not remove_units_on is None :
        nmr_journal.index = [ idx.split(remove_units_on)[0] for idx in nmr_journal.index ]
    journal_df = pd.concat( [nmr_journal,str_journal] )
    return( journal_df )

def merge_significance ( significance_df , distance_type='euclidean' ) :
    # TAKES P VALUES OR Q VALUES
    # TRANSFORMS INTO A MERGED P OR Q VALUE VIA
    # THE DISTANCE SCORE
    # THE DATA DOMAIN SIGNIFICANCE IS ALONG COLUMNS AND
    # GROUPS ALONG INDICES
    # EX: pd.DataFrame( np.random.rand(20).reshape(5,4) , columns=['bio','cars','oil','money']).apply( lambda x: -1.*np.log10(x) ).T.apply( lambda x: np.sqrt(np.sum(x**2)) )
    #
    distance = lambda x : np.sqrt(np.sum(x**2))
    if distance_type == 'euclidean' : # ESTIMATE
        distance = lambda x : np.sqrt(np.sum(x**2))
    if distance_type == 'extreme' :   # ANTI-CONSERVATIVE ESTIMATE
        distance = lambda x : np.max(x)
    if distance_type == 'mean' :      # MEAN ESTIMATE
        distance = lambda x : np.mean(x)
    get_pvalue = lambda x : 10**(-x)
    return ( significance_df.apply( lambda x: -1.*np.log10(x) ).T.apply(distance).apply(get_pvalue) )

def group_significance( subset , all_analytes_df = None ,
                        tolerance = 0.05 , significance_name = 'pVal' ,
                        AllAnalytes = None , SigAnalytes = None,
                        alternative = 'two-sided' ) :
    # FISHER ODDS RATIO CHECK
    # CHECK FOR ALTERNATIVE :
    #   'greater'   ( ENRICHMENT IN GROUP )
    #   'two-sided' ( DIFFERENTIAL GROUP EXPERSSION )
    #   'less'      ( DEPLETION IN GROUP )
    if AllAnalytes is None :
        if all_analytes_df is None :
            AllAnalytes = set( all_analytes_df.index.values )
    if SigAnalytes is None :
        if all_analytes_df is None :
            SigAnalytes = set( all_analytes_df.iloc[(all_analytes_df<tolerance).loc[:,significance_name]].index.values )
    Analytes       = set(subset.index.values)
    notAnalytes    = AllAnalytes - Analytes
    notSigAnalytes = AllAnalytes - SigAnalytes
    AB  = len(Analytes&SigAnalytes)    ; nAB  = len(notAnalytes&SigAnalytes)
    AnB = len(Analytes&notSigAnalytes) ; nAnB = len(notAnalytes&notSigAnalytes)
    oddsratio , pval = stats.fisher_exact([[AB, nAB], [AnB, nAnB]], alternative=alternative )
    return ( pval , oddsratio )

def quantify_groups_by_analyte_pvalues( analyte_df, grouping_file, delimiter='\t',
                                 tolerance = 0.05 , p_label = 'C(Status),p' ,
                                 group_prefix = '' ,  alternative = 'two-sided'  ) :
    AllAnalytes = set( analyte_df.index.values ) ; nidx = len( AllAnalytes )
    SigAnalytes = set( analyte_df.iloc[ (analyte_df.loc[:,p_label].values < tolerance), : ].index.values )
    if len( AllAnalytes ) == len(SigAnalytes) :
        print ( 'THIS STATISTICAL TEST WILL BE NONSENSE' )
    eval_df = None
    with open( grouping_file ) as input :
        for line in input :
            vline = line.replace('\n','').split(delimiter)
            gid, gdesc, analytes_ = vline[0], vline[1], vline[2:]
            try :
                group = analyte_df.loc[[a for a in analytes_ if a in AllAnalytes] ].dropna( axis=0, how='any', thresh=analyte_df.shape[1]/2 ).drop_duplicates()
            except KeyError as e :
                continue
            L_ = len( group ) ; str_analytes=','.join(group.index.values)
            if L_ > 0 :
                pv , odds = group_significance( group , AllAnalytes=AllAnalytes, SigAnalytes=SigAnalytes , alternative=alternative )
                rdf = pd.DataFrame( [[pv]], columns = [ group_prefix + 'Fisher_' + p_label ] , index = [ gid ] )
                rdf .columns = [ col+',p' if ',p' not in col else col for col in rdf.columns ]
                rdf[ 'description' ] = gdesc+',' + str(L_) ; rdf['analytes'] = str_analytes
                rdf[ group_prefix + 'NGroupAnalytes'    ] = L_
                rdf[ group_prefix + 'AllFracFilling'    ] = L_ / float( len(analytes_) )
                present_sig = set(group.index.values)&SigAnalytes
                rdf[ group_prefix + 'SigFracGroupFill'  ] = float ( len ( present_sig ) ) / float( len(analytes_) )
                ndf = rdf
                if eval_df is None :
                    eval_df = ndf
                else :
                    eval_df = pd.concat( [ eval_df,ndf ] )
    edf = eval_df.T
    for col in eval_df.columns :
        if ',p' in col :
            q = [q_[0] for q_ in qvalues(eval_df.loc[:,col].values)]; l=col.split(',')[0]+',q'
            edf.loc[l] = q
    return ( edf.T )

class APCA ( object ) :
    #
    # THIS CLASS PERFORMS A SPARSE PCA IF REQUESTED
    # IT THEN USES THE SPARSE SVD ALGORITHM FOUND IN SCIPY
    # THE STANDARD IS TO USE THE NUMPY SVD
    #
    def __init__ ( self , X = None , k =-1 , fillna = None , transcending = True , not_sparse = True ) :
        from scipy.sparse import csc_matrix
        from scipy.sparse.linalg import svds
        self.svds_ , self.smatrix_ = svds , csc_matrix
        self.components_ = None
        self.F_ = None
        self.U_ , self.S_, self.V_ = None,None,None
        self.evr_ = None
        self.var_ = None
        self.fillna_ = fillna
        self.X_   = self.interpret_input(X)
        self.k_   = k
        self.transcending_ = transcending
        self.not_sparse = not_sparse

    def interpret_input ( self,X ) :
        if 'pandas' in str(type(X)) :
            for idx in X.index :
                X.loc[idx] = [ np.nan if 'str' in str(type(v)) else v for v in X.loc[idx].values ]
            if 'float' in str(type(self.fillna_)) or 'int' in str(type(self.fillna_)) :
                X = X.fillna(self.fillna_)
            self.X_ = X.values
        else :
            self.X_ = X
        return ( self.X_ )

    def fit ( self , X=None ) :
        self.fit_transform( X=X )

    def fit_transform ( self , X=None ) :
        if X is None:
            X = self.X_
        if not X is None :
            X = self.interpret_input(X)
        Xc = X - np.mean( X , 0 )
        if self.k_<=0 :
            k_ = np.min( np.shape(Xc) ) - 1
        else:
            k_ = self.k_

        if self.not_sparse :
                u, s, v = np.linalg.svd( Xc , full_matrices = False )
                self.transcending_ = False
        else :
                u, s, v = self.svds_ ( self.smatrix_(Xc, dtype=float) , k=k_ )

        if self.transcending_ :
            u, s, v = self.transcending_order(u,s,v)
        S = np.diag( s )
        self.F_   = np.dot(u,S)
        self.var_ = s ** 2 / Xc.shape[0]
        self.explained_variance_ratio_ = self.var_/self.var_.sum()
        self.U_ , self.S_ , self.V_ = u,s,v
        self.components_ = self.V_
        return ( self.F_ )

    def transcending_order(self,u,s,v) :
        return ( u[:,::-1],s[::-1],v[::-1,:] )

    def apply_matrix( self , R ) :
        self.U_ = np.dot( self.U_,R.T  )
        self.V_ = np.dot( self.V_.T,R.T ).T
        self.F_ = np.dot( self.F_,R.T )
        self.components_ = self.V_
        return ( self.F_ )

dimred = PCA()

def quantify_groups ( analyte_df , journal_df , formula , grouping_file , synonyms = None ,
                      delimiter = '\t' , test_type = 'random' ,
                      split_id = None , skip_line_char = '#'
                    ) :
    statistical_formula = formula
    if not split_id is None :
        nidx = [ idx.split(split_id)[-1].replace(' ','') for idx in analyte_df.index.values ]
        analyte_df.index = nidx
    sidx = set( analyte_df.index.values ) ; nidx=len(sidx)
    eval_df = None
    with open ( grouping_file ) as input:
        for line in input:
            if line[0] == skip_line_char :
                continue
            vline = line.replace('\n','').split(delimiter)
            gid,gdesc,analytes_ = vline[0],vline[1],vline[2:]
            if not synonyms is None :
                [ analytes_.append(synonyms[a]) for a in analytes_ if a in synonyms ]
            try :
                group = analyte_df.loc[[a for a in analytes_ if a in sidx] ].dropna( axis=0, how='any', thresh=analyte_df.shape[1]/2 ).drop_duplicates()
            except KeyError as e :
                continue
            L_ = len( group ) ; str_analytes=','.join(group.index.values)
            if L_>0 :
                dimred.fit(group.values)
                group_expression_df = pd.DataFrame([dimred.components_[0]],columns=analyte_df.columns.values,index=[gid])
                rdf = pd.DataFrame( parse_test( statistical_formula, group_expression_df , journal_df , test_type=test_type )).T
                rdf .columns = [ col+',p' if (not ',s' in col) else col+',s' for col in rdf.columns ]
                rdf['description'] = gdesc+','+str(L_)
                rdf['analytes'] = str_analytes
                rdf.index = [ gid ] ; ndf = pd.concat([rdf.T,group_expression_df.T]).T
                if eval_df is None :
                    eval_df = ndf
                else :
                    eval_df = pd.concat([eval_df,ndf])
    edf = eval_df.T
    for col in eval_df.columns :
        if ',p' in col :
            q = [q_[0] for q_ in qvalues(eval_df.loc[:,col].values)]; l=col.split(',')[0]+',q'
            edf.loc[l] = q
    return ( edf.T )

from scipy.stats import combine_pvalues

def quantify_by_dictionary ( analyte_df , journal_df , formula , split_id=None,
                    grouping_dictionary = dict() , synonyms = None ,
                    delimiter = ':' ,test_type = 'random', tolerance = 0.05,
                    supress_q = False , analyte_formula = None,
                    use_loc_pca=False , k=-1 ) :

    if use_loc_pca :
        dimred = APCA(X=analyte_df,k=k)

    if not 'dict' in str(type(grouping_dictionary)) :
        print ( 'INVALID GROUPING' )
        return
    statistical_formula = formula
    if not split_id is None :
        nidx = [ idx.split(split_id)[-1].replace(' ','') for idx in analyte_df.index.values ]
        analyte_df.index = nidx
    sidx = set( analyte_df.index.values ) ; nidx = len(sidx)
    eval_df = None
    if True :
        for line in grouping_dictionary.items() :
            gid,analytes_ = line[0],line[1:][0]
            gdesc = line[0].split(delimiter)[0]
            if not synonyms is None :
                [ analytes_.append(synonyms[a]) for a in analytes_ if a in synonyms ]
            try :
                group = analyte_df.loc[[a for a in analytes_ if a in sidx] ].dropna( axis=0, how='any', thresh=analyte_df.shape[1]/2 ).drop_duplicates()
            except KeyError as e :
                continue
            L_ = len( group ) ; str_analytes=','.join(group.index.values)
            if L_>0 :
                dimred .fit( group.values )
                ddf = None
                for ic in range(len( dimred.components_ )) :
                    group_expression_df = pd.DataFrame([dimred.components_[ic]],columns=analyte_df.columns.values,index=[gid])
                    rdf = pd.DataFrame( parse_test( statistical_formula, group_expression_df , journal_df , test_type=test_type )).T
                    rdf .columns = [ col+',p' if (not ',s' in col) else col+',s' for col in rdf.columns ]
                    if ddf is None:
                        ddf = rdf
                    else:
                        ddf = pd.concat([ddf,rdf])
                rdf = pd.DataFrame([ [ combine_pvalues( ddf[c].values )[1] for c in ddf.columns if ',p' in c ] ] , columns=ddf.columns )
                rdf [ 'description' ] = gdesc + ',' + str( L_ )
                rdf [ 'analytes' ] = str_analytes
                rdf .index = [ gid ]
                if not analyte_formula is None :
                    group_analytes_pos_neg_ind_d = dict()
                    qad   = quantify_analytes( group , journal_df , analyte_formula , bRegular=False )
                    loc_q = qad .loc[ :,[c for c in qad.columns.values if not 'mwu' in c and ',p' in c ] ]
                    metrics = [ c.split(',')[0] for c in loc_q.columns]
                    for metric in metrics:
                        statistic = qad.loc[ :, [c for c in qad.columns if metric in c and ',s' in c] ]
                        group_analytes_pos_neg_ind_d[ metric + ',N_positive' ] = np.sum (
                            [ 1 if p<tolerance and s>0 else 0 for (p,s) in zip(loc_q.loc[:,[metric+',p']].values,statistic.values) ]
                        )
                        group_analytes_pos_neg_ind_d[ metric + ',N_negative' ] = np.sum (
                            [ 1 if p<tolerance and s<0 else 0 for (p,s) in zip(loc_q.loc[:,[metric+',p']].values,statistic.values) ]
                        )
                        group_analytes_pos_neg_ind_d[ metric + ',N_indetermined' ] = np.sum (
                            [ 1 if p>tolerance else 0 for (p,s) in zip(loc_q.loc[:,[metric+',p']].values,statistic.values) ]
                        )
                        group_analytes_pos_neg_ind_d[ metric + ',N_tot' ] = len(statistic)

                    loc_a_df = pd.DataFrame(group_analytes_pos_neg_ind_d.items(),columns=['name',gid] )
                    loc_a_df.index = loc_a_df['name']; del loc_a_df['name']
                    rdf = pd.concat([rdf.T,loc_a_df ]).T
                if False : # SUPRESS GROUP EXPRESSION
                    ndf = pd.concat([rdf.T,group_expression_df.T]).T
                else :
                    ndf = rdf
                if eval_df is None :
                    eval_df = ndf
                else :
                    eval_df = pd.concat([eval_df,ndf])
    edf = eval_df.T
    if not supress_q :
        for col in eval_df.columns :
            if ',p' in col :
                q = [q_[0] for q_ in qvalues(eval_df.loc[:,col].values)]; l=col.split(',')[0]+',q'
                edf.loc[l] = q
    return ( edf.T )



def quantify_analytes( analyte_df , journal_df , formula ,
                       delimiter = '\t' , test_type = 'random',
                       verbose = True , only_include = None ,
                       bRegular = True ) :
    statistical_formula = formula
    sidx = set(analyte_df.index.values) ; nidx=len(sidx)
    eval_df = None ; N_ = len(analyte_df)
    for iline in range ( len( analyte_df ) ) :
        group = analyte_df.iloc[ [iline],: ]
        if 'str' in str(type(only_include)) :
            if not only_include in group.index :
                continue
        L_ = len ( group ) ; str_analytes = '.'.join( group.index.values )
        if L_>0 :
            gid = group.index.values[0].split('.')[-1].replace(' ','') ; gdesc = group.index.values[0].split('.')[0]
            group_expression_df = pd.DataFrame([group.values[0]], columns=analyte_df.columns.values, index=[gid] )
            rdf = pd.DataFrame(parse_test( statistical_formula, group_expression_df, journal_df, test_type=test_type )).T
            rdf .columns = [ col+',p' if (not ',s' in col) else col+',s' for col in rdf.columns ]
            if bRegular :
                rdf['description'] = gdesc+','+str(L_)
                rdf['analytes'] = str_analytes
            rdf .index = [ gid ] ; ndf = rdf
            if bRegular :
                ndf = pd.concat([rdf.T,group_expression_df.T]).T
            if eval_df is None :
                eval_df = ndf
            else :
                eval_df = pd.concat([eval_df,ndf])
        if verbose :
            print ( 'Done:', str(np.floor(float(iline)/N_*1000.)/10.)+'%'  , end="\r")
    edf = eval_df.T
    if not bRegular :
        return ( edf.T )
    for col in eval_df.columns :
        if ',p' in col :
            q = [q_[0] for q_ in qvalues(eval_df.loc[:,col].values)]; l=col.split(',')[0]+',q'
            edf.loc[l] = q
    return ( edf.T )

def group_counts( analyte_df, grouping_file, delimiter = '\t',
                  tolerance = 0.05 , p_label = 'C(Status),p' ,
                  group_prefix = ''
                ) :
    AllAnalytes = list( analyte_df.index.values )
    AllAnalytes = set( AllAnalytes ) ; nidx = len( AllAnalytes )
    SigAnalytes = set( analyte_df.iloc[ (analyte_df.loc[:,p_label].values < tolerance), : ].index.values )
    eval_df = None
    with open( grouping_file ) as input :
        for line in input :
            vline = line.replace('\n','').split(delimiter)
            gid, gdesc, analytes_ = vline[0], vline[1], vline[2:]
            useSigAnalytes = [ a for a in analytes_ if a in SigAnalytes ]
            try :
                group = analyte_df.loc[ useSigAnalytes ].dropna( axis=0, how='any', thresh=analyte_df.shape[1]/2 ).drop_duplicates()
            except KeyError as e :
                continue
            L_ = len( group ) ; str_analytes=','.join(group.index.values)
            if L_ > 0 :
                rdf = pd.DataFrame( [[L_,L_/float(len(analytes_))]], columns = [ 
                          group_prefix + 'NsigFrom' + p_label , 
                          group_prefix + 'FsigFrom' + p_label ] , index = [ gid ] )
                ndf = rdf
                if eval_df is None :
                    eval_df = ndf
                else :
                    eval_df = pd.concat ( [eval_df,ndf] )
    return ( eval_df.sort_values( group_prefix + 'FsigFrom' + p_label ) )


def retrieve_genes_of ( group_name, grouping_file, delimiter='\t', identifier='ENSG', skip_line_char='#' ):
    all_analytes = []
    with open ( grouping_file ) as input:
        for line_ in input :
            if skip_line_char == line_[0] :
                continue
            if group_name is None :
                line  = line_.replace( '\n','' )
                dline = line.split( delimiter )
                if identifier is None :
                    [ all_analytes.append(d) for d in dline ]
                else :
                    [ all_analytes.append(d) for d in dline if identifier in d ]
            else:
                if group_name in line_:
                    line=line_.replace('\n','')
                    dline = line.split(delimiter)
                    if identifier is None :
                        return ( [ d for d in dline ] )
                    else:
                        return ( [ d for d in dline if identifier in d ] )
    return ( list(set(all_analytes)) )

import math
def differential_analytes ( analyte_df , cols = [['a'],['b']] ):
    adf = analyte_df.loc[ :,cols[0] ].copy().apply(pd.to_numeric)
    bdf = analyte_df.loc[ :,cols[1] ].copy().apply(pd.to_numeric)
    regd_l = ( adf.values - bdf.values )
    regd_r = -regd_l
    ddf = pd.DataFrame( np.array( [ regd_l.reshape(-1) , regd_r.reshape(-1) , regd_l.reshape(-1)**2 ] ).T ,
                        columns=['DiffL','DiffR','Dist'] , index=adf.index )
    for col in adf.columns :
        ddf.loc[:,col] = adf.loc[:,col]
    for col in bdf.columns :
        ddf.loc[:,col] = bdf.loc[:,col]
    ddf = ddf.sort_values('Dist', ascending = False )
    return ( ddf )

def add_kendalltau( analyte_results_df , journal_df , what='M' , sample_names = None, ForceSpearman=False ) :
    # ADD IN CONCORDANCE WITH KENDALL TAU
    if what in set(journal_df.index.values) :
        from scipy.stats import kendalltau,spearmanr
        concordance = lambda x,y : kendalltau( x,y )
        if ForceSpearman :
            concordance = lambda x,y : spearmanr( x,y )
        K = []
        if sample_names is not None :
            patients = sample_names
        else :
            patients = [ c for c in analyte_results_df.columns if '_' in c ]
        patients = [ p for p in sample_names if p in set(patients) &
                     set( analyte_results_df.columns.values) &
                     set( journal_df.loc[[what],:].T.dropna().T.columns.values ) ]
        for idx in analyte_results_df.index :
            y = journal_df.loc[ what,patients ].values
            x = analyte_results_df.loc[ [idx],patients ].values[0] # IF DUPLICATE GET FIRST
            k = concordance( x,y )
            K .append( k )
        analyte_results_df['KendallTau'] = K
    return ( analyte_results_df )


def calculate_rates( journal_df , inferred_df ,
                     formula , inference_label = 'owner',
                     bVerbose = False ,
                     strictness = 'intersect' ) :

    strictness_function = { 'any':any,'intersect':lambda x:x }

    if strictness not in set(strictness_function.keys()):
        print ( 'ERROR: COULD NOT ASSIGN A STRICTNESS FUNCTION' )
        print ( 'VIABLE STRICTNESS OPTIONS ARE: ' , set( strictness_function.keys()) )
        exit(1)
    check = []
    for idx in journal_df.index.values:
        if idx in formula :
            check.append( idx )
    check = list( set(check) )
    if len( check ) == 0 :
        print( 'Cannot assert quality' )
        results_lookup = dict( )
        return ( results_lookup )

    known_df = journal_df.loc[check,:]

    known_OH = create_encoding_journal( known_df.index.values, known_df )
    known_instances = known_OH.index
    inferred_OH = known_OH*0
    for o in inferred_df.iterrows():
        for known_instance in known_instances:
            inferred_OH.loc[known_instance,o[0]] = int( known_instance in o[1][inference_label] )

    OH_not = lambda df:df.apply( lambda x:1-x )

    not_known_OH    = OH_not( known_OH )
    not_inferred_OH = OH_not(inferred_OH)

    if bVerbose:
        print(known_OH.iloc[:6,:6])
        print(not_known_OH.iloc[:6,:6])
        print(inferred_OH.iloc[:6,:6])
        print(np.sum(np.sum(inferred_OH.iloc[:6,:6] * known_OH.iloc[:6,:6] )) )

    TP = np.sum( np.sum( ( inferred_OH     * known_OH     ).apply(strictness_function[strictness]) ) )
    FP = np.sum( np.sum( ( inferred_OH     * not_known_OH ).apply(strictness_function[strictness]) ) )
    TN = np.sum( np.sum( ( not_inferred_OH * not_known_OH ).apply(strictness_function[strictness]) ) )
    FN = np.sum( np.sum( ( not_inferred_OH * known_OH     ).apply(strictness_function[strictness]) ) )

    results_lookup = { 'TP':TP , 'TN':TN ,
                'FN':FN ,'FP':FP ,
                'causality'   : ( TP+TN ) / ( FP+FN ) ,
                'sensitivity' : TP / ( TP+FN ) ,
                'specificity' : TN / ( TN+FP ) ,
                'precision'   : TP / ( TP+FP ) ,
                'recall'      : TP / ( TP+FN ) ,
                'accuracy'    : ( TP+TN ) / ( TP+TN+FP+FN ) ,
                'negation'    : TN / ( TN+FN ) , # FNR
                'FPR:'        : FP / ( FP+TN ) , # False positive rate
                'FDR'         : FP / ( FP+TP )   # False discovery rate
    }
    return ( results_lookup )


def assign_quality_measures( journal_df , result_dfs ,
                             formula , inference_label='owner' ,
                             plabel = ',p' , qlabel = ',q' ) :

    for label in [ col for col in result_dfs[0].columns if plabel in col[-2:] ] :
        result_dfs[0].loc[:, label[:-2]+',q'] = [ qvs[0] for qvs in qvalues( result_dfs[0].loc[:,label].values ) ]

    results_lookup = calculate_rates ( journal_df , result_dfs[1] ,
                          formula , inference_label = inference_label )
    return( results_lookup )

import math
def isItPrime( N , M=None,p=None,lM05=None ) :
    if p is None :
        p = 1
    if M is None :
        M = N
    if lM05 is None:
        lM05 = math.log(M)*0.5
    if ((M%p)==0 and p>=2) :
        return ( N==2 )
    else :
       if math.log(p) > lM05:
           return ( True )
       return ( isItPrime(N-1,M=M,p=p+1,lM05=lM05) )

# FIRST APPEARENCE:
# https://gist.github.com/richardtjornhammar/ef1719ab0dc683c69d5a864cb05c5a90
def Fibonacci(n):
    if n-2>0:
        return ( Fibonacci(n-1)+Fibonacci(n-2) )
    if n-1>0:
        return ( Fibonacci(n-1) )
    if n>0:
       return ( n )

def F_truth(i):
    return ( Fibonacci(i)**2+Fibonacci(i+1)**2 == Fibonacci(2*i+1))

if __name__ == '__main__' :

    test_type = 'random'

    path_ = './'
    analyte_file  = path_ + 'fine.txt'
    journal_file  = path_ + 'coarse.txt'
    grouping_file = path_ + 'groups.gmt'

    analyte_df = pd.read_csv(analyte_file,'\t' , index_col=0 )
    journal_df = prune_journal( pd.read_csv(journal_file,'\t', index_col=0 ) )

    print ( quantify_groups( analyte_df, journal_df, 'Group ~ Var + C(Cat) ', grouping_file ) )


    import impetuous.quantification as impq
    import sys
    sys.setrecursionlimit(20000)
    for i in range(6):
        Fi = 2**(2**i)+1
        print ("Fermats ",i,"th number = ", Fi, " and is it Prime?", impq.isItPrime(Fi) )
