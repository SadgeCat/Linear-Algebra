import numpy as np
import os, random

from Markov import clear_bigram, build, build_bigram, print_bigram
from LSA import get_word_list, get_word_list2, get_word_set, context_based, apply_svd, cos_sim

s = "txt_files/test.txt"
f = "txt_files/shakespeare.txt"
f2 = "txt_files/shakespeare_full.txt"
f3 = "txt_files/small_shakespeare.txt"

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
    global bigrams, words, svd, word_set, word_indices, word_list, text_list, word_context, matrix_approx
    build_bigram(file, bigrams=bigrams)
    context_based(file)
    apply_svd()

def apply_LSA(cur, next_words, probs):
    for i, word in enumerate(next_words):
        v1 = matrix_approx[word_indices[cur]]
        v2 = matrix_approx[word_indices[word]]
        probs[i] *= cos_sim(v1,v2)
        probs = np.array(probs)
        probs = probs / probs.sum()
    return probs

def make_text(start, length):
    # print_bigram(bigrams=bigrams)
    # print(bigrams.keys())
    print(word_indices)
    if isinstance(start, str):
        start = start.lower()
    if start not in bigrams:
        return start + "Starting word is not in the text."
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

run(f3)
print(make_text("why", 100))