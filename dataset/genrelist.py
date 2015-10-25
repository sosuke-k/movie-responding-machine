#!/usr/bin/python
# -*- coding: utf-8 -*-

from sets import Set

filepath = 'cornell movie-dialogs corpus/movie_titles_metadata.txt'
genres = Set([])

f = open(filepath)
line = f.readline()
print genres
while line:
    genrelist = line.split(' +++$+++ ')[5][1:-2].split(', ')
    for genre in genrelist:
        if genre != '':
            genres.add(genre[1:-1])
    line = f.readline()
f.close

print genres
