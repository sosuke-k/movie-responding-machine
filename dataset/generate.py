#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sets import Set
from storm.locals import *
from mdcorpus.mdcorpus import *
from mdcorpus.parser import *

MOVIE_TITLES_METADATA_PATH = "dataset/cornell movie-dialogs corpus/movie_titles_metadata.txt"
# DB_PATH = "dataset/corpus.db"

# print "CREATE " + DB_PATH
database = create_database("sqlite:")
store = Store(database)
store.execute(MovieTitlesMetadata.CREATE_SQL)
store.execute(Genre.CREATE_SQL)
store.execute(MovieGenreLine.CREATE_SQL)

parser = Parser()

f = open(MOVIE_TITLES_METADATA_PATH)
genres = Set([])
line = f.readline()
while line:
    list = parser.movie_titles_metadata(line)
    genre_set = list.pop()
    for genre_name in genre_set:
        if genre_name != '':
            genres.add(genre_name)
    line = f.readline()
f.close
print "genre list:"
for genre_name in genres:
    print genre_name
    store.add(Genre(genre_name))
store.flush()

f = open(MOVIE_TITLES_METADATA_PATH)
line = f.readline()
while line:
    print line
    list = parser.movie_titles_metadata(line)
    genre_set = list.pop()
    movie = store.add(MovieTitlesMetadata(*list))

    for genre_name in genre_set:
        genre = store.find(Genre, Genre.name == genre_name.decode('utf-8')).one()
        movie.genres.add(genre)

    store.commit()
    line = f.readline()
f.close
