#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <random>
#include <cmath>
#include <map>
#include <unordered_map>

using std::cout;
using std::vector;
using std::exp;
using std::pow;
using std::tanh;

void cluster_size_distribution(vector<int> &g_info, vector<double> &c_dist, int N) {
	std::unordered_map<int, int> freq;
	for (int num : g_info) freq[num]++;
	
	std::unordered_map<int, int> freq_of_freq;
	for (const auto& pair : freq) freq_of_freq[pair.second]++;

	for (const auto& pair : freq_of_freq) {
		int k = static_cast<int>(pair.first);
		double c_k = static_cast<double>(pair.second);
		c_dist[(int)pair.first] = c_k;
	}
}

double R(int m, int n) {
	double prob = (2.5*exp(-((double)(m-1)/pow((double)(m+n), 0.4))) - 1.5*exp(-1.5*(double)(m-1)/pow((double)(m+n), 0.4)))/(double)(m+n);
	return prob;
}

double P(int m, int n) {
	double prob = 1.0/((double)m + 2.4*pow((double)(m+n),1.0/3.0)*(1-tanh(0.31*(double)m*pow((double)(m+n), -1.0/3.0))));
	return prob;
}

double P_star(int m) {
	double prob = 1.0/(double)(m);
	return prob;
}

double Q(int n) {
	double prob = 1.0/(double)(n+1);
	return prob;
}

void Fragmentation(vector<int> &g_info, int o) {
  int max_idx = *std::max_element(g_info.begin(), g_info.end());
	g_info[o] = max_idx + 1;
}

void Migration(vector<int> &g_info, int o, int d) {
	g_info[o] = g_info[d];
}

void MC_cluster(vector<double> &c_dist, int N, int MCS, int init_option) {
	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_int_distribution<> dist(0,N-1);
	std::uniform_real_distribution<> dist_u(0,1);
	
	int space = N; int i_start=0;
	int g_idx=0;
	vector<int> g_info;
		switch(init_option) {
			case 0:
				for (int i=0; i<N; i++) {
					g_info.push_back(g_idx);
				}
				break;
			case 1:
				for (int i=0; i<N; i++) {
					g_info.push_back(i);
				}
				break;
			case 2:
				while (true) {
					int c_size = dist(gen);
					space -= c_size;
					if (space <= 0) {
						for (int i=i_start; i<N; i++) {
							g_info.push_back(g_idx);
						}
						break;
					}
					int i_check;
					for (int i=i_start; i<i_start + c_size; i++) {
						g_info.push_back(g_idx);
						i_check = i;
					}
					i_start = i_check+1;
					g_idx += 1;
			 }
			 break;
	}
	for (int t=0; t<MCS; t++) {
		int o = dist(gen); int d = dist(gen); // pair of an event (assessment error)
		int m; int n; m = n = 0;
		if (o!=d){
			for (int i=0; i<N; i++) {
				if (g_info[i] == g_info[o]) m += 1;
				else if (g_info[i] == g_info[d]) n += 1;
			}
	
			int m_idx = g_info[o]; int n_idx = g_info[d];
			//for (int i=0; i<N; i++) cout << g_info[i] << " ";

			if (m_idx != n_idx and m != 1) {
				if (dist_u(gen) <= P(m,n)) Fragmentation(g_info, o);
				else if (dist_u(gen) > P(m,n) && dist_u(gen) <= P(m,n) + R(m,n)) Migration(g_info, o, d);
				//cout << m << ", "  << n << " : " << P(m,n) << ", " << R(m,n) << ", " << P_star(m) << ", " << Q(n) << "\n";
			}
			else if (m_idx != n_idx and m==1) {
				if (dist_u(gen) <= Q(n)) Migration(g_info, o, d);
			}
			else if (m_idx == n_idx and m!=1) {
				if (dist_u(gen) <= P_star(m)) Fragmentation(g_info, o);
			}
		}
	}
	cluster_size_distribution(g_info, c_dist, N);
}

int main(int argc, char *argv[]) {
		if (argc < 3 || atoi(argv[3]) > 2) {
			printf("./Asym_cluster_dynamics N MCS init_option \n");
			printf("[init_option] {0, 1, 2} : {paradise, all-fragmented, random} \n");
			exit(1);
		}
		
		int N = atoi(argv[1]);
		int MCS = atoi(argv[2]);
		int init_option = atoi(argv[3]);
    
    vector<double> c_dist(N+1, 0);
		
		MC_cluster(c_dist, N, MCS, init_option);
		for (int k=0; k<N+1; k++) cout << c_dist[k] << " ";
		cout << "\n";
	return 0; 
}
