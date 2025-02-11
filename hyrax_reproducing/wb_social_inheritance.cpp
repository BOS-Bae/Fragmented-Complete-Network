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

void print_mat(vector<vector<int>> &Mat, int N) {
	for (int i=0; i<N; i++){
		for (int j=0; j<N; j++){
			cout << Mat[i][j] << " ";
		}
		cout << "\n";
	}
	cout << "\n";
}

void init_network(vector<vector<int>> &net, int N) {
	random_device rd;
	mt19937 gen(rd());
	uniform_real_distribution<> dist_u(0, 1);
	
	for (int i = 0; i < N; i++) {
		for (int j = i; j < N; j++) {
			if (i!=j && dist_u(gen) < 0.5) net[i][j] = net[j][i] = 1;
			else net[i][j] = net[j][i] = 0;
		}
	}
}

double mean_degree(vector<vector<int>> &net, int N) {
	double deg = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) deg += (double)net[i][j];
	}
	deg /= (double)N;

	return deg;
}

int Phi(int kd, int dr, int kr) {
	int kd_p = 2*kd - 1;
	int dr_p = 2*dr - 1;
	int kr_p = 2*kr - 1;
	
	return (kd_p*dr_p*kr_p);
}

double balance(vector<vector<int>> &net, int N) {
	double B = 0;
	int count = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < N; k++) {
				if (i != j && j != k && i != k) {
					count += 1;
					if (Phi(net[i][j], net[j][k], net[i][k]) == 1) B += 1;
				}
			}
		}
	}
	B /= (double)count;
	return B;
}

double weak_balance(vector<vector<int>> &net, int N) {
	double WB = 0;
	int count = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < N; k++) {
				if (i != j && j != k && i != k) {
					count += 1;
					if (Phi(net[i][j], net[j][k], net[i][k]) == 1) WB += 1;
					else if (net[i][j] == 0 && net[j][k] == 0 && net[i][k] == 0) WB += 1;
				}
			}
		}
	}
	WB /= (double)count;
	return WB;
}

int find_mother(vector<vector<int>> &net, int i, int N) {
	random_device rd;
	mt19937 gen(rd());
	vector<int> mothers_i = {};
	uniform_int_distribution<> dist_k(0, N-2);
	for (int k = 0; k < N; k++) {
		if (k!=i) mothers_i.push_back(k);
	}
	int mom_idx = dist_k(gen);

	return mothers_i[mom_idx];
}

int mother_node(vector<vector<int>> &net, int i, int N) {
	random_device rd;
	mt19937 gen(rd());
	vector<int> nn = {};
	int nn_selected;

	int deg=0;	
	for (int k=0; k<N; k++) {
		if (i!=k && net[i][k] == 1) {
			deg += 1;
			nn.push_back(k);
		}
	}
//	cout << deg <<"\n";
	if (deg > 0) {
		uniform_int_distribution<> dist_k(0, deg);
		int nn_idx = dist_k(gen);
		int nn_selected = nn[nn_idx];
	}
	else nn_selected = i;
	
	return nn_selected;
}

void evolution(vector<vector<int>> &net, int N, double pr, double pn, int MCS) {
	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<> dist_i(0, N-1);
	uniform_real_distribution<> dist_u(0, 1);
	
	//vector<double> WB_t(MCS, 0);
	init_network(net, N);
	//print_mat(net, N);

	for (int t = 0; t < MCS; t++) {
		int i = dist_i(gen); //newborn (x:die -> i:born)
		int mom = find_mother(net, i, N);
		for (int k = 0; k < N; k++) net[i][k] = net[k][i] = 0; // initialize its connection
		net[i][mom] = net[mom][i] = 1; // pb = 1 is assumed here.

		//int mom = mother_node(net, i, N);
		for (int k = 0; k < N; k++) {
			if (k!=i && net[k][mom] == 1 && dist_u(gen) <= pn) net[i][k] = net[k][i] = 1;
			else if (k!=i && net[k][mom] == 0 && dist_u(gen) <= pr) net[i][k] = net[k][i] = 1;
		}
		cout << t << "  " << balance(net, N) << "  " << weak_balance(net, N) << "\n";
	}
}

int main(int argc, char *argv[]) {
	if (argc < 4) {
		cout << "./wb_social_inheritance N pn pr MCS \n";
		exit(1);
	}
	// Minwoo Bae : 'pb is assumed to be 1, according to the paper.' (25.02.07)
	int N = atoi(argv[1]);
	double pn = atof(argv[2]);
	double pr = atof(argv[3]);
	int MCS = atoi(argv[4]);

	vector<vector<int>> net(N, vector<int>(N,0));
	evolution(net, N, pr, pn, MCS);

	return 0;
}

