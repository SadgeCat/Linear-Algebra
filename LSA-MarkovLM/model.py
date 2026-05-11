import numpy as np
import os

from Markov import *
from LSA import *

f = "txt_files/shakespeare.txt"
f2 = "txt_files/shakespeare_full.txt"

p = "./generated_files"

# markov
bigrams = {}
words = []

# LSA
svd = []
word_set = set()
word_indices = {}
word_list = []
text_list = {}
word_context = []
matrix_approx = []
window = 2
k = 5

def run(file):
    build_bigram(file)
    context_based(file)
    apply_svd()

def apply_LSA(cur, next_words, probs):
    for i, word in enumerate(next_words):
        v1 = matrix_approx[word_indices[cur]]
        v2 = matrix_approx[word_indices[word]]
        probs[i] *= cos_sim(v1,v2)
    return probs

def make_text(start, length):
    if isinstance(start, str):
        start = start.lower()
    if start not in bigrams:
        return "Starting word is not in the text."
    if start is None:
        start = random.choice(list(bigrams.keys()))
    res = [start]
    cur = start
    for i in range(length):
        next_words = list(bigrams[cur].keys())      # keys are words that follows the current word
        probs = list(bigrams[cur].values())         # values are probabilities
        probs = apply_LSA(cur, next_words, probs)   # scale by cos sim from svd
        current = np.random.choice(next_words, p=probs)
        res.append(current)
    text = " ".join(res)
    return text

run()
make_text("I", 100)