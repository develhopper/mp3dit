# mp3dit

story: i downloaded some sort of music from a website and find out music files metadata tags such as artist name and album name and song title are manipulated and missing

so i decide to write a script to change metadata tags of mp3 files in a directory based on file name

and here we go

## dependencies

`` pip install eyed3 ``

## usage

`` mp3dit.py [mp3file or folder] [regex file] ``

## examples

write your searching patterns in a file like regex.sample and place it somewhere in your hard disk

if the song file names are in a format like below

6 - Billie Eilish - copycat.mp3
7 - Billie Eilish - six feet under.mp3

so the searching pattern should be like this

\d+ \- {artist} \- {title}

write each pattern in one line

and run the script as below

`` python mp3dit ./Music/Billie-Eilish ./regex.txt ``

and let it do its job

it will find each mp3 file in that directory that matching patterns mentioned in regex.txt
and it will change mp3 tags as you described
