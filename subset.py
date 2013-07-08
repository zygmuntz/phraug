'Save a subset of lines from an input file; start at offset and count n lines'
'default 100 lines starting from 0'

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
try:
	offset = int( sys.argv[3] )
except IndexError:
	offset = 0
	
try:
	lines = int( sys.argv[4] )
except IndexError:
	lines = 100	


i = open( input_file )
o = open( output_file, 'wb' )

count =  0
for line in i:

	if offset > 0:
		offset -= 1
		continue

	o.write( line )
	count += 1
	
	if count >= lines:
		break
	

		
		
		
		
		
		
		