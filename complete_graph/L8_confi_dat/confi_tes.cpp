#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>
#include <sstream> // stringstream
using namespace std;

constexpr int N = 7;

void print_mat(int mat[][N]);
void idx_to_mat(unsigned long long idx, int mat[][N]);
unsigned long long mat_to_idx(int mat[][N]);

int main() {
    ifstream inputFile("p_to_m.dat");
    if (!inputFile) {
        cerr << "File is not available." << endl;
        return 1;
    }
    vector<unsigned long long> idx_list;
    string line;
    while (getline(inputFile, line)) {
        stringstream ss(line);
        unsigned long long num;
        while (ss >> num) {
            idx_list.push_back(num);
        }
    }
    inputFile.close();
		
		for (int i = 0; i < idx_list.size(); i++) {
			unsigned long long idx = idx_list[i];
			int mat[N][N];

			idx_to_mat(idx, mat);
			print_mat(mat);

		}
    return 0;
}

void print_mat(int mat[][N]){
	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			std::cout << mat[i][j] << " ";
		}
		std::cout << "\n";
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

