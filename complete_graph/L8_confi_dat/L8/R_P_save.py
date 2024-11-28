import numpy as np

N = 100
R_mat = np.zeros([N+1,N+1])
P_mat = np.zeros([N+1,N+1])

def convert_complex(s):
    return complex(s.replace(" I", "j").replace(" ", ""))  # ' I' -> 'j', empty space removing

file_path = "./L8-p-r-results.txt" # I have to check this path!!

data = np.loadtxt(file_path, delimiter=",", converters={2: convert_complex})
print(data)

for dat in data:
    m = dat[0]
    n = dat[1]
    R = dat[2].imag
    P = 1-(dat[2].real + R)
    R_mat[m,n] = R
    P_mat[m,n] = P

np.savetxt("./L8-prob-R.dat",R_mat)
np.savetxt("./L8-prob-P.dat",P_mat)
