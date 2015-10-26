#!/usr/bin/python
# -*- coding: utf-8 -*-

from sets import Set
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
        " (id INTEGER PRIMARY KEY, title VARCHAR, year INTEGER, rating FLOAT, votes INTEGER)"
    id = Int(primary=True)
    title = Unicode()
    year = Int()
    rating = Float()
    votes = Int()

    def __init__(self, id, title, year, rating, votes):
        self.id = id
        self.title = title.decode("utf-8")
        self.year = year
        self.rating = rating
        self.votes = votes


class Genre(object):
    __storm_table__ = "genres"
    CREATE_SQL = "CREATE TABLE " + __storm_table__ + " (id INTEGER PRIMARY KEY, name VARCHAR)"
    id = Int(primary=True)
    name = Unicode()

    def __init__(self, name):
        self.name = name.decode("utf-8")


class MovieGenreLine(object):
    __storm_table__ = "movie_genre_lines"
    __storm_primary__ = "movie_id", "genre_id"
    CREATE_SQL = "CREATE TABLE " + __storm_table__ + \
        " (movie_id INTEGER, genre_id INTEGER, PRIMARY KEY (movie_id, genre_id))"
    movie_id = Int()
    genre_id = Int()


class Parser:

    def __init__(self, separator=" +++$+++ "):
        self.separator = separator

    def movie_titles_metadata(self, line):
        metadata = line.split(self.separator)
        id = int(metadata[0][1:])                   # e.g. m0
        title = metadata[1]                         # e.g. 10 things i hate about you
        year = int(metadata[2][0:4])                # e.g. 1999
        rating = float(metadata[3])                 # e.g. 6.90
        votes = int(metadata[4])                    # e.g. 62847
        genre_list = metadata[5][1:-2].split(", ")  # e.g. ['comedy', 'romance']\n
        genres = Set([])
        for genre_name in genre_list:
            if genre_name != "":
                genres.add(genre_name[1:-1])
        return [id, title, year, rating, votes, genres]
