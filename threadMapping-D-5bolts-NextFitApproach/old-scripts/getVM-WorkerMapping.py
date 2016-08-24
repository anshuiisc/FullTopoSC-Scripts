import pandas as pd
import numpy as np
import matplotlib
import os
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt
import sys
import os.path
import numpy as np



expType="test-max-our"
outDir="/Users/anshushukla/PycharmProjects/FullTopoSC/threadMapping-D-5bolts/"+expType+"/out/"
os.system("mkdir -p "+outDir)
# expID="-1031*310*"
# print expID
cmd="ls -1 "+"/Users/anshushukla/PycharmProjects/FullTopoSC/threadMapping-D-5bolts/"+expType+"/*.csv"


out_dir_list=[]
for out_dir in os.popen(cmd).read().split("\n"):
   if out_dir:
       out_dir_list.append(out_dir)
print out_dir_list



filename1=outDir + "boltThreadCount-"+expType
if os.path.exists(filename1 ):
    print "yes present"
    os.remove(filename1)

for i in out_dir_list:
       dSpout = pd.read_csv(i, engine='python', sep=',',header=None, names = ['Id','Uptime','Host','Port','Debug','Emitted','Transferred','Capacity (last 10m)','Execute latency (ms)','Executed,Process latency (ms)','Acked,Failed'])

       print dSpout.head(3)

       dSpoutgrouped=dSpout.groupby(['Id', 'Uptime']).count()['Host']

       boltType = i.split("/")[-1].split("-")[-1].split(".")[0]
       print boltType
       print dSpoutgrouped[0:-1]
       dSpoutgrouped[0:-1].to_csv(outDir+"temp",header=None)

       # exit()

       dReadTemp=pd.read_csv(outDir+"temp", engine='python', sep=',',header=None,names=['ip','port','count'])
       dReadTemp['boltType']=boltType
       dReadTemp.to_csv(outDir + "boltThreadCount-"+expType,mode="a",header=None)

       ##reading file to verify
       print "##reading file to verify if count is correct ==========="
       dReadTemp1 = pd.read_csv(outDir +"boltThreadCount-"+expType, engine='python', sep=',', header=None, names=['ip', 'port', 'count','bolt'])
       print dReadTemp1.groupby('bolt').sum()['count']




       # rate=i.split("/")[-1].split("-")[-1].split(".")[0]+"."+i.split("/")[-1].split("-")[-1].split(".")[1]
       # print rate,10/float(rate)
       ##
       # plt.plot(dSpout['msgid'], dSpout['latency'], label=i.split("/")[-1].split("-")[-2]+"-"+i.split("/")[-1].split("-")[-1]+"("+str(int(100/float(rate)))+")")
       # plt.plot(dSpout['ts1']-dSpout['ts1'][0], dSpout['latency'], label=i.split("/")[-1].split("-")[-2]+"-"+i.split("/")[-1].split("-")[-1])

exit()
