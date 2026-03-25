#include <string>
#include <vector>

using namespace std;

double MA_calculator(const vector<double>& data, int index, int window) {
    double sum = 0;
    for (int i = index - window; i < index; i++) {
        sum += data[i];
    }
    return sum / window;
}

string single_MA(const vector<double>& data, int index, int window = 10) {
    if (index < window) {
        return "HOLD";
    }
    if (data[index] > MA_calculator(data, index, window)) {
        return "BUY";
    } else if (data[index] < MA_calculator(data, index, window)) {
        return "SELL";
    } else {
        return "HOLD";
    }
}