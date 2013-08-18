"""
compute column means and standard deviations from data in csv file
colstats.py <input file> <output file> [<label index>]
"""

import sys, csv
import numpy as np
from f_is_headers import *

print __doc__

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
	label_index = int( sys.argv[3] )
except IndexError:
	label_index = False
	
i = open( input_file )
reader = csv.reader( i )
writer = csv.writer( open( output_file, 'wb' ))

# check headers

first_line = reader.next()
if not is_headers( first_line ):
	# rewind
	i.seek( 0 )		
	
n = 0
sums_x = 0		# will be a np array
sums_x2 = 0		# will be a np array

for line in reader:
	n += 1
	
	if not label_index is False:
		line.pop( label_index )
	
	x = np.array( map( float, line ))
	x2 = np.square( x )

	sums_x += x
	sums_x2 += x2


# preparation

print n	
print sums_x
print sums_x2
	
means = sums_x / n	
sums2_x = np.square( sums_x )

#print means
#print sums2_x

variances = sums_x2 / n - sums2_x / ( n ** 2 )
standard_deviations = np.sqrt( variances )

#print variances
#print standard_deviations

# save stats

writer.writerow( means )
writer.writerow( standard_deviations )
