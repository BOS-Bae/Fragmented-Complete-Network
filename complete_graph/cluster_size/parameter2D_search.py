import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib.ticker import FixedLocator, FixedFormatter
import sys

if (len(sys.argv) < 6):
	print("python3 parameter2D_search.py c2 c1_start c1_fin M_start M_fin xmin")
	exit(1)

c2 = float(sys.argv[1])
c1_start = float(sys.argv[2])
c1_fin = float(sys.argv[3])
M_start = float(sys.argv[4])
M_fin = float(sys.argv[5])
xmin = int(sys.argv[6])

real_exponent = -3.4
N = 500
c1_sl = M_sl = 50

c1_arr = np.linspace(c1_start, c1_fin, c1_sl)
M_arr = np.linspace(M_start, M_fin, M_sl)
print(c1_arr)
print(M_arr)
   # Initial condition c[0]
A = 0.64
B = 0.84

def frac(k):
	return ((k-1)/k)

def Q(k):
	A = 0.64
	B = 0.84
	return A*(k ** (1-B))


def power_law(k, a, b):
	return a * k ** b


def solve_fit_diff_eq(c2, c1_arr, M_arr, N):
	result_mat = np.zeros([len(list(M_arr)), len(list(c1_arr))])
	k_values = np.arange(xmin, N+1)
	
	for M_idx in range(len(list(M_arr))):
		M = M_arr[M_idx]
		for c1_idx in range(len(list(c1_arr))):
			c1 = c1_arr[c1_idx]
			c = np.zeros(N)
			c[0] = c1
			c[1] = c2
	
			for k in range(2, N):
				k_idx = k - 1
				c[k_idx+1] = frac(k)*c[k_idx] - (M**2)*N*(c1/k)*(c[k_idx-1]*Q(k-1) - c[k_idx]*Q(k))
			#for k in range(3, N+1):
			#	k_idx = k - 1
			#	c[k_idx+1] = frac(k)*c[k_idx] - (M**2)*N*(c1/k)*(c[k_idx-1]*Q(k-1) - c[k_idx]*Q(k))
		
			summ = 0
			check = 0
			for k in range(1, N+1):
				k_idx = k-1
				if (c[k_idx] < 0) : check += 1
				summ += k*c[k_idx]
			c /= summ; c[0] = c1; c[1] = c2

			c_values = c[xmin-1:N]
			popt, _ = curve_fit(power_law, k_values, c_values)
			
			if (check == 0) :	result_mat[M_idx, c1_idx] = popt[1]
			if (check != 0) :	result_mat[M_idx, c1_idx] = 100
		
	
	return result_mat

def plot_fig(c1_arr, M_arr, Mat):
	fig, ax = plt.subplots()
	Mat_raw = Mat
	Mat = abs(Mat - real_exponent)
	for i in range(len(M_arr)):
		for j in range(len(c1_arr)):
			if (Mat_raw[i,j] == 100): Mat_raw[i,j] = 0
	cax = ax.imshow(Mat_raw, cmap='terrain', origin='upper')  # Use `origin='upper'` to match matrix indexing

	min_idx = np.unravel_index(np.argmin(Mat), Mat.shape)
	
	M_idx, c1_idx = min_idx
	
	c1_val = c1_arr[c1_idx]  # x-values correspond to columns (second index)
	M_val = M_arr[M_idx]  # y-values correspond to rows (first index)
	xticks = np.linspace(0,len(c1_arr)-1, 5)
	yticks = np.linspace(0,len(M_arr)-1, 5)
	ax.set_xticks(xticks)
	ax.set_yticks(yticks)
	plt.colorbar(cax)

	x_show = [];	y_show = []
	for x in xticks:
		x_show.append(np.round(c1_arr[int(x)],2))
	for y in yticks:
		y_show.append(np.round(M_arr[int(y)],2))
	
	ax.set_xticklabels(x_show, fontsize=12)
	ax.set_yticklabels(y_show, fontsize=12)
	plt.xlabel('c1', fontsize=15)
	plt.ylabel('M', fontsize=15)
	plt.title("c2={} / c1={:.2f}, M={:.2f}, best alpha={:.2f}".format(c2, c1_val, M_val, Mat_raw[M_idx, c1_idx]))
	plt.show()

Mat = solve_fit_diff_eq(c2, c1_arr, M_arr, N)
plot_fig(c1_arr, M_arr, Mat)
