#!/usr/bin/env python3

""" calculate mean and std for all settings over three runs (requires results for each run) """

import numpy as np


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


print(get_mean(read_file("mmt_0_remaining_results")))
print(get_mean(read_file("mmt_1_remaining_results")))
print(get_mean(read_file("mmt_2_remaining_results")))
print(get_mean(read_file("mmt_3_remaining_results")))
print(get_mean(read_file("mmt_4_remaining_results")))
print(get_mean(read_file("mmt_6_remaining_results")))
print(get_mean(read_file("mmt_12_remaining_results")))
print(get_mean(read_file("mmt_20_remaining_results")))
print("all pos")
print(get_mean(read_file("mmt_random_pos_replacement_results")))
print("dt")
print(get_mean(read_file("mmt_random_pos_replacement_of_dt_results")))
print("nn")
print(get_mean(read_file("mmt_random_pos_replacement_of_nn_results")))
print("vb")
print(get_mean(read_file("mmt_random_pos_replacement_of_vb_results")))
print("jj")
print(get_mean(read_file("mmt_random_pos_replacement_of_jj_results")))
print("prp")
print(get_mean(read_file("mmt_random_pos_replacement_of_prp_results")))
print("in")
print(get_mean(read_file("mmt_random_pos_replacement_of_in_results")))
