'delete some columns from file, given by their indexes'

import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
headers = sys.argv[3:]

headers = map( int, headers )
headers.sort( reverse = True )

print "%s ---> %s" % ( input_file, output_file )
print "header indices: %s" % ( headers )

i = open( input_file )
o = open( output_file, 'wb' )

reader = csv.reader( i )
writer = csv.writer( o )

counter = 0
for line in reader:

	for h in headers:
		del line[h]

	writer.writerow( line )
	
	counter += 1
	if counter % 10000 == 0:
		print counter


		
		
		
		
		
		
		