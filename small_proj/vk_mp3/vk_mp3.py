#!/usr/bin/python3
#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
#from stagger.id3 import *
from urllib.request import urlopen
import os.path

output_dir = 'vk_mp3'
fname = "vk_song.html"
f = open(fname, encoding="windows-1251", errors="surrogateescape")
html_content = f.read()
soup = BeautifulSoup(html_content)
max_song = 20
cnt = 0
for song_item in soup.findAll("input", {"type": "hidden"}):
    cnt += 1
    if cnt >= max_song:
        break
    url = song_item['value']
    author = song_item.findNext('a').string
    track_name = song_item.findNext('a').findNext('a').string
    if not track_name:
        continue
    if not author:
        author = "None"
    out_file_name = output_dir + '/' + author + " - " + track_name + ".mp3"
    if os.path.isfile(out_file_name):
        print("file:", out_file_name, "already exists!")
        continue

    print("process: " + author + " " + track_name)
    try:
        mp3 = urlopen(url)
    except:
        print('Sorry, cant open, move on!')
        continue
    with open(out_file_name, 'wb') as f:
        f.write(mp3.read())
#    try:
#        tag = stagger.read_tag(out_file_name)
#        tag.title = track_name
#        tag.author = author
#        tag.write()
#    except:
#        print('Sorry, no tag for you')
