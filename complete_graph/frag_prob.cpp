#include <random>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;
using std::cout;
using std::find;
using std::uniform_int_distribution;
using std::uniform_real_distribution;
using std::random_device;
using std::mt19937;
using std::vector;

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

void union_cluster(vector<vector<int>> &subset_i, vector<vector<int>> &subset_j, int g_plus) {
	vector<int> new_cluster;
	for (int i=0; i<subset_i[0].size(); i++) new_cluster.push_back(subset_i[0][i]);
	for (int i=0; i<subset_i[g_plus].size(); i++) new_cluster.push_back(subset_i[g_plus][i]);
	subset_j.push_back(new_cluster);

	for (int g=1; g<subset_i.size(); g++) {
		if (g != g_plus) subset_j.push_back(subset_i[g]);
	}
}
 
void case_err_gen(vector<vector<vector<int>>> &subset_list, vector<vector<int>> &error_i, vector<double> &result_arr, int M) {
	vector<vector<int>> subset_i;
	int node_idx = 0;

	for (int i=0; i<M; i++) {
		int m = M-i;
		vector<int> cluster_m;
		for (int j=0; j<m; j++) {
			cluster_m.push_back(node_idx);
			node_idx += 1;
		}
		subset_i.push_back(cluster_m);
	}
	subset_list.push_back(subset_i);
	// confi 0 : initial configuration (absorbing state)
	result_arr.push_back(0);
	
	vector<int> o_d_pair = {0, 1};
	error_i.push_back(o_d_pair);
	for (int g=1; g<subset_i.size(); g++) {
		vector<int> o_d_pair;
		o_d_pair.push_back(0);
		o_d_pair.push_back(subset_i[g][0]);
		error_i.push_back(o_d_pair);

		o_d_pair.clear();
		o_d_pair.push_back(subset_i[g][0]);
		o_d_pair.push_back(0);
		error_i.push_back(o_d_pair);
	}
	vector<vector<int>> subset_j;
	vector<int> node_0 = {0};
	subset_j.push_back(node_0);
	vector<int> node_g0;
	for (int n=1; n<subset_i[0].size(); n++) node_g0.push_back(subset_i[0][n]);
	subset_j.push_back(node_g0);
	for (int g=1; g<subset_i.size(); g++) {
		subset_j.push_back(subset_i[g]);
  }
	subset_list.push_back(subset_j); // confi 1 : 0 is separted from g1.
	result_arr.push_back(0);
	
	for (int g=1; g<subset_i.size()-1; g++) {
		vector<vector<int>> subset_j;
		subset_j.push_back(subset_i[0]);
		
		if (g == 1) {
			vector<int> subset_g1 = {subset_i[g][0]};
			subset_j.push_back(subset_g1);

			vector<int> subset_g2;
			for (int n=1; n < subset_i[g].size(); n++) subset_g2.push_back(subset_i[g][n]);
			subset_j.push_back(subset_g2);
			for (int g=2; g < subset_i.size(); g++) subset_j.push_back(subset_i[g]);
		}
		else if (g > 1 && g < subset_i.size() - 1) {
			for (int g_l=1; g_l < g; g_l++) subset_j.push_back(subset_i[g_l]);
			vector<int> subset_g1 = {subset_i[g][0]};
			subset_j.push_back(subset_g1);
			vector<int> subset_g2;
			for (int n=1; n < subset_i[g].size(); n++) subset_g2.push_back(subset_i[g][n]);
			subset_j.push_back(subset_g2);
			for (int g_u = g+1; g_u < subset_i.size(); g_u++) subset_j.push_back(subset_i[g_u]);
		}
		else {
			for (int g_l=1; g_l < g; g_l++) subset_j.push_back(subset_i[g_l]);
			vector<int> subset_g1 = {subset_i[g][0]};
			vector<int> subset_g2;
			for (int n=1; n < subset_i[g].size(); n++) subset_g2.push_back(subset_i[g][n]);
			subset_j.push_back(subset_g2);
		}
		subset_list.push_back(subset_j);
		result_arr.push_back(0);
	} // seperated

	for (int g=1; g<subset_i.size(); g++) {
		vector<vector<int>> subset_j;
		union_cluster(subset_i, subset_j, g);
		subset_list.push_back(subset_j);
		result_arr.push_back(0);
	} // merged
	
	for (int g=1; g<subset_i.size(); g++) {
		vector<vector<int>> subset_j;
		vector<int> cluster_j = {0};
		for (int n=0; n<subset_i[g].size(); n++) cluster_j.push_back(subset_i[g][n]);
		subset_j.push_back(cluster_j);
		
		cluster_j.clear();
		for (int i=1; i<M; i++) cluster_j.push_back(subset_i[0][i]);
		subset_j.push_back(cluster_j);

		for (int g_others=1; g_others < subset_i.size(); g_others++) {
			if (g_others != g) subset_j.push_back(subset_i[g_others]);
		}
		subset_list.push_back(subset_j);
		result_arr.push_back(0);
	} // migration of 0 toward another cluster

	for (int g=1; g<subset_i.size() - 1; g++) {
		vector<vector<int>> subset_j;
		vector<int> cluster_j;
		for (int i=0; i<M; i++) cluster_j.push_back(subset_i[0][i]);
		cluster_j.push_back(subset_i[g][0]);
		subset_j.push_back(cluster_j);

		for (int g_others=1; g_others < subset_i.size(); g_others++) {
			if (g_others != g) subset_j.push_back(subset_i[g_others]);
			else {
				vector<int> cluster_k;
				for (int n=1; n<subset_i[g_others].size(); n++) cluster_k.push_back(subset_i[g_others][n]);
				subset_j.push_back(cluster_k);
			} 
		}
		subset_list.push_back(subset_j);
		result_arr.push_back(0);
	} // migration of one node from another cluster toward first cluster.
	
	for (int g=1; g<subset_i.size(); g++) {
		vector<vector<int>> subset_j;
		vector<int> cluster_j; cluster_j.push_back(0);
		subset_j.push_back(cluster_j); cluster_j.clear();
		for (int i=1; i<M; i++) cluster_j.push_back(subset_i[0][i]);
		for (int i=0; i<subset_i[g].size(); i++) cluster_j.push_back(subset_i[g][i]);
		subset_j.push_back(cluster_j);
		cluster_j.clear();
		for (int g_l=1; g_l<subset_i.size(); g_l++) {
			if (g_l != g)	subset_j.push_back(subset_i[g_l]);
		} // migration of M-1 nodes from first cluster toward another existing cluster.
		subset_list.push_back(subset_j);
		result_arr.push_back(0);
	}

}

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

