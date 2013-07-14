'sample lines from input file with probability P, save them to output file'

import csv
import sys
import random

try:
	P = float( sys.argv[3] )
except IndexError:
	P = 0.5
	
print "P = %s" % ( P )

input_file = sys.argv[1]
output_file = sys.argv[2]

i = open( input_file )
o = open( output_file, 'w' )

reader = csv.reader( i )
writer = csv.writer( o )

headers = reader.next()
writer.writerow( headers )

for line in reader:
	r = random.random()
	if r > P:
		continue

	writer.writerow( line )
	

	

		
		
		
		
		
		
		