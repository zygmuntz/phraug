import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

i = open( input_file )
o = open( output_file, 'wb' )

reader = csv.reader( i, delimiter = '\t' )
writer = csv.writer( o )

for line in reader:
	writer.writerow( line )
