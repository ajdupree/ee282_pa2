#!/usr/bin/python
from subprocess import call
import os
import sys
import re
###################
### parts 1 and 2 #
###################

##print "Starting Part 1"
##applications = ["blackscholes", "fluidanimate", "streamcluster", "swaptions", "art"]
##for app in applications:
##	for cores in range(1,9):
##		command = "zsim.sh -a "
##		command += str(app)
##		command += " -c "
##		command += str(cores)
##		print "Running job ", command
##		os.system(command)
##
##print "finished dispatching all jobs"

#############
### part 3 ##
#############

r,w = os.pipe();

root = "/afs/ir/class/ee282/spring13_pa2/bin/zsim.sh"

coreType = "wide"
numCores = 8
l2size = 32768

call([root, "-S","-a", "blackscholes", "-f" "1700", "-b", coreType, "-c", str(numCores), "--l2size", str(l2size)], stdout=w, stderr=w);

out = os.read(r,1024)
found = re.search("error", out)

if found == None:
	print "success"
else:
	print "fail"



exit()
