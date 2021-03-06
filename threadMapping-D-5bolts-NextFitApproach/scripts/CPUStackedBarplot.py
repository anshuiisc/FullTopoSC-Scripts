
import pandas as pd
import numpy as np
import matplotlib
import os
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt
import sys
import os.path

import numpy as np
import matplotlib.pyplot as plt


N = 5
# menMeans = (20, 35, 30, 35, 27)
# womenMeans = (25, 32, 34, 20, 25)


# expType="linear-default"
# expType="max-default"
# expType="linear-rstorm"
expType="max-rstorm"

outDir="/Users/anshushukla/PycharmProjects/FullTopoSC/threadMapping-D-5bolts-NextFitApproach/"+expType+"/out/"
dCPUandMem = pd.read_csv(outDir + "boltThreadCountWithCPUMEM-" + expType + ".csv", engine='python', sep=',',
                         header=None,
                         names=['ip', 'port', 'count', 'bolt', 'CPU', 'cpuval', 'MEM', 'memval'])

print "Initial data\n--"
print dCPUandMem.head(10)

# print dCPUandMem.groupby(['ip','bolt'])['cpuval'].sum()

# dCPUandMem2 = dCPUandMem.groupby(['ip','bolt'])['cpuval'].sum().unstack('bolt').fillna(0).T.reset_index()

dCPUandMem2 = dCPUandMem.groupby(['ip','bolt'])['cpuval'].sum().unstack('bolt').fillna(0).T.reset_index()

print "Data after group BY\n - "
print  dCPUandMem2
print "\ndCPUandMem2.loc[1][1:]\n",dCPUandMem2.loc[1][1:]

# print
# print(dCPUandMem2.loc[dCPUandMem2['10.3.0.10'] == 'parse'])

# print dCPUandMem2['10.3.0.10']
# print  dCPUandMem2['parse']

# dCPUandMem2[['10.3.0.9','10.3.0.10' ,'10.3.0.11','10.3.0.12','10.3.0.13','10.3.0.14']].plot(kind='bar', stacked=True)
# dCPUandMem2[['blob','parse' ,'table','pi']].plot(kind='bar', stacked=True)

# dCPUandMem2.loc[1][1:].plot(kind='bar', stacked=True)


commonCoreDiv=4
# //ordering is hard coded  VERIFY ************************
p=[dCPUandMem2.loc[0][1:]/commonCoreDiv,dCPUandMem2.loc[1][1:]/commonCoreDiv,dCPUandMem2.loc[2][1:]/commonCoreDiv,dCPUandMem2.loc[3][1:]/commonCoreDiv,dCPUandMem2.loc[4][1:]/commonCoreDiv]
pd=pd.DataFrame(p)

print pd
print pd.T
print pd.T.reset_index()
pd2=pd.T.reset_index()

print "TEST1-\n",pd2

pd2.columns = ["ip", "blob", 'fileWrite',"parse", "pi","table"]
pd2.plot(kind='bar', stacked=True)

# print "TEST1-\n",pd2

# exit()

# dCPUandMem2[['abuse','nff']].plot(kind='bar', stacked=True)

ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

# p1 = plt.bar(ind, menMeans, width, color='r')
# p2 = plt.bar(ind, womenMeans, width, color='y',
#              bottom=menMeans)
#
# plt.ylabel('Scores')
# plt.title('Scores by group and gender')

# plt.xticks(ind + width/2., ('V2', 'V3', 'V4','V5','V6','V1'))
plt.xticks(ind + width/2., ('V1','V2', 'V3', 'V4','V5'))

# plt.yticks(np.arange(0, 81, 10))
# plt.legend((, ), ('Men', 'Women'))

plt.savefig(outDir+expType+"-CPUstackPlot.png")


# df2 = df.groupby(['Name', 'Abuse/NFF'])['Name'].count().unstack('Abuse/NFF').fillna(0)
# df2[['abuse','nff']].plot(kind='bar', stacked=True)