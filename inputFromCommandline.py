#!/usr/bin/python

import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

args = str(sys.argv).split()
for arg in args:
    print(arg)

## We can get inputs from command line by using "getopt"
## module

