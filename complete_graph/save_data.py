import numpy as np
import matplotlib.pyplot as plt
import sys

if (len(sys.argv) < 2):
	print("python3 save_data.py M_max rule_num")
	exit(1)

M_max = int(sys.argv[1])
r = int(sys.argv[2])

p_prime = []
p_data = []
q_data = []
r_data = []

for M in range(2, M_max+1):
    L = (2*M - 1)
    N = 0
    for i in range(1,M+1):
    	N += i
    
    fr_to_mat = np.zeros([L-1,2])
    
    fr = M
    to1 = M-1
    to2 = M-1
    for i in range(L-1):    
        if (i % 2 == 0):
            fr_to_mat[i][0] = fr
            fr_to_mat[i][1] = to1
            to1 = to1 - 1
        else:
            fr_to_mat[i][0] = to2
            fr_to_mat[i][1] = fr
            to2 = to2 - 1
    
    for idx in range(L):
        if (idx == 0): 
            data = np.loadtxt("./result_frag_N{}/L{}/idx{}-avg.dat".format(N,r,idx))
            dat = np.transpose(data)
            p_prime.append([int(M), dat[0,1], dat[1,1]])
        else:
            err_idx = idx - 1
            fr = fr_to_mat[err_idx][0]
            to = fr_to_mat[err_idx][1]
            for c_idx in range(4*M - 5 + 1):
                data = np.loadtxt("./result_frag_N{}/L{}/idx{}-avg.dat".format(N,r,idx))
                dat = np.transpose(data)
                dat_list = [int(fr), int(to), dat[0,c_idx], dat[1,c_idx]]
                if (dat[0,c_idx] != 0 and dat[1,c_idx] != 0):
                    if ((c_idx == 1 and fr == M) or (c_idx > 1 and c_idx < M and M+1-fr == c_idx)) : p_data.append(dat_list)
                    elif (c_idx >= M and c_idx <= 2*M-2) : q_data.append(dat_list)
                    elif (c_idx >= 2*M-1 and c_idx <= 3*M-3) : r_data.append(dat_list)
                    elif (c_idx >= 3*M-2 and c_idx <= 4*M-5) : r_data.append(dat_list)
    
p_prime_dat = np.array(p_prime)
np.savetxt('./prob_dat/dat/prime_L{}'.format(r), p_prime_dat, fmt='%.6f')
p_dat = np.array(p_data)
np.savetxt('./prob_dat/dat/p_L{}'.format(r), p_dat, fmt='%.6f')
q_dat = np.array(q_data)
np.savetxt('./prob_dat/dat/q_L{}'.format(r), q_dat, fmt='%.6f')
r_dat = np.array(r_data)
np.savetxt('./prob_dat/dat/r_L{}'.format(r), r_dat, fmt='%.6f')
