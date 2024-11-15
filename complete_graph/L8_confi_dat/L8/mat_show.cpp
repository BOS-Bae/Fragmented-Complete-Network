#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>
#include <sstream> // stringstream
#include <string>

void print_mat(std::vector<std::vector <int>> &mat);
void idx_to_mat(unsigned long long idx, std::vector <std::vector <int> > &mat);
unsigned long long mat_to_idx(std::vector<std::vector<int>> &mat);

int main(int argc, char *argv[]) {
		int N = atoi(argv[1]);
		unsigned long long cidx = atoi(argv[2]);
		std::string filename = "./flip_dat/uni-N" + std::to_string(N) + "-L8-idx" + std::to_string(cidx) + ".dat";
    std::ifstream inputFile(filename);
    if (!inputFile) {
        std::cerr << "File is not available." << std::endl;
        return 1;
		}
    std::vector<unsigned long long> idx_list;
    std::string line;
    while (getline(inputFile, line)) {
        std::stringstream ss(line);
        unsigned long long num;
        while (ss >> num) {
            idx_list.push_back(num);
        }
    }
    inputFile.close();
		
		for (int i = 0; i < idx_list.size(); i++) {
			unsigned long long idx = idx_list[i];
			std::vector<std::vector<int>> mat(N, std::vector<int> (N,0));

			idx_to_mat(idx, mat);
			print_mat(mat);

		}
    return 0;
}

void print_mat(std::vector < std::vector <int> > &mat){
	for (int i = 0; i < mat.size(); i++){
		for (int j = 0; j < mat.size(); j++){
			std::cout << mat[i][j] << " ";
		}
		std::cout << "\n";
	}
	std::cout << "\n";
}

void idx_to_mat(unsigned long long idx, std::vector <std::vector <int> > &mat) {
	unsigned long long idx_tmp = idx;
  for (int i = 0; i < mat.size(); i++) {
		mat[i][i] = 1;
    for (int j = 0; j < mat.size(); j++) {
    		int M_ij = idx_tmp & 1;  // [TODO] check this line
    		mat[i][j] = 2 * M_ij - 1;
				idx_tmp = idx_tmp >> 1;
		}
  }
}

unsigned long long mat_to_idx(std::vector<std::vector<int>> &mat) {
  unsigned long long idx = 0, binary_num = 0;
  idx = binary_num = 0;
  for (int i = 0; i < mat.size(); i++) {
    for (int j = 0; j < mat.size(); j++) {
    		unsigned long long element = ((unsigned long long) (mat[i][j] + 1) / 2);
    		idx += element * (unsigned long long) pow(2, binary_num);
    		binary_num += 1;
		}
  }
  return idx;
}

