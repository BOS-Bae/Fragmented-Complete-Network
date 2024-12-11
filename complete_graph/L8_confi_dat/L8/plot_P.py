import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys

N_max = 50

R_dat = np.loadtxt("./L8-prob-R.dat")
P_dat = np.loadtxt("./L8-prob-P.dat")

for N in np.arange(10,N_max+10,10):
	m_arr = []; R = []; R = []; P = []
	for m in range(2, N):
		m_arr.append(m)
		R.append(R_dat[m,N-m])
	m_list = np.array(m_arr); R_list = np.array(R);
	plt.plot(m_list, R_list, marker='.', label="L={}".format(N))
	#def fn(m):
	#	return (1+np.exp((m-N)/N**0.4))*(2.5*np.exp(-1.0*(m-1)/N**0.4)-1.5*np.exp(-1.5*(m-1)/N**0.4)) / N

	#plt.plot(m_list, fn(m_list), color='black')
	
plt.legend(fontsize=14)
plt.xticks(fontsize=15)
plt.yticks(fontsize=14)
plt.xlabel("m", fontsize=17)
plt.ylabel("R(m,L-m)", fontsize=17)
#plt.xscale('log')
plt.yscale('log')
plt.show()	
