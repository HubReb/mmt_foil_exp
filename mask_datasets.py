#!/usr/bin/env python3
# author: R. Hubert
# email: hubert@cl.uni-heidelberg.de

placeholder = "[v]"

filenames = [
    "new_train.lc.norm.tok.en",
    "test_2016_flickr.lc.norm.tok.en",
    "test_2017_flickr.lc.norm.tok.en"
]

path = "/home/rebekka/t2b/Projekte/vision/multi30k-dataset/data/task1/tok/"
ks = [i for i in range(4)]

for filename in filenames:
    with open(path+filename) as f:
        content = f.read().split("\n")[:-1]
    new_contents = {1: [], 0: [], 2: [], 3: []}
    for line in content:
        for k in ks:
            new_line = ""
            counter = 0
            for word in line.split():
                if (counter < k) or ((line.index(word) == len(line) -1) and (word == ".")):
                    new_line += word
                else:
                    new_line += placeholder
                new_line += " "
                counter += 1
            new_contents[k].append(new_line.strip())
    for k in ks:
        with open(path+filename.split(".txt")[0]+"_%s_words_remaining.txt" % k, "w") as f:
            f.write("\n".join(new_contents[k]))

