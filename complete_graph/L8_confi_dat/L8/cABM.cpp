#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <random>
#include <map>
#include <unordered_map>
#include <iomanip>

using std::cout;
using std::vector;

void import_initial_dist(int N, double p, vector<vector<int>> &dist_list) {
    std::ostringstream filename;
		filename << "N" << N << "-p" << std::fixed << std::setprecision(1) << p << "-L8.dat";
		std::string filepath = filename.str();

		std::ifstream file(filepath);
		if (!file.is_open()) {
			std::cerr << "Error: Unable to open file: " << filepath << std::endl;
			return;
		}
		dist_list.clear();
		std::string line;
		while (std::getline(file, line)) {
				std::istringstream iss(line);
				vector<int> row;
				int value;
				while (iss >> value) {
					row.push_back(value);
				}
				dist_list.push_back(row);
		}
		file.close();
}

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

void MC_cluster(vector<double> &c_dist, vector<vector<double>> &R, vector<vector<double>> &P, int N, int MCS, vector<int> &g_info) {
	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_int_distribution<> dist(0,N-1);
	std::uniform_real_distribution<> dist_u(0,1);
	
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
		if (argc < 3 || atoi(argv[1]) > 100 || atof(argv[2]) < 0.5 || atof(argv[2]) > 0.9) {
			printf("./cABM N p MCS s_idx \n");
			printf("N must be less than or equal to 100. \n");
			exit(1);
		}
		
		int N = atoi(argv[1]);
		double p = atof(argv[2]);
		int MCS = atoi(argv[3]);
		int s_idx = atoi(argv[4]);

    vector<vector<double>> R;
    vector<vector<double>> P;
    vector<vector<int>> dist_list;
		import_P_R(R, P);
		import_initial_dist(N, p, dist_list);
		//cout << dist_list.size() << "\n";
		vector<int> g_init = dist_list[s_idx];
   	//cout << g_init.size() << "\n";
		//for (int k=0; k<N; k++) cout << g_init[k] << " ";
		//cout << "\n";
    vector<double> c_dist(N+1, 0);
		
		MC_cluster(c_dist, R, P, N, MCS, g_init);
		for (int k=0; k<N+1; k++) cout << c_dist[k] << " ";
		cout << "\n";
	return 0; 
}

