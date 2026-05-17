import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import svds
from collections import Counter

from Markov import clear_bigram, build, build_bigram, print_bigram
from LSA import get_word_list, get_word_list2, get_word_set, context_based, apply_svd, cos_sim

s = "txt_files/test.txt"
f = "txt_files/shakespeare.txt"
f2 = "txt_files/shakespeare_full.txt"
f3 = "txt_files/small_shakespeare.txt"
darwin = "txt_files/darwin.txt"

p = "./generated_files"

def get(f, bigrams, word_list, word_indices, word_set):
    word_counts = Counter(word_list)
    total = 0
    for w1 in bigrams:
        for w2 in bigrams[w1]:
            total += bigrams[w1][w2]
    unique = len(word_set)
    PPMI = lil_matrix((unique, unique), dtype=np.float32)
    for word1 in bigrams:
        idx1 = word_indices[word1]
        for word2 in bigrams[word1]:
            idx2 = word_indices[word2]
            freq = bigrams[word1][word2]
            value = np.log(1.0 * freq * (total-1) / (word_counts[word1] * word_counts[word2]))
            print(f"{word1} {word2}: {value}")
            PPMI[idx1, idx2] = max(0, value)
    return PPMI

# get(s)