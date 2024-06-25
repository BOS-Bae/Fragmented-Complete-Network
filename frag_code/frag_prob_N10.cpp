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

constexpr int N = 10;

void init_matrix(int mat[][N], int val) {
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) mat[i][j] = val;
	}	
}

void subset_to_mat(vector<vector<int>> &subsets_i, int mat[][N]) {
	init_matrix(mat, -1);
	
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

void print_subsets(vector<vector<int>> &subsets) {
	for (int i=0; i<subsets.size(); i++){
		for (int j=0; j<subsets[i].size(); j++) cout << subsets[i][j] << " ";
		cout << "\n";
	}
	cout << "\n";
}

void print_mat(int mat[][N]) {
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) cout << mat[i][j] << " ";
		cout << "\n";
	}
	cout << "\n";
}

void mat_to_subset(int mat[][N], vector<vector<int>> &subsets) {
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

unsigned long long ABM_complete(int rule_num, int mat_i[][N]){
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
	if (argc < 3) {
		cout << "./frag_prob rule_num init_idx n_sample \n";
		exit(1);
	}
	int rule_num = atoi(argv[1]);
	int init_idx = atoi(argv[2]);
	int n_sample = atoi(argv[3]);
	
	int confi_len	= 29;
	double result_arr[confi_len] = {0};

	vector<vector<vector<int>>> subsets_list;

	vector<vector<int>> subsets_i = {{0,1,2,3},{4,5,6},{7,8},{9}}; subsets_list.push_back(subsets_i);
	vector<vector<int>> subsets_1 = {{0,2,3},{1},{4,5,6},{7,8},{9}}; subsets_list.push_back(subsets_1);

	vector<vector<int>> subsets_2 = {{0},{1,2,3},{4,5,6},{7,8},{9}}; subsets_list.push_back(subsets_2);
	vector<vector<int>> subsets_3 = {{0,1,2,3,4,5,6},{7,8},{9}}; subsets_list.push_back(subsets_3);
	vector<vector<int>> subsets_4 = {{0,4,5,6},{1,2,3},{7,8},{9}}; subsets_list.push_back(subsets_4);
	vector<vector<int>> subsets_5 = {{0,1,2,3},{4},{5,6},{7,8},{9}}; subsets_list.push_back(subsets_5);
	vector<vector<int>> subsets_6 = {{0,1,2,3,7},{4,5,6},{8},{9}}; subsets_list.push_back(subsets_6);
	vector<vector<int>> subsets_7 = {{0,1,2,3},{4,5,6},{7},{8},{9}}; subsets_list.push_back(subsets_7);
	vector<vector<int>> subsets_8 = {{0,1,2,3,7,8},{4,5,6},{9}}; subsets_list.push_back(subsets_8);
	vector<vector<int>> subsets_9 = {{0,1,2,3,9},{4,5,6},{7,8}}; subsets_list.push_back(subsets_9);
	vector<vector<int>> subsets_10 = {{0,1,2,3},{4,5,6,7,8},{9}}; subsets_list.push_back(subsets_10);
	vector<vector<int>> subsets_11 = {{0,1,2,3},{4,5,6,9},{7,8}}; subsets_list.push_back(subsets_11);
	vector<vector<int>> subsets_12 = {{0,1,2,3},{4,5,6},{7,8,9}}; subsets_list.push_back(subsets_12);
	vector<vector<int>> subsets_13 = {{0,1,2,3},{4,5,6,7},{8},{9}}; subsets_list.push_back(subsets_13);
	vector<vector<int>> subsets_14 = {{0,1,2,3},{4},{5,6,7},{8},{9}}; subsets_list.push_back(subsets_14);
	vector<vector<int>> subsets_15 = {{0,1,2,3,4},{5,6},{7,8},{9}}; subsets_list.push_back(subsets_15);
	vector<vector<int>> subsets_16 = {{0,7,8}, {1,2,3}, {4,5,6}, {9}}; subsets_list.push_back(subsets_16);
	vector<vector<int>> subsets_17 = {{0,9}, {1,2,3}, {4,5,6}, {7,8}}; subsets_list.push_back(subsets_17);
	vector<vector<int>> subsets_18 = {{0,1,2,3},{4,7,8},{5,6},{9}}; subsets_list.push_back(subsets_18);
	vector<vector<int>> subsets_19 = {{0,1,2,3},{4,9},{5,6},{7,8}}; subsets_list.push_back(subsets_19);
	vector<vector<int>> subsets_20 = {{0,1,2,3},{4,5,6},{7,9},{8}}; subsets_list.push_back(subsets_20);
	vector<vector<int>> subsets_21 = {{0,1,2,3}, {4}, {5,6,7,8},{9}}; subsets_list.push_back(subsets_21);
	vector<vector<int>> subsets_22 = {{0,1,2,3,8},{4,5,6},{7},{9}}; subsets_list.push_back(subsets_22);
	vector<vector<int>> subsets_23 = {{0},{1,2,3,9},{4,5,6},{7,8}}; subsets_list.push_back(subsets_23);
	vector<vector<int>> subsets_24 = {{0,1,2,3}, {4,5,6,8},{7},{9}}; subsets_list.push_back(subsets_24);
	vector<vector<int>> subsets_25 = {{0}, {1,2,3,4,5,6}, {7,8}, {9}}; subsets_list.push_back(subsets_25);
	vector<vector<int>> subsets_26 = {{0,1,2,3,5,6}, {4}, {7,8}, {9}}; subsets_list.push_back(subsets_26);
	vector<vector<int>> subsets_27 = {{0},{1,2,3,7,8},{4,5,6},{9}}; subsets_list.push_back(subsets_27);
	vector<vector<int>> subsets_28 = {{0,1,2,3},{4},{5,6,9},{7,8}}; subsets_list.push_back(subsets_28);

	
	for (int n_s=0; n_s<n_sample; n_s++){
		int mat_i[N][N];
		subset_to_mat(subsets_i, mat_i);
		
		if (init_idx == 0) mat_i[0][1] *= -1;
		else if (init_idx == 1) mat_i[7][8] *= -1; 
		else if (init_idx == 2) mat_i[0][4] *= -1; 
		else if (init_idx == 3) mat_i[4][0] *= -1;
		else if (init_idx == 4) mat_i[0][7] *= -1;
		else if (init_idx == 5) mat_i[7][0] *= -1;
		else if (init_idx == 6) mat_i[0][9] *= -1;
		else if (init_idx == 7) mat_i[9][0] *= -1;
		else if (init_idx == 8) mat_i[4][7] *= -1;
		else if (init_idx == 9) mat_i[7][4] *= -1;
		else if (init_idx == 10) mat_i[4][9] *= -1;
		else if (init_idx == 11) mat_i[9][4] *= -1;
		else if (init_idx == 12) mat_i[7][9] *= -1;
		else if (init_idx == 13) mat_i[9][7] *= -1;
		else if (init_idx == 14) mat_i[4][5] *= -1;
		else cout << "Error : set 'init_idx' to be within 0 ~ 14." << "\n";
		
		unsigned long long result = ABM_complete(rule_num, mat_i);
		vector<vector<int>> subsets_f;
		mat_to_subset(mat_i, subsets_f);

//		print_subsets(subsets_f);

		//print_subsets(subsets_list[1]);

		//vector<vector<int>> subsets_check;
		//int mat_check[N][N];
		//subset_to_mat(subsets_list[1], mat_check);
		//mat_to_subset(mat_check, subsets_check);
		//
		//print_subsets(subsets_check);
		//bool well = (subsets_list[1] == subsets_check);
		//cout << well <<"\n";

		int check = 0;
		for (int i=0; i<subsets_list.size(); i++) {
			//int mat_check[N][N];
			//vector<vector<int>> subsets_check;
			//subset_to_mat(subsets_list[i], mat_check);
			//mat_to_subset(mat_check, subsets_check);

			//int well = subsets_list[i] == subsets_check ? 1 : -1;
			//cout << well << "\n";

			if (subsets_f == subsets_list[i]) {
				//cout << i << "\n";
				result_arr[i] += 1;
			}
			else check += 1;
		}
		if (check == subsets_list.size()) print_mat(mat_i);
	}
	double summ = 0;
	for (int i=0; i<confi_len; i++) {
		double elem = result_arr[i] / (double)n_sample;
		cout << elem  << " "; 
		summ += elem;
	}
	cout << summ << "\n";
	return 0;
}
