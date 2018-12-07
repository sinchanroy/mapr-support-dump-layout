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




f_dumplayout.close()

