import matplotlib.pyplot as plt
import numpy as np
import sys

if (len(sys.argv) < 3):
    print("python3 plot.py 'm or n' 'p, q, or r' rule_num")
    exit(1)

M_max = 7
m_or_n = sys.argv[1]
prob_name = sys.argv[2]
r = int(sys.argv[3])
cluster_size_list = range(2, M_max + 1)

dat = np.loadtxt("./dat/{}_L{}".format(prob_name, r))

color_list = ["black", "purple", "blue", "lightseagreen", "green","orange", "gold", "red"]

color_idx = 0
for cluster_size in cluster_size_list:
	arg_name = 'm, n'
	x_name = 'm or n'
	if (m_or_n == 'm'):
	    arg_name = "{}, n".format(cluster_size)
	    x_name = 'n'
	elif (m_or_n == 'n'):
	    arg_name = "m, {}".format(cluster_size)
	    x_name = 'm'

	x = []
	p = []
	err = []
	if (m_or_n == 'm') :
		for i in range(len(dat)):
			if (dat[i, 0] == cluster_size):
				x.append(dat[i, 1])
				p.append(dat[i, 2])
				err.append(dat[i, 3])
					
	elif (m_or_n == 'n'):
		for i in range(len(dat)):
			if (dat[i, 1] == cluster_size):
				x.append(dat[i, 0])
				p.append(dat[i, 2])
				err.append(dat[i, 3])
	#each data format : m n p err
	sorted_idx = np.argsort(np.array(x))
	x = np.array(x)[sorted_idx]
	p = np.array(p)[sorted_idx]
	
	plt.plot(x,p,label="{}={}".format(m_or_n, cluster_size).format(r),color=color_list[color_idx],marker='.')
	plt.errorbar(x,p,yerr=err,color=color_list[color_idx])
	color_idx += 1

plt.xlabel("{}".format(x_name),fontsize=17)
plt.ylabel("{}(m,n)".format(prob_name),fontsize=17)
plt.title("L{}".format(r),fontsize=17)

plt.xticks(range(1,M_max+1), fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=13)
plt.yscale('log')
#plt.savefig("{},{}_fixed,L{}.png".format(prob_name,m_or_n,r))
plt.show()
