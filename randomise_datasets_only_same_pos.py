#!/usr/bin/env python3
# author: R. Hubert
# email: hubert@cl.uni-heidelberg.de

""" replace one word in each sentence with a randomly chosen word of the same pos-tag """

import random
from collections import defaultdict

import numpy as np

from constants import filepath


placeholder = "[v]"

filenames = [
    "new_train.lc.norm.tok.en.pos_tagged",
    "test_2016_flickr.lc.norm.tok.en.pos_tagged",
    "test_2017_flickr.lc.norm.tok.en.pos_tagged",
]

vocabulary_file = "new_train.lc.norm.tok.en.vocab.pos_tagged"

with open(filepath + vocabulary_file) as f:
    # print(f.read())
    vocab = f.read().split(",\n")
# print(vocab)
vocab = vocab[1:-1]
vocabulary = defaultdict(list)
for line in vocab:
    word = line.split(":")[0]
    word = word.strip(" ")
    word = word.strip('"')
    if not ("<" in word or word == ""):
        word, pos_tag = word.split("_")
        vocabulary[pos_tag].append(word)

print(vocabulary.keys())

"""
for filename in filenames:
    for k in range(2,5):
        with open(filepath + filename) as f:
            content = f.read().split("\n")[:-1]
        new_content = []
        for line in content:
            words = line.split()
            for index in range(k):
                word_index = random.randint(0, len(words) - 2)
                pos_tag = words[word_index].split("_")[1]
                if pos_tag == ":":
                    pos_tag = "."
                words = [word.split("_")[0] for word in words]
                # print(pos_tag)
                words[word_index] = random.choice(vocabulary[pos_tag])
            new_content.append(" ".join(words))
        with open(
            filepath + filename.split(".txt")[0] + f"_pos_tag_controlled_random_{k}_replacement.txt",
            "w",
        ) as f:
            f.write("\n".join(new_content))

"""
for filename in filenames:
    if "test_2017" not in filename:
        continue
    # pos_replacements = ["VB","DT", "NN", "JJ", "PRP", "IN"]
    pos_replacements = ["NN"]
    for k in range(4,5):
        with open(filepath + filename) as f:
            content = f.read().split("\n")[:-1]
        print(filepath + filename.split("en")[0] + "fr")
        with open(filepath + filename.split("en")[0] + "fr") as f:
            fr_content = f.read().split("\n")[:-1]
        for pos_type in pos_replacements:
            indices_im = []
            new_content = []
            new_fr_content = []
            for index, line in enumerate(content):
                words = line.split()
                pos_tag = "begin"
                pos_tags = [word.split("_")[1] for word in words]
                exists = False
                p_c = 0
                for tag in pos_tags:
                    if pos_type in tag:
                        p_c += 1
                # if p_c >= k:
                        exists = True
                if exists:
                    chosen_indices = set([])
                    for j in range(k):
                        while (pos_type not in pos_tag):
                            word_index = random.randint(0, len(words) - 1)
                            while word_index in chosen_indices:
                                word_index = random.randint(0, len(words) - 1)
                            pos_tag = words[word_index].split("_")[1]
                        chosen_indices.add(word_index)
                        words[word_index] = random.choice(vocabulary[pos_tag])
                        pos_tag = "begin"
                        if len(chosen_indices) >= p_c:
                            break
                    words = [word.split("_")[0] for word in words]
                    new_content.append(" ".join(words))
                    new_fr_content.append(fr_content[index])
                    indices_im.append(index)
            """
            image_features = np.load(filepath+"../../features/features_resnet50/test_2017_flickr-resnet50-res4frelu_l2_normed.npy")
            new_features = []
            for index in indices_im:
                new_features.append(image_features[index])
            new_features = np.array(new_features)
            np.save(filepath+f"../../features/features_resnet50/test_2017_flickr-resnet50-res4frelu_l2_normed_{k}_{pos_type}.npy", new_features)
            """
            with open(
                filepath
                + filename.split(".txt")[0]
                + f"_pos_tag_controlled_random_{k}_replacement_of_{pos_type}_all.txt",
                "w",
            ) as f:
                f.write("\n".join(new_content))
            with open(
                filepath
                + filename.split("en")[0] + "fr"
                + f"_pos_tag_controlled_random_{k}_replacement_of_{pos_type}_all.txt",
                "w",
            ) as f:
                f.write("\n".join(new_fr_content))
