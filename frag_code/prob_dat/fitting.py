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
M_max = 7

def p7(X,a,b,c,d,f,g,h,k):
	m, n = X
	return ((b*m)*np.exp(-c*m) + (d*np.power(n,3) + f*np.power(n,2) + g*n)*np.exp(-h*n) + k)

def r7(X,a,b,c,d,f):
	m, n = X
	return ((a*np.exp(b*n) + c*np.power(m,2) + d*m)*np.exp(f*m))

def q7(X,a,b,c,d,f,g):
	m, n = X
	return (a*m +b*n +c/m +d/n +f*m*n +g)

def p8(X,a,b,c,d,f):
	m, n = X
	return (a*m)*(b - c*m - d*np.exp(f*n))

def r8(X,a,b,c,d):
	m, n = X
	return ((a*np.exp(b*n) + c*np.power(m,2) )*np.exp(d*m))

dat = np.loadtxt("./dat/%s_L%d" %(prob_name, r_num))
m = np.transpose(dat)[0]
n = np.transpose(dat)[1]
prob = np.transpose(dat)[2]

#print(prob)
func_name = ""
if (prob_name == 'p' and r_num == 7): 
	popt, pcov = curve_fit(p7, (m,n), prob)
	fit_prob = p7((m,n), *popt)
elif (prob_name == 'p' and r_num == 8): 
	popt, pcov = curve_fit(p8, (m,n), prob)
	fit_prob = p8((m,n), *popt)
	func_name = "(am^2+ bm)(c/m - exp(dn)) (n=1 x)"
elif (prob_name == 'q' and r_num == 7): 
	popt, pcov = curve_fit(q7, (m,n), prob)
	fit_prob = q7((m,n), *popt)
elif (prob_name == 'r' and r_num == 7): 
	popt, pcov = curve_fit(r7, (m,n), prob)
	fit_prob = r7((m,n), *popt)
	#fit_prob = r7((m,n), popt[0],popt[1],popt[2],popt[3], popt[4], popt[5], popt[6])
elif (prob_name == 'r' and r_num == 8): 
	popt, pcov = curve_fit(r8, (m,n), prob)
	fit_prob = r8((m,n), *popt)
	func_name = "(a*exp(bn) + c*m^2)exp(dm)"

#print(fit_prob)
print(popt)

ax.scatter(m,n,prob, label="numerical data, L{}, {}(m,n)".format(r_num,prob_name))
ax.scatter(m,n, fit_prob, label="{}".format(func_name))

ax.set_xticks(range(1,M_max+1))
ax.set_xlabel('m')
ax.set_yticks(range(1,M_max+1))
ax.set_ylabel('n')
ax.set_xlim([1,M_max+1])
ax.set_ylim([1,M_max+1])
plt.legend(fontsize='7.5', loc='upper right')
plt.show()
