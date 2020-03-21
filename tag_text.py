#!/usr/bin/env python3 

import os, glob, sys
import nltk
from six import text_type

from nltk.tag.stanford import StanfordPOSTagger


tagger = StanfordPOSTagger(
    "/home/rebekka/Downloads/stanford-postagger-2018-10-16/models/english-bidirectional-distsim.tagger",
    "/home/rebekka/Downloads/stanford-postagger-2018-10-16/stanford-postagger.jar"
)

files = [
    "/home/rebekka/t2b/Projekte/vision/multi30k-dataset/data/task1/tok/new_train.lc.norm.tok.en",
    "/home/rebekka/t2b/Projekte/vision/multi30k-dataset/data/task1/tok/test_2016_flickr.lc.norm.tok.en",
    "/home/rebekka/t2b/Projekte/vision/multi30k-dataset/data/task1/tok/test_2017_flickr.lc.norm.tok.en",
    "/home/rebekka/t2b/Projekte/vision/multi30k-dataset/data/task1/tok/new_train.lc.norm.tok.vocab.en"
]

for filename in files:
    with open(filename) as f:
        data = f.read().split("\n")
    parsed_text = ""
    old_index = 0
    length = len(data)
    for index in range(0, len(data)):
        if index % 100 == 0:
            print(f"{index}/{length}")
        st = tagger.tag(data[index].split(" "))
        for parsed_token in st:
            token_pos = parsed_token[0] + "_" + parsed_token[1]
            parsed_text += token_pos + " "
        parsed_text += "\n"
    with open(f"{filename}.pos_tagged", "w") as f:
        f.write(parsed_text)
