basepath="/Users/anshushukla/PycharmProjects/FullTopoSC/mappingAlgo/"
algo="test"
expID="1"

import os
filename1=basepath + algo +"-"+expID+".csv"
print filename1

bolt_to_CoreMapping={}
bolt_to_ThreadMapping={}
with open(filename1) as f:
    for line in f:
        print line
        boltName = line.split(",")[0]
        cpu=line.split(",")[4]
        mem=line.split(",")[6]
        threads=line.split(",")[2]
        bolt_to_CoreMapping[boltName]=float(max(cpu,mem))
        bolt_to_ThreadMapping[boltName]=threads

print bolt_to_CoreMapping
print bolt_to_ThreadMapping

cores=map(lambda x:x/100,bolt_to_CoreMapping.values())
print "cores-",cores

cores_rounded=map(lambda x:round(x),cores)
print "cores_rounded-",cores_rounded


#####

v1=['orion']

#####

# for i in xrange(len(cores)):

    # if(cores[i]>=0.5)
    #     cores[i]=1




