# -*- coding: utf-8 -*-
"""
Autogenerated IBEISController functions

TemplateInfo:
    autogen_time = 15:14:53 2015/03/11
    autogen_key = party

ToRegenerate:
    python -m wbia.templates.template_generator --key party --Tcfg with_api_cache=False with_web_api=False with_deleters=False --diff
    python -m wbia.templates.template_generator --key party --Tcfg with_api_cache=False with_web_api=False with_deleters=False --write
"""
import logging
import functools  # NOQA
from wbia import constants as const
import utool as ut
from wbia.control import controller_inject
from wbia.control import accessor_decors  # NOQA

print, rrr, profile = ut.inject2(__name__)
logger = logging.getLogger('wbia')

# Create dectorator to inject functions in this module into the IBEISController
CLASS_INJECT_KEY, register_ibs_method = controller_inject.make_ibs_register_decorator(
    __name__
)


register_api = controller_inject.get_wbia_flask_api(__name__)


def testdata_ibs(defaultdb='testdb1'):
    r"""
    Auto-docstr for 'testdata_ibs'
    """
    import wbia

    ibs = wbia.opendb(defaultdb=defaultdb)
    qreq_ = None
    return ibs, qreq_


# AUTOGENED CONSTANTS:
PARTY_ROWID = 'party_rowid'
PARTY_TAG = 'party_tag'


@register_ibs_method
def _get_all_party_rowids(ibs):
    r"""
    all_party_rowids <- party.get_all_rowids()

    Returns:
        list_ (list): unfiltered party_rowids

    TemplateInfo:
        Tider_all_rowids
        tbl = party

    Example:
        >>> # ENABLE_DOCTEST
        >>> from wbia.control._autogen_party_funcs import *  # NOQA
        >>> ibs, qreq_ = testdata_ibs()
        >>> ibs._get_all_party_rowids()
    """
    all_party_rowids = ibs.db.get_all_rowids(const.PARTY_TABLE)
    return all_party_rowids


@register_ibs_method
# @register_api('/api/autogen/', methods=['POST'])
def add_party(ibs, party_tag_list):
    r"""
    Returns:
        returns party_rowid_list of added (or already existing partys)

    TemplateInfo:
        Tadder_native
        tbl = party

    RESTful:
        Method: POST
        URL:    /api/autogen/
    """
    # WORK IN PROGRESS
    colnames = (PARTY_TAG,)
    params_iter = ((party_tag,) for (party_tag,) in zip(party_tag_list))
    get_rowid_from_superkey = ibs.get_party_rowid_from_superkey
    party_rowid_list = ibs.db.add_cleanly(
        const.PARTY_TABLE, colnames, params_iter, get_rowid_from_superkey
    )
    return party_rowid_list


@register_ibs_method
# @register_api('/api/autogen/party/rowid/superkey/', methods=['GET'])
def get_party_rowid_from_superkey(ibs, party_tag_list, eager=True, nInput=None):
    r"""
    party_rowid_list <- party[party_tag_list]

    Args:
        superkey lists: party_tag_list

    Returns:
        party_rowid_list

    TemplateInfo:
        Tgetter_native_rowid_from_superkey
        tbl = party

    RESTful:
        Method: GET
        URL:    /api/autogen/party_rowid_from_superkey/
    """
    colnames = (PARTY_ROWID,)
    # FIXME: col_rowid is not correct
    params_iter = zip(party_tag_list)
    andwhere_colnames = (PARTY_TAG,)
    party_rowid_list = ibs.db.get_where_eq(
        const.PARTY_TABLE,
        colnames,
        params_iter,
        andwhere_colnames,
        eager=eager,
        nInput=nInput,
    )
    return party_rowid_list


@register_ibs_method
# @register_api('/api/autogen/party/tag/', methods=['GET'])
def get_party_tag(ibs, party_rowid_list, eager=True, nInput=None):
    r"""
    party_tag_list <- party.party_tag[party_rowid_list]

    gets data from the "native" column "party_tag" in the "party" table

    Args:
        party_rowid_list (list):

    Returns:
        list: party_tag_list

    TemplateInfo:
        Tgetter_table_column
        col = party_tag
        tbl = party

    RESTful:
        Method: GET
        URL:    /api/autogen/party/tag/

    Example:
        >>> # ENABLE_DOCTEST
        >>> from wbia.control._autogen_party_funcs import *  # NOQA
        >>> ibs, qreq_ = testdata_ibs()
        >>> party_rowid_list = ibs._get_all_party_rowids()
        >>> eager = True
        >>> party_tag_list = ibs.get_party_tag(party_rowid_list, eager=eager)
        >>> assert len(party_rowid_list) == len(party_tag_list)
    """
    id_iter = party_rowid_list
    colnames = (PARTY_TAG,)
    party_tag_list = ibs.db.get(
        const.PARTY_TABLE,
        colnames,
        id_iter,
        id_colname='rowid',
        eager=eager,
        nInput=nInput,
    )
    return party_tag_list
