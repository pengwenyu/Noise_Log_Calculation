from pm4py.objects.log.importer.xes import importer as xes_importer
import os
import datetime

logfile = "D:\process mining\log file\Real life event log\BPI_Challenge_2013_open_problems.xes"

log = xes_importer.apply(logfile)

from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner

heu_net = heuristics_miner.apply_heu(log, parameters={
    heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.9})

from pm4py.visualization.heuristics_net import visualizer as hn_visualizer

gviz = hn_visualizer.apply(heu_net)
# hn_visualizer.view(gviz)

starttime = datetime.datetime.now()
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner

heu_net = heuristics_miner.apply_heu(log, parameters={
    heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.9})
endtime = datetime.datetime.now()
print("Heuristic miner time is", (endtime - starttime).microseconds)

from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner

net, im, fm = heuristics_miner.apply(log, parameters={
    heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.9})

from pm4py.visualization.petrinet import visualizer as visualizer

gviz = visualizer.apply(net)
visualizer.view(gviz)

# from pm4py.evaluation.replay_fitness import evaluator as replay_fitness_evaluator
# fitness = replay_fitness_evaluator.apply(log, net, im, fm, variant=replay_fitness_evaluator.Variants.TOKEN_BASED)
#
# print("fitness is equal to",fitness)
#
# from pm4py.evaluation.precision import evaluator as precision_evaluator
# prec = precision_evaluator.apply(log, net, im, fm, variant=precision_evaluator.Variants.ETCONFORMANCE_TOKEN)
#
# print("precision is euqal to",prec)