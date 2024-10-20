#include <iostream>
#include <cstdlib>
#include <fstream>
#include <cmath>
#include <vector>
#include <array>
#include <algorithm>

constexpr int N = 7;

// The reason for using 'usigned long long' : 2^(N*N) exceeds the maximum of 'int', when N=6.
void idx_to_mat(unsigned long long idx, int mat[][N]);

void idx_to_2Dvector(unsigned long long idx, std::vector<std::vector<int>> &mat);

void init_matrix(std::vector<std::vector<int>> &mat, int val, int N);

void subset_to_mat(std::vector<std::vector<int>> &subsets_i, std::vector<std::vector<int>> &mat, int N);

void mat_to_subset(std::vector<std::vector<int>> &mat, std::vector<std::vector<int>> &subsets, int N);

void print_subsets(std::vector<std::vector<int>> &subsets);

void print_2D_vector(std::vector<std::vector<int>> &mat, int N);

void print_mat(int mat[][N]);

unsigned long long mat_to_idx(int mat[][N]);

void balanced_idx(std::vector<unsigned long long> &bal_list);

void L4_rule(int mat_f[][N], int o, int d, int r, int idx_err);

void L6_rule(int mat_f[][N], int o, int d, int r, int idx_err);

void n_list_gen(int n_num, int n_list[][N]);

void power_method(double err, int max_iter, int rule_num, int flip_idx);

