#!/usr/bin/env python3

import glob

import numpy as np

from constants import imagepath

for filename in glob.iglob(
    imagepath + "*"
):
    if (not "avg" in filename) and (not "train" in filename):
        print(filename)
        features = np.load(filename)
        features = np.nan_to_num(
            features / np.linalg.norm(features, axis=-1, keepdims=True)
        )
        np.save("%s_l2_normed.npy" % (filename.split(".npy")[0]), features)
