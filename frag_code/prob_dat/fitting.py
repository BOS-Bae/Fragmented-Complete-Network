import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
import sys

ax = plt.figure().add_subplot(projection='3d')
if (len(sys.argv) < 2):
	print("python3 fitting r_num prob_name")
	exit(1)

r_num = int(sys.argv[1])
prob_name = sys.argv[2]

def p(X,a,b,c,d):
	m, n = X
	return (a*np.power(m,2) + b*m + c*np.power(n,2) + d*n)

dat = np.loadtxt("%s_L%d.dat" %(prob_name, r_num))
m = np.transpose(dat)[0]
n = np.transpose(dat)[1]
prob = np.transpose(dat)[2]

print(m)
print(n)
print(prob)
popt, pcov = curve_fit(p, (m,n), prob)
fit_prob = p((m,n), popt[0],popt[1],popt[2],popt[3])
print(popt)
print(fit_prob)
ax.scatter(m,n,prob, label="numerical data")
ax.scatter(m,n, fit_prob,label="{:.4f}m^2+{:.4f}m+{:.4f}n^2+{:.4f}n".format(popt[0],popt[1],popt[2],popt[3]))
ax.set_xticks([2,3,4,5])
ax.set_yticks([2,3,4,5])
plt.legend()
plt.title("L%d, %s(m,n)" %(r_num, prob_name))
plt.show()
