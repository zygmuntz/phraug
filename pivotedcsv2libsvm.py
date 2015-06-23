#!/usr/bin/env python

"""
Convert pivoted CSV file to libsvm format. Works only with numeric variables.
Expecting no labels and no headers. If present, headers can be skipped with argv[4] == 1.

Example call: python pivotedlibsvm2csv.py pivoted.csv output.txt
format: row_id, zero_based_feature_index [, value = 1]

input example:
id1,1
id1,2
id1,3
id2,2,0.5
id2,3,0.6
id2,4,0.7

output example:
1 2:1 3:1 4:1
1 3:0.5 4:0.6 5:0.7

"""

import sys
import csv

def construct_line( label, line ):
	print line
	new_line = []
	if float( label ) == 0.0:
		label = "0"
	new_line.append( label )

	for i_item in line:
		i, item = i_item
		if item == '' or float( item ) == 0.0:
			continue
		new_item = "%s:%s" % ( i + 1, item )
		new_line.append( new_item )
		
	print new_line
	new_line = " ".join( new_line )
	new_line += "\n"
	return new_line

# ---

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
	skip_headers = sys.argv[3]
except IndexError:
	skip_headers = 0

i = open( input_file, 'rb' )
o = open( output_file, 'wb' )

reader = csv.reader( i )

if skip_headers:
	headers = reader.next()


line = reader.next()
current_row = line[0].strip()
current_feature = int( line[1].strip())
current_value = line[2].strip() if len( line ) > 2 else '1'
current_line = [ ( current_feature, current_value ) ]
print current_line

for line in reader:
	row_id = line[0]
	feature_index = int( line[1].strip())
	feature_value = line[2].strip() if len( line ) > 2 else '1'
	
	if row_id != current_row:
		new_line = construct_line( '1', current_line )
		o.write( new_line )	
		
		current_row = row_id
		current_line = [( feature_index, feature_value )]
	else:
		current_line.append(( feature_index, feature_value ))

# the last row
new_line = construct_line( '1', current_line )
o.write( new_line )	
