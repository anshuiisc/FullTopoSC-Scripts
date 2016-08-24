basepath="/Users/anshushukla/PycharmProjects/FullTopoSC/script/data/"

algo="linear"
# algo="max"
expID="rate-70"

import os
filename1=basepath + algo +"-"+expID+".csv"

# print filename1

print "//"+expID

with open(filename1,"r") as f:
    text = f.readlines()
    for line in text:
        # print line
        entry=line.split(",")
        bolt_name=entry[0]
        threads=float(entry[2])
        total_Cpu = float(entry[4])
        total_Mem = float(entry[6])

        cpu_per_thread_Perc = float(total_Cpu / threads)
        Mem_per_thread_MB = (float(total_Mem / threads))*(3600/100)   # Conversion to MB's
        # print "\n****",bolt_name,cpu_per_thread_Perc,Mem_per_thread_MB

        if("blob" in bolt_name):
            s=" builder.setBolt(\"identityblob\",new AzureBlobDownloadTaskBolt(p_),"+ str(threads)+ ")"
            grouping_string=".shuffleGrouping(\"spout\")"
            mem_string=".setMemoryLoad("+str(Mem_per_thread_MB)+")"
            cpu_string=".setCPULoad("+str(cpu_per_thread_Perc)+");"

            print s+grouping_string+mem_string+cpu_string

        if ("table" in bolt_name):
            s=" builder.setBolt(\"identitytable\",new IdentityTable(sinkLogFileName),"+ str(threads)+ ")"
            grouping_string=".shuffleGrouping(\"identityblob\")"
            mem_string=".setMemoryLoad("+str(Mem_per_thread_MB)+")"
            cpu_string=".setCPULoad("+str(cpu_per_thread_Perc)+");"

            print s+grouping_string+mem_string+cpu_string

        if ("pi" in bolt_name):
            s=" builder.setBolt(\"identitypi\",new IdentityPI(sinkLogFileName),"+ str(threads)+ ")"
            grouping_string=".shuffleGrouping(\"identitytable\")"
            mem_string=".setMemoryLoad("+str(Mem_per_thread_MB)+")"
            cpu_string=".setCPULoad("+str(cpu_per_thread_Perc)+");"

            print s+grouping_string+mem_string+cpu_string

        if ("parse" in bolt_name):
            s=" builder.setBolt(\"identityparse\",new Identity_SAXparser(sinkLogFileName),"+ str(threads)+ ")"
            grouping_string=".shuffleGrouping(\"identitypi\")"
            mem_string=".setMemoryLoad("+str(Mem_per_thread_MB)+")"
            cpu_string=".setCPULoad("+str(cpu_per_thread_Perc)+");"

            print s+grouping_string+mem_string+cpu_string

        if ("batch" in bolt_name):
            s=" builder.setBolt(\"batchFileWriteTaskBolt\",new BatchFileWriteTaskBolt(p_),"+ str(threads)+ ")"
            grouping_string=".shuffleGrouping(\"identityparse\")"
            mem_string=".setMemoryLoad("+str(Mem_per_thread_MB)+")"
            cpu_string=".setCPULoad("+str(cpu_per_thread_Perc)+");"

            print s+grouping_string+mem_string+cpu_string

        # if ("blob" in bolt_name):
        #     s = " builder.setBolt(\"identitytable\",new IdentityTable(sinkLogFileName)," + str(
        #         threads) + ").shuffleGrouping(\"identityblob\").setMemoryLoad(" + str(
        #         Mem_per_thread_MB) + ").setCPULoad(" + str(cpu_per_thread_Perc) + ");"
        #     print s




# builder.setBolt("identityblob",
#                 new
# AzureBlobDownloadTaskBolt(p_), 25)
# .shuffleGrouping("spout").setMemoryLoad(1217.16).setCPULoad(8.6);


#
# builder.setBolt("identitytable",
#             new
# IdentityTable(sinkLogFileName), 17)
# .shuffleGrouping("identityblob").setMemoryLoad(494.11).setCPULoad(2.94);


#
# builder.setBolt("identitypi",
#             new
# IdentityPI(sinkLogFileName), 1)
# .shuffleGrouping("identitytable").setMemoryLoad(253.44).setCPULoad(44.04);


#
# builder.setBolt("identityparse",
#             new
# Identity_SAXparser(sinkLogFileName), 1)
# .shuffleGrouping("identitypi").setMemoryLoad(255.24).setCPULoad(13.7);


#
# builder.setBolt("batchFileWriteTaskBolt",
#             new
# BatchFileWriteTaskBolt(p_), 1)
# .shuffleGrouping("identityparse").setMemoryLoad(0.684).setCPULoad(0.04);