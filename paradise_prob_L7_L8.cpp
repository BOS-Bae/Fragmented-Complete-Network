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

int L8_rule(vector<vector<int>> &mat_f, int o, int d, int r, int idx_err) {
	int val = mat_f[o][d];
	if (mat_f[d][r] == 1) val = mat_f[o][r];
	else if (mat_f[d][r] == -1)	{
		if (mat_f[o][d] == 1)
			val = -mat_f[o][r];
		else
			val = -1;
	}	
  int val_update = idx_err == 0 ? val : -val;
	return val_update;
}

int L7_rule(vector<vector<int>> &mat_f, int o, int d, int r, int idx_err) {
	int val = mat_f[o][d];
	if (mat_f[d][r] == 1) {
		if (mat_f[o][d] == 1)
			val = 1;
		else
			val = mat_f[o][r];
	}
	else if (mat_f[d][r] == -1)	{
		if (mat_f[o][d] == 1)
			val = -mat_f[o][r];
		else
			val = -1;
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

bool check_absorbing(int rule_num, vector<vector<int>> &mat_i){
	bool bool_val = false;
	int check = 0;
	int count = 0;
	int N = mat_i.size();
  vector<vector<int>> mat_f = mat_i;
	
	//std::copy(&mat_i[0][0], &mat_i[0][0] + N * N, &mat_f[0][0]);
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

int ABM_complete(int rule_num, vector<vector<int>> &subsets_i, int init_idx){
	int N = 0;
	for (int i=0; i<subsets_i.size(); i++) {
		for (int k=0; k<subsets_i[i].size(); k++) N += 1;
	}
	vector<vector<int>> mat_i;
	subset_to_mat(subsets_i, mat_i, N);
	//cout << N << "\n";
	
	int node_i = subsets_i[0][0]; int node_ii = subsets_i[0][1];
	int node_j = subsets_i[1][0];

	if (init_idx == 0) mat_i[node_i][node_ii] *= -1;
	else if (init_idx == 1) mat_i[node_i][node_j] *= -1;
	else cout << "error occurs\n";
	
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) cout << mat_i[i][j] << " ";
		cout <<"\n";
	}
	cout <<"\n";
	
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
		if (check_absorbing(rule_num, mat_i))	{
				//idx = mat_to_idx(mat_i);
				break;
		}	
	}
	int sum_oij = 0;
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) sum_oij += mat_i[i][j];
	}
	
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) cout << mat_i[i][j] << " ";
		cout <<"\n";
	}
	cout <<"\n";
	
	return sum_oij;
}

int main(int argc, char *argv[]) {
	if (argc < 2) {
		cout << "./sim_L7_L8 rule_num init_idx num_sim \n";
		cout << "[init_idx] 0 : inward error\n";
		cout << "[init_idx] 1 : outward error\n";
		exit(1);
	}
	int rule_num = atoi(argv[1]);
	int init_idx = atoi(argv[2]);
	int n_r = atoi(argv[3]);

	vector<int> result_list(n_r);
	for (int n=0; n<n_r; n++) {
		vector<vector<int>> subsets_i = {{0,1,2},{3,4},{5}};
		int sum_oij = ABM_complete(rule_num, subsets_i, init_idx);
		result_list[n] = sum_oij;
		cout << result_list[n] << "\n\n\n";
		if (sum_oij > 0) cout << "!\n";
	}

	return 0;
}
