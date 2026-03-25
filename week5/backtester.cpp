#include <functional>
#include <vector>
using namespace std;

double backtester(function<string(const vector<double>&, int, int)> strategy, const vector<double>& data, int window, double initial_cash = 1000) {
    double cash = initial_cash;
    bool holding = false;
    for (int i = 0; i < data.size(); i++) {
        string signal = strategy(data, i, window);
        if (signal == "BUY" && !holding) {
            cash -= data[i];
            holding = true;
        } else if (signal == "SELL" && holding) {
            cash += data[i];
            holding = false;
        }
    }
    return cash;
}