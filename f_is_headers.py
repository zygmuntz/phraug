import re

def is_headers( line ):
	line = ''.join( line )
	if re.match( '.*[a-df-zA-Z].*', line ):
		return True
		
		