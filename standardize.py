'standardize (shift and scale to zero mean and unit standard deviation) data from csv file'
'meant to be used together with colstats.py'
'standardize.py <stats file> <input file> <output file> [<label index>]'

import sys, csv
import numpy as np
from f_is_headers import *

stats_file = sys.argv[1]
input_file = sys.argv[2]
output_file = sys.argv[3]

try:
	label_index = int( sys.argv[4] )
except IndexError:
	label_index = False
	
i = open( input_file )	
stats_reader = csv.reader( open( stats_file ))	
reader = csv.reader( i )
writer = csv.writer( open( output_file, 'wb' ))

# get stats

means = stats_reader.next()
means = np.array( map( float, means ))

standard_deviations = stats_reader.next()
standard_deviations = np.array( map( float, standard_deviations ))

# check headers

first_line = reader.next()
if is_headers( first_line ):
	headers = first_line
else:
	headers = False
	i.seek( 0 )
	
# go

for line in reader:
	
	if not label_index is False:
		l = line.pop( label_index )	
		print l
		
	x = np.array( map( float, line ))
	
	# shift and scale
	x = x - means
	x = x / standard_deviations
	
	if not label_index is False:
		# -1.0,...
		#x = np.insert( x, 0, l )
		line = list( x )
		line.insert( 0, l )
	
	writer.writerow( line )
	
