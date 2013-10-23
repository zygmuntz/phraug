"""
Unshuffle previously shuffled file
unshuffle.py input_file.csv output_file.csv <max. lines in memory> <random seed>

"""

import sys
import random

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
	lines_in_memory = int( sys.argv[3] )
except IndexError:
	lines_in_memory = 100000
	
print "caching %s lines at a time..." % ( lines_in_memory )
	
try:
	random_seed = sys.argv[4]
	random.seed( random_seed )
	print "random seed: %s" % ( random_seed )
except IndexError:
	print "need a seed..."
	sys.exit( 1 )
	
# first count

print "counting lines..."

f = open( input_file )

count =  0
for line in f:
	count += 1
	
	if count % 100000 == 0:
		print count
	
print count
		
# then shuffle		

print "(un)shuffling..."

o_f = open( output_file, 'wb' )
	
order = range( count )
random.shuffle( order )

# un-shuffle

order_dict = { shuf_i: orig_i for shuf_i, orig_i in enumerate( order ) }
# sort by original key asc, will get shuffled keys in the right order to unshuffle
order = sorted( order_dict, key = order_dict.get )

epoch = 0
	
while order:

	current_lines = {}
	current_lines_count = 0

	current_chunk = order[:lines_in_memory]
	current_chunk_dict = { x: 1 for x in current_chunk }		# faster "in"
	current_chunk_length = len( current_chunk )
	
	order = order[lines_in_memory:]
	
	f.seek( 0 )
	count = 0
		
	for line in f:
		if count in current_chunk_dict:
			current_lines[count] = line
			current_lines_count += 1
			if current_lines_count == current_chunk_length:
				break
		count += 1	
		if count % 100000 == 0:
			print count		
	
	print "writing..."
	
	for l in current_chunk:
		o_f.write( current_lines[l] )
	
	lines_saved = current_chunk_length + epoch * lines_in_memory
	epoch += 1
	print "pass %s complete (%s lines saved)" % ( epoch, lines_saved )
		