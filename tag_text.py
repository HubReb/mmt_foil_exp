#!/usr/bin/env python3

""" use StanfordPOSTagger to tag dataset """

from nltk.tag.stanford import StanfordPOSTagger

from constants import filepath, path, filenames


tagger = StanfordPOSTagger(
    path + "models/english-bidirectional-distsim.tagger",
    path + "stanford-postagger.jar",
)

for filename in filenames:
    with open(filepath + filename) as f:
        data = f.read().split("\n")
    parsed_text = ""
    old_index = 0
    length = len(data)
    for index, line in enumerate(data):
        if index % 100 == 0:
            print(f"{index}/{length}")
        st = tagger.tag(line.split(" "))
        for parsed_token in st:
            token_pos = parsed_token[0] + "_" + parsed_token[1]
            parsed_text += token_pos + " "
        parsed_text += "\n"
    with open(f"{filepath}{filename}.pos_tagged", "w") as f:
        f.write(parsed_text)
