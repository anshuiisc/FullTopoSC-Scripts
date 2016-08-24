#!/usr/bin/env bash

#/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshudreamdf.cloudapp.net 22"  anshu@anshudreamdf.cloudapp.net:/home/anshu/data/storm/output/FullLog/*-152*   /Users/anshushukla/PycharmProjects/FullTopoSC/log1/log

#sshpass -p dream@119  scp -o "ProxyCommand corkscrew proxy.iisc.ernet.in 3128 anshudreamdf.cloudapp.net 22"  anshu@anshudreamdf.cloudapp.net:/home/anshu/data/storm/output/FullLog/Rstorm/*-11*   /Users/anshushukla/PycharmProjects/FullTopoSC/log1/log

#sshpass -p dream@119  scp -o "ProxyCommand corkscrew proxy.iisc.ernet.in 3128 anshudreamdfsup1.cloudapp.net 22"  anshu@anshudreamdfsup1.cloudapp.net:/home/anshu/data/storm/output/FullLog/*-112*   /Users/anshushukla/PycharmProjects/FullTopoSC/log1/log

expID=241157852111*

#dest=/Users/anshushukla/PycharmProjects/FullTopoSC/log1/log
dest=/Users/anshushukla/PycharmProjects/FullTopoSC/defaultscheduler/log

#/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshudf1sup2.cloudapp.net 22"  anshu@anshudf1sup2.cloudapp.net:/home/anshu/*.csv   /Users/anshushukla/PycharmProjects/FullTopoSC/defaultscheduler/scripts/

/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshudreamdf1.cloudapp.net 22"  anshu@anshudreamdf1.cloudapp.net:/home/anshu/data/storm/output/Microbenchmarkiotbm/*-$expID*   $dest
/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshudf1sup2.cloudapp.net 22"  anshu@anshudf1sup2.cloudapp.net:/home/anshu/data/storm/output/Microbenchmarkiotbm/*-$expID*   $dest
/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshudf1sup3.cloudapp.net 22"  anshu@anshudf1sup3.cloudapp.net:/home/anshu/data/storm/output/Microbenchmarkiotbm/*-$expID*   $dest
/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshudf1sup4.cloudapp.net 22"  anshu@anshudf1sup4.cloudapp.net:/home/anshu/data/storm/output/Microbenchmarkiotbm/*-$expID*  $dest
/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshudf1sup5.cloudapp.net 22"  anshu@anshudf1sup5.cloudapp.net:/home/anshu/data/storm/output/Microbenchmarkiotbm/*-$expID*   $dest
/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshudf1sup6.cloudapp.net 22"  anshu@anshudf1sup6.cloudapp.net:/home/anshu/data/storm/output/Microbenchmarkiotbm/*-$expID*   $dest