"convert a file from libsvm format to VW format"
"in case of binary classification with 0/1 labels set the third argument to True"
"this will convert labels to -1/1"

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
try:
	convert_zero_to_negative_one = bool( sys.argv[3] )
except IndexError:
	convert_zero_to_negative_one = False

i = open( input_file )
o = open( output_file, 'wb' )

for line in i:
	y, x = line.split( " ", 1 )
	if convert_zero_to_negative_one and y == '0':
		y = '-1'
	new_line = y + " |n " + x
	o.write( new_line )
	