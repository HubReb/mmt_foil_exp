#!/usr/bin/env python3
# author: R. Hubert
# email: hubert@cl.uni-heidelberg.de

""" create training and test files with k remaining words """

from constants import filepath, filenames

placeholder = "[v]"

ks = [4, 6, 12, 20]

for filename in filenames:
    with open(filepath + filename) as f:
        content = f.read().split("\n")[:-1]
    new_contents = {4: [], 6: [], 12: [], 20: []}
    for line in content:
        for k in ks:
            new_line = ""
            counter = 0
            for word in line.split():
                if (counter < k) or (
                    (line.index(word) == len(line) - 1) and (word == ".")
                ):
                    new_line += word
                else:
                    new_line += placeholder
                new_line += " "
                counter += 1
            new_contents[k].append(new_line.strip())
    for k in ks:
        with open(
            filepath + filename.split(".txt")[0] + f"_{k}_words_remaining.txt", "w"
        ) as f:
            f.write("\n".join(new_contents[k]))
