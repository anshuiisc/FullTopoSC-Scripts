import collections
import math

# blob_rateTothreadMap={3:1}
# blob_rateTothreadMap_rev=collections.OrderedDict(sorted(blob_rateTothreadMap.items(),reverse=True))
# blob_threadTorateMap = dict(zip(blob_rateTothreadMap.values(), blob_rateTothreadMap.keys()))
# blob_threadToCPU_RAMMap={1:(3,15.3)}
#
# table_rateTothreadMap={3:1}
# table_threadTorateMap = dict(zip(table_rateTothreadMap.values(), table_rateTothreadMap.keys()))
# table_threadToCPU_RAMMap={1:(3,14)}
# table_rateTothreadMap_rev=collections.OrderedDict(sorted(table_rateTothreadMap.items(),reverse=True))
#
# xmlparse_rateTothreadMap={310:1}
# xmlparse_threadTorateMap = dict(zip(xmlparse_rateTothreadMap.values(), xmlparse_rateTothreadMap.keys()))
# xmlparse_threadToCPU_RAMMap={1:(85,44)}
# xmlparse_rateTothreadMap_rev=collections.OrderedDict(sorted(xmlparse_rateTothreadMap.items(),reverse=True))
#
# floatpi_rateTothreadMap={105:1}
# floatpi_threadTorateMap = dict(zip(floatpi_rateTothreadMap.values(), floatpi_rateTothreadMap.keys()))
# floatpi_threadToCPU_RAMMap={1:(92.5,14.8)}
# floatpi_rateTothreadMap_rev=collections.OrderedDict(sorted(floatpi_rateTothreadMap.items(),reverse=True))


blob_rateTothreadMap={2:1}
blob_rateTothreadMap_rev=collections.OrderedDict(sorted(blob_rateTothreadMap.items(),reverse=True))
blob_threadTorateMap = dict(zip(blob_rateTothreadMap.values(), blob_rateTothreadMap.keys()))
blob_threadToCPU_RAMMap={1:(8.6,33.81)}

table_rateTothreadMap={3:1}
table_threadTorateMap = dict(zip(table_rateTothreadMap.values(), table_rateTothreadMap.keys()))
table_threadToCPU_RAMMap={1:(3,14)}
table_rateTothreadMap_rev=collections.OrderedDict(sorted(table_rateTothreadMap.items(),reverse=True))

xmlparse_rateTothreadMap={310:1}
xmlparse_threadTorateMap = dict(zip(xmlparse_rateTothreadMap.values(), xmlparse_rateTothreadMap.keys()))
xmlparse_threadToCPU_RAMMap={1:(85,44)}
xmlparse_rateTothreadMap_rev=collections.OrderedDict(sorted(xmlparse_rateTothreadMap.items(),reverse=True))

floatpi_rateTothreadMap={105:1}
floatpi_threadTorateMap = dict(zip(floatpi_rateTothreadMap.values(), floatpi_rateTothreadMap.keys()))
floatpi_threadToCPU_RAMMap={1:(92.5,14.8)}
floatpi_rateTothreadMap_rev=collections.OrderedDict(sorted(floatpi_rateTothreadMap.items(),reverse=True))

#file write with 100 byte and 10^4 Batch size
batchedWrite_rateTothreadMap={60000:1 }
batchedWrite_threadTorateMap = dict(zip(batchedWrite_rateTothreadMap.values(), batchedWrite_rateTothreadMap.keys()))
batchedWrite_threadToCPU_RAMMap={1:(59.1,23.4)}
batchedWrite_rateTothreadMap_rev=collections.OrderedDict(sorted(batchedWrite_rateTothreadMap.items(),reverse=True))

# 		CPU and MEM at 1 Thread
#
# 	threads	Rate	CPU%	Mem%	Mem (megaBytes)
# Blob	1	3	3	15.3	548
# table	1	3	3	14	502
# FloatPI	1	105	92.5	14.8	530
# xmlparse	1	310	85	43.9	1573



