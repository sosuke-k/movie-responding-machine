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

MovieTitlesMetadata.genres = ReferenceSet(MovieTitlesMetadata.id,
                                          MovieGenreLine.movie_id,
                                          MovieGenreLine.genre_id,
                                          Genre.id)

f = open(MOVIE_TITLES_METADATA_PATH)
genres = Set([])
line = f.readline()
while line:
    genre_list = line.split(' +++$+++ ')[5][1:-2].split(', ')
    for genre in genre_list:
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

f = open(MOVIE_TITLES_METADATA_PATH)
line = f.readline()
while line:
    metadata = line.split(' +++$+++ ')
    id = int(metadata[0][1:])
    title = metadata[1]
    year = int(metadata[2][0:4])
    rating = float(metadata[3])
    votes = int(metadata[4])
    movie = MovieTitlesMetadata(id, title.decode('utf-8'), year, rating, votes)
    store.add(movie)
    store.commit()

    genre_list = metadata[5][1:-2].split(', ')
    for genre_name in genre_list:
        if genre_name != '':
            genre = store.find(Genre, Genre.name == genre_name.decode('utf-8')).one()
            movie.genres.add(genre)

    store.commit()
    line = f.readline()
f.close
