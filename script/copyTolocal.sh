#!/usr/bin/env bash

#sshpass -p dream@119  scp -o "ProxyCommand corkscrew proxy.iisc.ernet.in 3128 anshudreamdf.cloudapp.net 22"  anshu@anshudreamdf.cloudapp.net:/home/anshu/data/storm/output/FullLog/*-10*   /Users/anshushukla/PycharmProjects/FullTopoSC/log1/log

#sshpass -p dream@119  scp -o "ProxyCommand corkscrew proxy.iisc.ernet.in 3128 anshudreamdf.cloudapp.net 22"  anshu@anshudreamdf.cloudapp.net:/home/anshu/data/storm/output/FullLog/Rstorm/*-11*   /Users/anshushukla/PycharmProjects/FullTopoSC/log1/log



#copy to all node inlcuding head node

#*1spouts*mps*

/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshudreamdf.cloudapp.net 22"      /Users/anshushukla/PycharmProjects/DataAnlytics1/Storm-Scheduler-SC-scripts/*1spouts*mps*    anshu@anshudreamdf.cloudapp.net:/home/anshu/data/storm/dataset/
/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshudreamdfsup1.cloudapp.net 22"  /Users/anshushukla/PycharmProjects/DataAnlytics1/Storm-Scheduler-SC-scripts/*1spouts*mps*    anshu@anshudreamdfsup1.cloudapp.net:/home/anshu/data/storm/dataset
/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshudreamdfsup2.cloudapp.net 22"  /Users/anshushukla/PycharmProjects/DataAnlytics1/Storm-Scheduler-SC-scripts/*1spouts*mps*    anshu@anshudreamdfsup2.cloudapp.net:/home/anshu/data/storm/dataset
/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshudreamdfsup3.cloudapp.net 22"  /Users/anshushukla/PycharmProjects/DataAnlytics1/Storm-Scheduler-SC-scripts/*1spouts*mps*    anshu@anshudreamdfsup3.cloudapp.net:/home/anshu/data/storm/dataset
/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshudreamdfsup4.cloudapp.net 22"  /Users/anshushukla/PycharmProjects/DataAnlytics1/Storm-Scheduler-SC-scripts/*1spouts*mps*    anshu@anshudreamdfsup4.cloudapp.net:/home/anshu/data/storm/dataset
/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshudreamdfsup5.cloudapp.net 22"  /Users/anshushukla/PycharmProjects/DataAnlytics1/Storm-Scheduler-SC-scripts/*1spouts*mps*    anshu@anshudreamdfsup5.cloudapp.net:/home/anshu/data/storm/dataset