import numpy as np
import sys

if (len(sys.argv) < 4):
	print("python3 dat_show.py N idx_len rule_num confi_idx")
	exit(1)

N = int(sys.argv[1])
idx_len = int(sys.argv[2])
r = int(sys.argv[3])
c_idx = int(sys.argv[4])

for idx in range(idx_len):
	data = np.loadtxt("./result_frag_N{}/L{}/idx{}-avg.dat".format(N,r,idx))
	dat = np.transpose(data)
	print(idx, " ", dat[0,c_idx], " ", dat[1,c_idx])
