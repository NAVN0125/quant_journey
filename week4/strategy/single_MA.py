def MA_calculator(data, index, window):
    return sum(float(x) for x in data[index - window:index]) / window

def single_MA(data, index, window=10):
    if index < window:
        return "HOLD"
    if float(data[index]) > MA_calculator(data, index, window):
        return "BUY"
    elif float(data[index]) < MA_calculator(data, index, window):
        return "SELL"
    else:
        return "HOLD"
        