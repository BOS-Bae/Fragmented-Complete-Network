import numpy as np
import matplotlib.pyplot as plt
import sys

if (len(sys.argv) < 2):
	print("python3 compare.py m log_setting(1)")
	exit(1)

m = int(sys.argv[1])
log_or_not = int(sys.argv[2])

P_exact = np.loadtxt("./L8-prob-P.dat")
R_exact = np.loadtxt("./L8-prob-R.dat")
P_num_dat = np.loadtxt("../../prob_dat/dat/p_L8")
R_num_dat = np.loadtxt("../../prob_dat/dat/r_L8")

n_list = range(14+1)
P_exact_m1 = np.zeros(15)
R_exact_m1 = np.zeros(15)
P_num_m1 = np.zeros(15)
R_num_m1 = np.zeros(15)
P_err_m1 = np.zeros(15)
R_err_m1 = np.zeros(15)

for n in n_list:
	P_exact_m1[n] = P_exact[m,n]
	R_exact_m1[n] = R_exact[m,n]
	
for l_idx in range(len(P_num_dat)):
	dat_p = P_num_dat[l_idx]
	dat_r = R_num_dat[l_idx]
	if (dat_p[1] <= 14 and int(dat_p[0]) == m and dat_p[0] != dat_p[1]):
		P_num_m1[int(dat_p[1])] = dat_p[2]
		P_err_m1[int(dat_p[1])] = dat_p[3]
	if (dat_r[1] <= 14 and int(dat_r[0]) == m and dat_r[0] != dat_r[1]):
		R_num_m1[int(dat_p[1])] = dat_r[2]
		R_err_m1[int(dat_p[1])] = dat_r[3]

tot_dat_P = []
tot_dat_P.append(n_list[2:])
tot_dat_P.append(P_exact_m1[2:])
tot_dat_P.append(P_num_m1[2:])
tot_dat_P.append(P_err_m1[2:])
np.savetxt("./compare_dat/P_m{}.dat".format(int(m)), np.transpose(tot_dat_P))

tot_dat_R = []
tot_dat_R.append(n_list[2:])
tot_dat_R.append(R_exact_m1[2:])
tot_dat_R.append(R_num_m1[2:])
tot_dat_R.append(R_err_m1[2:])
np.savetxt("./compare_dat/R_m{}.dat".format(int(m)), np.transpose(tot_dat_R))
