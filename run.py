#!/usr/bin/python
from subprocess import call
import os
import sys
import re
###################
### part 1       ##
###################

##print "Starting Part 1"
##applications = ["blackscholes", "fluidanimate", "streamcluster", "swaptions", "art"]
##for app in applications:
##  for cores in range(1,9):
##    command = "/afs/ir/class/ee282/spring13_pa2/bin/zsim.sh -a "
##    command += str(app)
##    command += " -c "
##    command += str(cores)
##    print "Running job ", command
##    os.system(command)
##
##print "finished dispatching all jobs"

################
## part 2     ##
################

print "Starting Part 2"
root = "/afs/ir/class/ee282/spring13_pa2/bin/zsim.sh"
for bw in range(1000, 10000+200, 200):
    print "Membw: ", bw
    call([root, "-B", "-a", "art", "-c", "8", "--membw", str(bw)])


#############
### part 3 ##
#############
#print "Starting Part 3"
#r,w = os.pipe();
#
#root = "/afs/ir/class/ee282/spring13_pa2/bin/zsim.sh"
#coreType = ["wide", "narrow"]
#fileOut = open("q3_out", "w");
#
#for width in coreType:
#  corelist = range(1,9) if width == "wide" else range(1,17)
#  
#  for cores in corelist:
#    print "RUNNING", width, cores
#    powers = [2**x for x in range(8,16)]
#    
#    for size in powers:
#      os.chdir("junk")
#      call([root, "-S","-a", "blackscholes", "-f", "1700", "-b", width, "-c", str(cores), "--l2size", str(size)], stdout=w, stderr=w)
#      os.chdir("../")
#
#      out = os.read(r,1024)
#      #print width, cores, size
#      #print out
#      found = re.search("error", out)
#      
#      if found != None or size==32768:
#          sizeout = size/2 if found!=None else size
#          out = width + " " + str(cores) + " " + str(sizeout)
#          print out
#          fileOut.write(out)
#          fileOut.write('\n')
#          fileOut.flush()
#
#          os.chdir("data")
#          call([root, "-B", "-a", "blackscholes", "-f", "1700", "-b", width, "-c", str(cores), "--l2size", str(sizeout)])
#          os.chdir("../")
#          break;
#
#fileOut.close()
#
#
#
#exit()
