import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
import sys

if (len(sys.argv) < 7):
	print("python3 fitting.py r_num prob_name M_fit proj_mode m_or_n_fixed xlog ylog")
	exit(1)

r_num = int(sys.argv[1])
prob_name = sys.argv[2]
M_fit = int(sys.argv[3])
proj_mode = int(sys.argv[4])
m_or_n = sys.argv[5]
xlog = int(sys.argv[6])
ylog = int(sys.argv[7])
M_max = 8

color_list = ["black", "purple", "blue", "lightseagreen", "green","orange", "gold", "red"]

if ((prob_name != 'P' and prob_name != 'prime' and not(prob_name == 'Q' and r_num == 8)) and proj_mode != 1): 
	ax = plt.figure().add_subplot(projection='3d')

def P7(m,a,b):
	return (a*np.exp(-b*m))

def R7(X,a,b,c):
	m, n = X
	return (a + b*(m+n) + c*m*n)

def Q7(X,a,b,c):
	m, n = X
	return (a + b*(m+n) + c*m*n)

def Q8(n,a,b):
	return (a*np.power(n,b))

def P8(m,a,b):
	return (a*m + b)

def R8(X,a,b,c):
	m, n = X
	return (a*np.power(n,b))*(np.exp(c*m))

def prime7(m,a,b):
	return (a*np.power(m,b))

def prime8(m,a,b):
	return (a*m + b)

dat_name = 'none'
if (prob_name == 'P') : dat_name = 'p'
elif (prob_name == 'Q') : dat_name = 'q'
elif (prob_name == 'R') : dat_name = 'r'
elif (prob_name == 'prime') : dat_name = 'prime'


dat = np.loadtxt("./dat/%s_L%d" %(dat_name, r_num))
m_arr = []; m_fit = []
n_arr = []; n_fit = []
prob_arr = []; prob_fit = []
err_arr = []; err_fit = []

if (prob_name == 'Q' and r_num == 7):
	for i in range(len(dat)):
		if (i % 2 == 0):
			m = dat[i,0];	n = dat[i,1]; prob1 = dat[i,2]; prob2 = dat[i+1,2]
			err = dat[i,3]
			prob = (prob1 + prob2)*m*n
			m_arr.append(m); n_arr.append(n); prob_arr.append(prob); err_arr.append(err)
			if (m >= M_fit and n >= M_fit):
				m_fit.append(m); n_fit.append(n); prob_fit.append(prob); err_fit.append(err)
elif (prob_name == 'Q' and r_num == 8):
	for i in range(len(dat)):
		m = dat[i,0];	n = dat[i,1]; prob = dat[i,2];
		err = dat[i,3]
		prob *= m*n
		m_arr.append(m); n_arr.append(n); prob_arr.append(prob); err_arr.append(err)
		if (n >= M_fit):
			m_fit.append(m); n_fit.append(n); prob_fit.append(prob); err_fit.append(err)
elif (prob_name == 'R'):
	for i in range(len(dat)):
		m = dat[i,0];	n = dat[i,1]; prob = dat[i,2]
		err = dat[i,3]
		prob *= (m*n)
		m_arr.append(m); n_arr.append(n); prob_arr.append(prob); err_arr.append(err)
		if (m >= M_fit and n >= M_fit):
			m_fit.append(m); n_fit.append(n); prob_fit.append(prob); err_fit.append(err)
elif (prob_name == 'P'):
	sorted_idx = np.argsort(np.array(dat[:,0]))
	dat = dat[sorted_idx]
	for m in range(1, M_max+1):
		prob_sum = 0
		check = 0
		for i in range(len(dat)):
			if (dat[i,0] == m):
				check += 1
				n = dat[i,1]; prob = dat[i,2]; err = dat[i,3]
				prob *= (m*n)
				prob_sum += prob
		if (check != 0) : 
			m_arr.append(m); prob_arr.append(prob_sum); err_arr.append(err)
		#print(m, " ",check)
		if (m >= M_fit):
			m_fit.append(m); prob_fit.append(prob_sum); err_fit.append(err)
