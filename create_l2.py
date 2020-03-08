#!/usr/bin/env python3

import glob

import numpy as np

for filename in glob.iglob("/home/rebekka/t2b/Projekte/vision/multi30k-dataset/data/features/features_resnet50/*"):
    if (not "avg" in filename) and (not "train" in filename):
        print(filename)
        features = np.load(filename)
        features  = np.nan_to_num(features/np.linalg.norm(features, axis=-1, keepdims=True))
        np.save("%s_l2_normed.npy" % (filename.split(".npy")[0]), features)

