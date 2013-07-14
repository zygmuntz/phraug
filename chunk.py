'''
split a file into a given number of chunks randomly, line by line. 
Usage: chunk.py <input file> <number of chunks> [<seed>]'
'''

import sys, random, os

input_file = sys.argv[1]
num_chunks = int( sys.argv[2] )

try:
	seed = sys.argv[3]
except IndexError:
	seed = None
	
if seed:
	print "seeding: %s" % ( seed )
	random.seed( seed )

basename = os.path.basename( input_file )
basename, ext = os.path.splitext( basename )

i = open( input_file )

os = {}
for n in range( num_chunks ):
	output_file = "%s_%s%s" % ( basename, n, ext )
	os[n] = open( output_file, 'wb' )

counter = 0

for line in i:
	n = random.randint( 0, num_chunks - 1 )
	os[n].write( line )
	
	counter += 1
	if counter % 100000 == 0:
		print counter
	

		
		
		
		
		
		
		