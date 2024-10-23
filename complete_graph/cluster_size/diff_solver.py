import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.integrate import odeint
from scipy.optimize import curve_fit
import sys

if (len(sys.argv) < 5):
	print("python3 diff_solver.py N T k_fit k_fin fit_mode")
	exit(1)

N = int(sys.argv[1])
T = float(sys.argv[2])
#M = float(sys.argv[3])
k_fit = int(sys.argv[3])
k_fin = int(sys.argv[4])
fit_mode = int(sys.argv[5])

#mul_factor = (1/M)
mul_factor = 1
a = 0.40
b = 0.32
c = 0.47
A = 0.64
B = 0.84
alpha = 0.27
beta = 1.48
gamma = 0.36

def Q(k):
	return A * (k ** B)

def R(m,n):
	return a * np.exp(-b*m) * np.power(n,-c)

def P(m,n):
	return alpha*np.power(m,-beta)*(m+np.exp(-gamma*n))

def power_law(k, a, b):
	return a * (k ** b)

def fit_power(k, c, k_min, k_fin):
	popt, _ = curve_fit(power_law, k, c)

	c_fitted = power_law(k, *popt)
	return ([popt[0], popt[1]])

def coupled_ODE(t,c,N):
	dc_dt = np.zeros(N)

	dc_dt[0] = (mul_factor*(sum(sum((m*n*c[m-1]*c[n-1]*P(m,n)) for m in range(2, N-1)) for n in range(1, N-1)))
			+ mul_factor*(sum((c[k-1] * (k - 1) - c[0]*c[k-1]*Q(k) +2*k*c[0]*c[k-1]*R(2,k) ) for k in range(2, N-1)) - c[0]**2))

	for k in range(2, N-1):
		dc_dt[k-1] = ( mul_factor*(sum(( -c[k-1]*k*n*c[n-1]*(P(k,n)+R(k,n)) + c[k]*(k+1)*n*c[n-1]*(P(k+1,n)+R(k+1,n)) + c[k-2]*n*(k-1)*c[n-1]*R(n,k-1)) for n in range(1,N-1)) 
				+  mul_factor*(-(c[k-1] * (k-1) - c[k]*k) + c[0]*(c[k-2]*(k-1)*Q(k-1) - c[k-1]*k*Q(k)))))

		dc_dt[N-1] = ( mul_factor*(sum(( -c[N-1]*N*n*c[n-1]*(P(N,n)+R(N,n)) + c[N-2]*n*(N-1)*c[n-1]*R(n,N-1)) for n in range(1,N-2)) 
				+  mul_factor*(-(c[N-1] * (N-1)) + c[0]*(c[N-2]*(N-1)*Q(N-1) - c[N-1]*N*Q(N)))))
	
	return (dc_dt)

	#return dc_dt

#c_initial = list(np.random.uniform(low=0.00001, high=0.001, size=N))
c_initial = list(0.0001*np.ones(N))
#print(c_initial)
t_list = (0, T)
#t_list = np.arange(0,T,0.05)

sol = solve_ivp(coupled_ODE, t_list, c_initial, args=(N,), method='RK45')
#sol = np.array(odeint(coupled_ODE, c_initial, t_list, args=(N,mul_factor)))

c_at_T = sol.y[:, -1]
#c_at_T = np.exp(sol[-1,:])
k_list = np.arange(1,N+1,1)
sum_val = np.sum(k_list*c_at_T)
sum_M = np.sum(c_at_T)
print(sum_val)
print(sum_M)
k = k_list
print(c_at_T)
#c_at_T[2:] = c_at_T[2:] / sum_val
c_at_T /= sum_val

#np.savetxt('c_N{}_T{}.dat'.format(N,T), c)
k = k_list[k_fit-1:k_fin-1]
c = c_at_T[k_fit-1:k_fin-1]
print(k)

if (fit_mode == 1):
	print(c)
	fit_parameters = fit_power(k, c, k_fit, k_fin)
	factor = fit_parameters[0]
	exponent_star = fit_parameters[1]
	plt.plot(k_list, factor*(k_list**exponent_star), label='exponent={:.2f}'.format(exponent_star), color='red')

#plt.scatter(k_list, c_at_T, label='T={}'.format(T), color='blue')
plt.scatter(k, c, label='T={}'.format(T), color='blue')
#plt.scatter(k[k_fit-1:k_fin-1], c[k_fit-1:k_fin-1], label='T={} steps'.format(T))
plt.title("N={}".format(N), fontsize=17)
plt.xlabel('k', fontsize=16)
plt.ylabel('c_k', fontsize=16)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xscale('log')
plt.yscale('log')
plt.legend(fontsize=13)
plt.show()

#plt.scatter(np.linspace(0,T,len(sol.y[5,:])), sol.y[5,:]/sum_val)
#plt.show()
