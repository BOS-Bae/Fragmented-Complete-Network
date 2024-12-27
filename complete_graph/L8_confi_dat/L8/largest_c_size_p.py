import matplotlib.pyplot as plt
import numpy as np
import sys

if (len(sys.argv) < 3):
	print("python3 largest_c_size_p.py p MCS ns")
	exit(1)

N_arr = np.arange(80,110,10)
N_len = len(list(N_arr))

p = float(sys.argv[1])
MCS = int(sys.argv[2])
ns = int(sys.argv[3])

label_info = ["paradise", "fully fragmented", "randomly distributed"]

tot_check = 0
max_N = []
Avg_max_N = []; Err_max_N = []
count_non_single = 0
for N in N_arr:
    dat = []
    max_size_list = np.zeros(ns)
    check = 0
    for i in range(ns):
        g_info = np.loadtxt("./p_L8_cABM/N{}-p{}-{}MCS-s{}.dat".format(N, p, MCS, i))
        dat.append(g_info)
        non_zeros_idx = np.nonzero(g_info)[0]
        max_size = np.max(non_zeros_idx)
        if (g_info[int(max_size)] == 1): check += 1
        else: count_non_single += 1
        max_size_list[i] = max_size

    if (check == ns): tot_check += 1
    max_N.append(np.max(max_size_list))
    Avg_max_N.append(np.average(max_size_list))
    Err_max_N.append(np.std(max_size_list))

if (tot_check == len(list(N_arr))): print("Check : All cases show that there is only one largest cluster.")
else: print("as a ratio of", count_non_single/(N_len*ns))

plt.plot(N_arr, Avg_max_N, color="lightseagreen", label="average of max[k]",  marker='o')
plt.errorbar(N_arr, Avg_max_N, yerr=np.array(Err_max_N)/np.sqrt(ns),color="lightseagreen")
plt.xlabel("N", fontsize=16)
plt.ylabel("max[k]", fontsize=16)

plt.show()

plt.plot(N_arr, max_N, color="green", label="Maximum of max[k]",  marker='o')
plt.xlabel("N", fontsize=16)
plt.ylabel("max[k]", fontsize=16)

plt.show()
