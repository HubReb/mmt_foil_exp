#!/usr/bin/env python3
# author: R. Hubert
# email: hubert@cl.uni-heidelberg.de

import random
from collections import defaultdict

placeholder = "[v]"

filenames = [
    "new_train.lc.norm.tok.en_pos_tagged",
    "test_2016_flickr.lc.norm.tok.en_pos_tagged",
    "test_2017_flickr.lc.norm.tok.en_pos_tagged"
]

path = "/home/rebekka/t2b/Projekte/vision/multi30k-dataset/data/task1/tok/"
ks = [i for i in range(4)]
vocabulary_file = "new_train.lc.norm.tok.vocab.en_pos_tagged"

with open(path+vocabulary_file) as f:
    vocab = f.read().split(",\n")
vocab = vocab[1:-1]
vocabulary = defaultdict(list)
for line in vocab:
    word = line.split(":")[0]
    word = word.strip(" ")
    word = word.strip('"')
    if not ("<" in word or word == ""):
        word, pos_tag  = word.split("_")
        vocabulary[pos_tag].append(word)

print(vocabulary.keys())

for filename in filenames:
    with open(path+filename) as f:
        content = f.read().split("\n")[:-1]
    new_content = []
    for line in content:
        words = line.split()
        word_index = random.randint(0, len(words)-2)
        pos_tag = words[word_index].split("_")[1]
        if pos_tag == ":":
            pos_tag = "."
        words = [word.split("_")[0] for word in words]
        # print(pos_tag)
        words[word_index] = random.choice(vocabulary[pos_tag])
        new_content.append(" ".join(words))
    with open(path+filename.split(".txt")[0]+"_pos_tag_controlled_random_replacement.txt", "w") as f:
            f.write("\n".join(new_content))


for filename in filenames:
    pos_replacements = ["VB", "DT", "NN", "JJ", "PRP", "IN"]
    with open(path+filename) as f:
        content = f.read().split("\n")[:-1]
    for pos_type in pos_replacements:
        new_content = []
        for line in content:
            words = line.split()
            pos_tag = "begin"
            pos_tags = [word.split("_")[1] for word in words]
            exists = False
            for tag in pos_tags:
                if pos_type in tag:
                    exists = True
            if exists:
                while pos_type not in pos_tag:
                    word_index = random.randint(0, len(words)-2)
                    pos_tag = words[word_index].split("_")[1]
                words[word_index] = random.choice(vocabulary[pos_tag])
            words = [word.split("_")[0] for word in words]
            new_content.append(" ".join(words))
        with open(path+filename.split(".txt")[0]+f"_pos_tag_controlled_random_replacement_of_{pos_type}.txt", "w") as f:
            f.write("\n".join(new_content))
