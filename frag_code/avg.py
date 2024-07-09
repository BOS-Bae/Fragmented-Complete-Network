import numpy as np
import sys

if (len(sys.argv) < 2):
	print("python3 avg.py M r_num")
	exit(1)

M = int(sys.argv[1])
r_num = int(sys.argv[2])
n_s = 20 # number of samples

L = (2*M - 1)
N = 0
for i in range(1,M+1):
	N += i

confi_len = (len(list(np.loadtxt("./result_frag_N{}/L{}/num_data/idx0-sample0.dat".format(N, r_num)))) - 1)

for idx in range(L):
    tot_dat = np.zeros([n_s, confi_len])
    for s in range(n_s):
        dat = np.loadtxt("./result_frag_N{}/L{}/num_data/idx{}-sample{}.dat".format(N, r_num, idx, s))
        tot_dat[s] = dat[0:confi_len]
    std_err = np.std(tot_dat, 0)
    std_err /= np.sqrt(n_s)
    avg = np.average(tot_dat, 0)
    dat_f = np.zeros([2, confi_len])
    dat_f[0] = avg
    dat_f[1] = std_err
    dat_result = np.transpose(dat_f)

    np.savetxt("./result_frag_N{}/L{}/idx{}-avg.dat".format(N, r_num, idx), dat_result, fmt="%.6f")
