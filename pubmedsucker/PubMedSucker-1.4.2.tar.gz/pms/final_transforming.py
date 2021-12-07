import logging
from pms.tools import get_graph
from Configs import getConfig
from DZDutils.neo4j import run_periodic_iterate

config = getConfig()

log = logging.getLogger("PubmedSuckerFinalTransform")


def delete_old_articles() -> int:
    graph = get_graph()
    del_query = """UNWIND $pmids as pmid 
                MATCH p=(a:_PubmedArticle_DELETED)-[*1..2]->(n) 
                WHERE n:ELocationID OR n:Abstract OR n:AbstractText OR n:ArticleId OR n:ReferenceList OR n:Reference OR n:GrantList OR n:GeneralNote OR n:Contribution OR n:KeywordList OR n:MeshHeadingList OR n:MeshHeading OR n:PersonalNameSubjectList
                DETACH DELETE p
                return count(p) as cnt"""
    log.info(f"RUN 'delete'-QUERY:\n'{del_query}'")
    return graph.run(del_query, pmids=get_phase2_delete_pmids()).data()[0]["cnt"]


def run_transforming_queries():
    log.info("Detach MedLineJournal info from article and connect it to Journal")
    run_periodic_iterate(
        graph=get_graph(),
        cypherIterate="MATCH (p:PubMedArticle)-[r:PUBMEDARTICLE_HAS_JOURNALISSUE]->(ji:JournalIssue)-[jij:JOURNALISSUE_HAS_JOURNAL]->(j:Journal) return p as article,j as journal",
        cypherAction="MATCH (article)-[rj:PUBMEDARTICLE_HAS_MEDLINEJOURNALINFO]->(mji:MedlineJournalInfo) MERGE (journal)-[:JOURNAL_HAS_MEDLINEJOURNALINFO]->(mji) DELETE rj",
        batchSize=100,
        parallel=False,
    )
