import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

target_country = sys.argv[1]

def size_distribution(c_size, M_max):
    dist_arr = np.zeros(int(M_max))
    idx = 0
    for s_val in range(1,int(M_max + 1)):
        for s in c_size:
            if s_val == s: dist_arr[idx] += 1
        idx += 1
    return dist_arr

input_file = "./41598_2021_84147_MOESM3_ESM.xlsx"
data = pd.read_excel(input_file, header=1)

expected_columns = ["Country", "DateElection", "DateFailure", "DateGovernment", "Parties", "Seats", "Government", "PoliticalPosition"]
data.columns = expected_columns[:data.shape[1]]

filtered_data = data[data["Country"] == target_country]

c_dist_dat = pd.to_numeric(filtered_data["Seats"], errors="coerce").fillna(0).astype(int).tolist()
c_dist_dat = np.array(c_dist_dat)

c_dist_hist = size_distribution(c_dist_dat, np.max(c_dist_dat))

c_dist_hist /= np.sum(c_dist_hist)
cumul_dist = np.zeros(len(c_dist_hist))
for i in range(len(c_dist_hist)):
    cumul_dist[i] = sum(list(c_dist_hist[i:]))
print(cumul_dist)
print(np.max(c_dist_dat))
plt.figure(figsize=(10,3.5))
#plt.plot(range(1,np.max(c_dist_dat)+1), c_dist_hist, marker='o', color="black")
plt.plot(range(1,np.max(c_dist_dat)+1), cumul_dist, marker='o', color="black")
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('k', fontsize=23)
plt.ylabel('C(k)', fontsize=23)
plt.title("{}".format(target_country), fontsize=22)
plt.xscale('log')
plt.yscale('log')
plt.show()
np.savetxt("./ref_dat/{}.dat".format(target_country), cumul_dist)
