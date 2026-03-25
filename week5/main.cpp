#include <iostream>
#include <vector>
#include <string>
#include <functional>
#include <chrono>

using namespace std;

// Function prototypes
vector<double> data_loader(string file_path);
string single_MA(const vector<double>& data, int index, int window = 10);
double backtester(function<string(const vector<double>&, int, int)> strategy, const vector<double>& data, int window, double initial_cash = 1000);

int main() {
    string file_path = "/Users/nhna/coding/coding_roadmap/week4_backtester/data/AAPL.csv";
    
    auto start = chrono::high_resolution_clock::now();
    vector<double> data = data_loader(file_path);
    // cout << data.size() << endl;
    double final_cash = backtester(single_MA, data, 20, 1000);
    
    cout << final_cash << endl;
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = end - start;
    cout << "Elapsed time: " << elapsed.count() << " seconds" << endl;
    
    return 0;
}
