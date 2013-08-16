#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyper import R


class supervisedLDA():

    def __init__(self, alpha=1.0, numtopics=5, eta=0.1, logistic=True, lamda=1.0, e_iter=10, m_iter=4, variance=0.25):
        self.params = {
            "numtopics": numtopics,
            "alpha": alpha,
            "eta": eta,
            "logistic": logistic,
            "lambda": lamda,
            "e_iter": e_iter,
            "m_iter": m_iter,
            "variance": variance
        }
        self.r = R(use_pandas=True, use_numpy=True)
        self.assign_R_params()

    def update_params(self, param_name, param_value):
        self.params[param_name] = param_value

    def assign_R_params(self):
        for (key, value) in self.params.iteritems():
            self.r.assign(key, value)

    def train(self, documents, labels):
        self.r.assign("documents", documents)
        self.r.assign("labels", labels)
        self.r.run('source("trainLDA.R")')
        topics = self.r["topics"]
        model = self.r["model"]
        print "Got relevant variables"

    def predict(self, documents, model, vocabulary, num_iter=10, avg_iter=5):
        self.r.assign("documents", documents)
        self.r.assign("trainedModel", model)
        self.r.assign("vocabulary", vocabulary)
        self.r.run('source("testLDA.R")')

    def save_model(self, model_filename, vocab_filename):
        self.r.assign("model_filename", model_filename)
        self.r.assign("vocab_filename", vocab_filename)
        self.r.run('source("saveModel.R")')

    def load_model(self, model_filename, vocab_filename):
        self.r.run('source("loadModel.R")')
        model = self.r["model"]
        vocab = self.r["vocab"]
        topics = self.r["topics"]
        self.update_params("model", model)
        self.update_params("vocab", vocab)
        self.update_params("topics", topics)
