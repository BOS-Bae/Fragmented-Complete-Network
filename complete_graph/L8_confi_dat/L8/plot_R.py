import numpy as np
import matplotlib.pyplot as plt

N=50
R = np.loadtxt("./L8-prob-R.dat")
P = np.loadtxt("./L8-prob-P.dat")

for m in range(2,N+1):
	n_arr = np.array(range(N+1))
	R_m_n = R[m]
	P_m_n = P[m]
	plt.plot(n_arr[1:], R_m_n[1:], marker='.')
plt.plot(n_arr[1:], 1/(n_arr[1:]+1), label="Q(n)", marker='.')
plt.legend(fontsize=16)
#plt.legend(fontsize=12)
plt.xlabel("n", fontsize=18)
plt.xticks(fontsize=15)
plt.yticks(fontsize=14)
plt.yscale('log')
plt.show()	
