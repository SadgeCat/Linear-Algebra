import numpy as np
import os, random, re

from Markov import clear_bigram, build, build_bigram, print_bigram
from LSA import get_word_list, get_word_list2, get_word_set, context_based, apply_svd, cos_sim
from PPMI import get

s = "txt_files/test.txt"
f = "txt_files/shakespeare.txt"
f2 = "txt_files/shakespeare_full.txt"
f3 = "txt_files/small_shakespeare.txt"
darwin = "txt_files/darwin.txt"

p = "./text_made"

# markov
bigrams = {}
raw_bigrams = {}
words = []

# LSA
word_set = set()
word_indices = {}
word_list = []
text_list = {}
word_context = []
matrix_approx = []
window = 5
K = 50
LSA_const = 0.2

## PPMI
PPMI_scores = []

def run(file):
    global bigrams, raw_bigrams, words, word_set, word_indices, word_list, text_list, word_context, matrix_approx, PPMI_scores
    bigrams, raw_bigrams = build_bigram(file)
    word_list, word_indices, word_set = get_word_set(file)
    word_context = context_based(file, window)
    matrix_approx = apply_svd(K, word_context=word_context)
    PPMI_scores = get(file, raw_bigrams, word_list, word_indices, word_set)

def apply_LSA(cur, next_words, probs):
    newprobs = [0] * len(next_words)
    for i, word in enumerate(next_words):
        idx1 = word_indices[cur]
        idx2 = word_indices[word]
        v1 = matrix_approx[idx1]
        v2 = matrix_approx[idx2]
        newprobs[i] = max(0, probs[i] * (1 + LSA_const * cos_sim(v1,v2)))     # applying cos sim
        newprobs[i] *= PPMI_scores[idx1, idx2]           # applying PPMI
    newprobs = np.array(newprobs)
    newprobs = newprobs / newprobs.sum()
    return newprobs

def make_text(start, length):
    # print_bigram(bigrams=bigrams)
    # print(bigrams.keys())
    # print(word_indices)
    if isinstance(start, str):
        start = start.lower()
    if start not in bigrams:
        return start + "Starting word is not in the text."
    if start is None:
        start = random.choice(list(bigrams.keys()))
    res = [start]
    text = start
    cur = start
    for i in range(length):
        next_words = list(bigrams[cur].keys())      # keys are words that follows the current word
        probs = list(bigrams[cur].values())         # values are probabilities
        probs = apply_LSA(cur, next_words, probs)   # scale by cos sim from svd
        current = np.random.choice(next_words, p=probs)
        res.append(current)
        cur = current

        if re.search(r"[.,:?!]", current) == None:
            text += " " + current
        else:
            text += current

    # text = " ".join(res)
    text.strip()
    return text

run(darwin)
print(make_text("I", 100))

with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")