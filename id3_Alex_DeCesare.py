#!/usr/bin/env python3

"""
Parses a given mp3 from to a string representation of the file contents
"""

import sys

__author__ = 'Alex DeCesare'
__version__ = '22-October-2020'

file_location = sys.argv[1]

def get_file_contents(file_location):
    
    if file_location == '':
        print('file location cannot be empty')
    else:
        try:
            f = open(file_location, 'rb+')
            print(f.read(-1))
        except FileNotFoundError:
            print('The file was not found')

if __name__ == '__main__':
    get_file_contents(file_location)
