"convert libsvm file to vw format"
"skip malformed lines"

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

i = open( input_file )
o = open( output_file, 'wb' )

for line in i:
	try:
		y, x = line.split( " ", 1 )
	# ValueError: need more than 1 value to unpack
	except ValueError:
		print "line with ValueError (skipping):"
		print line

	new_line = y + " |n " + x
	o.write( new_line )
