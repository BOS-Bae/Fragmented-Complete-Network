import numpy as np
import matplotlib.pyplot as plt
import sys

fix_setting = int(sys.argv[1])
if (fix_setting != 0 and fix_setting != 1):
    print("fix_setting should be 0 or 1.")
    exit(1)
# 0 : pr fixed
# 1 : pn fixed
n_points = 21

tot_dat = np.loadtxt("./fig2_pn_pr.dat")
pr_fix_arr = [0.5, 0.3, 0.1]
pn_fix_arr = [0.9, 0.6, 0.3]

p_list = np.linspace(0.0, 1.0, n_points)

if (fix_setting == 0):
    fig2_avg = np.zeros([len(pr_fix_arr), n_points])
    fig2_stderr = np.zeros([len(pr_fix_arr), n_points])
    idx = 0
    for pr in pr_fix_arr:
        idx2 = 0
        for i in range(len(tot_dat)):
            dat_i = tot_dat[i]
            if (dat_i[1] == pr):
                fig2_avg[idx, idx2] = dat_i[2]
                fig2_stderr[idx, idx2] = dat_i[3]
                idx2 += 1
        idx += 1
    
    idx = 0
    for pr in pr_fix_arr:
        plt.plot(p_list, fig2_avg[idx, :], marker='o', color='black')
        plt.errorbar(p_list, fig2_avg[idx, :], yerr=fig2_stderr[idx, :], color='black')
        idx += 1
    plt.xlabel("pn", fontsize=15)

elif (fix_setting == 1):
    fig2_avg = np.zeros([len(pn_fix_arr), n_points])
    fig2_stderr = np.zeros([len(pn_fix_arr), n_points])
    idx = 0
    for pn in pn_fix_arr:
        idx2 = 0
        for i in range(len(tot_dat)):
            dat_i = tot_dat[i]
            if (dat_i[0] == pn):
                fig2_avg[idx, idx2] = dat_i[2]
                fig2_stderr[idx, idx2] = dat_i[3]
                idx2 += 1
        idx += 1
    
    idx = 0
    for pr in pr_fix_arr:
        plt.plot(p_list, fig2_avg[idx, :], marker='o', color='black')
        plt.errorbar(p_list, fig2_avg[idx, :], yerr=fig2_stderr[idx, :], color='black')
        idx += 1
    plt.xlabel("pr", fontsize=15)

plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.ylabel("Mean degree", fontsize=15)
plt.show()
