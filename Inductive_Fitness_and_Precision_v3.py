from pm4py.objects.log.importer.xes import importer as xes_importer
import os
import datetime

array1=[]
array2=[]
list1=[5,10,15,20]
list2=["change name","missing head","missing tail","missing episode","perturbed order","double activity","align activity"]
for x in range(0,10):
    sum1=0
    sum2=0
    for i in list1:
        logfile = "E://noise log//Experiment 2 Ex//Level 4//log file//" + str(x) + "//" + list2[0] + "//" + str(
            i) + ".xes"
        #print(logfile)
        if os.path.exists(logfile) == True:
            log = xes_importer.apply(logfile)

            from pm4py.algo.discovery.inductive import algorithm as inductive_miner
            net, im, fm = inductive_miner.apply(log)

            from pm4py.evaluation.replay_fitness import evaluator as replay_fitness_evaluator
            fitness = replay_fitness_evaluator.apply(log, net, im, fm, variant=replay_fitness_evaluator.Variants.TOKEN_BASED)

            #print("fitness is equal to",fitness)
            fit = fitness['log_fitness']

            from pm4py.evaluation.precision import evaluator as precision_evaluator
            prec = precision_evaluator.apply(log, net, im, fm, variant=precision_evaluator.Variants.ETCONFORMANCE_TOKEN)

            #print("precision is euqal to",prec)

            array1.append(fit)
            array2.append(prec)
        print(array1)
        print(array2)
        starttime = datetime.datetime.now()
        print(starttime)

fitness1 = array1[0] + array1[4] + array1[8] + array1[12] + array1[16]
fitness2 = array1[1] + array1[5] + array1[9] + array1[13] + array1[17]
fitness3 = array1[2] + array1[6] + array1[10] + array1[12] + array1[18]
fitness4 = array1[3] + array1[7] + array1[11] + array1[13] + array1[19]

precision1 = array2[0] + array2[4] + array2[8] + array2[12] + array2[16]
precision2 = array2[1] + array2[5] + array2[9] + array2[13] + array2[17]
precision3 = array2[2] + array2[6] + array2[10] + array2[12] + array2[18]
precision4 = array2[3] + array2[7] + array2[11] + array2[13] + array2[19]

print(fitness1 / 5, fitness2 / 5, fitness3 / 5, fitness4 / 5)
print(precision1 / 5, precision2 / 5, precision3 / 5, precision4 / 5)