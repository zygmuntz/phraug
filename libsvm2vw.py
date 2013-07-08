import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

i = open( input_file )
o = open( output_file, 'wb' )

for line in i:
	y, x = line.split( " ", 1 )
	new_line = y + " |n " + x
	o.write( new_line )