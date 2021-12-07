# -*- coding: utf-8 -*-
# Autogenerated on 12:39:11 2016/10/13
# flake8: noqa
import logging
from wbia.algo.hots import _pipeline_helpers
from wbia.algo.hots import chip_match
from wbia.algo.hots import exceptions
from wbia.algo.hots import hstypes
from wbia.algo.hots import match_chips4
from wbia.algo.hots import name_scoring
from wbia.algo.hots import neighbor_index
from wbia.algo.hots import neighbor_index_cache
from wbia.algo.hots import nn_weights
from wbia.algo.hots import old_chip_match
from wbia.algo.hots import pipeline
from wbia.algo.hots import query_params
from wbia.algo.hots import query_request
from wbia.algo.hots import scoring
import utool

print, rrr, profile = utool.inject2(__name__, '[wbia.algo.hots]')
logger = logging.getLogger('wbia')


def reassign_submodule_attributes(verbose=True):
    """
    why reloading all the modules doesnt do this I don't know
    """
    import sys

    if verbose and '--quiet' not in sys.argv:
        print('dev reimport')
    # Self import
    import wbia.algo.hots

    # Implicit reassignment.
    seen_ = set([])
    for tup in IMPORT_TUPLES:
        if len(tup) > 2 and tup[2]:
            continue  # dont import package names
        submodname, fromimports = tup[0:2]
        submod = getattr(wbia.algo.hots, submodname)
        for attr in dir(submod):
            if attr.startswith('_'):
                continue
            if attr in seen_:
                # This just holds off bad behavior
                # but it does mimic normal util_import behavior
                # which is good
                continue
            seen_.add(attr)
            setattr(wbia.algo.hots, attr, getattr(submod, attr))


def reload_subs(verbose=True):
    """Reloads wbia.algo.hots and submodules"""
    if verbose:
        print('Reloading submodules')
    rrr(verbose=verbose)

    def wrap_fbrrr(mod):
        def fbrrr(*args, **kwargs):
            """fallback reload"""
            if verbose:
                print('No fallback relaod for mod=%r' % (mod,))
            # Breaks ut.Pref (which should be depricated anyway)
            # import imp
            # imp.reload(mod)

        return fbrrr

    def get_rrr(mod):
        if hasattr(mod, 'rrr'):
            return mod.rrr
        else:
            return wrap_fbrrr(mod)

    def get_reload_subs(mod):
        return getattr(mod, 'reload_subs', wrap_fbrrr(mod))

    get_rrr(_pipeline_helpers)(verbose=verbose)
    get_rrr(chip_match)(verbose=verbose)
    get_rrr(exceptions)(verbose=verbose)
    get_rrr(hstypes)(verbose=verbose)
    get_rrr(match_chips4)(verbose=verbose)
    get_rrr(name_scoring)(verbose=verbose)
    get_rrr(neighbor_index)(verbose=verbose)
    get_rrr(neighbor_index_cache)(verbose=verbose)
    get_rrr(nn_weights)(verbose=verbose)
    get_rrr(old_chip_match)(verbose=verbose)
    get_rrr(pipeline)(verbose=verbose)
    get_rrr(query_params)(verbose=verbose)
    get_rrr(query_request)(verbose=verbose)
    get_rrr(scoring)(verbose=verbose)
    rrr(verbose=verbose)
    try:
        # hackish way of propogating up the new reloaded submodule attributes
        reassign_submodule_attributes(verbose=verbose)
    except Exception as ex:
        print(ex)


rrrr = reload_subs

IMPORT_TUPLES = [
    ('_pipeline_helpers', None),
    ('chip_match', None),
    ('exceptions', None),
    ('hstypes', None),
    ('match_chips4', None),
    ('name_scoring', None),
    ('neighbor_index', None),
    ('neighbor_index_cache', None),
    ('nn_weights', None),
    ('old_chip_match', None),
    ('pipeline', None),
    ('query_params', None),
    ('query_request', None),
    ('scoring', None),
]
"""
Regen Command:
    cd /home/joncrall/code/wbia/wbia/algo/hots
    makeinit.py --modname=wbia.algo.hots
"""
