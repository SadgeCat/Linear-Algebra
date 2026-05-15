import numpy as np
import re, os

# files = ["txt_files/f1.txt", "txt_files/f2.txt", "txt_files.f3.txt"]

# svd = []
# word_set = set()
# word_indices = {}
# word_list = []
# text_list = {}
# word_context = []
# window = 2
# k = 5
# matrix_approx = []

f = "txt_files/shakespeare.txt"
f2 = "txt_files/shakespeare_full.txt"
f3 = "txt_files/small_shakespeare.txt"

# p = "./txt_files"
p = "./generated_files"

def get_word_list(path, word_list):
    for e in os.scandir(path):
        if e.is_file():
            words = []
            with open(e.path, "r") as file:
                content = file.read()
                words = re.findall(r"\b\w+\b", content.lower())
            word_list.extend(words)

def get_word_list2(file):
    with open(file, "r") as f:
        content = f.read()
        word_list = re.findall(r"\b\w+\b", content.lower())
    return word_list

def get_word_set(path):
    # get_word_list(path)
    word_list = get_word_list2(path)
    word_set = set(word_list)
    word_indices = {}
    idx = 0
    for word in word_set:
        word_indices[word] = idx
        idx += 1
    # word_indices = {
    #     word:i for i, word in enumerate(word_set)
    # }
    return word_indices, word_set

def context_based(path, word_list, window):
    word_indices, word_set = get_word_set(path)
    word_context = np.zeros((len(word_set), len(word_set)))
    for i, word in enumerate(word_list):
        target_idx = word_indices[word]
        left = max(0, i-window)
        right = min(i+window+1, len(word_list))
        for k in range(left, right):
            if(k != i):
                context_idx = word_indices[word_list[k]]
                word_context[target_idx][context_idx] += 1
    # print(word_context)
    return word_context

context_based(p)

def apply_svd(matrix_approx, word_context, K):
    u, s, vh = np.linalg.svd(word_context, full_matrices=True,compute_uv=True)
    matrix_approx = u[:, :K] * s[:K]
    # print(matrix_approx[word_indices["liberty"]])
    # print(matrix_approx[word_indices["flower"]])
    return matrix_approx

apply_svd()

def cos_sim(v1, v2):
    return np.dot(v1,v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# print(cos_sim(matrix_approx[word_indices["crime"]], matrix_approx[word_indices["liberty"]]))
# print(cos_sim(matrix_approx[word_indices["crime"]], matrix_approx[word_indices["hell"]]))
# print(cos_sim(matrix_approx[word_indices["crime"]], matrix_approx[word_indices["pleasure"]]))

# print(cos_sim(matrix_approx[word_indices["flower"]], matrix_approx[word_indices["rose"]]))
# print(cos_sim(matrix_approx[word_indices["flower"]], matrix_approx[word_indices["hell"]]))
# print(cos_sim(matrix_approx[word_indices["flower"]], matrix_approx[word_indices["heart"]]))


# def doc_based():
#     for e in os.scandir(p):
#         if e.is_file():
#             words = []
#             with open(e.path, "r") as file:
#                 content = file.read()
#                 # words = re.split(r"[,\s;:]+", content.lower())
#                 words = re.findall(r"\b\w+\b", content.lower())
#             words_dict = {}
#             for word in words:
#                 if word not in words_dict:
#                     words_dict[word] = 1
#                 else:
#                     words_dict[word] += 1
#             text_list[e.path] = words_dict

#     for text in text_list:
#         col = []
#         for word in word_set:
#             cnt = 0
#             if word in text_list[text]:
#                 cnt = text_list[text][word]
#             col.append(cnt)
#         svd.append(col)

# for i in range(len(files)):
#     words = []
#     with open(files[i], "r") as file:
#         content = file.read()
#         # words = re.split(r"[,\s;:]+", content.lower())
#         words = re.findall(r"\b\w+\b", content.lower())
#     words_dict = {}
#     for word in words:
#         word_set.add(word)
#         if word not in words_dict:
#             words_dict[word] = 1
#         else:
#             words_dict[word] += 1
#     text_list[files[i]] = words_dict

# for text in text_list:
#     col = {}
#     for word in word_set:
#         cnt = 0
#         if word in text_list[text]:
#             cnt = text_list[text][word]
#         col[word] = cnt
#     svd.append(col)            
    

# print(svd)

# u, s, vh = np.linalg.svd(svd, full_matrices=True,compute_uv=True)

# n = len(s)
# matrix_approx_2 = np.zeros((len(text_list),len(word_set))) 

# k = 5

# for i in range(k):
#   matrix_approx_2 += s[i]*np.outer(u[:,i],vh[i])

# print(matrix_approx_2)

# print(u)
# print("/n*********************************/n")
# print(s)
# print("/n*********************************/n")
# print(vh)