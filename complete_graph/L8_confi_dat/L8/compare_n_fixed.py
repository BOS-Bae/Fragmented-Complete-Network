import numpy as np
import matplotlib.pyplot as plt
import sys

if (len(sys.argv) < 2):
	print("python3 compare.py n log_setting(1)")
	exit(1)

n = int(sys.argv[1])
log_or_not = int(sys.argv[2])

P_exact = np.loadtxt("./L8-prob-P.dat")
R_exact = np.loadtxt("./L8-prob-R.dat")
P_num_dat = np.loadtxt("../../prob_dat/dat/p_L8")
R_num_dat = np.loadtxt("../../prob_dat/dat/r_L8")

m_list = range(14+1)
P_exact_n1 = np.zeros(15)
R_exact_n1 = np.zeros(15)
P_num_n1 = np.zeros(15)
R_num_n1 = np.zeros(15)
P_err_n1 = np.zeros(15)
R_err_n1 = np.zeros(15)

for m in m_list:
	P_exact_n1[m] = P_exact[m,n]
	R_exact_n1[m] = R_exact[m,n]
	
for l_idx in range(len(P_num_dat)):
	dat_p = P_num_dat[l_idx]
	dat_r = R_num_dat[l_idx]
	if (dat_p[0] <= 14 and int(dat_p[1]) == n and dat_p[0] != dat_p[1]):
		P_num_n1[int(dat_p[0])] = dat_p[2]
		P_err_n1[int(dat_p[0])] = dat_p[3]
	if (dat_r[0] <= 14 and int(dat_r[1]) == n and dat_r[0] != dat_r[1]):
		R_num_n1[int(dat_p[0])] = dat_r[2]
		R_err_n1[int(dat_p[0])] = dat_r[3]

plt.figure(figsize=(10,7))
P_num_n1[P_num_n1 == 0] = np.nan
plt.plot(m_list[2:], P_exact_n1[2:], color='blue', label = "derived", marker='o')
plt.plot(m_list[2:], P_num_n1[2:], color='lime', label = "numerical", marker='o')
plt.errorbar(m_list[2:], P_num_n1[2:], yerr=P_err_n1[2:], color='lime')
plt.xlabel('m', fontsize=16)
plt.ylabel('P(m,{})'.format(n), fontsize=16)
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.legend(fontsize=16)
if (log_or_not == 1): plt.yscale('log')
plt.show()

plt.figure(figsize=(10,7))
R_num_n1[R_num_n1 == 0] = np.nan
plt.plot(m_list[2:], R_exact_n1[2:], color='blue', label = "derived", marker='o')
plt.plot(m_list[2:], R_num_n1[2:], color='lime', label = "numerical", marker='o')
plt.errorbar(m_list[2:], R_num_n1[2:], yerr=R_err_n1[2:], color='lime')
plt.xlabel('m', fontsize=16)
plt.ylabel('R(m,{})'.format(n), fontsize=16)
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.legend(fontsize=16)

if (log_or_not == 1): plt.yscale('log')
plt.show()

