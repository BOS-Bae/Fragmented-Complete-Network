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

int L8_rule(vector<vector<int>> &mat_f, int o, int d, int r) {
	int val = mat_f[o][d];
	if (mat_f[d][r] == 1) val = mat_f[o][r];
	else if (mat_f[d][r] == -1)	{
		if (mat_f[o][d] == 1) val = -mat_f[o][r];
		else val = -1;
	}	

	return val;
}

bool check_absorbing(vector<vector<int>> &mat_i, int N){
	bool bool_val = false;
	int check = 0;
	int count = 0;
	vector<vector<int>> mat_f(N, vector<int>(N,0));
  std::copy(mat_i.begin(), mat_i.end(), mat_f.begin());
	for (int o=0; o<N; o++){
		for (int d=0; d<N; d++){
			for (int r=0; r<N; r++){
				int tmp = mat_f[o][d];
				mat_f[o][d] = L8_rule(mat_f, o, d, r);
        //switch (rule_num) {
        //  case 4 :
        //    mat_f[o][d] = L4_rule(mat_f, o, d, r);
        //    break;
        //  case 6 :
        //    mat_f[o][d] = L6_rule(mat_f, o, d, r);
        //    break;
				//	case 7 :
				//		mat_f[o][d] = L7_rule(mat_f, o, d, r);
				//		break;
				//	case 8 :
				//		mat_f[o][d] = L8_rule(mat_f, o, d, r);
				//		break;
        //}
				count += 1;
				if (mat_f[o][d] == mat_i[o][d]) check += 1;
				mat_f[o][d] = tmp;
			}
		}
	}
	if (count == check) bool_val = true;
	return bool_val;
}

void print_mat(vector<vector<int>> Mat, int N){
	for (int i=0; i<N; i++){
		for (int j=0; j<N; j++){
			cout << Mat[i][j] << " ";
		}
		cout << "\n";
	}
	cout << "\n";
}

void seek_cluster(int N, vector<vector<int>> &mat_f, vector<int> &g_info) {
	g_info[0] = 1;
	int group_idx = 2;
	for (int i=0; i<N; i++) {
		if (g_info[i] == 0) {
			g_info[i] = group_idx;
			group_idx += 1;
		}
		for (int j=0; j<N; j++) {
			if (mat_f[i][j] == 1 && g_info[i] != 0) g_info[j] = g_info[i];
		}
	}
}

void gen_init_info(int N, double p, vector<int> &g_info) {
		std::random_device rd;
		std::mt19937 gen(rd());
		std::uniform_int_distribution<> dist(0,N-1);
		std::uniform_real_distribution<> dist_u(0,1);

		vector<vector<int>> mat_i(N, vector<int> (N,0));
		
		for (int i=0; i<N; i++) {
			for (int j=0; j<N; j++) {
				if (dist_u(gen) < p) mat_i[i][j] = 1;
				else mat_i[i][j] = -1;
			}
		}
		int count = 0;
		int check_bool = 0;

		while (true){
			int val_check = 0;
			int d = dist(gen);
			int r = dist(gen);		
			vector<int> update_od = {};

			for (int o=0; o<N; o++) {
					double rand_num = dist_u(gen);
  	      update_od.push_back(L8_rule(mat_i, o, d, r));
  	      //switch (rule_num) {
  	      //  case 4 :
  	      //    update_od.push_back(L4_rule(mat_i, o, d, r));
  	      //    break;
  	      //  case 6 :
  	      //    update_od.push_back(L6_rule(mat_i, o, d, r));
  	      //    break;
  	      //  case 7 :
  	      //    update_od.push_back(L7_rule(mat_i, o, d, r));
  	      //    break;
  	      //  case 8 :
  	      //    update_od.push_back(L8_rule(mat_i, o, d, r));
  	      //    break;
					//}
			}
			for (int o=0; o<N; o++) mat_i[o][d] = update_od[o];
			check_bool = 0;

			if (check_absorbing(mat_i, N)) break;
		}
		//print_mat(mat_i, N);
		seek_cluster(N, mat_i, g_info);
}

//void import_initial_dist(int N, double p, vector<vector<int>> &dist_list) {
//    std::ostringstream filename;
//		filename << "N" << N << "-p" << std::fixed << std::setprecision(1) << p << "-L8.dat";
//		std::string filepath = filename.str();
//		//cout << filepath << "\n";
//
//		std::ifstream file(filepath);
//		if (!file.is_open()) {
//			std::cerr << "Error: Unable to open file: " << filepath << std::endl;
//			return;
//		}
//		dist_list.clear();
//		std::string line;
//		while (std::getline(file, line)) {
//				std::istringstream iss(line);
//				vector<int> row;
//				int value;
//				while (iss >> value) {
//					row.push_back(value);
//				}
//				dist_list.push_back(row);
//		}
//		file.close();
//}

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
			printf("./cABM N p MCS \n");
			printf("N must be less than or equal to 100. \n");
			exit(1);
		}
		
		int N = atoi(argv[1]);
		double p = atof(argv[2]);
		int MCS = atoi(argv[3]);
		//int s_idx = atoi(argv[4]);

    vector<vector<double>> R;
    vector<vector<double>> P;
    vector<int> g_info(N,0);
		import_P_R(R, P);
		gen_init_info(N, p, g_info);
		//cout << dist_list.size() << "\n";
   	//cout << g_init.size() << "\n";
		//for (int k=0; k<N; k++) cout << g_init[k] << " ";
		//cout << "\n";
    vector<double> c_dist(N+1, 0);
		
		MC_cluster(c_dist, R, P, N, MCS, g_info);
		//int max_idx1 = *std::max_element(g_info.begin(), g_info.end());
		//cout << max_idx1 << "\n";

		for (int k=0; k<N+1; k++) cout << c_dist[k] << " ";
		cout << "\n";
	return 0; 
}

