#!/bin/bash

for filename in *.mp3
    do echo $filename
    "$(dirname "$(readlink -f -- "$0")")"/id3_alex_decesare.py ./$filename
done
