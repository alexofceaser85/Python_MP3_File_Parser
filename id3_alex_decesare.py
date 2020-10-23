#!/usr/bin/env python3

"""
Parses a given mp3 from to a string representation of the file contents
"""

import sys

__author__ = 'Alex DeCesare'
__version__ = '22-October-2020'

def parse_mp3_file():

    """
    parses the data in the mp3 file
    """

    try:
        file_location_input = sys.argv[1]
        mp3_file = open(file_location_input, 'rb')
        mp3_file.seek(-128, 2)

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
            + 'Comment: ' + mp3_contents['comment'] + '\n'

            print(mp3_output)
            mp3_file.close()
        else:
            print('No ID3 information')

    except FileNotFoundError:
        print('file was not found')
    except IndexError:
        print('please add the path to an mp3 file as a command line argument')

if __name__ == '__main__':
    parse_mp3_file()
