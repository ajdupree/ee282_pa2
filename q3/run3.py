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
##    command = "zsim.sh -a "
##    command += str(app)
##    command += " -c "
##    command += str(cores)
##    print "Running job ", command
##    os.system(command)
##
##print "finished dispatching all jobs"

#############
### part 3 ##
#############

r,w = os.pipe();

root = "/afs/ir/class/ee282/spring13_pa2/bin/zsim.sh"
coreType = ["wide", "narrow"]
fileOut = open("q3_out", "w");

for width in coreType:
  corelist = range(1,9) if width == "wide" else range(1,17)
  
  for cores in corelist:
    print "RUNNING", width, cores
    
    for size in range(256, 32768+256, 256):
      os.chdir("junk")
      call([root, "-S","-a", "blackscholes", "-f" "1700", "-b", width,"-c", str(cores), "--l2size", str(size)], stdout=w, stderr=w)
      os.chdir("../")

      out = os.read(r,1024)
      found = re.search("error", out)
      
      if found != None or size==32768:
          sizeout = size-256 if found!=None else size
          out = width + " " + str(cores) + " " + str(sizeout)
          print out
          fileOut.write(out)
          fileOut.write('\n')
          fileOut.flush()

          os.chdir("data")
          call([root, "-B" "-a", "blackscholes", "-f" "1700", "-b", width,"-c", str(cores), "--l2size", str(sizeout)])
          os.chdir("../")
          break;

fileOut.close()



exit()
