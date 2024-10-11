import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib.ticker import FixedLocator, FixedFormatter
import sys

if (len(sys.argv) < 3):
	print("python3 parameter2D_search.py c2_sl M_sl xmin")
	exit(1)

c1 = 1
c2_sl = int(sys.argv[1])
M_sl = int(sys.argv[2])
xmin = int(sys.argv[3])

N = 500
c2_start = 0.01
c2_fin = 0.9
M_start = 0.1
M_fin = 3.0

c2_arr = np.linspace(c2_start, c2_fin, c2_sl)
M_arr = np.linspace(M_start, M_fin, M_sl)
print(c2_arr)
print(M_arr)
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


def solve_fit_diff_eq(c1, c2_arr, M_arr, N):
	result_mat = np.zeros([len(list(c2_arr)), len(list(M_arr))])
	k_values = np.arange(xmin, N+1)
	
	for M_idx in range(len(list(M_arr))):
		M = M_arr[M_idx]
		for c2_idx in range(len(list(c2_arr))):
			c2 = c2_arr[c2_idx]
			c = np.zeros(N)
			c[0] = c1
			c[1] = c2
	
			for k in range(3, N+1):
				k_idx = k - 1
				c[k_idx] = frac(k-1)*c[k_idx-1] - (M*c1/(k-1))*(c[k_idx-2]*Q(k-2) - c[k_idx-1]*Q(k-1))
		
			c_values = c[xmin-1:N]
			popt, _ = curve_fit(power_law, k_values, c_values)
	
			result_mat[M_idx, c2_idx] = popt[1]
	
	return result_mat

def plot_fig(c2_arr, M_arr, Mat):
	fig, ax = plt.subplots()
	cax = ax.imshow(Mat, cmap='viridis', origin='upper')  # Use `origin='upper'` to match matrix indexing
	min_idx = np.unravel_index(np.argmin(Mat), Mat.shape)
	
	# Get the x and y indices
	c2_idx, M_idx = min_idx
	
	# Get the x and y values from the original arrays
	c2_val = c2_arr[c2_idx]  # x-values correspond to columns (second index)
	M_val = M_arr[M_idx]  # y-values correspond to rows (first index)
	xticks = np.linspace(0,len(c2_arr)-1, 5)
	yticks = np.linspace(0,len(M_arr)-1, 5)
	ax.set_xticks(xticks)
	ax.set_yticks(yticks)
	plt.colorbar(cax)

	x_show = [];	y_show = []
	for x in xticks:
		x_show.append(np.round(c2_arr[int(x)],2))
	for y in yticks:
		y_show.append(np.round(M_arr[int(y)],2))

	ax.set_xticklabels(x_show, fontsize=12)
	ax.set_yticklabels(y_show, fontsize=12)
	plt.xlabel('c2', fontsize=15)
	plt.ylabel('M', fontsize=15)
	plt.title("c2={:.2f}, M={:.2f}, best alpha={:.2f}".format(c2_val, M_val, np.min(Mat)))
	plt.show()

Mat = solve_fit_diff_eq(c1, c2_arr, M_arr, N)
plot_fig(c2_arr, M_arr, Mat)
