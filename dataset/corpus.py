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
    __storm_table__ = "movie_titles_metadata"
    CREATE_SQL = "CREATE TABLE " + __storm_table__ + \
        " (id INTEGER PRIMARY KEY, title VARCHAR, year INTEGER, rating INTEGER, votes INTEGER)"
    id = Int(primary=True)
    title = Unicode()
    year = Int()
    rating = Int()
    votes = Int()

    def __init__(self, title, year, rating, votes):
        self.title = title
        self.year = year
        self.rating = rating
        self.votes = votes


class Genre(object):
    __storm_table__ = "genres"
    CREATE_SQL = "CREATE TABLE " + __storm_table__ + " (id INTEGER PRIMARY KEY, name VARCHAR)"
    id = Int(primary=True)
    name = Unicode()

    def __init__(self, name):
        self.name = name


class MovieGenreLine(object):
    __storm_table__ = "movie_genre_lines"
    __storm_primary__ = "movie_id", "genre_id"
    CREATE_SQL = "CREATE TABLE " + __storm_table__ + \
        " (movie_id INTEGER, genre_id INTEGER, PRIMARY KEY (movie_id, genre_id))"
    movie_id = Int()
    genre_id = Int()
