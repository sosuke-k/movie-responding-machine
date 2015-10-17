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
class MovieTitlesMetadata
  __storm_table__ = 'movie_titles_metadata'
  movie_id = Int(primary=True)
  movie_title = Unicode()
  movie_year = Int()
  imdb = Int()
  no = Int()

  def __init__(self, movie_id, movie_title, movie_year, imdb, no):
    self.movie_id = movie_id
    self.movie_title = movie_title
    self.movie_year = movie_year
    self.imdb  = imdb
    self.no = no

class MovieGenreLine
  __storm_table__ = 'movie_genre_line'
  id = Int(primary=True)
  movie_id = Int()
  genre_id = Int()
