import numpy as np
import re, os

# files = ["txt_files/f1.txt", "txt_files/f2.txt", "txt_files.f3.txt"]

svd = []
word_set = set()
text_list = {}
total_word_cnt = []

# p = "./txt_files"
p = "./generated_files"

for e in os.scandir(p):
    if e.is_file():
        words = []
        with open(e.path, "r") as file:
            content = file.read()
            # words = re.split(r"[,\s;:]+", content.lower())
            words = re.findall(r"\b\w+\b", content.lower())
        total_word_cnt.append(len(words))
        words_dict = {}
        for word in words:
            word_set.add(word)
            if word not in words_dict:
                words_dict[word] = 1
            else:
                words_dict[word] += 1
        text_list[e.path] = words_dict

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

for text in text_list:
    col = []
    for word in word_set:
        cnt = 0
        if word in text_list[text]:
            cnt = text_list[text][word]
        col.append(cnt)
    svd.append(col)

def TF_IDF():
    col = []
    for word in word_set:
        cnt = 0
        if word in text_list[text]:
            cnt = text_list[text][word]
            
    

# print(svd)

u, s, vh = np.linalg.svd(svd, full_matrices=True,compute_uv=True)

n = len(s)
matrix_approx_2 = np.zeros((len(text_list),len(word_set))) 

k = 5

for i in range(k):
  matrix_approx_2 += s[i]*np.outer(u[:,i],vh[i])

print(matrix_approx_2)



# print(u)
# print("/n*********************************/n")
# print(s)
# print("/n*********************************/n")
# print(vh)