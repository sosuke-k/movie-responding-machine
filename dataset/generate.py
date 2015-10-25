#!/usr/bin/python
# -*- coding: utf-8 -*-

from sets import Set
from storm.locals import *
from corpus import *

MOVIE_TITLES_METADATA_PATH = 'dataset/cornell movie-dialogs corpus/movie_titles_metadata.txt'
DB_PATH = "dataset/corpus.db"

print "CREATE " + DB_PATH
database = create_database("sqlite:" + DB_PATH)
store = Store(database)

print MovieTitlesMetadata.CREATE_SQL
store.execute(MovieTitlesMetadata.CREATE_SQL)
store.commit()

print Genre.CREATE_SQL
store.execute(Genre.CREATE_SQL)
store.commit()

print MovieGenreLine.CREATE_SQL
store.execute(MovieGenreLine.CREATE_SQL)
store.commit()

f = open(MOVIE_TITLES_METADATA_PATH)
genres = Set([])
line = f.readline()
while line:
    genrelist = line.split(' +++$+++ ')[5][1:-2].split(', ')
    for genre in genrelist:
        if genre != '':
            genres.add(genre[1:-1])
    line = f.readline()
f.close
print "genre list:"
for genre_name in genres:
    print genre_name
    genre = Genre(genre_name.decode('utf-8'))
    store.add(genre)
store.commit()
