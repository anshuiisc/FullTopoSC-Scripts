import collections

blob_rateTothreadMap={2:1}
blob_rateTothreadMap_rev=collections.OrderedDict(sorted(blob_rateTothreadMap.items(),reverse=True))
blob_threadTorateMap = dict(zip(blob_rateTothreadMap.values(), blob_rateTothreadMap.keys()))
blob_threadToCPU_RAMMap={1: (6.73, 23.92)}

table_rateTothreadMap={3:1}
table_threadTorateMap = dict(zip(table_rateTothreadMap.values(), table_rateTothreadMap.keys()))
table_threadToCPU_RAMMap={1: (1.02, 1.15)}
table_rateTothreadMap_rev=collections.OrderedDict(sorted(table_rateTothreadMap.items(),reverse=True))

xmlparse_rateTothreadMap={310:1}
xmlparse_threadTorateMap = dict(zip(xmlparse_rateTothreadMap.values(), xmlparse_rateTothreadMap.keys()))
xmlparse_threadToCPU_RAMMap={1: (84.69, 35.63)}
xmlparse_rateTothreadMap_rev=collections.OrderedDict(sorted(xmlparse_rateTothreadMap.items(),reverse=True))

floatpi_rateTothreadMap={105:1}
floatpi_threadTorateMap = dict(zip(floatpi_rateTothreadMap.values(), floatpi_rateTothreadMap.keys()))
floatpi_threadToCPU_RAMMap={1: (92.35, 2.07)}
floatpi_rateTothreadMap_rev=collections.OrderedDict(sorted(floatpi_rateTothreadMap.items(),reverse=True))

#file write with 100 byte and 10^4 Batch size
batchedWrite_rateTothreadMap={60000:1 }
batchedWrite_threadTorateMap = dict(zip(batchedWrite_rateTothreadMap.values(), batchedWrite_rateTothreadMap.keys()))
batchedWrite_threadToCPU_RAMMap={1: (58.27, 11.95)}
batchedWrite_rateTothreadMap_rev=collections.OrderedDict(sorted(batchedWrite_rateTothreadMap.items(),reverse=True))