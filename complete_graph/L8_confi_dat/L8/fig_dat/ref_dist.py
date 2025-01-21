import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

clusters = data.loc[:, ["Parties", "Seats"]]

clusters.loc[:, "Parties"] = clusters["Parties"].str.replace(r"\s+", "-", regex=True)

grouped_data = clusters.groupby("Parties").sum().reset_index()

result = grouped_data.to_numpy()

np.savetxt("REF_dist.dat", result, delimiter="\t", fmt="%s")

numeric_result = result[:, 1:]

seats = numeric_result.flatten()
c_dist_ref = np.array(seats)
c_dist_dat = []
print(c_dist_ref)
for i in range(len(c_dist_ref)):
	c_dist_dat.append(int(c_dist_ref[i]))

c_dist_hist = size_distribution(c_dist_dat, np.max(c_dist_dat))

cumul_dist = np.zeros(len(c_dist_hist))
for i in range(len(c_dist_hist)):
    cumul_dist[i] = sum(list(c_dist_hist[i:]))
print(cumul_dist)
print(np.max(c_dist_dat))
#plt.plot(range(1,np.max(c_dist_dat)+1), c_dist_hist, marker='o', color="black")
plt.plot(range(1,np.max(c_dist_dat)+1), cumul_dist, marker='o', color="black")
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.xlabel('k', fontsize=20)
plt.xscale('log')
plt.yscale('log')
plt.show()
