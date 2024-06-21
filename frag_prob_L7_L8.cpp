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

constexpr int N = 6;

void init_matrix(int mat[][N], int val) {
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) mat[i][j] = val;
	}	
}

void split_structure(int mat[][N], vector<vector<int>> &subsets) {
	vector<int> cluster;
	cluster.push_back(0);
	for (int k=1; k<N; k++) {
		if (mat[0][k] == 1) cluster.push_back(k);
	}
	subsets.push_back(cluster);

	for (int i=1; i<N; i++) {
		if (find(cluster.begin(), cluster.end(), i) != cluster.end()) {
			cluster.clear();
			cluster.push_back(i);
			for (int j=i+1; j<N; j++) {
				if (mat[i][j] == 1) cluster.push_back(j);
			}
			subsets.push_back(cluster);
		}
	}
}

void print_mat(int mat[][N]) {
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) {
			cout << mat[i][j] << " ";
		}
		cout << "\n";
	}
	cout << "\n";
}

void idx_to_mat(unsigned long long idx, int mat[][N]) {
	int idx_tmp = idx;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
    	int M_ij = idx_tmp & 1;  // [TODO] check this line
    	mat[i][j] = 2 * M_ij - 1;
			idx_tmp = idx_tmp >> 1;
    }
  }
}

unsigned long long mat_to_idx(int mat[][N]) {
  unsigned long long idx = 0, binary_num = 0;
  idx = binary_num = 0;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
    	int element = ((int) (mat[i][j] + 1) / 2);
    	idx += element * (int) pow(2, binary_num);
    	binary_num += 1;
    }
  }
  return idx;
}

int L8_rule(int mat_f[][N], int o, int d, int r, int idx_err) {
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

int L7_rule(int mat_f[][N], int o, int d, int r, int idx_err) {
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

int L4_rule(int mat_f[][N], int o, int d, int r, int idx_err) {
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

int L6_rule(int mat_f[][N], int o, int d, int r, int idx_err) {
  // mat_f should be empty matrix whose size is N by N.
  int val_update = (idx_err == 0 ? mat_f[o][r] * mat_f[d][r] : -mat_f[o][r] * mat_f[d][r]);
	return val_update;
}

bool check_absorbing(int rule_num, int mat_i[][N]){
	bool bool_val = false;
	int check = 0;
	int count = 0;
  int mat_f[N][N] = {0,};
  std::copy(&mat_i[0][0], &mat_i[0][0] + N * N, &mat_f[0][0]);
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

void (int mat[][N], vector<vector<int>> &subsets) {
	init_matrix(mat[][N], -1);


}

unsigned long long ABM_complete(int rule_num, int mat_i[][N]){
	int mat_i[N][N] = { -1 };
	for (int i=0; i<subsets_i.size(); i++) {
		for (int j=0; j<subsets_i[i].size(); j++) {
			int v = subsets_i[i][j];
			mat_i[v][v] = 1;
			for (int k=0; k<subsets_i[i].size(); k++) {
				mat_i[v][k] = mat_i[k][v] = 1;
			}
		}
	}
	unsigned long long idx = 0;
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
				//print_mat(mat_i);
				//cout << "\n";
				idx = mat_to_idx(mat_i);
				break;
		}	
	}
	return idx;
}

int main(int argc, char *argv[]) {
	if (argc < 2) {
		cout << "./sim_L7_L8 rule_num init_idx \n";
		exit(1);
	}
	int rule_num = atoi(argv[1]);
	int init_idx = atoi(argv[2]);

	if (init_idx == 0) mat_i[0][1] *= -1; // L7
	else if (init_idx == 1) mat_i[0][3] *= -1; 
	else if (init_idx == 2) mat_i[3][0] *= -1;
	else cout << "Error : set 'init_idx' as 0, 1, or 2." << "\n";
	vector<vector<int>> subsets_i = {{0,1,2},{3,4},{5}}

	unsigned long long result = ABM_complete(rule_num, subsets_i);
	if (result == org) cout << 0 << "\n";
	else if (result == d1) cout << 1 << "\n";
	else if (result == d2) cout << 2 << "\n";
	else if (result == d3) cout << 3 << "\n";
	else if (result == d4) cout << 4 << "\n";
	else if (result == d5) cout << 5 << "\n";
  else cout << 6 << "\n";
	//else	print_mat(mat_i);	

	return 0;
}