/*
	init_vect_idx = 0 : r_i has elments with uniform values (=1/num_matrix)
	init_vect_idx = 1 : r_i has an element for a balanced index only
	init_vect_idx = 2 : r_i has an element for a balanced index only
	
	init_vect_idx = 0 : 2^(N*N) elements in dat file (whole possible states)
	init_vect_idx = 1 : 2^(N-1) elements in dat file (only balanced states)
	init_vect_idx = 2 : 2^(N-1) elements in dat file (only balanced states)
*/
int main() {
	unsigned long long init_idx = 425517493470087;
	int mat_i[N][N];
		
	idx_to_mat(init_idx, mat_i);
	print_mat(mat_i);
	std::cout << "\n";

	std::vector<unsigned long long> L7_absorbing = {562949953421311, 549651923009923, 545219244277243, 531921213965191, 531921213915523, 456544338179047, 443247930969499, 443247119368579, 438815794082275, 438814711558627, 425519386972063, 425518575321475, 425518304398747, 425517492847495, 425517492797827};


	std::vector<unsigned long long> L6_absorbing = {549651923009923, 531921213965191, 456544338179047, 443247930969499, 438815794082275, 425519386972063};

	for (int i = 0; i < L6_absorbing.size(); i++) {
		unsigned long long idx_i = L6_absorbing[i];
		std::vector<std::vector<int>> mat_vec(N, std::vector<int> (N,0));

		idx_to_2Dvector(idx_i, mat_vec);

		std::vector<std::vector<int>> subsets_f;

		mat_to_subset(mat_vec, subsets_f, N);

		print_subsets(subsets_f);
	}
		

	//std::vector<std::vector<int>> mat_N7 = {{1,1,1,-1,-1,-1,-1},{1,1,1,-1,-1,-1,-1},{1,-1,1,1,-1,1,-1},
	//{-1,-1,-1,1,1,-1,-1},{-1,-1,-1,1,1,-1,-1},{-1,-1,-1,-1,-1,1,1},{-1,-1,-1,-1,-1,1,1}}; // big cluster : - -> +  


	//std::vector<std::vector<int>> mat_0 = {{1,-1,1,1,1},{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1}}; // big cluster : - -> +  
	//std::vector<std::vector<int>> mat_1 = {{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1}}; // big cluster : - -> +  
	//int matN7[N][N] = {0,};
	//int mat0[N][N] = {0,};
	//int mat1[N][N] = {0,};
	//for (int i = 0; i < N; i++){
	//	for (int j = 0; j < N; j++){
	//		matN7[i][j] = mat_N7[i][j];
	//	}
	//}
	////int idx0 = mat_to_idx(mat0);
	////int idx1 = mat_to_idx(mat1);
	//unsigned long long idxN7 = mat_to_idx(matN7);
	//std::cout << idxN7 << " \n";
	//print_mat(matN7);
	//std::cout << "\n";

	//int matN7_prime[N][N] = {0,};
	//idx_to_mat(idxN7, matN7_prime);

	//print_mat(matN7_prime);
	//unsigned long long idxN7_prime = mat_to_idx(matN7_prime);
	//std::cout << "\n";
	//std::cout << idxN7_prime << " \n";
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

void idx_to_2Dvector(unsigned long long idx, std::vector<std::vector<int>> &mat) {
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

void n_list_gen(int n_num, int n_list[][N]) {
  for (int i = 0; i < n_num; i++) {
    // The number of possible configurations of assessment eror is n_num.
    int val = i;
    for (int j = 0; j < N; j++) {
      n_list[i][j] = val & 1;
      val = val >> 1;
    }
  }
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


void power_method(double err, int max_iter, int rule_num, int flip_idx) {
  /*
    init_vect_idx = 0 : r_i has elments with uniform values (=1/num_matrix)
    init_vect_idx = 1 : r_i has an element for a balanced index only
    init_vect_idx = 2 : r_i has an element for a balanced index only

    init_vect_idx = 0 : 2^(N*N) elements in dat file (whole possible states)
    init_vect_idx = 1 : 2^(N-1) elements in dat file (only balanced states)
    init_vect_idx = 2 : 2^(N-1) elements in dat file (only balanced states)
  */
  constexpr int n_num = 1 << N;
  double array[2];
  array[0] = (1.0 - err);
  array[1] = err;

  int num_of_bal = (int) pow(2, N - 1);
  std::vector<unsigned long long> bal_list = {};
  balanced_idx(bal_list);
  sort(bal_list.begin(), bal_list.end());

  int n_list[n_num][N];
  double prob_mul;
  n_list_gen(n_num, n_list);

  const size_t num_matrix = 1ull << (N * N);
  std::ofstream opening;
  
	char result[100];
  sprintf(result, "./network_flip/N%dL%d_flip%d.dat", N, rule_num, flip_idx);
  opening.open(result);
	std::vector<unsigned long long> flip_list_N5 = {846865, 838737, 822289, 838657};
  unsigned long long flip_elem = flip_list_N5[flip_idx];
	
	std::vector<unsigned long long> s_i = {};
	std::vector<unsigned long long> s_f = {};
  // measure elapsed time
  std::vector<double> r_i(num_matrix, 0.0);
	r_i[flip_elem] = 1;
	int chk = 0;
  for (int t = 0; t < max_iter; t++) {
		s_i.clear();
		int len_f = s_f.size();
		if (t==0) s_i.push_back(flip_elem);
		else {
			for (int i = 0 ; i < len_f; i++) s_i.push_back(s_f[i]);
		}
		s_f.clear();
		int len = s_i.size();
    std::vector<double> r_f(num_matrix, 0.0);
    for (int i = 0; i < num_matrix; i++) {
      int mat_i[N][N] = {0,};
      int mat_f[N][N] = {0,};
      idx_to_mat(i, mat_i);
      for (int x = 0; x < N; x++) {
        for (int y = 0; y < N; y++) {
          for (int m = 0; m < n_num; m++) {
            std::copy(&mat_i[0][0], &mat_i[0][0] + N * N, &mat_f[0][0]);
            prob_mul = 1.0;
            for (int l = 0; l < N; l++) {
              int idx_n = n_list[m][l];
              switch (rule_num) {
                case 4 :
                  L4_rule(mat_f, l, x, y, idx_n);
                  break;
                case 6 :
                  L6_rule(mat_f, l, x, y, idx_n);
                  break;
              }
              prob_mul *= array[idx_n];
           } 
           int idx_f = mat_to_idx(mat_f);
       	  	r_f[idx_f] += prob_mul * (1 / (double) (N * N)) * r_i[i];
						
          }
        }
      }
		}
    for (unsigned long long i = 0; i < num_matrix; i++) {
			r_i[i] = r_f[i];
    	if (r_f[i] != 0.0) s_f.push_back(i);
		}
		chk += 1;
		if (s_f == s_i) break;
  }
	std::cout << flip_idx << " " << chk << "\n";
	int len_f = s_f.size();
	for (int i = 0; i < len_f; i++){
    std::vector<double> r_f(num_matrix, 0.0);
		int state_i = s_f[i];
    int mat_i[N][N] = {0,};
    int mat_f[N][N] = {0,};
    idx_to_mat(state_i, mat_i);
    for (int x = 0; x < N; x++) {
      for (int y = 0; y < N; y++) {
        for (int m = 0; m < n_num; m++) {
          std::copy(&mat_i[0][0], &mat_i[0][0] + N * N, &mat_f[0][0]);
          prob_mul = 1.0;
          for (int l = 0; l < N; l++) {
            int idx_n = n_list[m][l];
            switch (rule_num) {
              case 4 :
                L4_rule(mat_f, l, x, y, idx_n);
                break;
              case 6 :
                L6_rule(mat_f, l, x, y, idx_n);
                break;
            }
            prob_mul *= array[idx_n];
         } 
         int state_f = mat_to_idx(mat_f);
     	   r_f[state_f] += prob_mul * (1 / (double) (N * N));
        }
      }
    }
		for (int k = 0; k < num_matrix; k++) {
			if ((r_f[k] != 0) && (state_i != k)) opening << state_i << " " << k << " " << r_f[k] << "\n"; 
		}
	}
  opening.close();
}

void print_subsets(std::vector<std::vector<int>> &subsets) {
	for (int i=0; i<subsets.size(); i++){
		for (int j=0; j<subsets[i].size(); j++) std::cout << subsets[i][j] << " ";
		std::cout << "\n";
	}
	std::cout << "\n";
}

void print_2D_vector(std::vector<std::vector<int>> &mat, int N) {
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) std::cout << mat[i][j] << " ";
		std::cout << "\n";
	}
	std::cout << "\n";
}

void print_mat(int mat[][N]){
	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			std::cout << mat[i][j] << " ";
		}
		std::cout << "; ";
	}
	std::cout <<"\n";
}

void init_matrix(std::vector<std::vector<int>> &mat, int val, int N) {
	for (int i=0; i<N; i++) {
		std::vector<int> list;
		for (int j=0; j<N; j++) list.push_back(val);
		mat.push_back(list);
	}
}

void subset_to_mat(std::vector<std::vector<int>> &subsets_i, std::vector<std::vector<int>> &mat, int N) {
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

void mat_to_subset(std::vector<std::vector<int>> &mat, std::vector<std::vector<int>> &subsets, int N) {
	std::vector<int> cluster;
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

