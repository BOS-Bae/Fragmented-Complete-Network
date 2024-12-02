#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <random>
#include <map>
#include <unordered_map>

using std::cout;
using std::vector;

void import_P_R(vector<vector<double>> &R, vector<vector<double>> &P) {
    std::string file_path_R = "./L8-prob-R.dat"; 
    std::string file_path_P = "./L8-prob-P.dat";

    std::ifstream file_R(file_path_R);
    std::ifstream file_P(file_path_P);

    if (!file_R.is_open() || !file_P.is_open()) {
        std::cerr << "Failed to open file: " << std::endl;
    }

    std::string line;
    while (std::getline(file_R, line)) {
        std::istringstream ss(line);
        vector<double> row;
        double value;

        while (ss >> value) {
            row.push_back(value);
        }
        R.push_back(row);
    }
    file_R.close();

    std::string line2;
    while (std::getline(file_P, line2)) {
        std::istringstream ss(line2);
        vector<double> row2;
        double value2;

        while (ss >> value2) {
            row2.push_back(value2);
        }
        P.push_back(row2);
    }
    file_P.close();
}

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

void MC_cluster(vector<double> &c_dist, vector<vector<double>> &R, vector<vector<double>> &P, int N, int MCS, int init_option) {
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
				if (dist_u(gen) <= P[m][n]) Fragmentation(g_info, o);
				else if (dist_u(gen) > P[m][n] && dist_u(gen) <= P[m][n] + R[m][n]) Migration(g_info, o, d);
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
		if (argc < 3 || atoi(argv[1]) > 50 || atoi(argv[3]) > 2) {
			printf("./cluster_dynamics N MCS init_option \n");
			printf("[init_option] {0, 1, 2} : {paradise, all-fragmented, random} \n");
			printf("N must be less than or equal to 50. \n");
			exit(1);
		}
		
		int N = atoi(argv[1]);
		int MCS = atoi(argv[2]);
		int init_option = atoi(argv[3]);
    vector<vector<double>> R;
    vector<vector<double>> P;
		import_P_R(R, P);
    
    vector<double> c_dist(N+1, 0);
		
		MC_cluster(c_dist, R, P, N, MCS, init_option);
		for (int k=0; k<N+1; k++) cout << c_dist[k] << " ";
		cout << "\n";
	return 0; 
}
