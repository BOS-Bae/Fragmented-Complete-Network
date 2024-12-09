import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys

N_max = 50
A = float(sys.argv[1])
a = float(sys.argv[2])

R_dat = np.loadtxt("./L8-prob-R.dat")
P_dat = np.loadtxt("./L8-prob-P.dat")

for N in np.arange(20,N_max+10,10):
	m_arr = []; R = []; R = []; P = []
	for m in range(2, N-1):
		m_arr.append(m)
		R.append(R_dat[m,N-m])
	m_list = np.array(m_arr); R_list = np.array(R);
	plt.plot(m_list*np.power(N,-1/3), N*R_list, marker='.', label="L={}".format(N))
	def fn(m):
		return A*np.exp(-a*m)
	
plt.plot(np.arange(1,N_max,1)*np.power(N,-1/3), fn(np.arange(1,N_max,1)*np.power(N,-1/3)), color='black', label="{:.1f}e^(-{:.1f}x)".format(A,a))
plt.legend(fontsize=14)
plt.xticks(fontsize=15)
plt.yticks(fontsize=14)
plt.xlabel("mL^{-1/3}", fontsize=16)
plt.ylabel("LR(m,L-m)", fontsize=16)
#plt.xscale('log')
plt.yscale('log')
plt.xlim([0,13])
plt.show()	
