# -*- coding: utf-8 -*-
"""Testing for RNNNumpy"""

from pprint import pprint
from unittest import TestCase
import nose
from nose.tools import eq_
import numpy as np
from rnn import RNNNumpy

unknown_token = "UNKNOWN_TOKEN"
sentence_start_token = "SENTENCE_START"
sentence_end_token = "SENTENCE_END"

index_to_word = [sentence_start_token, sentence_end_token, "you",
                 "choosing", "are", "one", "I", "am", "a", "man", "ordinary"]
index_to_word.append(unknown_token)
word_to_index = dict([(w, i) for i, w in enumerate(index_to_word)])

vocabulary_size = len(index_to_word)
hidden_size = 3


class RNNNumpyTestCase(TestCase):

    def setUp(self):
        print ""
        np.random.seed(10)
        self.x_train = np.array([1, 4, 7])
        self.model = RNNNumpy(vocabulary_size, hidden_dim=hidden_size)

    def tearDown(self):
        print "done"

    def test_init(self):
        eq_(self.model.word_dim, vocabulary_size)
        eq_(self.model.hidden_dim, hidden_size)

    def test_forward_propagation(self):
        # print type(self.x_train) # <type 'numpy.ndarray'>
        o, s = self.model.forward_propagation(self.x_train)
        eq_(o.shape, (len(self.x_train), vocabulary_size))
        pprint(o)

    def test_predict(self):
        predictions = self.model.predict(self.x_train)
        pprint(predictions)
