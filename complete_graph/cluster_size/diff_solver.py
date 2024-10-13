import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import curve_fit
import sys

if (len(sys.argv) < 5):
	print("python3 diff_solver.py N T M k_start k_fin")
	exit(1)

N = int(sys.argv[1])
T = int(sys.argv[2])
M = float(sys.argv[3])
k_start = int(sys.argv[4])
k_fin = int(sys.argv[5])

mul_factor = (1/(M*N))
#mul_factor = 1
A = 0.64
B = 0.84

def Q(k):
	return A * (k ** B)

def power_law(k, a, b):
	return a * (k ** b)

def fit_power(k, c, k_min, k_fin):
	popt, _ = curve_fit(power_law, k, c)

	c_fitted = power_law(k, *popt)
	return ([popt[0], popt[1]])

def coupled_ODE(t, c, N):
	dc_dt = np.zeros(N)

	dc_dt[0] = sum(mul_factor*c[k-1] * (k - 1) - M*c[0]*c[k-1]*Q(k) for k in range(2, N+1)) - M*c[0]**2

	for k in range(2, N):
		dc_dt[k-1] = -mul_factor*(c[k-1] * (k-1) + c[k]*k) + M*c[0]*(c[k-2]*Q(k-1) - c[k-1]*Q(k))

	dc_dt[N-1] = -mul_factor*(c[N-1] * (N-1)) + M*c[0]*(c[N-2]*Q(N-1))
	
	return dc_dt

#c_initial = np.random.uniform(low=1, high=N, size=N)
c_initial = np.random.uniform(low=1, high=N, size=N)
c_initial /= N*N
#c_initial = np.ones(N) / (N*M)

t_list = (0, T)

sol = solve_ivp(coupled_ODE, t_list, c_initial, args=(N,), method='RK45', dense_output=False)

c_at_T = sol.y[:, -1]

k_list = np.arange(1,N+1,1)
sum_val = np.sum(k_list*c_at_T)
sum_M = np.sum(c_at_T)
print(sum_val)
print(sum_M)
k = k_list
c_at_T[2:] = c_at_T[2:] / sum_val
c = c_at_T

np.savetxt('c_N{}_T{}.dat'.format(N,T), c)
k = k_list[k_start-1:k_fin-1]
c = c_at_T[k_start-1:k_fin-1]

fit_parameters = fit_power(k, c, k_start, k_fin)
factor = fit_parameters[0]
alpha = fit_parameters[1]

plt.scatter(k_list, c_at_T, label='T={} steps'.format(T), color='blue')
#plt.scatter(k[k_start-1:k_fin-1], c[k_start-1:k_fin-1], label='T={} steps'.format(T))
plt.plot(k_list, factor*(k_list**alpha), label='exponent={:.2f}'.format(alpha), color='red')
plt.title("N={}, M={}".format(N, M))
plt.xlabel('k')
plt.ylabel('c_k')
plt.xscale('log')
plt.yscale('log')
plt.legend(fontsize=15)
plt.show()

