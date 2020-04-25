#!/usr/bin/env python3

""" calculate mean and std for all settings over three runs (requires results for each run) """

import numpy as np

results_files = [
    "mmt_0_remaining_results",
    "mmt_1_remaining_results",
    "mmt_2_remaining_results",
    "mmt_3_remaining_results",
    "mmt_4_remaining_results",
    "mmt_6_remaining_results",
    "mmt_12_remaining_results",
    "mmt_20_remaining_results",
    "nmt_on_random_pos_results",
    "mmt_random_pos_replacement_results",
    "nmt_on_random_pos2_results",
    "mmt_random_pos_replacement2_results",
    "nmt_on_random_pos3_results",
    "mmt_random_pos_replacement3_results",
    "nmt_on_random_pos4_results",
    "mmt_random_pos_replacement4_results",
    "mmt_random_pos_replacement_of_dt_results",
    "mmt_random_pos_replacement_of_dt_results",
    "mmt_random_pos_replacement_of_nn_results",
    "mmt_random_pos_replacement_of_vb_results",
    "mmt_random_pos_replacement_of_jj_results",
    "mmt_random_pos_replacement_of_prp_results",
    "mmt_random_pos_replacement_of_in_results",
    "nmt_on_random_results",
    "nmt_on_random_pos_results",
    "nmt_on_random_pos_jj_results",
    "nmt_on_random_pos_nn_results",
    "nmt_on_random_pos_vb_results",
    "nmt_on_random_pos_in_results",
    "nmt_on_random_pos_prp_results",
    "nmt_on_random_pos_dt_results",
    "mmt_random_pos_replacement_of_jj_results",
    "mmt_random_pos_replacement_of_nn_results",
    "mmt_random_pos_replacement_of_vb_results",
    "mmt_random_pos_replacement_of_prp_results",
    "mmt_random_pos_replacement_of_dt_results",
    "nmt_on_random_pos_jj2_results",
    "mmt_random_pos_replacement_of_jj2_results",
    "nmt_on_random_pos_nn2_results",
    "mmt_random_pos_replacement_of_nn2_results",
    "nmt_on_random_pos_vb2_results",
    "mmt_random_pos_replacement_of_vb2_results",
    "nmt_on_random_pos_in2_results",
    "mmt_random_pos_replacement_of_in2_results",
    "nmt_on_random_pos_prp2_results",
    "mmt_random_pos_replacement_of_prp2_results",
    "nmt_on_random_pos_dt2_results",
    "mmt_random_pos_replacement_of_dt2_results",
    "nmt_on_random_pos_jj3_results",
    "mmt_random_pos_replacement_of_jj3_results",
    "nmt_on_random_pos_nn3_results",
    "mmt_random_pos_replacement_of_nn3_results",
    "nmt_on_random_pos_vb3_results",
    "mmt_random_pos_replacement_of_vb3_results",
    "nmt_on_random_pos_in3_results",
    "mmt_random_pos_replacement_of_in3_results",
    "nmt_on_random_pos_prp3_results",
    "mmt_random_pos_replacement_of_prp3_results",
    "nmt_on_random_pos_dt3_results",
    "mmt_random_pos_replacement_of_dt3_results",
    "nmt_on_random_pos_jj4_results",
    "mmt_random_pos_replacement_of_jj4_results",
    "nmt_on_random_pos_nn4_results",
    "mmt_random_pos_replacement_of_nn4_results",
    "nmt_on_random_pos_vb4_results",
    "mmt_random_pos_replacement_of_vb4_results",
    "nmt_on_random_pos_in4_results",
    "mmt_random_pos_replacement_of_in4_results",
    "nmt_on_random_pos_prp4_results",
    "mmt_random_pos_replacement_of_prp4_results",
    "nmt_on_random_pos_dt4_results",
    "mmt_random_pos_replacement_of_dt4_results",
    "mmt_random_replacement2_results",
    "mmt_random_replacement3_results",
    "mmt_random_replacement4_results",
    "nmt_on_random2_results",
    "nmt_on_random3_results",
    "nmt_on_random4_results",
    "nmt_on_random_pos_dt_all_results",
    "nmt_on_random_pos_in_all_results",
    "nmt_on_random_pos_prp_all_results",
    "nmt_on_random8_results",
    "mmt_random_replacement8_results",
    "nmt_on_random10_results",
    "mmt_random_replacement10_results",
    "nmt_on_random12_results",
    "mmt_random_replacement12_results",
    "nmt_on_random20_results",
    "mmt_random_replacement20_results",
    "nmt_on_random_all_results",
    "mmt_random_replacement_all_results",
    "nmt_abl0_results",
    "nmt_abl1_results",
    "nmt_abl2_results",
    "nmt_abl3_results",
    "nmt_abl4_results",
    "nmt_abl6_results",
    "nmt_abl12_results",
    "nmt_abl20_results"
]

def read_file(filename):
    with open(filename) as f:
        data = f.read().split("\n")[:-1]
    return data


def get_mean(data):
    data = [[d.replace("|", "").strip() for d in line.split("||")] for line in data]
    b1, b2, b3, b4, meteor, cider, rouge = [], [], [], [], [], [], []
    scores = [b1, b2, b3, b4, meteor, cider, rouge]
    counter = 0
    for sample in data:
        if counter % 2 == 0:
            counter += 1
            continue
        counter += 1
        for index, datapoint in enumerate(sample):
            scores[index].append(float(datapoint))
    print(scores)
    scores = [np.array(data) for data in scores]
    output = "| "
    for score in scores:
        output += f" {np.around(score.mean(), 3)} ({np.around(score.std(), 3)}) ||"
    return output[:-1]

for filename in results_files:
    print(filename)
    print(get_mean(read_file(filename)))
