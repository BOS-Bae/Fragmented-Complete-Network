import pandas as pd
import numpy as np

input_file = "41598_2021_84147_MOESM3_ESM.xlsx"
data = pd.read_excel(input_file, header=None)

expected_columns = ["Country", "DateElection", "DateFailure", "DateGovernment", "Parties", "Seats", "Government", "PoliticalPosition"]
data.columns = expected_columns[:data.shape[1]]

clusters = data[["Parties", "Seats"]]

grouped_data = clusters.groupby("Parties").sum().reset_index()

result = grouped_data.to_numpy()
np.savetxt("./REF_dist.dat", result, delimiter="\t", fmt="%s")
print(result)

