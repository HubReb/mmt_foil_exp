import matplotlib.pyplot as plt
plt.xticks(ticks=[0, 1, 2, 3, 4, 6, 12, 20, 25], labels=[0, 1, 2, 3, 4, 6, 12, 20, "all"], fontsize=16)
plt.errorbar([0, 1, 2, 3, 4, 6, 12, 20, 25], [16.609, 18.453, 22.802, 26.748, 30.873, 41.032, 64.069, 69.458, 70.257], [0.107, 0.302, 0.164, 0.219, 0.091, 0.352, 0.38, 0.032, 0.143])
plt.xlabel("k remaining tokens", fontsize=20)
plt.ylabel("METEOR score", fontsize=20)
#plt.show()
plt.close()


plt.xticks(ticks=[0, 1, 2, 3, 4, 6, 8, 10, 12], labels=[0, 1, 2, 3, 4, 6, 8, 10, 12], fontsize=14)
plt.yticks(ticks=[0, 20, 30, 40, 50, 60, 70, 80, 90], labels=[0, 20, 30, 40, 50, 60, 70, 80, 90], fontsize=12)
plt.errorbar([0, 1, 2, 3, 4, 6, 8, 10, 12], [70.257, 61.709, 54.259, 50.141, 45.375, 37.879, 33.663, 29.315, 26.369], [0.143, 0.421, 0.461, 0.022, 0.276, 0.084, 0.128, 0.179, 0.177], label="MMT")
plt.errorbar([0, 1, 2, 3, 4, 6, 8, 10, 12], [70.661, 62.183, 54.673, 49.724, 44.918, 36.923, 31.456, 25.77, 23.381], [0.260, 0.372, 0.026, 0.002, 0.262, 0.199, 0.442, 0.072, 0.239], label="NMT")

plt.xlabel("k random replacements", fontsize=16)
plt.ylabel("METEOR score", fontsize=16)
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.savefig("/home/rebekka/Studium/master/vision/report/random_replacements.png")
