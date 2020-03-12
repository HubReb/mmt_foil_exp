#!/usr/bin/env python3
# author: R. Hubert
# email: hubert@cl.uni-heidelberg.de

import random

placeholder = "[v]"

filenames = [
    "new_train.lc.norm.tok.en",
    "test_2016_flickr.lc.norm.tok.en",
    "test_2017_flickr.lc.norm.tok.en"
]

path = "/home/rebekka/t2b/Projekte/vision/multi30k-dataset/data/task1/tok/"
ks = [i for i in range(4)]
vocabulary_file = "new_train.lc.norm.tok.vocab.en"

with open(path+vocabulary_file) as f:
    vocab = f.read().split(",\n")
vocab = vocab[1:-1]
vocabulary = []
for line in vocab:
    word = line.split(":")[0]
    word = word.strip(" ")
    word = word.strip('"')
    vocabulary.append(word)


for filename in filenames:
    with open(path+filename) as f:
        content = f.read().split("\n")[:-1]
    new_content = []
    for line in content:
        words = line.split()
        word_index = random.randint(0, len(words)-2)
        words[word_index] = random.choice(vocabulary)
        new_content.append(" ".join(words))
    with open(path+filename.split(".txt")[0]+"_random_replacement.txt", "w") as f:
            f.write("\n".join(new_content))

