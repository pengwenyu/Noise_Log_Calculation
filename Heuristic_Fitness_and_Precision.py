from pm4py.objects.log.importer.xes import importer as xes_importer

array1=[]
array2=[]
for x in range(1,6):
    sum1=0
    sum2=0
    for i in range(1,6):
        logfile = "E://noise log//Experiment 2 Ex//Level "+ str(x) +"//log file//"+str(i)+ "//0.xes"

        log = xes_importer.apply(logfile)

        from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
        net, im, fm = heuristics_miner.apply(log, parameters={heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.9})


        from pm4py.evaluation.replay_fitness import evaluator as replay_fitness_evaluator
        fitness = replay_fitness_evaluator.apply(log, net, im, fm, variant=replay_fitness_evaluator.Variants.TOKEN_BASED)

        #print("fitness is equal to",fitness)
        sum1 = sum1 + fitness['log_fitness']
        from pm4py.evaluation.precision import evaluator as precision_evaluator
        prec = precision_evaluator.apply(log, net, im, fm, variant=precision_evaluator.Variants.ETCONFORMANCE_TOKEN)

        #print("precision is euqal to",prec)
        sum2 = sum2 + prec
    array1.append(sum1 / 5)
    array2.append(sum2 / 5)
    print(array1)
    print(array2)
print(array1)
print(array2)