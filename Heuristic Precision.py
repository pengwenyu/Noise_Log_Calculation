from pm4py.objects.log.util.log import project_traces

from da4py.main import formulas
from pm4py.objects.petri import importer
from pm4py.objects.log.importer.xes import factory as xes_importer
from da4py.main.conformanceArtefacts import ConformanceArtefacts
from pm4py.visualization.petrinet import factory as vizu

log = xes_importer.apply("D:\process mining\log file\Benchmarking logs to test scalability of process discovery algorithms\data\XES-files\event_log_sequence_5_1000.xes")

from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
net, m0, mf = heuristics_miner.apply(log, parameters={heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.9})


artefacts=ConformanceArtefacts()
artefacts.setMax_d(14)
artefacts.setSize_of_run(8)
artefacts.setDistance_type("hamming")
artefacts.setSilentLabel(None)
artefacts.antiAlignment(net, m0, mf,log)
#print(artefacts.getPrecision())
#print( artefacts.getRun())
#print(artefacts.getTracesWithDistances())
print(artefacts.getPrecision())