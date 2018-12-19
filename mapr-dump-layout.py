#!/usr/bin/env python

import os
import sys
import shutil
import commands

##########################################
# Author: sinchan.roy.89@gmail.com.com
# Apply: MapR 5.X/MapR 6.X
# Usage: change dir to unzipped support dump folder, execute mapr-dump-layout.py
# Option: -p package
# Version: v1.0 (August 4th 2018)
##########################################

### name the output file with hostname and date
st_hostname = commands.getoutput('cat hostname')
date = commands.getoutput('cat system_info/date| grep -i ":" |awk \'{print $2$3}\'')
st_date = date.replace(" ", "-")
st_layout = "mapr-dump-layout_" + st_hostname.strip() + "_" + st_date.strip()
print "file " + st_layout + " will be created under " + os.getcwd() + "\n"

f_dumplayout = open(st_layout,"w+r")


## General Info 
f_dumplayout.write("--uname\n")
f_dumplayout.write(commands.getoutput('cat system_info/uname_a | grep -i linux')+'\n')
f_dumplayout.write("\n")

f_dumplayout.write("--date\n")
f_dumplayout.write(commands.getoutput('cat system_info/date | grep -i ":"')+'\n')
f_dumplayout.write("\n")

f_dumplayout.write("--uptime\n")
f_dumplayout.write(commands.getoutput('cat system_info/uptime  | grep -i up')+'\n')
f_dumplayout.write("\n")

f_dumplayout.write("--release\n")
f_dumplayout.write(commands.getoutput('cat system_info/*release* | grep -i Description | cut -d ":" -f2')+'\n')
f_dumplayout.write("\n")

f_dumplayout.write("--sysinfo\n")
cpu_nr = commands.getoutput('cat system_info/cpuinfo.txt | grep -i core')
ram_all = commands.getoutput('cat system_info/proc_meminfo|grep MemTotal|awk \'{print $2}\'')
ram_nr = float(ram_all)/1024/1024
f_dumplayout.write('total phy memory: %.2f GB\n' %ram_nr)
f_dumplayout.write("\n")


### mounted file systems
f_dumplayout.write('--mount (ext, ocfs2, nfs, gfs, fuse, cifs, btrfs)\n')
f_dumplayout.write(commands.getoutput('cat system_info/proc_mounts | egrep -i "root|mapr|opt|fuse|posix" |egrep -v "xenfs|tmpfs|debugfs|sunrpc|dlmfs|nfsd|config|cgroup"|sort')+'\n')
f_dumplayout.write("\n")

f_dumplayout.write('--network - ifconfig\n')
f_dumplayout.write(commands.getoutput('cat system_info/ifconfig_a |egrep -i "inet|hwaddr"  | egrep -v "ether|loop|UP|127\.0\.0\.1|inet6|vif|tap"')+'\n')
f_dumplayout.write("\n")

f_dumplayout.write('-- mapr-cluster.conf \n')
f_dumplayout.write(commands.getoutput('cat conf/mapr-conf/mapr-clusters.conf')+'\n')
f_dumplayout.write("\n")


f_dumplayout.close()

print "file " + st_layout + " created under " + os.getcwd() + "\n"

