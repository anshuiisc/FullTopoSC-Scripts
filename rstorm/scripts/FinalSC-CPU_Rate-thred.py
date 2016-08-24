def orderinglogic(s1):
    id1=int(s1.split("/")[-1].split("-")[2])
    ratelist1=s1.split("/")[-1].split("-")[3].split(".")
    ratelist1.pop()
    rate1=float(".".join(ratelist1))

    return id1-rate1

import pandas as pd
import numpy as np
import matplotlib
import os
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt
import sys
import os.path
outDirForBoxplot="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/float/log1/plot/"
listclearedfiles="ls -1 "+"/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/float/log1/cpu/clear-*.txt"

listbeforegrep="ls -1 "+"/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/float/log1/cpu/cpu*.txt"
for out_dir in os.popen(listbeforegrep).read().split("\n"):
    if(len(out_dir)!=0):
        # print out_dir.split("/")[-1]
        temp=out_dir.split("/")
        # print temp
        temp[-1]="clear-"+temp[-1]
        newout_dir="/".join(temp)

        cmdforGrep="grep Cpu "+out_dir +"> " +newout_dir
        print cmdforGrep
        os.popen(cmdforGrep)

out_dir_list=[]
for out_dir in os.popen(listclearedfiles).read().split("\n"):
   if out_dir:
       out_dir_list.append(out_dir)

## using x as method declared above
out_dir_list=sorted(out_dir_list,key=orderinglogic)
print out_dir_list

out_dir_list=['/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/float/log1/cpu/clear-cpuFloat-111-1.2.txt', '/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/float/log1/cpu/clear-cpuFloat-121-0.80.txt', '/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/float/log1/cpu/clear-cpuFloat-131-0.50.txt','/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/float/log1/cpu/clear-cpuFloat-141-0.45.txt', '/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/float/log1/cpu/clear-cpuFloat-151-0.40.txt','/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/float/log1/cpu/clear-cpuFloat-171-0.37.txt','/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/float/log1/cpu/clear-cpuFloat-181-0.33.txt','/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/float/log1/cpu/clear-cpuFloat-1381-0.28.txt']
print out_dir_list

p=[]
for i in out_dir_list:
       # dSpout = pd.read_csv(i, engine='python', header=None)
       dSpout = pd.read_csv(i, engine='c', header=None,delim_whitespace=True)
       dSpout = dSpout[dSpout[1] >= 10]
       print dSpout[1]+dSpout[3]
       p.append(dSpout[1]+dSpout[3])

# dSpout = pd.read_csv(name1, engine='c', header=None,delim_whitespace=True)
                     # names=['us','sy','ni','id','wa','hi','si','st'],sep=' ')
# print dSpout
# file sample
#      0      1    2     3    4   5    6     7    8    9    10  11   12  13   14  15  16
# %Cpu(s):   9.3  us,   4.0  sy,   0  ni,  85.7  id,  0.9   wa, 0    hi, 0.1  si, 0   st

# print p
#
fig = plt.figure(1, figsize=(9, 6))
# Create an axes instance
ax = fig.add_subplot(111)
ax.set_ylabel('CPU utilisation (%)', color='b')
ax.tick_params(axis='y', colors='blue')

# Create the boxplot
# bp = ax.boxplot(p)

def slice(x):
    # id1=int(s1.split("/")[-1].split("-")[2])
    ratelist1=x.split("/")[-1].split("-")[3].split(".")
    ratelist1.pop()
    rate1=float(".".join(ratelist1))
    return x.split("/")[-1].split("/")[-1]+"-("+str(int(100/rate1))+")"


print map(slice,out_dir_list)
print len(out_dir_list)
# ax.set_yticklabels(1000,2000,3000,4000,5000,7000,1000,15000,20000)

# ax.set_xticklabels(map(slice,out_dir_list), rotation='90')

bp = ax.boxplot(p)
plt.cla()


print "Median values are - "
medianList1=[]
medianList=[]
i=1
for medline in bp['medians']:
    linedata = medline.get_ydata()
    # medianList1.append((i,float(linedata[0])))
    medianList1.append(float(linedata[0]))
    medianList.append(float(linedata[0]))
    print i,float(linedata[0])
    i=i+1

print "Median values are-\n",medianList1

# axes = plt.gca()
# axes.set_xlim([xmin,xmax])


# t = np.arange(0.01, 10.0, 0.01)
# s1 = np.exp(t)
thread_list=[1,2,3,4,5,7,8,38]
rate_list=[83,125,200,222,250,270,300,357]
ax2 = ax.twinx()
# s2 = np.sin(2*np.pi*t)
ax2.plot(thread_list, rate_list, 'r',marker='o')
ax2.set_ylabel('msg per sec', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')

ax = fig.add_subplot(111)
ax.set_ylabel('Median CPU utilisation (%)', color='b')
ax.set_xlabel('Number of threads')
ax.tick_params(axis='y', colors='blue')
ax.set_ylim([0,100])

ax.plot(thread_list, medianList1, 'b',marker='o')


# ax.set_xticklabels(map(slice,out_dir_list), rotation='90')
# ax.set_xticklabels(thread_list)

# ax2.set_xticklabels(thread_list)
print "Check final mapping--"
print "thread_list-",thread_list,medianList1



# thread_list=[1,2,3,4,5,6,8,38]
# rate_list=[83,100,150,200,250,250,300,357]
# plt.plot(thread_list,rate_list)


# Save the figure
fig.savefig(outDirForBoxplot+'Final-CPU_Rate-thread1.png', bbox_inches='tight')