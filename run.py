#!/usr/bin/python
import subprocess
import os

# part 1
print "Starting Part 1"
applications = ["blackscholes", "fluidanimate", "streamcluster", "swaptions", "art"]
for app in applications:
	for cores in range(1,9):
		command = "zsim.sh -a "
		command += str(app)
		command += " -c "
		command += str(cores)
		print "Running job ", command
		os.system(command)

print "finished dispatching all jobs"

