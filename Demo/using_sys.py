#!/usr/bin/env python
# Filename: using_sys.py

import sys

print ('The command line arguments are:')
#for i in range(0, len(sys.argv)):
	#print (sys.argv[i])
for i in sys.argv:
	print (i)

print ('\n\nThe PYTHONPATH is',sys.path,'\n')
input()
