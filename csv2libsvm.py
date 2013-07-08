'Convert CSV file to libsvm format. '
'Expecting no headers. If present, headers can be skipped with argv[4] == true.'
'-1 for label index if no label in file'

import sys
import csv

def construct_line( label, line ):
	new_line = []
	if float( label ) == 0.0:
		label = "0"
	new_line.append( label )
	
	for i, item in enumerate( line ):
		if float( item ) == 0.0:
			continue	# sparse!!!
		new_item = "%s:%s" % ( i + 1, item )
		new_line.append( new_item )
	new_line = " ".join( new_line )
	new_line += "\n"
	return new_line

# ---

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
	label_index = int( sys.argv[3] )
except IndexError:
	label_index = 0
	
try:
	skip_headers = sys.argv[4]
except IndexError:
	skip_headers = 0	

i = open( input_file )
o = open( output_file, 'w' )

reader = csv.reader( i )
if skip_headers:
	headers = reader.next()

for line in reader:
	if label_index == -1:
		label = 0
	else:
		label = line.pop( label_index )
		
	new_line = construct_line( label, line )
	o.write( new_line )