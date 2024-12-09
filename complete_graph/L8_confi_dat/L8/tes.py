import numpy as np
import matplotlib.pyplot as plt
import sys

A = 2.9
N_max = 50

R_dat = np.loadtxt("./L8-prob-R.dat")
P_dat = np.loadtxt("./L8-prob-P.dat")

for N in np.arange(20,N_max+10,10):
	m_arr = []; R = []; R = []; P = []
	for m in range(2, N-1):
		m_arr.append(m)
		R.append(R_dat[m,N-m])
	m_list = np.array(m_arr); R_list = np.array(R);
	plt.plot(m_list, R_list, marker='.', label="L={}".format(N))
	def fn(m,n):
		return A*np.exp(-0.78*m*np.power((m+n),-1.0/3.0))/(m+n)

	plt.plot(m_list, fn(m_list, N-m_list), color='black')

plt.legend(fontsize=14)
plt.xticks(fontsize=15)
plt.yticks(fontsize=14)
plt.xlabel("m", fontsize=16)
#plt.xscale('log')
plt.yscale('log')
plt.show()	
