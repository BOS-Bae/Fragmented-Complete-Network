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

bool check_absorbing(int rule_num, int mat_i[][N]);

unsigned long long mat_to_idx(int mat[][N]);

void balanced_idx(std::vector<unsigned long long> &bal_list);

int L4rule(int Mat[][N], int o, int d, int r);

int L6rule(int Mat[][N], int o, int d, int r);

int L7rule(int mat_f[][N], int o, int d, int r);

int L8rule(int mat_f[][N], int o, int d, int r);

void L4_rule(int mat_f[][N], int o, int d, int r, int idx_err);

void L6_rule(int mat_f[][N], int o, int d, int r, int idx_err);

void L7_rule(int mat_f[][N], int o, int d, int r, int idx_err);

void L8_rule(int mat_f[][N], int o, int d, int r, int idx_err);

void n_list_gen(int n_num, int n_list[][N]);

void power_method(double err, int max_iter, int rule_num, unsigned long long confi_idx);

/*
	init_vect_idx = 0 : r_i has elments with uniform values (=1/num_matrix)
	init_vect_idx = 1 : r_i has an element for a balanced index only
	init_vect_idx = 2 : r_i has an element for a balanced index only
	
	init_vect_idx = 0 : 2^(N*N) elements in dat file (whole possible states)
	init_vect_idx = 1 : 2^(N-1) elements in dat file (only balanced states)
	init_vect_idx = 2 : 2^(N-1) elements in dat file (only balanced states)
*/
int main(int argc, char *argv[]) {
  int num_of_bal = (int) pow(2, N - 1);
  if ((argc < 3) || (atoi(argv[2]) != 4 && atoi(argv[2]) != 6 &&  atoi(argv[2]) != 7 && atoi(argv[2]) != 8)) {
    printf("./improved_power max_iter rule_num init_confi_idx \n");
    printf("rule_num : 4(L4_rule), 6(L6_rule?), 7(L7_rule) or 8(L8_rule) \n");
    exit(1);
  }
  int max_iter = atoi(argv[1]);
  int rule_num = atoi(argv[2]);
	unsigned long long confi_idx = strtoull(argv[3], nullptr, 10);

  power_method(0, max_iter, rule_num, confi_idx);
  return 0;
}

