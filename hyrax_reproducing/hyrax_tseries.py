import matplotlib.pyplot as plt
import numpy as np

ns = 50
N = 100
MCS = 1000
dat_PLS_B = np.zeros([ns, MCS])
dat_PLS_WB = np.zeros([ns, MCS])
dat_An_B = np.zeros([ns, MCS])
dat_An_WB = np.zeros([ns, MCS])

for s in range(ns):
    dat_PLS = np.loadtxt("WB_dat/hyrax_PLS_N{}_s{}.dat".format(N, s))
    dat_An = np.loadtxt("WB_dat/hyrax_Analytic_N{}_s{}.dat".format(N, s))
    dat_PLS_B[s] = np.transpose(dat_PLS)[1]
    dat_PLS_WB[s] = np.transpose(dat_PLS)[2]
    dat_An_B[s] = np.transpose(dat_An)[1]
    dat_An_WB[s] = np.transpose(dat_An)[2]

PLS_B_avg = np.average(dat_PLS_B, 0)
PLS_B_stderr = np.std(dat_PLS_B, 0) / np.sqrt(ns)
PLS_WB_avg = np.average(dat_PLS_WB, 0)
PLS_WB_stderr = np.std(dat_PLS_WB, 0) / np.sqrt(ns)
An_B_avg = np.average(dat_An_B, 0)
An_B_stderr = np.std(dat_An_B, 0) / np.sqrt(ns)
An_WB_avg = np.average(dat_An_WB, 0)
An_WB_stderr = np.std(dat_An_WB, 0) / np.sqrt(ns)

t = range(MCS)
plt.scatter(t, PLS_WB_avg, color='blue', marker='.', label="weak balance")
plt.errorbar(t, PLS_WB_avg, yerr=PLS_WB_stderr, color="blue")
plt.scatter(t, PLS_B_avg, color='lightseagreen', marker='.', label="balance")
plt.errorbar(t, PLS_B_avg, yerr=PLS_B_stderr, color="lightseagreen")
plt.xlabel("t", fontsize=16)
plt.title("Hyrax: PLS", fontsize=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=16)
plt.legend(fontsize=14)
plt.show()

plt.scatter(t, An_WB_avg, color='blue', marker='.', label="weak balance")
plt.errorbar(t, An_WB_avg, yerr=An_WB_stderr, color="blue")
plt.scatter(t, An_B_avg, color='lightseagreen', marker='.', label="balance")
plt.errorbar(t, An_B_avg, yerr=An_B_stderr, color="lightseagreen")
plt.xlabel("t", fontsize=16)
plt.title("Hyrax: Analtycal", fontsize=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=16)
plt.legend(fontsize=14)
plt.show()

