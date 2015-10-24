#!/usr/bin/python
# -*- coding: utf-8 -*-

from storm.locals import *
from corpus import *

database = create_database("sqlite:dataset/corpus.db")
store = Store(database)

print MovieTitlesMetadata.CREATE_SQL

# store.execute("CREATE TABLE movie_titles_metadata (id INTEGER PRIMARY KEY, ")
