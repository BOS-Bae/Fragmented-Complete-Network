import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys

N_max = 50
sl = 10
R_dat = np.loadtxt("./L8-prob-R.dat")
P_dat = np.loadtxt("./L8-prob-P.dat")

m_arr = []; R = [];
for m in np.arange(2,N_max):
	m_arr.append(m)
	R.append(R_dat[m,1])
	m_list = np.array(m_arr); R_list = np.array(R);
plt.plot(m_list, R_list, marker='.')

def fn(m, a, b):
	return a*np.power(m,-b)
popt, cov = curve_fit(fn, m_list[sl:], R_list[sl:])
plt.plot(m_list, fn(m_list, *popt), marker='.', label="{:.2f}m^{:.2f}".format(popt[0], popt[1]))

print(popt[0], " ", popt[1])
print(fn(14, *popt))

plt.legend(fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=14)
plt.xlabel("m", fontsize=17)
plt.ylabel("R(m,1)", fontsize=17)
plt.xscale('log')
plt.yscale('log')
plt.show()	
