#!/bin/bash

for filename in *.mp3
    do echo $filename
    ../id3_alex_decesare.py ./$filename
done
