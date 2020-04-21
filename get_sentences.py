
indices = []
with open("../multi30k-dataset/data/task1/tok/test_2017_flickr.lc.norm.tok.fr_pos_tag_controlled_random_4_replacement_of_NN_only.txt") as f:
    data = f.read().split("\n")[:-1]
with open("../multi30k-dataset/data/task1/tok/test_2017_flickr.lc.norm.tok.en.pos_tagged_pos_tag_controlled_random_4_replacement_of_NN_only.txt") as f:
    foiled_data = f.read().split("\n")[:-1]

with open("../multi30k-dataset/data/task1/tok/test_2017_flickr.lc.norm.tok.fr") as f:
    complete_data = f.read().split("\n")[:-1]



for index, line in enumerate(complete_data):
    if line in data:
        indices.append(index)


with open("../multi30k-dataset/data/task1/tok/test_2017_flickr.lc.norm.tok.en") as f:
    original_data = f.read().split("\n")[:-1]

with open("translate_mmt_random_pos_replacement_of_nn4.test_2017_flickr_deepl_en.txt") as f:
    back_trans_data = f.read().split("\n")[:-1]

with open("nmt_nn.txt") as f:
    nmt_data = f.read().split("\n")[:-1]

bt_id = 0
from collections import defaultdict
length = defaultdict(int)
for index, line in enumerate(original_data):
    if index in indices:
        print(f"original: {line}\n foiled: {foiled_data[bt_id]}\nback: {back_trans_data[bt_id]}\nnmt: {nmt_data[bt_id]}")
        bt_id += 1
        length[len(line.split())] += 1

j = 0
total = 0
for k, v in length.items():
    j += k*v
    total += v

print(j/total)
print(sorted([a for a in length.items()], key=lambda x: x[1]))