# def getThreadsFromrate(rateNeeded):
#
#     blob_rateTothreadMap_rev = collections.OrderedDict(sorted(blob_rateTothreadMap.items(),reverse=True))
#     print blob_rateTothreadMap_rev
#
#
#     print blob_rateTothreadMap_rev
#     while(rateNeeded):
#         for r in blob_rateTothreadMap_rev:
#             if(rateNeeded==r):
#                 print "rateNeeded1-",rateNeeded,blob_rateTothreadMap[r]
#                 rateNeeded=0
#             elif(rateNeeded<r ):
#                 continue
#             else:
#                 print  "rateNeeded2-", rateNeeded,blob_rateTothreadMap[r]
#                 rateNeeded=rateNeeded-r
#                 break

# getThreadsFromrate(7)


# def getThreadsFromrate(rateNeeded):
#
#     blob_rateTothreadMap_rev = collections.OrderedDict(sorted(blob_rateTothreadMap.items(),reverse=True))
#     print blob_rateTothreadMap_rev
#
#     # print blob_rateTothreadMap_rev
#
#     for r in blob_rateTothreadMap_rev:
#         if(rateNeeded==r):
#             print "rateNeeded1-",rateNeeded,"threadNeeded1-",blob_rateTothreadMap[r]
#
#             return eval(i+'_rateTothreadMap[r]')
#
#
#
#         elif(rateNeeded<r and rateNeeded > min(blob_rateTothreadMap)):
#             continue
#
#         elif (rateNeeded < r and rateNeeded <= min(blob_rateTothreadMap)):
#             print  "rateNeeded2-", rateNeeded, "threadNeeded2-", 1
#             return 1
#         else:
#             print  "rateNeeded3-", rateNeeded,"threadNeeded3-",blob_rateTothreadMap[r]
#             return eval(i+'_rateTothreadMap[r]')




def getThreadsFromrate(rateNeeded,boltname):

    print boltname+"_rateTothreadMap_rev",eval(boltname+"_rateTothreadMap_rev")
    for r in eval(boltname+"_rateTothreadMap_rev"):
        # print r,rateNeeded
        if(rateNeeded==r):
            # print "rateNeeded1-",rateNeeded,"threadNeeded1-",blob_rateTothreadMap[r]
            print eval(i+'_rateTothreadMap[r]')
            return eval(i+'_rateTothreadMap[r]')


## extra comment
        # elif(rateNeeded<r and rateNeeded > min(eval(i+'_rateTothreadMap'))):
        #     continue

        elif (rateNeeded < r and rateNeeded <= min(eval(i+'_rateTothreadMap'))):
            print  "rateNeeded2-", rateNeeded, "threadNeeded2-", 1

            return 1
        else:
            # print  "rateNeeded3-", rateNeeded,"threadNeeded3-",blob_rateTothreadMap[r]
            print eval(i + '_rateTothreadMap[r]')
            return eval(i+'_rateTothreadMap[r]')

#############################



basepath="/Users/anshushukla/PycharmProjects/FullTopoSC/script/topoWiseAllocation/DiamondTopo/data/"
algo="linear"

commonrate=70
expID="rate-"+str(commonrate)

import os
filename1=basepath + algo +"-"+expID+".csv"
print filename1
if os.path.exists(filename1):
    print "yes present"
    os.remove(filename1)



c=0
m=0

#for reducing mem by 6% and using linear topo
# commonrate=330

# commonrate=80
# boltname_inputRateNeedMap={'blob':commonrate,'table':commonrate,'xmlparse':commonrate,'floatpi':commonrate}

boltname_inputRateNeedMap={'blob':commonrate,'table':commonrate,'xmlparse':commonrate,'floatpi':(commonrate)*4,'batchedWrite':commonrate}

# boltname_inputRateNeedMap={'blob':21}


