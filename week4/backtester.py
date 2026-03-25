def backtester(strategy, data, window, initial_cash=1000):
    cash = initial_cash
    holding = False

    for i in range(len(data)):
        signal = strategy(data, i, window)
        if signal == "BUY" and not holding:
            cash -= float(data[i])
            holding = True
        elif signal == "SELL" and holding:
            cash += float(data[i])
            holding = False
    
    return cash
    