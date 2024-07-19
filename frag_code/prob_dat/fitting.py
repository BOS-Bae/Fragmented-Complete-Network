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
M_max = 6

def p(X,a,b,c,d,f,g):
    m, n = X
    return (a*m +b*n +c/m +d/n +f*m*n +g)
#	return (a*(m+n) + b*m*n +c*(m/n) + d*np.power(m+n,2) + f*n/m)

dat = np.loadtxt("./dat/%s_L%d" %(prob_name, r_num))
m = np.transpose(dat)[0]
n = np.transpose(dat)[1]
prob = np.transpose(dat)[2]

#print(m)
#print(n)
print(prob)
popt, pcov = curve_fit(p, (m,n), prob)
fit_prob = p((m,n), popt[0],popt[1],popt[2],popt[3], popt[4], popt[5])
print(fit_prob)
print(popt)
ax.scatter(m,n,prob, label="numerical data, L{}, {}(m,n)".format(r_num,prob_name))
#ax.scatter(m,n, fit_prob,label="{:.2f}(m+n) + {:.2f}m*n + {:.2f}m/n + {:.2f}(m+n)^2 + {:.2f}n/m".format(popt[0],popt[1],popt[2],popt[3],popt[4]))
ax.scatter(m,n, fit_prob,label="am +bn +c/m + d/n + fmn + g")
ax.set_xticks(range(1,M_max+1))
ax.set_xlabel('m')
ax.set_yticks(range(1,M_max+1))
ax.set_ylabel('n')
ax.set_xlim([1,M_max+1])
ax.set_ylim([1,M_max+1])
plt.legend()

plt.title("a={:.3f}, b={:.3f}, c={:.3f}, d={:.3f}, f={:.3f}, g={:.3f}".format(popt[0],popt[1],popt[2],popt[3],popt[4],popt[5]))
plt.show()
