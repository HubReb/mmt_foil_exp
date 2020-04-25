#!/usr/bin/env python3

from collections import defaultdict

def get_data(filename):
    with open(filename) as f:
        content = f.read().split("\n")[:-1]
    return content


indices = []
data = get_data("../multi30k-dataset/data/task1/tok/test_2017_flickr.lc.norm.tok.fr_pos_tag_controlled_random_4_replacement_of_NN_only.txt")
foiled_data = get_data("../multi30k-dataset/data/task1/tok/test_2017_flickr.lc.norm.tok.en.pos_tagged_pos_tag_controlled_random_4_replacement_of_NN_only.txt")
complete_data = get_data("../multi30k-dataset/data/task1/tok/test_2017_flickr.lc.norm.tok.fr")
original_data = get_data("../multi30k-dataset/data/task1/tok/test_2017_flickr.lc.norm.tok.en")
back_trans_data = get_data(
    "translate_mmt_random_pos_replacement_of_nn4.test_2017_flickr_deepl_en.txt"
)
nmt_data = get_data("nmt_nn.txt")

for index, line in enumerate(complete_data):
    if line in data:
        indices.append(index)


bt_id = 0
length = defaultdict(int)
for index, line in enumerate(original_data):
    if index in indices:
        print(f"original: {line}\nfoiled: {foiled_data[bt_id]}")
        print(f"nback: {back_trans_data[bt_id]}\nnmt: {nmt_data[bt_id]}")
        print("-"*80)
        bt_id += 1
        length[len(line.split())] += 1

j = 0
total = 0
for k, v in length.items():
    j += k*v
    total += v

print(j/total)
print(sorted([a for a in length.items()], key=lambda x: x[1]))
