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

int ABM_complete(int N, int rule_num) {
	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<> dist(0, N-1);
	uniform_real_distribution<> dist_u(0, 1);
	vector<vector<int>> mat_i(N, vector<int>(N,0));	
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) {
			if (dist_u(gen) < 0.5) mat_i[i][j] = 1;
			else mat_i[i][j] = -1;
		}
	}
	//for (int i=0; i<N; i++) {
	//	for (int j=0; j<N; j++) cout << mat_i[i][j] << " ";
	//	cout <<"\n";
	//}
	//cout <<"\n";
	
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
	//for (int i=0; i<N; i++) {
	//	for (int j=0; j<N; j++) cout << mat_i[i][j] << " ";
	//	cout <<"\n";
	//}
	//cout <<"\n";
	
	return sum_oij;
}

int main(int argc, char *argv[]) {
	if (argc < 3) {
		cout << "./ABM_paradise_L7 rule_num num_sim \n";
		exit(1);
	}
	int N_max = 50;
	int N_init = 5;

	int rule_num = atoi(argv[1]);
	int n_run = atoi(argv[2]);

	for (int N=N_init; N<=N_max; N++) {
		int n_p = 0;
		for (int n=0; n<n_run; n++) {
			if (ABM_complete(N, rule_num) == N*N) n_p += 1;
		}
		cout << N << " " << double(n_p)/double(n_run) << std::endl;
	}
	return 0;
}
