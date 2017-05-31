#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from chatterbot.logic import LogicAdapter
from textblob.classifiers import NaiveBayesClassifier
from chatterbot.conversation import Statement
from chatterbot.database import Database
import os
import json
import inspect
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier


class QueryAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        super(QueryAdapter, self).__init__(**kwargs)
        training_file = '%s/../database/%s.json' % (
            os.path.dirname(os.path.realpath(inspect.getfile(self.__class__))),
            kwargs.get('training_file_for_query')
            )
        training_database = json.load(open(training_file))['data']
        training_data = [(data,int(classe)) for classe in ["0", "1"] for data in training_database[classe]]
        self.classifier = NaiveBayesClassifier(training_data)

        self.partners = Database('partners_fake', parse_db=True) #default fixed to partners
        self.fields = Database('fields') #lexical fields of different features in db
        self.clf = self.train_feature_finder(self.fields.db, RandomForestClassifier(n_estimators=20))

    def process(self, statement):
        
        confidence = self.classifier.classify(statement.text.lower())
        entry, query = self.build_query(statement.text.lower())
        if entry is None:
            if query is None:
                response = Statement('Je sais que tu cherches a savoir quelquechose sur les partners LV, mais je vais avoir besoin que tu me clarifies tout ça !')
            else:
                response = Statement("Hmm tu cherches un/une %s. Donne moi plus d'indice !" % query)
        else:
            if query is None:
                response = Statement("Hmm tu cherches une info a propos de %s... Dis moi ce que tu veux savoir exactement stp !" % entry[1])
            else:
                element = self.get_element(entry, query)
                response = Statement("Voila ce que j'ai pour toi : \n\t %s, %s" % (entry[1], element))

        return confidence, response

    def train_feature_finder(self, training_db, clf):
        training_sentences = []
        c = 0
        training_classes = []
        self.class_names = []
        self.vectorizer = CountVectorizer(analyzer = "word",   \
                              tokenizer = None,    \
                              preprocessor = None, \
                              stop_words = None,   \
                              max_features = 500)
        for key, value in training_db.iteritems():
            training_sentences += value
            training_classes += [c for i in range(len(value))] 
            c+=1
            self.class_names.append(key)
        train_data_features = self.vectorizer.fit_transform(training_sentences)
        train_data_features = train_data_features.toarray()
        clf = clf.fit( train_data_features, training_classes)
        return clf

    def predict_feature(self, sentence):
        sentence_vect = self.vectorizer.transform([sentence])
        sentence_vect = sentence_vect.toarray()
        class_id = self.clf.predict(sentence_vect)
        class_id = class_id[0]
        feature = self.class_names[class_id]
        return feature

    def predict_filter_key(self, sentence):
        for chunk in sentence.split():
            for feature in self.partners.index:
                if self.is_in_field_of_value(chunk, self.partners.index[feature]):
                    entry = (feature, chunk)
                    return entry

    def get_element(self, entry, query):
        for partner in self.partners.db:
            if entry[1] in partner[entry[0]]:
                return partner[query]
        return None

    def is_in_field_of_value(self, chunk, list_of_values):
        return (chunk in list_of_values)

    def build_query(self, statement):
        entry = None
        query = None
        query = self.predict_feature(statement)
        entry = self.predict_filter_key(statement)
        
        return entry, query

