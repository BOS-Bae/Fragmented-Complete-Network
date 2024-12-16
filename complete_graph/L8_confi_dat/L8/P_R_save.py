import numpy as np

N = 100
R_mat = np.zeros([N+1,N+1])
P_mat = np.zeros([N+1,N+1])

original_path = "./L8-N100-p-r-result.txt"
n1_path = "./L8-N100-n1-p-r-result.txt"

def convert_complex(s):
    return complex(s.decode('utf-8').replace(" I", "j").replace(" ", ""))

save_path = "./L8-N{}-p-r-result-revised.txt".format(N)

with open(original_path, 'r') as f:
		original_data = f.readlines()

with open(n1_path, 'r') as f:
		n1_data = f.readlines()

data = []; data_n1 = []
for line in original_data:
    parts = line.strip().split(',')
    row = [
        int(parts[0]),
        int(parts[1]),
        convert_complex(parts[2].encode('utf-8'))
    ]
    data.append(row)

for line in n1_data:
    parts = line.strip().split(',')
    row = [
        int(parts[0]),
        int(parts[1]),
        convert_complex(parts[2].encode('utf-8'))
    ]
    data_n1.append(row)

for dat in data:
    m = dat[0]
    n = dat[1]
    R = dat[2].imag
    P = 1.0000000000000000 -(dat[2].real + R)
    R_mat[int(m),int(n)] = R
    P_mat[int(m),int(n)] = P

for dat_new in data_n1:
	m = dat_new[0]
	n = dat_new[1]
	R = dat_new[2].imag
	P = 1.0000000000000000 -(dat_new[2].real + R)
	R_mat[int(m),int(n)] = R
	P_mat[int(m),int(n)] = P
print(data_n1)	
np.savetxt("./L8-prob-R.dat",R_mat)
np.savetxt("./L8-prob-P.dat",P_mat)
