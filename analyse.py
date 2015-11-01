#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
from storm.locals import *
from mdcorpus.orm import *
from gensim import corpora

DB_PATH = "dataset/corpus.db"
DIC_PATH = "dataset/dict.txt"

store = Store(create_database("sqlite:" + DB_PATH))
lines = store.find(MovieLine)

dic = corpora.Dictionary()

if os.path.isfile(DIC_PATH):
    print "load " + DIC_PATH
    dic = corpora.Dictionary.load_from_text(DIC_PATH)
else:
    print "create " + DIC_PATH + " from " + DB_PATH
    texts = [line.text.split() for line in lines[:10]]
    dic = corpora.Dictionary(texts)
    dic.save_as_text(DIC_PATH)

print dic.token2id

for line in lines[:10]:
    print ""
    print line.text
    print dic.doc2bow(line.text.split())
