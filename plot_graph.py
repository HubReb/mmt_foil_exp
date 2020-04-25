#!/usr/bin/env python3

''' plot random replacement METEOR score results '''

import matplotlib.pyplot as plt


plt.xticks(ticks=[0, 4, 8, 12, 16, 20, 24], labels=[0,  4, 8, 12, 16, 20, "all"], fontsize=14)
plt.yticks(
    ticks=[0, 20, 30, 40, 50, 60, 70, 80, 90],
    labels=[0, 20, 30, 40, 50, 60, 70, 80, 90],
    fontsize=12
)
plt.errorbar(
    [0, 1, 2, 3, 4, 6, 8, 10, 12, 20, 24],
    [
        70.257, 61.709, 54.259, 50.141, 45.375,
        37.879, 33.663, 29.315, 26.369, 19.414, 15.669
    ],
    [
        0.143, 0.421, 0.461, 0.022, 0.276, 0.084,
        0.128, 0.179, 0.177, 0.157, 0.129
    ],
    label="MMT"
)
plt.errorbar(
    [0, 1, 2, 3, 4, 6, 8, 10, 12, 20, 24],
    [
        70.661, 62.183, 54.673, 49.724, 44.918,
        36.923, 31.456, 25.77, 23.381, 15.035, 12.401
    ],
    [
        0.260, 0.372, 0.026, 0.002, 0.262,
        0.199, 0.442, 0.072, 0.239, 0.315, 0.204
    ],
    label="NMT"
)

plt.xlabel("k random replacements", fontsize=16)
plt.ylabel("METEOR score", fontsize=16)
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.savefig("random_replacements.png")
