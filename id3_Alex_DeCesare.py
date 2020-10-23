#!/usr/bin/env python3

"""
Parses a given mp3 from to a string representation of the file contents
"""

import sys

__author__ = 'Alex DeCesare'
__version__ = '22-October-2020'

file_location = sys.argv[1]


def parse_mp3_file():
   
    mp3_file = get_file(file_location)
    mp3_file.seek(-128,2)
    
    if str(mp3_file.read(3), 'utf-8') == 'TAG':

        mp3_contents = {

                    'title' : str(mp3_file.read(30), 'utf-8'),
                    'artist' : str(mp3_file.read(30), 'utf-8'),
                    'album' : str(mp3_file.read(30), 'utf-8'),
                    'year' : str(mp3_file.read(4), 'utf-8'),
                    'comment' : str(mp3_file.read(28), 'utf-8')
                        
                }
        mp3_output = 'Title: ' + mp3_contents['title'] + '\n' \
        + 'Artist: ' + mp3_contents['artist'] + '\n' \
        + 'Album: ' + mp3_contents['album'] + '\n' \
        + 'Year: ' + mp3_contents['year'] + '\n' \
        + 'Comment: ' + mp3_contents['comment']
        
        print(mp3_output)
        mp3_file.close()

    else:
        print('No ID3 information')

def get_file(file_location):

    if file_location == '':
        print('file location cannot be empty')
    else:
        try:
            mp3_file = open(file_location, 'rb')
            return mp3_file

        except FileNotFoundError:
            print('The file was not found')


if __name__ == '__main__':
    get_file(file_location)
    parse_mp3_file()
