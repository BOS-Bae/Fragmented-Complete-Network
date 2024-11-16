#include <iostream>
#include <cstdlib>
#include <fstream>
#include <cmath>
#include <vector>
#include <array>
#include <algorithm>

constexpr int N = 6;

// The reason for using 'usigned long long' : 2^(N*N) exceeds the maximum of 'int', when N=6.
void idx_to_mat(unsigned long long idx, int mat[][N]);

void print_mat(int mat[][N]);

unsigned long long mat_to_idx(int mat[][N]);

void balanced_idx(std::vector<unsigned long long> &bal_list);

void L4_rule(int mat_f[][N], int o, int d, int r, int idx_err);

void L6_rule(int mat_f[][N], int o, int d, int r, int idx_err);

void n_list_gen(int n_num, int n_list[][N]);

int main() {

	int mat[N][N];
	int slice_group = 3;
	std::vector<int> cluster_1 = {}; std::vector<int> cluster_2 = {};
	
	for (int i=0; i<slice_group; i++) cluster_1.push_back(i); 
	for (int i=slice_group; i<N; i++) cluster_2.push_back(i);

	for (int i=0; i<N; i++){
		for (int j=0; j<N; j++) mat[i][j] = -1;
	}
	for (int node1 = 0; node1 < N; node1++){
		for (int node2 = 0; node2 < N; node2++){
			if (node1 < cluster_2[0] && node2 < cluster_2[0]) mat[node1][node2] = mat[node2][node1] = 1;
			else if (node1 >= cluster_2[0] && node2 >= cluster_2[0]) mat[node1][node2] = mat[node2][node1] = 1;
		}
	}
	mat[cluster_1[0]][cluster_2[0]] = 1;
	
	print_mat(mat);
	unsigned long long idx = mat_to_idx(mat);
	std::cout << idx << "\n";
	int mat_i[N][N];
	idx_to_mat(idx, mat_i);
	print_mat(mat_i);
	return 0;
}

void balanced_idx(std::vector<unsigned long long> &bal_list) {
  const size_t max_idx = (1ull << N) - 1;
  std::vector<std::array<int, N> > id_mat(max_idx);
  for (int i = 0; i < max_idx; i++) {
    int idx = i;
    for (int j = 0; j < N; j++) {
      int id = idx & 1;
      id_mat[i][j] = id;
      idx = idx >> 1;
    }
  }
  int max_num = 0;
  for (int i = 0; i < max_idx; i++) {
    int mat[N][N] = {0,};
    for (int x = 0; x < N; x++) {
      for (int y = 0; y < N; y++) {
        if (id_mat[i][x] == id_mat[i][y]) mat[x][y] = mat[y][x] = 1;
        else mat[x][y] = mat[y][x] = -1;
      }
    }
    unsigned long long bal_idx = mat_to_idx(mat);
    if (i == 0) {
      bal_list.push_back(bal_idx);
      max_num += 1;
    } 
		else {
      int check = 0;
      int different = 0;
      for (int k = 0; k < max_num; k++) {
        check += 1;
        if (bal_list[k] != bal_idx) different += 1;
      }
      if (check == different) {
        bal_list.push_back(bal_idx);
        max_num += 1;
      }
    }
  }
}


void idx_to_mat(unsigned long long idx, int mat[][N]) {
	unsigned long long idx_tmp = idx;
  for (int i = 0; i < N; i++) {
		mat[i][i] = 1;
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
     	unsigned long long element = ((unsigned long long) (mat[i][j] + 1) / 2);
     	idx += element * (unsigned long long) pow(2, binary_num);
     	binary_num += 1;
    }
  }
  return idx;
}

void L4_rule(int mat_f[][N], int o, int d, int r, int idx_err) {
  // mat_f should be empty matrix whose size is N by N.
  int val = mat_f[o][d];
  if (mat_f[d][r] == 1) {
    if (mat_f[o][d] == -1)
      val = mat_f[o][r];
  } else
    val = -mat_f[o][r];

  mat_f[o][d] = idx_err == 0 ? val : -val;
}

void L6_rule(int mat_f[][N], int o, int d, int r, int idx_err) {
  // mat_f should be empty matrix whose size is N by N.
  mat_f[o][d] = (idx_err == 0 ? mat_f[o][r] * mat_f[d][r] : -mat_f[o][r] * mat_f[d][r]);
}


void print_mat(int mat[][N]){
	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			std::cout << mat[i][j] << " ";
		}
		std::cout << "\n";
	}
	std::cout <<"\n";
}

