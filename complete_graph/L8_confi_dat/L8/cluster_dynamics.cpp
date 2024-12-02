#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <random>
#include <map>
#include <unordered_map>

using std::cout;
using std::vector;

void init_matrix(vector<vector<int>> &mat, int val, int N) {
	for (int i=0; i<N; i++) {
		vector<int> list;
		for (int j=0; j<N; j++) list.push_back(val);
		mat.push_back(list);
	}
}

void subset_to_mat(vector<vector<int>> &subsets_i, vector<vector<int>> &mat, int N) {
	init_matrix(mat, -1, N);
	
	for (int i=0; i<subsets_i.size(); i++) {
		for (int j=0; j<subsets_i[i].size(); j++) {
			int v = subsets_i[i][j];
			mat[v][v] = 1;
			for (int k=0; k<subsets_i[i].size(); k++) {
				int nei = subsets_i[i][k];
				mat[v][nei] = mat[nei][v] = 1;
			}
		}
	}
}

void mat_to_subset(vector<vector<int>> &mat, vector<vector<int>> &subsets, int N) {
	vector<int> cluster;
	cluster.push_back(0);
	for (int k=1; k<N; k++) {
		if (mat[0][k] == 1) cluster.push_back(k);
	}
	subsets.push_back(cluster);
	int g_num = 1;
	for (int i=1; i<N; i++) {
		int check = 0;
		for (int g=0; g<g_num; g++) {
			if (find(subsets[g].begin(), subsets[g].end(), i) == subsets[g].end()) check += 1;
		}
		if (check == g_num) {
			cluster.clear();
			cluster.push_back(i);
			for (int j=i+1; j<N; j++) {
				if (mat[i][j] == 1) cluster.push_back(j);
			}
			subsets.push_back(cluster);
			g_num += 1;
		}
	}
}

void print_subsets(vector<vector<int>> &subsets) {
	for (int i=0; i<subsets.size(); i++){
		for (int j=0; j<subsets[i].size(); j++) cout << subsets[i][j] << " ";
		cout << "\n";
	}
	cout << "\n";
}

void print_mat(vector<vector<int>> &mat, int N) {
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) cout << mat[i][j] << " ";
		cout << "\n";
	}
	cout << "\n";
}

void import_P_R(vector<vector<double>> &R, vector<vector<double>> &P) {
    std::string file_path_R = "L8-prob-R.dat"; 
    std::string file_path_P = "L8-prob-P.dat";

    std::ifstream file_R(file_path_R);
    std::ifstream file_P(file_path_P);

    if (!file_R.is_open() || !file_P.is_open()) {
        std::cerr << "Failed to open file: " << std::endl;
        return 1;
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

void cluster_size_distribution(vector<int> &g_info, vector<vector<double>> &c_dist, int N) {
	std::unordered_map<int, int> freq;
	for (int num : nums) freq[num]++;
	
	std::unordered_map<int, int> freq_of_freq;
	for (const auto& pair : freq) freq_of_freq[pair.second]++;

	for (const auto& pair : freq_of_freq) {
		int k = static_cast<int>(pair.first);
		double c_k = static_cast<double>(pair.second);
		c_dist[(int)pair.first] = c_k;
	}
}

double P_star(int m) {
	double prob = 1.0/(double)m;
	return prob;
}

double Q(int n) {
	double prob = 1.0/(double)(n+1);
	return prob;
}

void Fragmentation(vector<vector<int>> &subsetes, vector<int> &g_info, int o) {
  auto it = std::find(subsets[g_info[o]].begin(), subsets[g_info[o]].end(), o);
  if (it != subsets[g_info[o]].end()) {
      subsets[g_info[o]].erase(it);
      break;
  }
	int g_idx_o = (g_info.back() + 1);
	g_info[o] = g_idx_o;
	subsets.push_back({o});
}

void Migration(vector<vector<int>> &subsets, vector<int> &g_info, int o, int d) {
  auto it = std::find(subsets[g_info[o]].begin(), subsets[g_info[o]].end(), o);
  if (it != subsets[g_info[o]].end()) {
      subsets[g_info[o]].erase(it);
      break;
  }
	g_info[o] = g_info[d];
	subsets[g_info[d]].push_back(o);
}

void MC_cluster(vector<vector<int>> &subsets, vector<double> &c_dist, vector<vector<double>> &R, vector<vector<double>> &P, int N, int MCS, int init_option) {
	std::random_device rd;
	std::mt19937 gen(rd());
	uniform_int_distribution<> dist(0,N-1);
	uniform_real_distribution<> dist_u(0,1);
	
	int space = N; int i_start=0;
	int g_idx=0;
	vector<int> g_info;
	while (true) { // initialization of cluster configuration for an ensemble
		switch(init_option) {
			vector<int> subset_i;
			int c_size = dist(gen);
			space -= c_size;
			if (space <= 0) {
				for (int i=i_start; i<N; i++) {
					g_info.push_back(g_idx);
					subset_i.push_back(i);
				}
				subsets.push_back(subset_i);
				break;
			}

			for (int i=i_start; i<c_size; i++) {
				subset_i.push_back(i);
				g_info.push_back(g_idx);
			}
			i_start = i+1;
			subsets.push_back(subset_i);
			g_idx += 1;
		}
	}
	for (int t=0; t<MCS; t++) {
		int o = dist(gen); int d = dist(gen); // pair of an event (assessment error)
		int m_idx = g_info[o]; int n_idx = g_info[d];
		int m = subsets[m_idx].size(); int n = subsets[n_idx].size();
		if (m_idx != n_idx and m != 1) {
			if (dist_u(gen) <= P[m][n]) Fragmentation(subsets, g_info, o);
			else if (dist_u(gen) > P[m][n] && dist_u(gen) <= P[m][n] + R[m][n]) Migration(subsets, g_info, o, d);
		}
		else if (m_idx != n_idx and m==1) {
			if (dist_u(gen) <= Q(n)) Migration(subsets, g_info, o, d);
		}
		else if (m_idx == n_idx) {
			if (dist_u(gen) <= P_star(m)) Fragmentation(subsets, g_info, o);
		}
	}
}

int main(int argc, char *argv[]) {
		if (argc < 3 || argv[1] > 50 || (init_option > 2)) {
			print("./cluster_dynamics N MCS init_option \n")
			print("[init_option] {0, 1, 2} : {paradise, all-fragmented, random} \n")
			print("N must be less than or equal to 50. \n")
			exit(1);
		}
		
		int N = atoi(argv[1]);
		int MCS = atoi(argv[2]);
		int init_option = atoi(argv[3]);
    vector<vector<double>> R;
    vector<vector<double>> P;
		import_P_R(R, P);
    
    vector<vector<int>> subsets; vector<double> c_dist(N+1, 0);
		
		MC_cluster(subsets, c_dist, R, P, N, MCS, init_option);
		
	return 0; 
}
