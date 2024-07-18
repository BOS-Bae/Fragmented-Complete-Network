import numpy as np
import matplotlib.pyplot as plt
import sys

if (len(sys.argv) < 2):
    print("python3 extract_data.py m_max rule_num ")
    exit(1)

m_max = int(sys.argv[1])
r = int(sys.argv[2])

for m_cluster in range(1, m_max+1):
    for m_or_n in ['m', 'n']:
        for prob_name in ['p', 'q', 'r']:
            sorting = []
            data = []
            dat_tot = np.loadtxt("./prob_dat/dat/{}_L{}".format(prob_name,r))
            for i in range(len(dat_tot)):
                if (m_or_n == 'm'):
                    if (int(dat_tot[i][0]) == int(m_cluster)):
                        data.append(dat_tot[i])
                        sorting.append(dat_tot[i][1])
                elif (m_or_n == 'n'):
                    if (int(dat_tot[i][1]) == int(m_cluster)):
                        data.append(dat_tot[i])
                        sorting.append(dat_tot[i][0])
            
            sorted_idx = np.argsort(np.array(sorting))
            dat = np.array(data)
            #print(dat)
            #print("")
            #print(m_cluster)
            if (dat.size != 0):
                #print(dat[sorted_idx,:])
                np.savetxt('./prob_dat/dat/{}/{}_{}{}_L{}'.format(prob_name,prob_name,m_or_n,m_cluster,r), dat[sorted_idx, :], fmt="%.6f")
