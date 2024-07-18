import matplotlib.pyplot as plt
import numpy as np
import sys

if (len(sys.argv) < 3):
    print("python3 plot.py m 'm or n' 'p, q, or r' rule_num")
    exit(1)

M_max = 6
cluster_size = int(sys.argv[1])
m_or_n = sys.argv[2]
prob_name = sys.argv[3]
r = int(sys.argv[4])
arg_name = 'm, n'
x_name = 'm or n'
if (m_or_n == 'm'):
    arg_name = "{}, n".format(cluster_size)
    x_name = 'n'
elif (m_or_n == 'n'):
    arg_name = "m, {}".format(cluster_size)
    x_name = 'm'

dat = np.loadtxt("./dat/{}/{}_{}{}_L{}".format(prob_name, prob_name, m_or_n, cluster_size, r))

x = []
if (m_or_n == 'm') :
    x = dat[:, 1]
elif (m_or_n == 'n'):
    x = dat[:, 0]

p = dat[:, 2]
err_list = dat[:, 3]

plt.plot(x,p,label="L{}".format(r),color="blue",marker='.')
plt.errorbar(x,p,yerr=err_list,color="blue")

plt.xlabel("{}".format(x_name),fontsize=17)
plt.ylabel("{}({})".format(prob_name, arg_name),fontsize=17)

plt.xticks(range(2,M_max+1), fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=13)
plt.show()
