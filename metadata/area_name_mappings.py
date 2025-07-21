from maps.graph_edges.base_graph.edges_arn import edges_arn
from maps.graph_edges.base_graph.edges_dgb import edges_dgb
from maps.graph_edges.base_graph.edges_dro import edges_dro
from maps.graph_edges.base_graph.edges_flo import edges_flo
from maps.graph_edges.base_graph.edges_hos import edges_hos
from maps.graph_edges.base_graph.edges_isk import edges_isk
from maps.graph_edges.base_graph.edges_iwa import edges_iwa
from maps.graph_edges.base_graph.edges_jan import edges_jan
from maps.graph_edges.base_graph.edges_kgr import edges_kgr
from maps.graph_edges.base_graph.edges_kkj import edges_kkj
from maps.graph_edges.base_graph.edges_kmr import edges_kmr
from maps.graph_edges.base_graph.edges_kpa import edges_kpa
from maps.graph_edges.base_graph.edges_kzn import edges_kzn
from maps.graph_edges.base_graph.edges_mac import edges_mac
from maps.graph_edges.base_graph.edges_mgm import edges_mgm
from maps.graph_edges.base_graph.edges_mim import edges_mim
from maps.graph_edges.base_graph.edges_nok import edges_nok
from maps.graph_edges.base_graph.edges_obk import edges_obk
from maps.graph_edges.base_graph.edges_omo import edges_omo
from maps.graph_edges.base_graph.edges_osr import edges_osr
from maps.graph_edges.base_graph.edges_pra import edges_pra
from maps.graph_edges.base_graph.edges_sam import edges_sam
from maps.graph_edges.base_graph.edges_sbk import edges_sbk
from maps.graph_edges.base_graph.edges_tik import edges_tik
from maps.graph_edges.base_graph.edges_trd import edges_trd

area_name_id_map = {
    "KMR": 0,
    "MAC": 1,
    "TIK": 2,
    "KGR": 3,
    "KKJ": 4,
    "HOS": 5,
    "NOK": 6,
    "TRD": 7,
    "IWA": 8,
    "DRO": 9,
    "SBK": 10,
    "ISK": 11,
    "MIM": 12,
    "OBK": 13,
    "ARN": 14,
    "DGB": 15,
    "OMO": 16,
    "JAN": 17,
    "KZN": 18,
    "FLO": 19,
    "SAM": 20,
    "PRA": 21,
    "KPA": 22,
    "OSR": 23,
    "END": 24,
    "MGM": 25,
    "GV":  26,
    "TST": 27,
}

area_name_edges_map = {
    "ARN": edges_arn,
    "DGB": edges_dgb,
    "DRO": edges_dro,
    "FLO": edges_flo,
    "HOS": edges_hos,
    "ISK": edges_isk,
    "IWA": edges_iwa,
    "JAN": edges_jan,
    "KGR": edges_kgr,
    "KKJ": edges_kkj,
    "KMR": edges_kmr,
    "KPA": edges_kpa,
    "KZN": edges_kzn,
    "MAC": edges_mac,
    "MGM": edges_mgm,
    "MIM": edges_mim,
    "NOK": edges_nok,
    "OBK": edges_obk,
    "OMO": edges_omo,
    "OSR": edges_osr,
    "PRA": edges_pra,
    "SAM": edges_sam,
    "SBK": edges_sbk,
    "TIK": edges_tik,
    "TRD": edges_trd,
}

chapter_areaname_map = {
    1: ["NOK","TRD"],
    2: ["IWA","SBK","DRO","ISK"],
    3: ["MIM","OBK","ARN","DGB"],
    4: ["OMO"],
    5: ["JAN","KZN"],
    6: ["FLO"],
    7: ["SAM","PRA"],
    8: ["KPA"],
}
