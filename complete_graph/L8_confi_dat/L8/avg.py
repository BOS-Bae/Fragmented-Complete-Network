import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.optimize import minimize
from scipy.special import zeta
import numpy as np
import sys

if (len(sys.argv) < 4):
	print("python3 avg.py N MCS condi sl")
	exit(1)

N = int(sys.argv[1])
MCS = int(sys.argv[2])
condi = int(sys.argv[3])
sl = int(sys.argv[4])
x_arr = range(N+1)
x_min = x_arr[sl]

label_info = ["paradise", "fully fragmented", "randomly distributed"]

dat = np.loadtxt("./dat_cluster_L8/N{}-{}MCS-condi{}.dat".format(N, MCS, condi))
ns = len(dat)

c_dist = np.average(dat, 0)
c_stderr = np.std(dat, 0) / np.sqrt(ns)
cumul_dist = np.zeros(len(c_dist))
print(len(c_dist))
count1 = 0
count2 = 0
ln_x_sum1 = 0
ln_x_sum2 = 0

for i in range(len(c_dist)):
    cumul_dist[i] = sum(list(c_dist[i:]))
    if (c_dist[i] != 0):
        idx = x_arr[i]
        count1 += 1
        ln_x_sum1 += np.log(x_arr[i])

for i in range(len(cumul_dist)):
    if (cumul_dist[i] != 0):
        count2 += 1
        ln_x_sum2 += np.log(x_arr[i])

print(x_min)
def loss_fn_1(a):
    return -(-count1*np.log(zeta(a,x_min)) - a*ln_x_sum1)

def loss_fn_2(a):
    return -(-count2*np.log(zeta(a,x_min)) - a*ln_x_sum2)

init_condition = 1.05
res1 = minimize(loss_fn_1, x0 = [init_condition])
res2 = minimize(loss_fn_2, x0 = [init_condition])

a1 = res1.x; alpha1 = a1[0]
#a2 = res2.x; alpha2 = a2[0]
alpha2 = alpha1 - 1
print("a1 = ", alpha1)
print("a2 = \n", alpha2)

C1 = np.sum(c_dist[x_min : ])/zeta(alpha1, x_min)
C2 = np.sum(c_dist[x_min : ])*np.power((1/x_min), -alpha2)
plt.figure(figsize=(10,3.5))
plt.plot(x_arr[1:], c_dist[1:]/N, label="cluster dynamics ({})".format(label_info[condi]), marker = 'o', color='blue')
plt.errorbar(x_arr[1:], c_dist[1:]/N, yerr= c_stderr[1:]/N, fmt = 'o', color='blue')
plt.plot(x_arr[1:], C1*np.power(x_arr[1:], -alpha1)/N, label="exponent : {:.2f}".format(-alpha1), color='black', linestyle = 'dashed')
plt.legend(fontsize=17)
plt.xscale('log')
plt.yscale('log')
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.xlim(0.9, idx+1)
plt.xlabel('k', fontsize=20)
plt.show()

plt.plot(x_arr[1:], cumul_dist[1:]/N, label="cluster dynamics ({})".format(label_info[condi]), marker = 'o', color='blue')
plt.errorbar(x_arr[1:], cumul_dist[1:]/N, yerr= c_stderr[1:]/N, color='blue')
plt.plot(x_arr[1:], C2*np.power(x_arr[1:], -alpha2)/N, label="exponent : {:.2f}".format(-alpha2), color='black', linestyle ='dashed')
plt.legend(fontsize=17)
plt.xscale('log')
plt.yscale('log')

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlim(0.9, idx+1)

plt.xlabel('k', fontsize=20)
plt.show()
