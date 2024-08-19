#include <random>
#include <vector>
#include <cmath>
#include <iostream>

using namespace std;
using std::cout;
using std::uniform_int_distribution;
using std::uniform_real_distribution;
using std::random_device;
using std::mt19937;
using std::vector;

double average_opinion(vector<vector<int>> Mat, int N){
	int sigma = 0;
	double aver_sigma = 0.0;
	for (int i=0; i<N; i++){
		for (int j=0; j<N; j++) sigma += Mat[i][j];
	}
	aver_sigma = (double)(sigma)/(double)(N*N);

	return aver_sigma;
}

int cluster_diff(vector<vector<int>> Mat, int N){
	int	cluster_size = 0;
	for (int i=0; i<N; i++){
		if (Mat[0][i] == 1) cluster_size += 1;
	}
	int diff = N-2*cluster_size;

	return diff;
}

bool balance(vector<vector<int>> Mat, int N){
	int	check = 0;
	int bal = 0;

	bool condition_check = false;
	for (int i=0; i<N; i++){
		for (int j=0; j<N; j++){
			for (int k=0; k<N; k++){
				check +=1;
				if (Mat[i][j]*Mat[i][k]*Mat[j][k] == 1) bal += 1;
			}
		}
	}
	if (bal == check) condition_check = true;

	return condition_check;
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

int L6_rule(vector<vector<int>> Mat, int o, int d, int r, double err, double rand_num){
	int val = 0;
	val = Mat[o][r]*Mat[d][r];
	if (rand_num < err) val *= -1;

	return val;
}

int L4_rule(vector<vector<int>> Mat, int o, int d, int r, double err, double rand_num){
	int val = 0;
	if (Mat[o][d] == 1 && Mat[d][r] == 1 && Mat[o][r] == -1) val = 1;
	else val = Mat[o][r]*Mat[d][r];

	if (rand_num < err) val *= -1;


	return val;
}

int L8_rule(vector<vector<int>> &mat_f, int o, int d, int r, double err, double rand_num) {
	int val = mat_f[o][d];
	if (mat_f[d][r] == 1) val = mat_f[o][r];
	else if (mat_f[d][r] == -1)	{
		if (mat_f[o][d] == 1) val = -mat_f[o][r];
		else val = -1;
	}	
  if (rand_num < err) val *= -1;

	return val;
}

int L7_rule(vector<vector<int>> &mat_f, int o, int d, int r, double err, double rand_num) {
	int val = mat_f[o][d];
	if (mat_f[d][r] == 1) {
		if (mat_f[o][d] == 1) val = 1;
		else val = mat_f[o][r];
	}
	else if (mat_f[d][r] == -1)	{
		if (mat_f[o][d] == 1) val = -mat_f[o][r];
		else val = -1;
	}
  if (rand_num < err) val *= -1;

	return val;
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
            mat_f[o][d] = L4_rule(mat_f, o, d, r, 0, 1);
            break;
          case 6 :
            mat_f[o][d] = L6_rule(mat_f, o, d, r, 0, 1);
            break;
					case 7 :
						mat_f[o][d] = L7_rule(mat_f, o, d, r, 0, 1);
						break;
					case 8 :
						mat_f[o][d] = L8_rule(mat_f, o, d, r, 0, 1);
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

void ABM_complete(int rule_num, vector<vector<int>> &mat_i, int N, double assess_err){
	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<> dist(0, N-1);
	uniform_real_distribution<> dist_u(0, 1);

	for (int i=0; i<N; i++){
		vector<int> sigma;
		for (int j=0; j<N; j++) {
			int s_ij = dist_u(gen) < 0.5 ? 1 : -1;
			sigma.push_back(s_ij);
		}
		mat_i.push_back(sigma);
	}

	int t = 0;
	int count = 0;
	int check_bool = 0;
	
	int segregation_count = 0;

	while (true){
		t += 1;	
		int val_check = 0;
		int d = dist(gen);
		int r = dist(gen);
		
		vector<int> update_od = {};
		for (int o=0; o<N; o++) {
				double rand_num = dist_u(gen);
        switch (rule_num) {
          case 4 :
            update_od.push_back(L4_rule(mat_i, o, d, r, assess_err, rand_num));
            break;
          case 6 :
            update_od.push_back(L6_rule(mat_i, o, d, r, assess_err, rand_num));
            break;
          case 7 :
            update_od.push_back(L7_rule(mat_i, o, d, r, assess_err, rand_num));
            break;
          case 8 :
            update_od.push_back(L8_rule(mat_i, o, d, r, assess_err, rand_num));
            break;
				}
		}
		for (int o=0; o<N; o++) mat_i[o][d] = update_od[o];
		//print_mat(mat_i);
		check_bool = 0;

		if (check_absorbing(rule_num, mat_i, N)) break;
	}
}

int main(int argc, char *argv[]) {
	if (argc < 3){
		cout << "./ABM N rule_num err \n";
		exit(1);
	}

	int N = atoi(argv[1]);
	int r = atoi(argv[2]);
	double err = atof(argv[3]);
	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<> dist(0, N-1);
	uniform_real_distribution<> dist_f(0, 1);
	
	vector<vector<double>> total_absorb;

	vector<vector<int>> Mat = {};
	
	ABM_complete(r, Mat, N, err);
	print_mat(Mat, N);
	return 0;
}
