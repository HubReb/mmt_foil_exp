#!/usr/bin/env python3
# author: R. Hubert
# email: hubert@cl.uni-heidelberg.de

""" replace one word in each sentence with a randomly chosen word """

import random

from constants import filepath, filenames

placeholder = "[v]"


vocabulary_file = "new_train.lc.norm.tok.vocab.en"

with open(filepath + vocabulary_file) as f:
    vocab = f.read().split(",\n")
vocab = vocab[1:-1]
vocabulary = []
for line in vocab:
    word = line.split(":")[0]
    word = word.strip(" ")
    word = word.strip('"')
    vocabulary.append(word)


for filename in filenames:
    for k in range(2, 5):
        with open(filepath + filename) as f:
            content = f.read().split("\n")[:-1]
        new_content = []
        for line in content:
            words = line.split()
            for index in range(k):
                word_index = random.randint(0, len(words) - 2)
                words[word_index] = random.choice(vocabulary)
            new_content.append(" ".join(words))
        with open(filepath + filename.split(".txt")[0] + f"{k}_random_replacement.txt", "w") as f:
            f.write("\n".join(new_content))
