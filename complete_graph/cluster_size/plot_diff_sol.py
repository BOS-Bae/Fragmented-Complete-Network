import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys

c1 = float(sys.argv[1])
c2 = float(sys.argv[2])
xmin = int(sys.argv[3])

N = 500
M_start = 0.01
M_fin = 1.00
M = 0.38
   # Initial condition c[0]
A = 0.64
B = 0.84


def frac(k):
	return ((k-1)/k)


def Q(k):
	A = 0.64
	B = 0.84
	return A*(k ** B)


def power_law(k, a, b):
	return a * k ** b


def solve_difference_equation(c1, c2, M, N):
	c = np.zeros(N)
	c[0] = c1
	c[1] = c2

	for k in range(3, N+1):
		k_idx = k - 1
		c[k_idx] = frac(k-1)*c[k_idx-1] - (M*c1/(k-1))*(c[k_idx-2]*Q(k-2) - c[k_idx-1]*Q(k-1))
	
	return c


def fit_power(c, N, xmin):
	k_values = np.arange(xmin, N+1)
	c_values = c[xmin-1:N]
	popt, _ = curve_fit(power_law, k_values, c_values)

	c_fitted = power_law(k_values, *popt)
	return ([popt[0], popt[1]])
	
def plot_fig(c_values, c_parameters, N):
	k_values = np.arange(1, N+1)
	plt.scatter(k_values, c_values, label='numerical solution', color='blue')
	plt.plot(k_values, power_law(k_values, c_parameters[0], c_parameters[1]), label='fitted curve: {:.2f}*k^{:.2f}'.format(c_parameters[0], c_parameters[1]), color='red')
	
	plt.xlabel('k')
	plt.ylabel('c[k]')
	plt.legend(fontsize=15)
	plt.xscale('log')
	plt.yscale('log')
	plt.show()
	

c_values = solve_difference_equation(c1, c2, M, N)
fit_parameters = fit_power(c_values, N, xmin)
fit_exponent = fit_parameters[1]
plot_fig(c_values, fit_parameters, N)
print(fit_exponent)
