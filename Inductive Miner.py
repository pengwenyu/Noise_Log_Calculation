from pm4py.objects.log.importer.xes import importer as xes_importer
import os
import datetime
log = xes_importer.apply("E:\Complex noise\s.xes")

starttime = datetime.datetime.now()
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
net, im, fm = inductive_miner.apply(log)
endtime = datetime.datetime.now()
print("Inductive miner time is",(endtime-starttime).microseconds)

from pm4py.evaluation.replay_fitness import evaluator as replay_fitness_evaluator
fitness = replay_fitness_evaluator.apply(log, net, im, fm, variant=replay_fitness_evaluator.Variants.TOKEN_BASED)

print("fitness is equal to",fitness)

from pm4py.evaluation.precision import evaluator as precision_evaluator
prec = precision_evaluator.apply(log, net, im, fm, variant=precision_evaluator.Variants.ETCONFORMANCE_TOKEN)

print("precision is euqal to",prec)