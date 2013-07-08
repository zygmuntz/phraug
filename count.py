'Count lines in a file'

import sys

file_path = sys.argv[1]
f = open( file_path )

count =  0
for line in f:
	count += 1
	
	if count % 100000 == 0:
		print count
	
print count
		
		
		
		
		
		
		