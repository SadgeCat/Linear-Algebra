import numpy as np
import re

import os

files = ["txt_files/f1.txt", "txt_files/f2.txt", "txt_files.f3.txt"]

svd = []
word_set = {}
text_list = {}

p = "/txt_files"

for e in os.scandir(p):
    if e.is_file():
        words = []
        with open(e.path, "r") as file:
            content = file.read()
            # words = re.split(r"[,\s;:]+", content.lower())
            words = re.findall(r"\b\w+\b", content.lower())
        words_dict = {}
        for word in words:
            word_set.add(word)
            if word not in words_dict:
                words_dict[word] = 1
            else:
                words_dict[word] += 1
        text_list[e.path] = words_dict

for i in range(len(files)):
    words = []
    with open(files[i], "r") as file:
        content = file.read()
        # words = re.split(r"[,\s;:]+", content.lower())
        words = re.findall(r"\b\w+\b", content.lower())
    words_dict = {}
    for word in words:
        word_set.add(word)
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1
    text_list[files[i]] = words_dict

for text in text_list:
    col = {}
    for word in word_set:
