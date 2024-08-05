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

def R7(X,a,b,c):
	m, n = X
	return (a + b*(m+n) + c*m*n)

def Q7(X,a,b,c):
	m, n = X
	return (a + b*(m+n) + c*m*n)

def p8(X,a,b,c):
	m, n = X
	return (a*m)*(b - c*m - d*np.exp(f*n))

def R8(X,a,b,c):
	m, n = X
	return (a + b*(m+n) + c*m*n)

dat = np.loadtxt("./dat/%s_L%d" %(prob_name, r_num))
m_arr = []
n_arr = []
prob_arr = []

if (prob_name == 'q'):
	for i in range(int(len(dat))):
		if (i % 2 == 0):
			m = dat[i,0];	n = dat[i,1]; prob1 = dat[i,2]; prob2 = dat[i+1,2]
			if (m >= 4 and n >= 4):
				prob = (prob1 + prob2)*m*n
				m_arr.append(m); n_arr.append(n); prob_arr.append(prob)
elif (prob_name == 'p' or prob_name == 'r'):
	check_idx = 0
	idx = 1
	for i in range(int(len(dat))):
		if (i == check_idx):
			#m = dat[i,0]; n = dat[i,1]; prob = dat[i,2]
			#m_arr.append(m); n_arr.append(n); prob_arr.append(prob)
			idx += 2
			check_idx += idx
		else:
			m = dat[i,0];	n = dat[i,1]; prob1 = dat[i,2]; prob2 = dat[i+1,2]
			if (m >= 4 and n >= 4):
				prob = (prob1 + prob2)*m*n
				m_arr.append(m); n_arr.append(n); prob_arr.append(prob)
			
m = np.array(m_arr)
n = np.array(n_arr)
prob = np.array(prob_arr)

print(prob)
func_name = ""
if (prob_name == 'p' and r_num == 7): 
	popt, pcov = curve_fit(p7, (m,n), prob)
	fit_prob = p7((m,n), *popt)
elif (prob_name == 'p' and r_num == 8): 
	popt, pcov = curve_fit(p8, (m,n), prob)
	fit_prob = p8((m,n), *popt)
	func_name = "(am^2+ bm)(c/m - exp(dn)) (n=1 x)"
elif (prob_name == 'q' and r_num == 7): 
	popt, pcov = curve_fit(Q7, (m,n), prob)
	fit_prob = Q7((m,n), *popt)
elif (prob_name == 'r' and r_num == 7): 
	popt, pcov = curve_fit(R7, (m,n), prob)
	fit_prob = R7((m,n), *popt)
	#fit_prob = R7((m,n), popt[0],popt[1],popt[2],popt[3], popt[4], popt[5], popt[6])
elif (prob_name == 'r' and r_num == 8): 
	popt, pcov = curve_fit(R8, (m,n), prob)
	fit_prob = R8((m,n), *popt)
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
