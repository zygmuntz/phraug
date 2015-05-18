#!/usr/bin/env python

"""
Convert CSV file to libsvm format. Works only with numeric variables.
Put -1 as label index (argv[3]) if there are no labels in your file.
Expecting no headers. If present, headers can be skipped with argv[4] == 1.
"""

import sys
import csv

def construct_line( label, line ):
    new_line = []
    if float( label ) == 0.0:
        label = "0"
    new_line.append( label )

    for i, item in line.items() if isinstance(line, dict) else enumerate(line):
        if item == '' or float( item ) == 0.0:
            continue
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

try:
    pivot = int( sys.argv[5] )
except IndexError:
    pivot = -1

i = open( input_file, 'rb' )
o = open( output_file, 'wb' )

reader = csv.reader( i )

if skip_headers:
    headers = reader.next()

 # pivot column "pivot"
if pivot > -1:
    piv = {}
    for line in reader:
        if not piv.has_key(line[pivot]): piv[ line[pivot] ] = {}
        piv[ line[pivot] ][ int(line[ int(not pivot) ]) ] = line[2] if len(line) > 2 else 1
    reader = piv.values()

for line in reader:
    if label_index == -1:
        label = '1'
    else:
        label = line.pop( label_index )

    new_line = construct_line( label, line )
    o.write( new_line )

