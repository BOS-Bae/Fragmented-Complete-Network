import numpy as np
import sys

N = 7

first_idx = int(sys.argv[1])
answer_arr = list(-np.ones(N, dtype=int))
answer_arr[first_idx] = 1
answer_arr[first_idx + 1] = 1
print(answer_arr)

dat = np.loadtxt("./mat_m_to_p.dat")

n_mat = int(len(dat)/N)

idx_1 = first_idx
idx_2 = first_idx + 1

idx_mat = 0

count = 0
check = 0
for n in range(n_mat):
	image = dat[idx_mat:idx_mat + N]
	#print(image)
	image_t = np.transpose(image)
	print(image)
	print("\n")
	#print(image_t)
	#print("\n")
	if (image.all() == image_t.all()): print(n)
	count += 4
	if (list(image[idx_1]) == answer_arr) : check += 1
	if (list(image[idx_2]) == answer_arr) : check += 1
	if (list(image_t[idx_1]) == answer_arr) : check += 1
	if (list(image_t[idx_2]) == answer_arr) : check += 1
	
	idx_mat += N

print(check)
print(count)