elif (prob_name == 'prime'):
	for i in range(len(dat)):
		m = dat[i,0];	prob = dat[i,1]; err = dat[i,2]
		prob *= (m*(m-1))
		m_arr.append(m); prob_arr.append(prob); err_arr.append(err)
		if (m >= M_fit):
			m_fit.append(m); prob_fit.append(prob); err_fit.append(err)
	
m_fit = np.array(m_fit); n_fit = np.array(n_fit); prob_fit = np.array(prob_fit)
m = np.array(m_arr); n = np.array(n_arr); prob = np.array(prob_arr)

#print(prob)
if (proj_mode == 0):
	func_name = ""
	if (prob_name == 'P' and r_num == 7): 
		popt, pcov = curve_fit(P7, m_fit, prob_fit)
		fit_prob = P7(m, *popt)
		func_name = "a*exp(-b*m)"
	elif (prob_name == 'P' and r_num == 8): 
		popt, pcov = curve_fit(P8, m_fit, prob_fit)
		fit_prob = P8(m, *popt)
		func_name = "(am^2+ bm)(c/m - exp(dn)) (n=1 x)"
	elif (prob_name == 'Q' and r_num == 7): 
		popt, pcov = curve_fit(Q7, (m_fit,n_fit), prob_fit)
		fit_prob = Q7((m,n), *popt)
		#fit_prob = Q7((m,n), *popt)
		func_name = "a + b*(m+n) + c*m*n"
	elif (prob_name == 'Q' and r_num == 8): 
		popt, pcov = curve_fit(Q8, n_fit, prob_fit)
		fit_prob = Q8(n, *popt)
		#fit_prob = Q7((m,n), *popt)
		func_name = "a*(n^b)"
	elif (prob_name == 'R' and r_num == 7): 
		popt, pcov = curve_fit(R7, (m_fit,n_fit), prob_fit)
		fit_prob = R7((m,n), *popt)
		#fit_prob = R7((m,n), popt[0],popt[1],popt[2],popt[3], popt[4], popt[5], popt[6])
	elif (prob_name == 'R' and r_num == 8): 
		popt, pcov = curve_fit(R8, (m_fit,n_fit), prob_fit)
		fit_prob = R8((m,n), *popt)
		func_name = "(a*n^b)*exp(c*m)"
	elif (prob_name == 'prime' and r_num == 7): 
		popt, pcov = curve_fit(prime7, m_fit, prob_fit)
		fit_prob = prime7(m, *popt)
		func_name = "a*exp(-bm)"
	elif (prob_name == 'prime' and r_num == 8): 
		popt, pcov = curve_fit(prime8, m_fit, prob_fit)
		fit_prob = prime8(m, *popt)
		func_name = "a*m + b"

	print(popt)
	if (prob_name != 'P' and prob_name != 'prime' and r_num == 7):
		m_fit = list(m_fit); n_fit = list(n_fit); err_fit = list(err_fit);
		ax.scatter(m,n,prob_arr, label="numerical data, L{}, {}(m,n)".format(r_num,prob_name))
		ax.scatter(m,n, fit_prob, label="{}".format(func_name))
		ax.set_xticks(range(1,M_max+1))
		ax.set_xlabel('m')
		ax.set_yticks(range(1,M_max+1))
		ax.set_ylabel('n')
		#ax.set_xlim([M_fit-1,M_max+1])
		#ax.set_ylim([M_fit-1,M_max+1])
		plt.legend(fontsize='10', loc='upper right')
		if (prob_name == 'Q'): plt.title("a={:.3f}, b={:.3f}, c={:.3f}".format(popt[0], popt[1], popt[2]))
	elif (prob_name == 'R' and r_num == 8):
		m_fit = list(m_fit); n_fit = list(n_fit); err_fit = list(err_fit);
		ax.scatter(m,n,prob_arr, label="numerical data, L{}, {}(m,n)".format(r_num,prob_name))
		ax.scatter(m,n, fit_prob, label="{}".format(func_name))
		ax.set_xticks(range(1,M_max+1))
		ax.set_xlabel('m')
		ax.set_yticks(range(1,M_max+1))
		ax.set_ylabel('n')
		#ax.set_xlim([M_fit-1,M_max+1])
		#ax.set_ylim([M_fit-1,M_max+1])
		plt.legend(fontsize='10', loc='upper right')
	elif (prob_name == 'Q' and r_num == 8):
		plt.plot(n,prob, label="numerical data, L{}, {}(1,n)".format(r_num,prob_name), marker = 'o')
		plt.plot(n,fit_prob, label="{}".format(func_name), marker ='o')
		plt.xticks(range(1,M_max+1))
		plt.xlabel('n', fontsize='20')
		plt.xlim([1,M_max+1])
		plt.legend(fontsize='13', loc='lower right')
		plt.title("a={:.3f}, b={:.3f}".format(popt[0], popt[1]))

	elif (prob_name == 'P' or prob_name == 'prime'):
		plt.plot(m,prob, label="numerical data, L{}, {}(m)".format(r_num,'P*'), marker = 'o')
		plt.plot(m,fit_prob, label="{}".format(func_name), marker ='o')
		plt.xticks(range(1,M_max+1))
		plt.xlabel('m', fontsize='20')
		plt.xlim([1,M_max+1])
		plt.legend(fontsize='13', loc='upper right')
		plt.title("a={:.3f}, b={:.3f}".format(popt[0], popt[1]))
	
