import numpy as np
import sys
from collections import Counter

N = int(sys.argv[1])
idx = int(sys.argv[2])

dat = np.loadtxt("./flip_dat/N{}-L8-idx{}.dat".format(N,idx))

dat_unique = []
for i in range(len(dat)):
	each_change = list(dat[i])
	count = Counter(each_change[1:])
	for num, occur in count.items():
		dat_unique.append([int(each_change[0]), int(num), int(occur)])

dat_unique = np.unique(dat_unique, axis=0)

for i in range(len(dat_unique)):
		print(dat_unique[i][0], " ", dat_unique[i][1], " ", dat_unique[i][2])
