# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z9Bq44ihp9D_z3h5kZVZtPUFopdbHtD5

IMPORTING LIBRARIES
"""

import itertools
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

"""LOADING THE NEWS DATASET

"""

news_df = pd.read_csv('news.csv')

news_df

news_df.head()

"""CHECKING FOR NULL VALUES IN THE DATASET"""

news_df.isnull().sum()

"""DIMENSIONS OF THE DATASET"""

news_df.shape

"""SPLIT THE NEWS AND THE LABELS"""

labels = news_df.label.copy()
news = news_df.text.copy()

"""INITIALIZE THE tf-idf VECTORIZER"""

tfidf_vec = TfidfVectorizer(stop_words='english', max_df=0.7)

"""FIT THE VECTORIZER TO THE DATA"""

news = tfidf_vec.fit_transform(news)

"""SPLIT THE TRAINING AND THE TESTING DATA"""

x_train, x_test, y_train, y_test = train_test_split(news, labels, test_size=0.2, random_state=42, stratify=labels)

"""INITIALIZE A PASSIVEAGGRESSIVECLASSIFIER"""

pac = PassiveAggressiveClassifier()

"""FIT THE CLASSIFIER TO HE TRAINING DATA"""

pac.fit(x_train, y_train)

PassiveAggressiveClassifier()

"""PREDICT THE LABELS OF THE TEST DATASET"""

y_pred = pac.predict(x_test)

"""EVALUATION OR PERFORMANCE METRICE"""

score = accuracy_score(y_test, y_pred)

score

confusion_matrix(y_test, y_pred, labels=['FAKE', 'REAL'])