else:
	if (m_or_n == 'm'):
		idx = 0
		for m_idx in range(M_fit, M_max + 1):
			n_list = []; p = []; err = []
			for i in range(len(prob_arr)):
				m = m_arr[i]; n = n_arr[i]; prob_i = prob_arr[i]; err_i = err_arr[i]
				if (m == m_idx): 
					n_list.append(n)
					p.append(prob_i)
					err.append(err_i)
			sorted_idx = np.argsort(np.array(n_list))
			n_list = np.array(n_list); p = np.array(p); err = np.array(err)
			n_list = n_list[sorted_idx]; p = p[sorted_idx]; err = err[sorted_idx]
			plt.plot(n_list, p, label = "m={}".format(m_idx), color = color_list[idx], marker='o')
			plt.errorbar(n_list, p, yerr=err, color = color_list[idx])
			idx += 1
		plt.legend()
		plt.xlabel('n', fontsize=20)
		plt.xticks(range(M_fit, M_max +1))
		plt.xlim([M_fit, M_max +1])
	elif (m_or_n == 'n'):
		idx = 0
		for n_idx in range(M_fit, M_max + 1):
			m_list = []; p = []; err = []
			for i in range(len(prob_arr)):
				m = m_arr[i]; n = n_arr[i]; prob_i = prob_arr[i]; err_i = err_arr[i]
				if (n == n_idx): 
					m_list.append(m)
					p.append(prob_i)
					err.append(err_i)
			sorted_idx = np.argsort(np.array(m_list))
			m_list = np.array(m_list); p = np.array(p); err = np.array(err)
			m_list = m_list[sorted_idx]; p = p[sorted_idx]; err = err[sorted_idx]
			plt.plot(m_list, p, label = "n={}".format(n_idx), color = color_list[idx], marker='o')
			plt.errorbar(m_list, p, yerr=err, color = color_list[idx])
			idx += 1
		plt.legend()
		plt.xlabel('m', fontsize=20)
		plt.xticks(range(M_fit, M_max +1))
		plt.xlim([M_fit, M_max +1])

if (xlog == 1): plt.xscale('log')
if (ylog == 1): plt.yscale('log')
plt.show()