int L8_rule(vector<vector<int>> &mat_f, int o, int d, int r, int idx_err) {
	int val = mat_f[o][d];
	if (mat_f[d][r] == 1) val = mat_f[o][r];
	else if (mat_f[d][r] == -1)	{
		if (mat_f[o][d] == 1) val = -mat_f[o][r];
		else val = -1;
	}	
  int val_update = idx_err == 0 ? val : -val;
	return val_update;
}

int L7_rule(vector<vector<int>> &mat_f, int o, int d, int r, int idx_err) {
	int val = mat_f[o][d];
	if (mat_f[d][r] == 1) {
		if (mat_f[o][d] == 1) val = 1;
		else val = mat_f[o][r];
	}
	else if (mat_f[d][r] == -1)	{
		if (mat_f[o][d] == 1) val = -mat_f[o][r];
		else val = -1;
	}
  int val_update = idx_err == 0 ? val : -val;
	return val_update;
}

int L4_rule(vector<vector<int>> &mat_f, int o, int d, int r, int idx_err) {
  // mat_f should be empty matrix whose size is N by N.
  int val = mat_f[o][d];
  if (mat_f[d][r] == 1) {
    if (mat_f[o][d] == -1)
      val = mat_f[o][r];
  } else
    val = -mat_f[o][r];

  int val_update = idx_err == 0 ? val : -val;
	return val_update;
}

