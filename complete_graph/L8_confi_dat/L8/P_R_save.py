import numpy as np

N = 50
R_mat = np.zeros([N+1,N+1])
P_mat = np.zeros([N+1,N+1])

def convert_complex(s):
    return complex(s.decode('utf-8').replace(" I", "j").replace(" ", ""))

file_path = "./L8-p-r-result.txt" 
with open(file_path, 'r') as f:
		raw_data = f.readlines()

data = []
for line in raw_data:
    parts = line.strip().split(',')
    row = [
        int(parts[0]),
        int(parts[1]),
        convert_complex(parts[2].encode('utf-8'))
    ]
    data.append(row)

print(data)
#data = np.loadtxt(file_path, delimiter=",", converters={2: convert_complex})

for dat in data:
    m = dat[0]
    n = dat[1]
    R = dat[2].imag
    P = 1-(dat[2].real + R)
    R_mat[int(m),int(n)] = R
    P_mat[int(m),int(n)] = P

np.savetxt("./L8-prob-R.dat",R_mat)
np.savetxt("./L8-prob-P.dat",P_mat)
