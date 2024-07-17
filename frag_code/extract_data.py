import numpy as np
import matplotlib.pyplot as plt
import sys

if ((len(sys.argv) < 4) or (sys.argv[2] != 'm' and sys.argv[2] != 'n') or (sys.argv[3] != 'p' and sys.argv[3] != 'q' and sys.argv[3] != 'r')):
	print("python3 extract_data.py m ('m' or 'n') ('p','q', or 'r') (7 or 8)")
	exit(1)

m_cluster = int(sys.argv[1])
m_or_n = sys.argv[2]
prob_name = sys.argv[3]
r = int(sys.argv[4])

data = []
dat_tot = np.loadtxt("./prob_dat/dat/{}_L{}".format(prob_name,r))

sorting = []
for i in range(len(dat_tot)):
    dat_tot[i][0] = int(dat_tot[i][0])
    dat_tot[i][1] = int(dat_tot[i][1])
    
    if (m_or_n == 'm'):
        if (dat_tot[i][0] == m_cluster):
            data.append(dat_tot[i])
            sorting.append(dat_tot[i][1])
    elif (m_or_n == 'n'):
        if (dat_tot[i][1] == m_cluster):
            data.append(dat_tot[i])
            sorting.append(dat_tot[i][0])

sorted_idx = np.argsort(np.array(sorting))
dat = np.array(data)
print(dat)
print("")
print(dat[sorted_idx,:])
#np.savetxt('./prob_dat/dat/{}/{}_{}{}_L{}'.format(prob_name,prob_name,m_or_n,m_cluster,r), dat, fmt="%.6f")
