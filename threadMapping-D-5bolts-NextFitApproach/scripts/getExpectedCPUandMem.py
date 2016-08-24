import collections
import math
import pandas as pd
import numpy as np
import matplotlib
import os
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt
import sys
import os.path

# blob_rateTothreadMap={3:1,5:2,10:20,20:30,30:50,40:60  }
# blob_rateTothreadMap_rev=collections.OrderedDict(sorted(blob_rateTothreadMap.items(),reverse=True))
# blob_threadTorateMap = dict(zip(blob_rateTothreadMap.values(), blob_rateTothreadMap.keys()))
# blob_threadToCPU_RAMMap={1:(3,15.3),2:(3.5,15.5),20:(15.4,18.08),30:(23 ,20.17),50:(37.8 ,24.65),60:(46.7,25.71)}
#
# table_rateTothreadMap={3:1,5:2,10:10,20:40,30:50,40:60 }
# table_threadTorateMap = dict(zip(table_rateTothreadMap.values(), table_rateTothreadMap.keys()))
# table_threadToCPU_RAMMap={1:(3,14),2:(4,14),10:(13,16),40:(28 ,21),50:(40 ,24),60:(55,27)}
# table_rateTothreadMap_rev=collections.OrderedDict(sorted(table_rateTothreadMap.items(),reverse=True))
#
#
# xmlparse_rateTothreadMap={310:1}
# xmlparse_threadTorateMap = dict(zip(xmlparse_rateTothreadMap.values(), xmlparse_rateTothreadMap.keys()))
# xmlparse_threadToCPU_RAMMap={1:(85,44)}
# xmlparse_rateTothreadMap_rev=collections.OrderedDict(sorted(xmlparse_rateTothreadMap.items(),reverse=True))
#
# floatpi_rateTothreadMap={105:1,110:2 }
# floatpi_threadTorateMap = dict(zip(floatpi_rateTothreadMap.values(), floatpi_rateTothreadMap.keys()))
# floatpi_threadToCPU_RAMMap={1:(92.5,14.8),2:(95,16.07)}
# floatpi_rateTothreadMap_rev=collections.OrderedDict(sorted(floatpi_rateTothreadMap.items(),reverse=True))

blob_rateTothreadMap={2:1,3:2,10:20,20:30,30:50 }
blob_rateTothreadMap_rev=collections.OrderedDict(sorted(blob_rateTothreadMap.items(),reverse=True))
blob_threadTorateMap = dict(zip(blob_rateTothreadMap.values(), blob_rateTothreadMap.keys()))
blob_threadToCPU_RAMMap={1:(8.6,33.81),2:(8.5,33.86),20:(16.4,35.88),30:(55.1 ,38),50:(77.2 ,40.3)}

table_rateTothreadMap={3:1,5:2,10:10,20:40,30:50,40:60 }
table_threadTorateMap = dict(zip(table_rateTothreadMap.values(), table_rateTothreadMap.keys()))
table_threadToCPU_RAMMap={1:(3,14),2:(4,14),10:(13,16),40:(28 ,21),50:(40 ,24),60:(55,27)}
table_rateTothreadMap_rev=collections.OrderedDict(sorted(table_rateTothreadMap.items(),reverse=True))

xmlparse_rateTothreadMap={310:1}
xmlparse_threadTorateMap = dict(zip(xmlparse_rateTothreadMap.values(), xmlparse_rateTothreadMap.keys()))
xmlparse_threadToCPU_RAMMap={1:(85,44)}
xmlparse_rateTothreadMap_rev=collections.OrderedDict(sorted(xmlparse_rateTothreadMap.items(),reverse=True))

floatpi_rateTothreadMap={105:1,110:2 }
floatpi_threadTorateMap = dict(zip(floatpi_rateTothreadMap.values(), floatpi_rateTothreadMap.keys()))
floatpi_threadToCPU_RAMMap={1:(92.5,14.8),2:(95,16.07)}
floatpi_rateTothreadMap_rev=collections.OrderedDict(sorted(floatpi_rateTothreadMap.items(),reverse=True))

