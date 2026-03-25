#include <fstream>
#include <sstream> // for stringstream (splitting)
#include <vector>
#include <string>

using namespace std;

vector<double> data_loader(string file_path) {
    vector<double> data;
    ifstream file(file_path);
    string line;
    getline(file, line);
    while (getline(file, line)) {

        stringstream ss(line);     // turn line into stream
        string value;
        int column = 0;

        // split by comma
        while (getline(ss, value, ',')) {

            if (column == 4) {
                data.push_back(stod(value));  // convert string → double
                break;
            }

            column++;
        }
    }

    return data;
}