'''
split a file into two randomly, line by line. 
Usage: split.py <input file> <output file 1> <output file 2> [<probability of writing to the first file>]'
'''

import csv
import sys
import random

input_file = sys.argv[1]
output_file1 = sys.argv[2]
output_file2 = sys.argv[3]

try:
	P = float( sys.argv[4] )
except IndexError:
	P = 0.9
	
try:
	seed = sys.argv[5]
except IndexError:
	seed = None

try:
	skip_headers = sys.argv[6]
except IndexError:
	skip_headers = False
	
try:
	skip_headers = sys.argv[6]
except IndexError:
	skip_headers = False	
	
print "P = %s" % ( P )

if seed:
	random.seed( seed )

i = open( input_file )
o1 = open( output_file1, 'wb' )
o2 = open( output_file2, 'wb' )

if skip_headers:
	i.readline()

counter = 0

for line in i:
	r = random.random()
	if r > P:
		o2.write( line )
	else:
		o1.write( line )
	
	counter += 1
	if counter % 100000 == 0:
		print counter
	

		
		
		
		
		
		
		
