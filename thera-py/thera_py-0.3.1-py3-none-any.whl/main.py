"""Main application for FastAPI"""
import html
from typing import Dict, Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.openapi.utils import get_openapi

from therapy import __version__
from therapy.query import QueryHandler, InvalidParameterException
from therapy.schemas import SearchService, NormalizationService


query_handler = QueryHandler()
app = FastAPI(docs_url="/therapy", openapi_url="/therapy/openapi.json")


def custom_openapi() -> Dict:
    """Generate custom fields for OpenAPI response"""
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="The VICC Therapy Normalizer",
        version=__version__,
        openapi_version="3.0.3",
        description="Normalize drugs and other therapy terms.",
        routes=app.routes
    )
#    openapi_schema["info"]["license"] = {  # TODO
#        "name": "Name-of-license",
#        "url": "http://www.to-be-determined.com"
#    }
    openapi_schema["info"]["contact"] = {  # TODO
        "name": "Alex H. Wagner",
        "email": "Alex.Wagner@nationwidechildrens.org"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi  # type: ignore

# endpoint description text
get_matches_summary = "Given query, provide highest matches from each source."
response_descr = "A response to a validly-formed query."
q_descr = "Therapy to search."
keyed_descr = ("If true, return response as key-value pairs of sources to source "
               "matches.")
incl_descr = ("Comma-separated list of source names to include in response. Will "
              "exclude all other sources. Will return HTTP status code 422: "
              'Unprocessable Entity if both "incl" and "excl" parameters are given.')
excl_descr = ("Comma-separated list of source names to exclude in response. Will "
              "include all other sources. Will return HTTP status code 422: "
              'Unprocessable Entity if both "incl" and "excl" parameters are given.')
infer_descr = ("If true, attempt namespace inference when queries match known "
               "Local Unique Identifier patterns.")
search_description = ("For each source, return strongest-match concepts for query "
                      "string provided by user")
normalize_description = ("Return merged strongest-match concept for query string "
                         "provided by user.")


@app.get("/therapy/search",
         summary=get_matches_summary,
         operation_id="getQueryResponse",
         response_description=response_descr,
         response_model=SearchService,
         description=search_description)
def search(q: str = Query(..., description=q_descr),
           keyed: Optional[bool] = Query(False, description=keyed_descr),
           incl: Optional[str] = Query(None, description=incl_descr),
           excl: Optional[str] = Query(None, description=excl_descr),
           infer_namespace: bool = Query(True, description=infer_descr)
           ) -> Dict:
    """For each source, return strongest-match concepts for query string
    provided by user.

    :param q: therapy search term
    :param bool keyed: if true, response is structured as key/value pair of sources to
        source match lists.
    :param str incl: comma-separated list of sources to include, with all others
        excluded. Raises HTTPException if both `incl` and `excl` are given.
    :param str excl: comma-separated list of sources exclude, with all others included.
        Raises HTTPException if both `incl` and `excl` are given.
    :param bool infer_namespace: if True, try to infer namespace from query term.
    :returns: JSON response with matched records and source metadata
    """
    try:
        response = query_handler.search_sources(html.unescape(q),
                                                keyed=keyed,  # type: ignore
                                                incl=incl, excl=excl,  # type: ignore
                                                infer=infer_namespace)  # type: ignore
    except InvalidParameterException as e:
        raise HTTPException(status_code=422, detail=str(e))
    return response


merged_matches_summary = "Given query, provide merged normalized record."
merged_response_descr = "A response to a validly-formed query."
merged_q_descr = "Therapy to normalize."


@app.get("/therapy/normalize",
         summary=merged_matches_summary,
         operation_id="getQuerymergedResponse",
         response_description=merged_response_descr,
         response_model=NormalizationService,
         description=normalize_description)
def normalize(q: str = Query(..., description=merged_q_descr),
              infer_namespace: bool = Query(True, description=infer_descr)
              ) -> Dict:
    """Return merged strongest-match concept for query string provided by
    user.

    :param q: therapy search term
    :param bool infer_namespace: if True, try to infer namespace from query term.
    :returns: JSON response with matching normalized record and source metadata
    """
    try:
        response = query_handler.search_groups(html.unescape(q),
                                               infer_namespace)  # type: ignore
    except InvalidParameterException as e:
        raise HTTPException(status_code=422, detail=str(e))
    return response
