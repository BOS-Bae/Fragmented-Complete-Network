import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys

if (len(sys.argv) < 4):
	print("python3 plot_diff_sol.py c1 c2 M xmin")
	exit(1)

c1 = float(sys.argv[1]) 
c2 = float(sys.argv[2]) 
M = float(sys.argv[3])
xmin = int(sys.argv[4])

N = 500
M_start = 0.01
M_fin = 1.00
#M = 0.38

A = 0.64
B = 0.84


def frac(k):
	return ((k-1)/k)


def Q(k):
	A = 0.64
	B = 0.84
	return A * (k ** (1-B))


def power_law(k, a, b):
	return a * (k ** b)


def solve_difference_equation(c1, c2, M, N):
	c = np.zeros(N)
	c[0] = c1
	c[1] = c2

	for k in range(2, N):
		k_idx = k - 1
		c[k_idx+1] = frac(k)*c[k_idx] - (M**2)*N*(c1/k)*(c[k_idx-1]*Q(k-1) - c[k_idx]*Q(k))
	
	summ = 0
	M_num = 0
	print(c)
	for k in range(1,N+1):
		k_idx = k - 1
		M_num += c[k_idx]
		summ += k*c[k_idx]
	c[2:] /= summ
	#c[0] = c1; c[1] = c2
	print(M_num)
	return c


def fit_power(c, N, xmin):
	k_values = np.arange(xmin, N+1)
	c_values = c[xmin-1:N]
	popt, _ = curve_fit(power_law, k_values, c_values)

	c_fitted = power_law(k_values, *popt)
	return ([popt[0], popt[1]])
	
def plot_fig(c_values, c_parameters):
	k_values = np.arange(1, N+1)
	plt.scatter(k_values, c_values, label='numerical solution', color='blue')
	plt.plot(k_values, power_law(k_values, c_parameters[0], c_parameters[1]), label='exponent : {:.2f}'.format(c_parameters[1]), color='red')
	
	plt.xlabel('k',fontsize=18)
	plt.ylabel('c[k]',fontsize=18)
	plt.xticks(fontsize=13)
	plt.yticks(fontsize=13)
	plt.legend(fontsize=15)
	plt.xscale('log')
	plt.yscale('log')
	plt.title('c1={}, c2={}, M={}, xmin={}'.format(c1,c2,M,xmin), fontsize=19)
	plt.show()
	
c_values = solve_difference_equation(c1, c2, M, N)
fit_parameters = fit_power(c_values, N, xmin)
fit_exponent = fit_parameters[1]
plot_fig(c_values, fit_parameters)
print(fit_exponent)
