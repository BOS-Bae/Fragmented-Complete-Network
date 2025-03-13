import numpy as np
import sys

if(len(sys.argv) < 3):
	print("python3 print_dat.py R (or P) m n")
	exit(1)

prob_name = sys.argv[1]
m = int(sys.argv[2])
n = int(sys.argv[3])

prob = np.loadtxt("./complete_graph/L8_confi_dat/L8/L8-prob-{}.dat".format(prob_name))

print(prob[m,n])