bool check_absorbing(int rule_num, int mat_i[][N]){
	bool bool_val = false;
	int check = 0;
	int count = 0;
	int mat_later[N][N] = {0,};
	
	for (int o=0; o<N; o++){
		for (int d=0; d<N; d++) mat_later[o][d] = mat_i[o][d];
	}	
 	//std::copy(mat_i.begin(), mat_i.end(), mat_later.begin());
	for (int o=0; o<N; o++){
		for (int d=0; d<N; d++){
			for (int r=0; r<N; r++){
				int tmp = mat_later[o][d];
        switch (rule_num) {
          case 4 :
            mat_later[o][d] = L4rule(mat_later, o, d, r);
            break;
          case 6 :
            mat_later[o][d] = L6rule(mat_later, o, d, r);
            break;
					case 7 :
						mat_later[o][d] = L7rule(mat_later, o, d, r);
						break;
					case 8 :
						mat_later[o][d] = L8rule(mat_later, o, d, r);
						break;
        }
				count += 1;
				if (mat_later[o][d] == mat_i[o][d]) check += 1;
				mat_later[o][d] = tmp;
			}
		}
	}
	if (count == check) bool_val = true;
	return bool_val;
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

int L6rule(int Mat[][N], int o, int d, int r){
	int val = 0;
	val = Mat[o][r]*Mat[d][r];

	return val;
}

int L4rule(int Mat[][N], int o, int d, int r){
	int val = 0;
	if (Mat[o][d] == 1 && Mat[d][r] == 1 && Mat[o][r] == -1) val = 1;
	else val = Mat[o][r]*Mat[d][r];

	return val;
}

int L7rule(int mat_f[][N], int o, int d, int r) {
	int val = mat_f[o][d];
	if (mat_f[d][r] == 1) {
		if (mat_f[o][d] == 1) val = 1;
		else val = mat_f[o][r];
	}
	else if (mat_f[d][r] == -1)	{
		if (mat_f[o][d] == 1) val = -mat_f[o][r];
		else val = -1;
	}

	return val;
}

int L8rule(int mat_f[][N], int o, int d, int r) {
	int val = mat_f[o][d];
	if (mat_f[d][r] == 1) val = mat_f[o][r];
	else if (mat_f[d][r] == -1)	{
		if (mat_f[o][d] == 1) val = -mat_f[o][r];
		else val = -1;
	}
	
	return val;
}

void L4_rule(int mat_f[][N], int o, int d, int r, int idx_err) {
  // mat_f should be empty matrix whose size is N by N.
  int val = mat_f[o][d];
  if (mat_f[d][r] == 1) {
    if (mat_f[o][d] == -1) val = mat_f[o][r];
  } 
	else val = -mat_f[o][r];

  mat_f[o][d] = idx_err == 0 ? val : -val;
}

void L6_rule(int mat_f[][N], int o, int d, int r, int idx_err) {
  // mat_f should be empty matrix whose size is N by N.
  mat_f[o][d] = (idx_err == 0 ? mat_f[o][r] * mat_f[d][r] : -mat_f[o][r] * mat_f[d][r]);
}

void L7_rule(int mat_f[][N], int o, int d, int r, int idx_err) {
  // mat_f should be empty matrix whose size is N by N.
  int val = mat_f[o][d];
  if (mat_f[d][r] == 1) {
    if (mat_f[o][d] == -1) val = mat_f[o][r];
  }
	else {
		if (mat_f[o][d] == 1) val = -mat_f[o][r];
		else val = -1;
	}

  mat_f[o][d] = idx_err == 0 ? val : -val;
}

void L8_rule(int mat_f[][N], int o, int d, int r, int idx_err) {
  // mat_f should be empty matrix whose size is N by N.
  int val = mat_f[o][d];
  if (mat_f[d][r] == 1) val = mat_f[o][r]; 
	else if (mat_f[d][r] == -1) {
		if (mat_f[o][d] == 1) val = -mat_f[o][r];
		else val = -1;
	}

  mat_f[o][d] = idx_err == 0 ? val : -val;
}

void power_method(double err, int max_iter, int rule_num, unsigned long long confi_idx) {
  /*
    init_vect_idx = 0 : r_i has elments with uniform values (=1/num_matrix)
    init_vect_idx = 1 : r_i has an element for a balanced index only
    init_vect_idx = 2 : r_i has an element for a balanced index only

    init_vect_idx = 0 : 2^(N*N) elements in dat file (whole possible states)
    init_vect_idx = 1 : 2^(N-1) elements in dat file (only balanced states)
    init_vect_idx = 2 : 2^(N-1) elements in dat file (only balanced states)
  */
  //constexpr int n_num = 1 << N;
  double array[2];
  array[0] = (1.0 - err);
  array[1] = err;

  int num_of_bal = (int) pow(2, N - 1);
  std::vector<unsigned long long> bal_list = {};
  balanced_idx(bal_list);
  sort(bal_list.begin(), bal_list.end());

  //int n_list[n_num][N];
  double prob_mul;
  //n_list_gen(n_num, n_list);

  const size_t num_matrix = 1ull << (N * N);
  std::ofstream opening;
  
	char result[100];
  sprintf(result, "./flip_dat/N%d-L%d-idx%llu.dat", N, rule_num, confi_idx);
  opening.open(result);

	unsigned long long flip_elem = confi_idx;
 	//if (N==7) flip_elem = 425517493470087; // for 7 node reduction. (N=7)
  //else if (N==5) flip_elem = 33554429; // smallest perturbation from paradise (N=5, paradise is 33554431)
  //else if (N==4) flip_elem = 65533; // smallest perturbation from paradise (N=4, paradise is 65535)
  //else if (N==3) flip_elem = 509; // smallest perturbation from paradise (N=3)
	
	std::vector<unsigned long long> s_i = {};
	std::vector<unsigned long long> s_f = {};
  // measure elapsed time
  //std::vector<double> r_i(num_matrix, 0.0);
  for (int t = 0; t < max_iter; t++) {
		s_i.clear();
		int len_f = s_f.size();
		if (t==0) s_i.push_back(flip_elem);
		else {
			for (int i = 0 ; i < len_f; i++) s_i.push_back(s_f[i]);
		}
		std::sort(s_f.begin(), s_f.end(), std::greater<unsigned long long>());
		
		//if (t == max_iter - 1){
		//	for (int k = 0; k < s_f.size(); k++) {
		//		int mat_k[N][N] = {0,};
    //		idx_to_mat(s_f[k], mat_k);
		//		if (check_absorbing(rule_num, mat_k)) opening << s_f[k] << " ";
		//	}
		//}
		std::sort(s_f.begin(), s_f.end(), std::greater<unsigned long long>());
		//for (int k = 0; k < s_f.size(); k++) opening << s_f[k] << " ";
		s_f.clear();

		int len = s_i.size();
    for (int i = 0; i < len; i++) {
    	//std::vector<double> r_f(num_matrix, 0.0);
			unsigned long long state_i = s_i[i];
    	std::vector<unsigned long long> s_idx_f;
			//std::fill_n(r_i.begin(), num_matrix, 0.0);
			//r_i[state_i] = 1;
			
      int mat_i[N][N] = {0,};
      int mat_f[N][N] = {0,};
      idx_to_mat(state_i, mat_i);
      for (int x = 0; x < N; x++) {
        for (int y = 0; y < N; y++) {
         std::copy(&mat_i[0][0], &mat_i[0][0] + N * N, &mat_f[0][0]);
         prob_mul = 1.0;
         for (int l = 0; l < N; l++) {
           //int idx_n = n_list[m][l];
           switch (rule_num) {
             case 4 :
               L4_rule(mat_f, l, x, y, 0);
               break;
             case 6 :
               L6_rule(mat_f, l, x, y, 0);
               break;
             case 7 :
               L7_rule(mat_f, l, x, y, 0);
               break;
             case 8 :
               L8_rule(mat_f, l, x, y, 0);
               break;
           }
        }
        unsigned long long idx_f = mat_to_idx(mat_f);
       	 //r_f[idx_f] += prob_mul * (1 / (double) (N * N)) * r_i[state_i];
				s_idx_f.push_back(idx_f);
				if (std::find(s_f.begin(), s_f.end(), idx_f) == s_f.end()) s_f.push_back(idx_f);
        }
      }
			opening << state_i << " ";
			for (int s_idx = 0; s_idx < s_idx_f.size(); s_idx++) {
				opening << s_idx_f[s_idx] << " ";
			}
			opening << "\n";
		}
  }
  opening.close();
}
