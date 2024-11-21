import sys
import numpy as np

if (len(sys.argv) < 3):
	print("python3 prob_show.py N idx s_i")
	exit(1)


N = int(sys.argv[1])
idx = int(sys.argv[2])

s_i = int(sys.argv[3])

dat = np.loadtxt("./flip_dat/prob-N{}-L8-idx{}.dat".format(N,idx))

#num = int(2**(N*N))

def idx_to_mat(s_f):
	mat = np.zeros([N, N])
	idx_f = int(s_f)
	for i in range(N):
		for j in range(N):
			val = int(idx_f & 1)
			mat[i,j] = 2*val-1
			idx_f = idx_f >> 1
	for i in range(N):
		for j in range(N):
			print(int(mat[i,j]), " ", end='')
		print("")
	print("")

idx_to_mat(s_i) # for test
print("")

for i in range(len(dat)):
	if (dat[i,0] == s_i) :
		print(int(dat[i,0]), " ", int(dat[i,1]), " ", int(dat[i,2]))
		idx_to_mat(dat[i,1])

