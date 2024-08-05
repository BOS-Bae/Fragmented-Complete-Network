import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
import sys

if (len(sys.argv) < 3):
	print("python3 fitting r_num prob_name M_fit")
	exit(1)

r_num = int(sys.argv[1])
prob_name = sys.argv[2]
M_fit = int(sys.argv[3])
M_max = 7

if (prob_name != 'p'): 
	ax = plt.figure().add_subplot(projection='3d')

def P7(m,a,b):
	return (a + b*m)

def R7(X,a,b,c):
	m, n = X
	return (a + b*(m+n) + c*m*n)

def Q7(X,a,b,c):
	m, n = X
	return (a + b*(m+n) + c*m*n)

def P8(m,a,b):
	return (a + b*m)

def R8(X,a,b,c):
	m, n = X
	return (a + b*(m+n) + c*m*n)

dat = np.loadtxt("./dat/%s_L%d" %(prob_name, r_num))
m_arr = []; m_fit = []
n_arr = []; n_fit = []
prob_arr = []; prob_fit = []

if (prob_name == 'q'):
	for i in range(len(dat)):
		if (i % 2 == 0):
			m = dat[i,0];	n = dat[i,1]; prob1 = dat[i,2]; prob2 = dat[i+1,2]
			prob = (prob1 + prob2)*m*n
			m_arr.append(m); n_arr.append(n); prob_arr.append(prob)
			if (m >= M_fit and n >= M_fit):
				m_arr.append(m); n_arr.append(n); prob_arr.append(prob)
				m_fit.append(m); n_fit.append(n); prob_fit.append(prob)
elif (prob_name == 'r'):
	for i in range(len(dat)):
		m = dat[i,0];	n = dat[i,1]; prob = dat[i,2]
		prob *= (m*n)
		m_arr.append(m); n_arr.append(n); prob_arr.append(prob)
		if (m >= M_fit and n >= M_fit):
			m_fit.append(m); n_fit.append(n); prob_fit.append(prob)
elif (prob_name == 'p'):
	sorted_idx = np.argsort(np.array(dat[:,0]))
	dat = dat[sorted_idx]

	for m in range(1, M_max+1):
		prob_sum = 0
		check = 0
		for i in range(len(dat)):
			if (dat[i,0] == m):
				check += 1
				n = dat[i,1]; prob = dat[i,2]
				prob *= (m*n)
				prob_sum += prob
		if (check != 0) : m_arr.append(m); prob_arr.append(prob_sum)
		print(m, " ",check)
		if (m >= M_fit):
			m_fit.append(m); prob_fit.append(prob_sum)
	
m_fit = np.array(m_fit); n_fit = np.array(n_fit); prob_fit = np.array(prob_fit)
m = np.array(m_arr); n = np.array(n_arr); prob = np.array(prob_arr)

#print(prob)
func_name = ""
if (prob_name == 'p' and r_num == 7): 
	popt, pcov = curve_fit(P7, m_fit, prob_fit)
	fit_prob = P7(m, *popt)
elif (prob_name == 'p' and r_num == 8): 
	popt, pcov = curve_fit(P8, m_fit, prob_fit)
	fit_prob = P8(m, *popt)
	func_name = "(am^2+ bm)(c/m - exp(dn)) (n=1 x)"
elif (prob_name == 'q' and r_num == 7): 
	popt, pcov = curve_fit(Q7, (m_fit,n_fit), prob_fit)
	fit_prob = Q7((m,n), *popt)
	func_name = "a + b*(m+n) + c*m*n"
elif (prob_name == 'r' and r_num == 7): 
	popt, pcov = curve_fit(R7, (m_fit,n_fit), prob_fit)
	fit_prob = R7((m,n), *popt)
	#fit_prob = R7((m,n), popt[0],popt[1],popt[2],popt[3], popt[4], popt[5], popt[6])
elif (prob_name == 'r' and r_num == 8): 
	popt, pcov = curve_fit(R8, (m_fit,n_fit), prob_fit)
	fit_prob = R8((m,n), *popt)
	func_name = "(a*exp(bn) + c*m^2)exp(dm)"

#print(fit_prob)
print(popt)

if (prob_name != 'p'): 
	ax.scatter(m,n,prob, label="numerical data, L{}, {}(m,n)".format(r_num,prob_name))
	ax.scatter(m,n, fit_prob, label="{}".format(func_name))
	ax.set_xticks(range(1,M_max+1))
	ax.set_xlabel('m')
	ax.set_yticks(range(1,M_max+1))
	ax.set_ylabel('n')
	ax.set_xlim([1,M_max+1])
	ax.set_ylim([1,M_max+1])
	plt.legend(fontsize='10', loc='upper right')
	if (prob_name == 'q'): plt.title("a={:.3f}, b={:.3f}, c={:.3f}".format(popt[0], popt[1], popt[2]))
else:
	print(m)
	print(prob)
	plt.plot(m,prob, label="numerical data, L{}, {}(m,1)".format(r_num,prob_name), marker = 'o')
	plt.plot(m,fit_prob, label="{}".format(func_name), marker ='o')
	plt.xticks(range(1,M_max+1))
	plt.xlabel('m')
	plt.xlim([1,M_max+1])
	plt.legend(fontsize='7.5', loc='upper right')

plt.show()
