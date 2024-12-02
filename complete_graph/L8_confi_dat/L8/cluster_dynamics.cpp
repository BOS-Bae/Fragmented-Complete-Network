#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

int main(int argc, char *argv[]) {

		int m = atoi(argv[1]);
		int n = atoi(argv[2]);

    std::string file_path_R = "L8-prob-R.dat"; 
    std::string file_path_P = "L8-prob-P.dat";

    std::vector<std::vector<double>> R;
    std::vector<std::vector<double>> P;
     
    std::ifstream file_R(file_path_R);
    std::ifstream file_P(file_path_P);

    if (!file_R.is_open() || !file_P.is_open()) {
        std::cerr << "Failed to open file: " << std::endl;
        return 1;
    }

    std::string line;
    while (std::getline(file_R, line)) {
        std::istringstream ss(line);
        std::vector<double> row;
        double value;

        while (ss >> value) {
            row.push_back(value);
        }
        R.push_back(row);
    }
    file_R.close();

    std::string line2;
    while (std::getline(file_P, line2)) {
        std::istringstream ss(line2);
        std::vector<double> row2;
        double value2;

        while (ss >> value2) {
            row2.push_back(value2);
        }
        P.push_back(row2);
    }
    file_P.close();
		
		std::cout << P[m][n] << ", " << R[m][n] << "\n";
    return 0;
}