#file write with 100 byte and 10^4 Batch size
batchedWrite_rateTothreadMap={60000:1,50000:2 }
batchedWrite_threadTorateMap = dict(zip(batchedWrite_rateTothreadMap.values(), batchedWrite_rateTothreadMap.keys()))
batchedWrite_threadToCPU_RAMMap={1:(59.1,23.4),2:(52.8,15.4)}
batchedWrite_rateTothreadMap_rev=collections.OrderedDict(sorted(batchedWrite_rateTothreadMap.items(),reverse=True))


# expType="linear-default"
# expType="max-default"
# expType="linear-rstorm"
expType="max-rstorm"

outDir="/Users/anshushukla/PycharmProjects/FullTopoSC/threadMapping-D-5bolts-NextFitApproach/"+expType+"/out/"
filename1=outDir + "boltThreadCountWithCPUMEM-"+expType+".csv"
filenameForTotalVal=outDir + "TotalCPUMEMperVM-"+expType+".csv"
cmd="ls -1 "+"/Users/anshushukla/PycharmProjects/FullTopoSC/threadMapping-D-5bolts-NextFitApproach/"+expType+"/*.csv"

if os.path.exists(filename1 ):
    print "yes present"
    os.remove(filename1)

if os.path.exists(filenameForTotalVal ):
    print "yes present"
    os.remove(filenameForTotalVal)

def findCpu(threadToCPU_RAMMap,threadCount,entry):
    print threadToCPU_RAMMap,threadCount

    C=0
    M=0
    maxThreads=int(max(threadToCPU_RAMMap))
    print "maxThreads-",maxThreads
    threadToCPU_RAMMap_rev = collections.OrderedDict(sorted(threadToCPU_RAMMap.items(), reverse=True))

    while(threadCount):
        if(threadCount==maxThreads):
            C+=threadToCPU_RAMMap[threadCount][0]
            M+= threadToCPU_RAMMap[threadCount][1]

            threadCount=0
            print "1CPU % --", C, "MEM % --", M

        elif(threadCount > maxThreads):
            C+=threadToCPU_RAMMap[maxThreads][0]
            M+= threadToCPU_RAMMap[maxThreads][1]
            threadCount=threadCount-maxThreads
            print "2CPU % --", C, "MEM % --", M

        elif(threadCount < maxThreads ):
            print "Interpolation for threadCount -",threadCount
            ## getting list of threads and cpu , mem
            thread_x=threadToCPU_RAMMap.keys()
            values_cpu=map(lambda (a,b):a,threadToCPU_RAMMap.values())
            values_Mem = map(lambda (a, b): b, threadToCPU_RAMMap.values())

            # check increasing over x axis
            if(np.all(np.diff(thread_x) > 0)):
                interp_cpu=np.interp(threadCount, thread_x, values_cpu)
                interp_mem = np.interp(threadCount, thread_x, values_Mem)

                C += interp_cpu
                M += interp_mem
                threadCount=0
                print "3CPU % --", C, "MEM % --", M,"REM. THREADS--",threadCount

            else:
                print "keys for it are not sorted -",threadToCPU_RAMMap
                exit()


            print "Interpolation Logic-","thread,cpu,mem",thread_x,values_cpu,values_Mem,"-interpolated Res-",interp_cpu,interp_mem
            # exit()


##previous logic of breaking in chunks ============================== BEGIN =========
            # for _threads in threadToCPU_RAMMap_rev:
            #     if(_threads > threadCount):
            #         continue
            #     else:
            #         C += threadToCPU_RAMMap[_threads][0]
            #         M += threadToCPU_RAMMap[_threads][1]
            #         threadCount-=_threads
            #         print "3CPU % --", C, "MEM % --", M,"REM. THREADS--",threadCount
            #         break

##previous logic of breaking in chunks ============================== END =========

    with open(filename1, "a") as myfile:
        # myfile.write(str(i) + "\n\n")
        myfile.write(entry+",CPU,"+str(C)+",MEM,"+str(M)+ "\n")
        # myfile.write("\t\t" + str((100 * (dSpout[4] / total_RAM)).describe()) + "\n")
    print "Final CPU % --",C,"MEM % --",M









out_dir_list=[]
for out_dir in os.popen(cmd).read().split("\n"):
   if out_dir:
       out_dir_list.append(out_dir)
print out_dir_list
dReadTemp1 = pd.read_csv(outDir + "boltThreadCount-" + expType, engine='python', sep=',', header=None,
                         names=['ip', 'port', 'count', 'bolt'])

