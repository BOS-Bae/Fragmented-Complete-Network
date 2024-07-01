import numpy as np
import sys

M = int(sys.argv[1])
r_num = int(sys.argv[2])
n_s = 20 # number of samples

L = (2*M - 1)
N = 0
for i in range(1,M+1):
	N += i

confi_len = (len(list(np.loadtxt("./result_frag_N{}/L{}/idx0-sample0.dat".format(N, r_num)))) - 1)

for idx in range(L):
	tot_dat = np.zeros([n_s, confi_len])
	for s in range(n_s):
		dat = np.loadtxt("./result_frag_N{}/L{}/idx{}-sample{}.dat".format(N, r_num, idx, s))
		tot_dat[s] = dat[0:confi_len]
	std_err = np.std(tot_dat, 0)
	avg = np.average(tot_dat, 0)
	std_err /= n_s
	std_err = np.sqrt(std_err)
	print(avg)
	print(std_err, "\n")
