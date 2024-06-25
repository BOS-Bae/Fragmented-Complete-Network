import numpy as np
import sys

if (len(sys.argv) < 3):
	print("python3 dat_show.py N rule_num error_idx confi_idx ")
	exit(1)

N=int(sys.argv[1])
r=int(sys.argv[2])
e_idx=int(sys.argv[3])
c_idx=int(sys.argv[4])

data = np.loadtxt("./result_frag_N{}/L{}/idx{}.dat".format(N,r,e_idx))
print(data[c_idx])
