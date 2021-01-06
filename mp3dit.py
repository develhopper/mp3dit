#!/usr/bin/env python3
import sys
import eyed3
import os
import glob
import re

def crawl_directory(path):
    return glob.glob(path+"/*.mp3")

def proccess_files():
    global files,regexes
    for audio in files:
        filename=os.path.basename(audio).strip(".mp3")
        print("proccessing file "+filename+".mp3")
        for regex in regexes:
            reg=re.compile(regex["regex"])
            match=reg.search(filename)
            if match:
                change_metadata(audio,getmeta(regex,match))
                break

def getmeta(regex,match):
    global fallbacks;
    result=dict()
    result["artist"]=match.group(regex["artist"]["position"]) if "artist" in regex.keys() else fallbacks["artist"]
    result["title"]=match.group(regex["title"]["position"]) if "title" in regex.keys() else fallbacks["title"]
    result["album"]=match.group(regex["album"]["position"]) if "album" in regex.keys() else fallbacks["album"]
    
    return result

def change_metadata(audio,metadata):
    id3=eyed3.load(audio)
    id3.tag.artist=metadata["artist"]
    id3.tag.album=metadata["album"]
    id3.tag.title=metadata["title"]
    id3.tag.save()

if(len(sys.argv)<3):
    print("usage: mp3dit.py [file or directory] [regex file]")
    exit()

files=list()
regexes=list()
fallbacks=dict()

path=sys.argv[1]

with open(sys.argv[2]) as regex:
    lines=[line.rstrip() for line in regex]
    for line in lines:
        match=re.findall(r"((?<=\{)\w+(?=\}))",line)
        if match:
            r=re.sub(r"\{\w+\}","(.+)",line)            
            items={"regex":r}
            for index,m in enumerate(match,start=1):
                items[m]={"value":"None","position":index}
            regexes.append(items)

if len(regexes)==0:
    print("regex file is empty ...")
    exit()

if os.path.isfile(path):
    files.append(path)
elif os.path.isdir(path):
    files=crawl_directory(path)
else:
    print("invalid input")
    exit()

if len(files)>0:
    fallbacks["artist"]=input("please enter fallback artist name (Empty for None): ") or "None"
    fallbacks["title"]=input("please enter fallback title (Empty for None): ") or "None"
    fallbacks["album"]=input("please enter fallback album name (Empty for None): ") or "None"
    proccess_files()
else:
    print("theres not mp3 file i guess")
    exit()

input("press any key to exit ...")