# print dReadTemp1.groupby(['ip', 'port'])['bolt'].apply(lambda x: "{%s}" % ', '.join(x))

#
# def f(x):
#     return pd.Series(dict(A="{%s}" % ', '.join(x['sum']),
#                           # B=x['B'].sum(),
#
#                           C="{%s}" % ', '.join(x['bolt'])))
#
# print dReadTemp1.groupby(['ip', 'port']).apply(f)



# print dReadTemp1.groupby(['ip', 'port']).agg(lambda col: ''.join(col))

# print dReadTemp1.groupby(['ip', 'port']).sum()
# for i in dReadTemp1.groupby(['ip', 'port']):
#     print i


# for i in xrange(6700,6790):
for i in xrange(6700,8000):
    grepCommand="grep  "+str(i)+"\t  "+outDir+"boltThreadCount-"+expType
    # print grepCommand
    print  grepCommand
    for entry in os.popen(grepCommand).read().split("\n"):
        if(entry):

            print "entry-",entry
            threadCount=int(entry.split(",")[-2])
            boltType = entry.split(",")[-1]
            boltType=''.join(list(boltType)[1:])
            print "boltType1-",boltType,

            if(boltType in "blob_threadToCPU_RAMMap"):
                # print "Boltname5 -",boltType
                blob_threadToCPU_RAMMap = collections.OrderedDict(sorted(blob_threadToCPU_RAMMap.items()))
                findCpu(blob_threadToCPU_RAMMap,threadCount,entry)

            if (boltType in "table_threadToCPU_RAMMap"):
                # print "Boltname6 -", boltType
                table_threadToCPU_RAMMap = collections.OrderedDict(sorted(table_threadToCPU_RAMMap.items()))
                findCpu(table_threadToCPU_RAMMap, threadCount,entry)

            if (boltType in "xmlparse_threadToCPU_RAMMap"):
                # print "Boltname7 -", boltType
                xmlparse_threadToCPU_RAMMap = collections.OrderedDict(sorted(xmlparse_threadToCPU_RAMMap.items()))
                findCpu(xmlparse_threadToCPU_RAMMap, threadCount,entry)

            if (boltType in "floatpi_threadToCPU_RAMMap"):
                # print "Boltname8 -", boltType
                floatpi_threadToCPU_RAMMap = collections.OrderedDict(sorted(floatpi_threadToCPU_RAMMap.items()))
                findCpu(floatpi_threadToCPU_RAMMap, threadCount,entry)

            if (boltType.strip() in "fileWrite_threadToCPU_RAMMap"):
                # print "Boltname8 -", boltType
                # print "testanshu"
                batchedWrite_threadToCPU_RAMMap = collections.OrderedDict(sorted(batchedWrite_threadToCPU_RAMMap.items()))
                findCpu(batchedWrite_threadToCPU_RAMMap, threadCount, entry)

    print "*****NEXT WORKER*****"*3
            # print threadCount,boltType


dCPUandMem = pd.read_csv(outDir + "boltThreadCountWithCPUMEM-" + expType+".csv", engine='python', sep=',', header=None,
                         names=['ip', 'port', 'count', 'bolt','CPU','cpuval','MEM','memval'])

print dCPUandMem.groupby(['ip']).sum()['cpuval']
print dCPUandMem.groupby(['ip']).sum()['memval']



# dCPUandMem.groupby(['ip']).sum()['cpuval'].to_csv(outDir + "boltThreadCountWithCPUMEM-TOTAL-" + expType+".csv")
# dCPUandMem.groupby(['ip']).sum()['memval'].to_csv(outDir + "boltThreadCountWithCPUMEM-TOTAL-" + expType+".csv")
# dCPUandMem.groupby(['ip'], as_index = False).sum()['cpuval'].to_csv(outDir + "boltThreadCountWithCPUMEM-TOTAL-" + expType+".csv")


with open(filenameForTotalVal, "a") as myfile1:
    myfile1.write(str(dCPUandMem.groupby(['ip']).sum()['cpuval'] )+"\n")
    myfile1.write(str(dCPUandMem.groupby(['ip']).sum()['memval'])+"\n")





    # exit()