int L6_rule(vector<vector<int>> &mat_f, int o, int d, int r, int idx_err) {
  // mat_f should be empty matrix whose size is N by N.
  int val_update = (idx_err == 0 ? mat_f[o][r] * mat_f[d][r] : -mat_f[o][r] * mat_f[d][r]);
	return val_update;
}

bool check_absorbing(int rule_num, vector<vector<int>> &mat_i, int N){
	bool bool_val = false;
	int check = 0;
	int count = 0;
	vector<vector<int>> mat_f(N, vector<int>(N,0));
  std::copy(mat_i.begin(), mat_i.end(), mat_f.begin());
	for (int o=0; o<N; o++){
		for (int d=0; d<N; d++){
			for (int r=0; r<N; r++){
				int tmp = mat_f[o][d];
        switch (rule_num) {
          case 4 :
            mat_f[o][d] = L4_rule(mat_f, o, d, r, 0);
            break;
          case 6 :
            mat_f[o][d] = L6_rule(mat_f, o, d, r, 0);
            break;
					case 7 :
						mat_f[o][d] = L7_rule(mat_f, o, d, r, 0);
						break;
					case 8 :
						mat_f[o][d] = L8_rule(mat_f, o, d, r, 0);
						break;
        }
				count += 1;
				if (mat_f[o][d] == mat_i[o][d]) check += 1;
				mat_f[o][d] = tmp;
			}
		}
	}
	if (count == check) bool_val = true;
	return bool_val;
}

void ABM_complete(int rule_num, vector<vector<int>> &mat_i, int N){
	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<> dist(0, N-1);
	int t = 0;
	while (true){
		t += 1;	
		int val_check = 0;
		int d = dist(gen);
		int r = dist(gen);
		
		vector<int> update_od = {};
		for (int o=0; o<N; o++) {
        switch (rule_num) {
          case 4 :
            update_od.push_back(L4_rule(mat_i, o, d, r, 0));
						//cout << L4_rule(mat_i, o, d, r, 0) << "\n"; 
            break;
          case 6 :
            update_od.push_back(L6_rule(mat_i, o, d, r, 0));
            break;
					case 7 :
            update_od.push_back(L7_rule(mat_i, o, d, r, 0));
						break;
					case 8 :
            update_od.push_back(L8_rule(mat_i, o, d, r, 0));
						break;
				}
		}
		for (int o=0; o<N; o++) mat_i[o][d] = update_od[o];
		//print_mat(mat_i);

		if (check_absorbing(rule_num, mat_i, N))	{
				//print_mat(mat_i);
				//cout << "\n";
				break;
		}	
	}
}

int main(int argc, char *argv[]) {
	if (argc < 4) {
		cout << "./frag_prob M rule_num init_idx n_sample \n";
		exit(1);
	}

	int M = atoi(argv[1]);
	int N = M*(M+1)/2;
	int rule_num = atoi(argv[2]);
	int init_idx = atoi(argv[3]);
	int n_sample = atoi(argv[4]);
	
	vector<vector<vector<int>>> subset_list;
	vector<vector<int>> error_i;
	vector<double> result_arr;
	case_err_gen(subset_list, error_i, result_arr, M);

	int fr = error_i[init_idx][0];
	int to = error_i[init_idx][1];
	
	for (int n_s=0; n_s<n_sample; n_s++){
		vector<vector<int>> mat_i;
		subset_to_mat(subset_list[0], mat_i, N);
		mat_i[fr][to] *= -1;
		
		ABM_complete(rule_num, mat_i, N);
		vector<vector<int>> subsets_f;
		mat_to_subset(mat_i, subsets_f, N);

		int check = 0;
		for (int i=0; i<subset_list.size(); i++) {
			if (subsets_f == subset_list[i]) result_arr[i] += 1;
			else check += 1;
		}
		if (check == subset_list.size()) print_mat(mat_i, N);
	}
	double summ = 0;
	for (int i=0; i<subset_list.size(); i++) {
		double elem = result_arr[i] / (double)n_sample;
		cout << elem  << " "; 
		summ += elem;
	}
	cout << summ << "\n";
	return 0;
}
