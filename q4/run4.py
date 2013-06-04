#!/usr/bin/python
from subprocess import call
import os
import sys
import re
###################
### part 1       ##
###################

#print "Starting Part 1"
#applications = ["blackscholes", "fluidanimate", "streamcluster", "swaptions", "art"]
#for app in applications:
#  for cores in range(1,9):
#    command = "/afs/ir/class/ee282/spring13_pa2/bin/zsim.sh -a "
#    command += str(app)
#    command += " -c "
#    command += str(cores)
#    print "Running job ", command
#    os.system(command)
#
#print "finished dispatching all jobs"

################
## part 2     ##
################

#print "Starting Part 2"
#root = "/afs/ir/class/ee282/spring13_pa2/bin/zsim.sh"
#for bw in range(1000, 10000+200, 200):
#    print "Membw: ", bw
#    call([root, "-B", "-a", "art", "-c", "8", "--membw", str(bw)])


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
#fileOut.close()
#exit()

##############
### part 4 ###
##############

#define the whole design space (that we care about)
root = "/afs/ir/class/ee282/spring13_pa2/bin/zsim.sh"
cores = {"wide":range(1,9), "narrow":range(1,17)}
frequencies = range(1500, 4250, 250)
l1sizes = [2**x for x in range(2,7)]
l2sizes = [2**x for x in range(9,10)]
l3sizes = [2**x for x in range(9,15)]
l1ways = [2**x for x in range(0,4)]
l2ways = l3ways = [2**x for x in range(0,6)]

print "l1 size: " + str(l1sizes)
print "l2 size: " + str(l2sizes)
print "l3 size: " + str(l3sizes)
print "l1ways: "  + str(l1ways)
print "l2ways/l3ways: " + str(l2ways)

##D: Performance/energy
numtests=0
frequencies = [4000, 3569, 3230, 2702, 2500];
for cores in [7]:
	for frequency in frequencies:
		if frequency == 4000:
			l1size = 4
			l1way = 1
		elif frequency == 3569:
			l1size = 4
			l1way = 2
		elif frequency == 3230:
			l1size = 8
			l1way = 2
		elif frequency == 2702 or frequency == 2500:
			l1size = 16
			l1way = 2	
		for l2size in l2sizes:
			for l3size in l3sizes[3:]:
				for l2way in l2ways[3:]:
					l3way = l2way
					numtests+=1
					print ''
					print "frequency: "+str(frequency)
					print "cores: " + str(cores)
					print "l1 size: " + str(l1size)
					print "l1 ways: " + str(l1way)
					print "l2 size: " + str(l2size)
					print "l3 size: " + str(l3size)
					print "l2ways  " +  str(l2way)
					print "l3ways  " +  str(l3way)
					call([root, "-B", "-a", "art", "-f", str(frequency), "-c", str(cores), "--l1size", str(l1size), "--l2size", str(l2size), "--l3size", str(l3size), "--l1ways", str(l1way), "--l2ways", str(l2way), "--l3ways", str(l3way)])
print "#TESTS:" + str(numtests)

###C: Performance/area
#numtests = 0
#for l2size in l2sizes[3:]:
#	#l3match = l2size if l2size!=256 else 512  
#	for l2way in l2ways[3:]:
#		for l3size in l3sizes[l3sizes.index(l2size):]:
#			l3way = 2*l2way if (l2way!=32) else 32
#			numtests+=1
#			#print ''
#			#print "l2 size: " + str(l2size)
#			#print "l3 size: " + str(l3size)
#			#print "l2ways  " +  str(l2way)
#			#print "l3ways  " +  str(l3way)
#			call([root, "-B", "-a", "art", "-f", str(4000), "-c", str(4), "--l1size", str(4), "--l2size", str(l2size), "--l3size", str(l3size), "--l1ways", str(1), "--l2ways", str(l2way), "--l3ways", str(l3way)])
#print "#TESTS:" + str(numtests)

##High performance? Let's maximize clock speed.
##Then dial back clock speed and increase cache, see if that gets good stuff.
#root = "/afs/ir/class/ee282/spring13_pa2/bin/zsim.sh"
#
#for k in cores.keys():
#    coreType = k;
#    numCores = cores[k][len(cores[k])-1];
#    print numCores
#    frequency = frequencies[len(frequencies)-1]
#    l1size = l1sizes[len(l1sizes)-1]
#    l2size = l2sizes[len(l2sizes)-1]
#    l3size = l3sizes[len(l3sizes)-1]
#    l1way = l1ways[len(l1ways)-1]
#    l2way = l2ways[len(l2ways)-1]
#    l3way = l3ways[len(l3ways)-1]
#    call([root, "-B", "-a", "art", "-f", str(frequency), "-b", coreType, "-c", str(numCores), "--l1size", str(l1size), "--l2size", str(l2size), "--l3size", str(l3size), "--l1ways", str(l1way), "--l2ways", str(l2way), "--l3ways", str(l3way)])
#
##Minimize energy?
##Everything smallest! Then try increasing cache size a little bit.
##The decrease in execution time might actually balance out increase in dynamic power.
#for k in cores.keys():
#    coreType = k;
#    numCores = cores[k][0];
#    print numCores
#    frequency = frequencies[0]
#    l1size  = l1sizes[0]
#    l2size  = l2sizes[0]
#    l3size  = l3sizes[0]
#    l1way = l1ways[0]
#    l2way = l2ways[0]
#    l3way = l3ways[0]
#    call([root, "-B", "-a", "art", "-f", str(frequency), "-b", coreType, "-c", str(numCores), "--l1size", str(l1size), "--l2size", str(l2size), "--l3size", str(l3size), "--l1ways", str(l1way), "--l2ways", str(l2way), "--l3ways", str(l3way)])
