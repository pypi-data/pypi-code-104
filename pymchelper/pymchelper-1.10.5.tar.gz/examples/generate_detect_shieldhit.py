import sys
from itertools import product

# import necessary code pieces from pymchelper
from pymchelper.shieldhit.detector.detector_type import SHDetType
from pymchelper.shieldhit.detector.estimator import SHEstimator
from pymchelper.shieldhit.detector.estimator_type import SHGeoType
from pymchelper.shieldhit.detector.fortran_card import EstimatorWriter, CardLine
from pymchelper.shieldhit.detector.geometry import CarthesianMesh
from pymchelper.shieldhit.particle import SHParticleType


def main(args=None):
    """
    Compose programatically detect.dat SHIELDHIT-12A input file
    with fixed mesh and many combinations of detector and particle type.
    :param args: part of sys.argv, used here to simplify automated testing
    :return: None
    """
    if args is None:
        args = sys.argv[1:]

    # create empty estimator object
    estimator = SHEstimator()

    # create carthesian mesh
    # it is done once and in single place
    # editing in manually in detect.dat file would require changes in many lines,
    # for every combination of particle and detector type, making it error prone
    estimator.estimator = SHGeoType.msh
    estimator.geometry = CarthesianMesh()
    estimator.geometry.set_axis(axis_no=0, start=-5.0, stop=5.0, nbins=1)
    estimator.geometry.set_axis(axis_no=1, start=-5.0, stop=5.0, nbins=1)
    estimator.geometry.set_axis(axis_no=2, start=0.0, stop=30.0, nbins=300)

    # possible detector types and associated names
    det_types = {SHDetType.energy: "en", SHDetType.fluence: "fl"}

    # possible particle types and associated names
    particle_types = {SHParticleType.all: "all", SHParticleType.proton: "p", SHParticleType.neutron: "n"}

    # open detector.dat file for writing
    with open("detect.dat", "w") as f:
        f.write(CardLine.credits + "\n")

        # loop over all combinations of detector and particle types
        # output filename will be composed from associated detector and particle names
        for dt, pt in product(det_types.keys(), particle_types.keys()):
            estimator.detector_type = dt
            estimator.particle_type = pt
            estimator.filename = det_types[dt] + "_" + particle_types[pt]
            text = EstimatorWriter.get_text(estimator, add_comment=True)
            f.write(text)
        f.write(CardLine.comment + "\n")

    # detect.dat file should have following content:
    #  * generated by pymchelper (https://github.com/DataMedSci/pymchelper) *
    # *----0---><----1---><----2---><----3---><----4---><----5---><----6--->
    # MSH             -5.0      -5.0       0.0       5.0       5.0      30.0
    #                    1         1       300         1    ENERGY      en_n
    # *----0---><----1---><----2---><----3---><----4---><----5---><----6--->
    # MSH             -5.0      -5.0       0.0       5.0       5.0      30.0
    #                    1         1       300         2    ENERGY      en_p
    # *----0---><----1---><----2---><----3---><----4---><----5---><----6--->
    # MSH             -5.0      -5.0       0.0       5.0       5.0      30.0
    #                    1         1       300        -1    ENERGY    en_all
    # *----0---><----1---><----2---><----3---><----4---><----5---><----6--->
    # MSH             -5.0      -5.0       0.0       5.0       5.0      30.0
    #                    1         1       300         1   FLUENCE      fl_n
    # *----0---><----1---><----2---><----3---><----4---><----5---><----6--->
    # MSH             -5.0      -5.0       0.0       5.0       5.0      30.0
    #                    1         1       300         2   FLUENCE      fl_p
    # *----0---><----1---><----2---><----3---><----4---><----5---><----6--->
    # MSH             -5.0      -5.0       0.0       5.0       5.0      30.0
    #                    1         1       300        -1   FLUENCE    fl_all
    # *----0---><----1---><----2---><----3---><----4---><----5---><----6--->


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