for i in boltname_inputRateNeedMap:
    c1=c
    m1=m
    print "Calculating for bolt =============",i,"================================================================="
    total_threadCountperbolt=0
    rateNeeded=boltname_inputRateNeedMap[i]
    maxrate_1core=max(eval(i+'_rateTothreadMap'))
    # maxrate_1core = max(blob_rateTothreadMap)
    print maxrate_1core
    ti=0

    while(rateNeeded):
        if(rateNeeded>=maxrate_1core):
            rateNeeded=rateNeeded-maxrate_1core
            t=getThreadsFromrate(maxrate_1core,i)
            total_threadCountperbolt+=t
            print "getThreadsFromrate t -",t
            ti=ti+t
            # c=c+ blob_threadToCPU_RAMMap[t][0]
            # m=m+ blob_threadToCPU_RAMMap[t][1]


            # c1=(c+ eval(i + '_threadToCPU_RAMMap[t][0]'))
            # m1=m+ eval(i + '_threadToCPU_RAMMap[t][1]')
            # print "Calculated C and M value -", c1, m1


            c=c+ eval(i + '_threadToCPU_RAMMap[t][0]')
            m=m+ eval(i + '_threadToCPU_RAMMap[t][1]')

            # #can use normalized CPU utilization also
            # c=c+ 100
            # m=m+ 100

            print "ti1-",ti




        else:

            t=getThreadsFromrate(rateNeeded,i)
            total_threadCountperbolt += t
            print "getThreadsFromrate t here1-",t
            ti=ti+t

            if(t==1):
                print "check:1 thread Linear scalng for it .... "
                # c=c+ blob_threadToCPU_RAMMap[t][0]*(rateNeeded/blob_threadTorateMap[t])
                # m=m+ blob_threadToCPU_RAMMap[t][1]*(rateNeeded/blob_threadTorateMap[t])


                # c1=c+ eval(i+'_threadToCPU_RAMMap[t][0]')*(rateNeeded/float(eval(i+'_threadTorateMap[t]')))
                # m1=m+ eval(i+'_threadToCPU_RAMMap[t][1]')*(rateNeeded/float(eval(i+'_threadTorateMap[t]')))
                # print "Calculated C and M value -", c1, m1

                print (rateNeeded/float(eval(i+'_threadTorateMap[t]'))),rateNeeded,eval(i+'_threadTorateMap[t]')
                # print eval(i+'_threadToCPU_RAMMap[t][0]')*(rateNeeded/float(eval(i+'_threadTorateMap[t]')))
                c=c+ eval(i+'_threadToCPU_RAMMap[t][0]')*(rateNeeded/float(eval(i+'_threadTorateMap[t]')))
                m=m+ eval(i+'_threadToCPU_RAMMap[t][1]')*(rateNeeded/float(eval(i+'_threadTorateMap[t]')))

                rateNeeded=0



                ## extra comment

            #
            # else:
            #
            #     # c = c + blob_threadToCPU_RAMMap[t][0]
            #     # m = m + blob_threadToCPU_RAMMap[t][1]
            #     # rateNeeded=rateNeeded-blob_threadTorateMap[t]
            #     # print "testing ", eval(i + '_threadToCPU_RAMMap[t][0]')
            #
            #     # c1=c + eval(i+'_threadToCPU_RAMMap[t][0]')
            #     # m1=m + eval(i+'_threadToCPU_RAMMap[t][1]')
            #     # print "Calculated C and M value -",c1,m1
            #
            #     print "TEST:1"
            #
            #     c = c + eval(i+'_threadToCPU_RAMMap[t][0]')
            #     m = m + eval(i+'_threadToCPU_RAMMap[t][1]')
            #     rateNeeded = rateNeeded - eval(i+'_threadTorateMap[t]')






            print "ti2-", ti

    print "total_threadCountperbolt-",total_threadCountperbolt
    print "Bolt name per bolt- ",i,",CPU --", c-c1, ",Mem --", m-m1
    print "Bolt name-", i, ",CPU --", c, ",Mem --", m

    s=i+",threads,"+str(total_threadCountperbolt)+",cpu,"+str(c-c1)+",mem,"+str(m-m1)
    with open(filename1, "a") as myfile:
        myfile.write( s+ "\n")


print "Total CPU --",c,"Total Mem --",m
print "Total Core Count -- ",math.ceil(float(max(c,m))/100)


