import numpy as np
import re, random, os

# test = "txt_files/test.txt"
f = "txt_files/shakespeare.txt"
f2 = "txt_files/shakespeare_full.txt"

p = "./generated_files"

# bigrams = {}
# words = []

def clear_bigram(bigrams):
    bigrams.clear()

def print_bigram(bigrams):
    # for key in bigrams:
    #     print(key)
    print(bigrams.keys())

def build(path):
    for e in os.scandir(path):
        if e.is_file():
            build_bigram(e)

def build_bigram(filename, bigrams):
    with open(filename, "r") as file:
        content = file.read()
        # words = re.split(r"[,\s;:]+", content.lower())
        words = re.findall(r"\b\w+\b", content.lower())

    for i in range(len(words)-1):
        if words[i] not in bigrams:
            bigrams[words[i]] = {}
        if words[i+1] not in bigrams[words[i]]:
            bigrams[words[i]][words[i+1]] = 1
        else:
            bigrams[words[i]][words[i+1]] += 1

    for key in bigrams:
        total = 0
        for subkey in bigrams[key]:
            total += bigrams[key][subkey]
        for subkey in bigrams[key]:
            bigrams[key][subkey] *= (1.0 / total)
    
    # print(bigrams)


def gen_text(start, length, bigrams):
    if isinstance(start, str):
        start = start.lower()
    if start not in bigrams:
        return "Starting word is not in the text."
    if start is None:
        start = random.choice(list(bigrams.keys()))
    res = [start]
    cur = start
    for i in range(length):
        next_words = list(bigrams[cur].keys())
        probs = list(bigrams[cur].values())
        current = np.random.choice(next_words, p=probs)
        res.append(current)
    text = " ".join(res)
    return text

# while True:
#     print(eval(input()))