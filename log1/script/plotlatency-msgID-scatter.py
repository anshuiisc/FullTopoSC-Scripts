
import pandas as pd
import numpy as np
import matplotlib
import os
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt
import sys
import os.path

# outDir="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/parsing/logwithstringxml/plot/"
# expID="2521151"
# print expID
# cmd="ls -1 "+"/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/parsing/logwithstringxml/dat/*-"+expID+"-*.dat"
#
#
# outDir="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/floatpi/log1/plot/"
# expID="*1101"
# print expID
# cmd="ls -1 "+"/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/floatpi/log1/dat/*-"+expID+"-*.dat"


outDir="/Users/anshushukla/PycharmProjects/FullTopoSC/log1/plot/"
expID="-31133030015111180*"
print expID
cmd="ls -1 "+"/Users/anshushukla/PycharmProjects/FullTopoSC/log1/dat/L-*"+expID+"-*.dat"


import numpy as np

out_dir_list=[]
for out_dir in os.popen(cmd).read().split("\n"):
   if out_dir:
       out_dir_list.append(out_dir)
print out_dir_list
## Full box plot
p=[]

colors = "bgrcmykw"
color_index = 0
area = np.pi * (5 *np.random.rand(5))**2

for i in out_dir_list:
       dSpout = pd.read_csv(i, engine='python', header=None, names = ['msgid', 'ts1', 'ts2', 'latency'])
       # print dSpout['ts1']-dSpout['ts1'][0]
       rate=i.split("/")[-1].split("-")[-1].split(".")[0]+"."+i.split("/")[-1].split("-")[-1].split(".")[1]
       print rate,10/float(rate)
       ##
       # plt.plot(dSpout['msgid'], dSpout['latency'], label=i.split("/")[-1].split("-")[-2]+"-"+i.split("/")[-1].split("-")[-1]+"("+str(int(100/float(rate)))+")")
       # plt.plot(dSpout['ts1']-dSpout['ts1'][0], dSpout['latency'], label=i.split("/")[-1].split("-")[-2]+"-"+i.split("/")[-1].split("-")[-1])

       #scatter plot
       plt.scatter(dSpout['msgid'], dSpout['latency'],
                   label=i.split("/")[-1].split("-")[-2] + "-" + i.split("/")[-1].split("-")[-1] + "(" + str(
                       int(10 / float(rate))) + ")", c=colors[color_index], s=area, alpha=0.4)
       # plt.scatter(dSpout['ts1']-dSpout['ts1'][0], dSpout['latency'],label=i.split("/")[-1].split("-")[-2]+"-"+i.split("/")[-1].split("-")[-1]+"("+str(int(10/float(rate)))+")",c=colors[color_index],s=area,alpha=0.4)
       color_index += 1

axes = plt.gca()
# axes.set_xlim([xmin,xmax])
axes.set_ylim([0,30000])

axes.set_ylabel('Latency (in milli. sec. )')
axes.set_xlabel('Message ID')


plt.legend(loc='upper center', bbox_to_anchor=(0.5,1.0),
          ncol=3, fancybox=True, shadow=True)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(15.5, 12.5)

plt.savefig(outDir+"MSGid-latency-updated1-"+expID+".png")
