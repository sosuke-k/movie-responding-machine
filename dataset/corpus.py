#!/usr/bin/python
# -*- coding: utf-8 -*-

from storm.locals import *

# - movie_titles_metadata.txt
# 	- contains information about each movie title
# 	- fields:
# 		- movieID,
# 		- movie title,
# 		- movie year,
# 		- IMDB rating,
# 		- no. IMDB votes,
# 		- genres in the format ['genre1','genre2',�,'genreN']


class MovieTitlesMetadata(object):
    CREATE_SQL = "CREATE TABLE movie_titles_metadata (id INTEGER PRIMARY KEY, movie_title VARCHAR, movie_year INTEGER, imdb INTEGER, no INTEGER)"
    __storm_table__ = "movie_titles_metadata"
    id = Int(primary=True)
    movie_title = Unicode()
    movie_year = Int()
    imdb = Int()
    no = Int()


class Genre(object):
    __storm_table__ = "genre"
    id = Int(primary=True)
    name = Unicode()


class MovieGenreLine(object):
    __storm_table__ = "movie_genre_line"
    id = Int(primary=True)
    movie_id = Int()
    genre_id = Int()
