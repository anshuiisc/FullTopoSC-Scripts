import collections

blob_rateTothreadMap={2:1,3:2,10:20,20:30,30:50 }
blob_rateTothreadMap_rev=collections.OrderedDict(sorted(blob_rateTothreadMap.items(),reverse=True))
blob_threadTorateMap = dict(zip(blob_rateTothreadMap.values(), blob_rateTothreadMap.keys()))
# blob_threadToCPU_RAMMap={1:(8.6,33.81),2:(8.5,33.86),20:(16.4,35.88),30:(55.1 ,38),50:(77.2 ,40.3)}
blob_threadToCPU_RAMMap={1: (6.73, 23.92), 2: (6.63, 23.98), 20: (14.69, 26.3), 30: (54.18, 28.74), 50: (76.73, 31.38) }


table_rateTothreadMap={3:1,5:2,10:10,20:40,30:50,40:60 }
table_threadTorateMap = dict(zip(table_rateTothreadMap.values(), table_rateTothreadMap.keys()))
# table_threadToCPU_RAMMap={1:(3,14),2:(4,14),10:(13,16),40:(28 ,21),50:(40 ,24),60:(55,27)}
table_threadToCPU_RAMMap={1: (1.02, 1.15), 2: (2.04, 1.15), 10: (11.22, 3.45),40: (26.53, 9.2), 50: (38.78, 12.64), 60: (54.08, 16.09)}
table_rateTothreadMap_rev=collections.OrderedDict(sorted(table_rateTothreadMap.items(),reverse=True))

xmlparse_rateTothreadMap={310:1}
xmlparse_threadTorateMap = dict(zip(xmlparse_rateTothreadMap.values(), xmlparse_rateTothreadMap.keys()))
# xmlparse_threadToCPU_RAMMap={1:(85,44)}
xmlparse_threadToCPU_RAMMap= {1: (84.69, 35.63)}
xmlparse_rateTothreadMap_rev=collections.OrderedDict(sorted(xmlparse_rateTothreadMap.items(),reverse=True))

floatpi_rateTothreadMap={105:1,110:2 }
floatpi_threadTorateMap = dict(zip(floatpi_rateTothreadMap.values(), floatpi_rateTothreadMap.keys()))
# floatpi_threadToCPU_RAMMap={1:(92.5,14.8),2:(95,16.07)}
floatpi_threadToCPU_RAMMap = {1: (92.35, 2.07), 2: (94.9, 3.53)}
floatpi_rateTothreadMap_rev=collections.OrderedDict(sorted(floatpi_rateTothreadMap.items(),reverse=True))

#file write with 100 byte and 10^4 Batch size
batchedWrite_rateTothreadMap={60000:1,50000:2 }
batchedWrite_threadTorateMap = dict(zip(batchedWrite_rateTothreadMap.values(), batchedWrite_rateTothreadMap.keys()))
# batchedWrite_threadToCPU_RAMMap={1:(59.1,23.4),2:(52.8,15.4)}
batchedWrite_threadToCPU_RAMMap= {1: (58.27, 11.95), 2: (51.84, 2.76)}
batchedWrite_rateTothreadMap_rev=collections.OrderedDict(sorted(batchedWrite_rateTothreadMap.items(),reverse=True))



# base_cpu=2
# base_Mem=13
# updated={}
# for i in batchedWrite_threadToCPU_RAMMap.keys():
#     updated_cpu=round( ( (batchedWrite_threadToCPU_RAMMap[i][0] - base_cpu) / float(100 -base_cpu))*100,2)
#     updated_mem =round((   (batchedWrite_threadToCPU_RAMMap[i][1] - base_Mem) / float(100 - base_Mem)  ) *100,2)
#     updated[i]=(  updated_cpu,updated_mem)
#
# # updated=collections.OrderedDict(sorted(updated.items(),reverse=False))
# print updated