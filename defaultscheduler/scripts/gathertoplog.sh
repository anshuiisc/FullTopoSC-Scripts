#!/usr/bin/env bash

file_serverinfo=/Users/anshushukla/PycharmProjects/FullTopoSC/log1/script/PrivateIPs.txt

#file_outputcommands=usefulcommands.txt

#file_pem=/home/ubuntu/anshu.pem

expNum=112
#expNum=$1

#memDriveBasePath="/tmp/ramdisk/"
#logFileWorker="$memDriveBasePath/logFileWorker.txt"
#
#file_src=$logFileWorker

#path_dest="/data/tetc/tetc-final/dataset/RECEIVED/$expNum/"
#path_dest="/Users/anshushukla/PycharmProjects/FullTopoSC/rstorm/cpu/$expNum/"
#
#mkdir -p "$path_dest"

#printf "" > $file_outputcommands

for i in `cat $file_serverinfo`
do
	#printf "ssh  -i $file_pem ubuntu@$i -o \"ProxyCommand corkscrew proxy.iisc.ernet.in 3128 $i 22\" \"sudo sed -i '20i\ServerAliveInterval 120' /etc/ssh/ssh_config\"\n" >> $file_outputcommands
#	printf "ssh  -i $file_pem ubuntu@$i -o \"ProxyCommand corkscrew proxy.iisc.ernet.in 3128 $i 22\" \"/home/ubuntu/apache-storm-0.9.4/bin/storm supervisor &\" &>/dev/null &\n" >> $file_outputcommands
	#printf "ssh  -i $file_pem ubuntu@$i -o \"ProxyCommand corkscrew proxy.iisc.ernet.in 3128 $i 22\" \"rm -rf storm-local\"\n" >> $file_outputcommands
	#printf "ssh -i $file_pem ubuntu@$i -o \"ProxyCommand corkscrew proxy.iisc.ernet.in 3128 $i 22\"\n" >> $file_outputcommands
	#printf "ssh -i $file_pem ubuntu@$i -o \"ProxyCommand corkscrew 10.16.40.13 3128 $i 22\"\n" >> $file_outputcommands
#	printf "ssh -i $file_pem ubuntu@$i -o \"ProxyCommand corkscrew proxy.iisc.ernet.in 3128 $i 22\"\n" >> $file_outputcommands
#	printf "scp -r -i $file_pem -o \"ProxyCommand corkscrew proxy.iisc.ernet.in 3128 $i 22\" $file_src ubuntu@$i:$file_dest\n" >> $file_outputcommands
#	printf "scp -r -i $file_pem -o \"ProxyCommand corkscrew proxy.iisc.ernet.in 3128 $i 22\" ubuntu@$i:/home/ubuntu/tetc-final/dataset/output/\'*.log\' ./RECEIVED/\n" >> $file_outputcommands

#	printf "scp  ubuntu@$i:$file_src $path_dest\n" >> $file_outputcommands
path_dest="/Users/anshushukla/PycharmProjects/FullTopoSC/rstorm/cpu/$expNum/$i"

mkdir -p "$path_dest"
	printf " sshpass -p dream@119 scp -r  -o \"ProxyCommand corkscrew proxy.iisc.ernet.in 3128  $i  22\"  anshu@$i:/home/anshu/toplogFinalSC/toplogFloatPI/cpuRstorm-$expNum*  $path_dest/$i-logFileWorkerTOP.txt "
	#scp -r -i $file_pem ubuntu@$i:$file_src $path_dest/$i-logFileWorkerTOP.txt

	#Data from /tmp/ramdisk/
	#scp -r   root@$i:$file_src $path_dest/$i-logFileWorkerTOP.txt

#	scp -r   root@$i:/data/storm/output/logFileWorker-$expNum*  $path_dest/$i-logFileWorkerTOP.txt

sshpass -p dream@119  scp -o "ProxyCommand corkscrew proxy.iisc.ernet.in 3128  $i 22"  anshu@$i:/home/anshu/toplogFinalSC/toplogFloatPI/cpuRstorm-$expNum*  $path_dest
#sshpass -p dream@119  scp -o "ProxyCommand corkscrew proxy.iisc.ernet.in 3128  $i 22"  anshu@$i:/home/anshu/toplogFinalSC/toplogFloatPI/cpuRstorm-$expNum*  $path_dest/$i-logFileWorkerTOP.txt

done
echo DONE

#echo "url1=http://`sed -n '1p' $file_serverinfo`:8080/cloud9-project0-web/echoweb" >> $file_outputcommands
#echo "url2=http://`sed -n '2p' $file_serverinfo`:8080/cloud9-project0-rest/echo" >> $file_outputcommands