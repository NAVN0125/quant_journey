from data_loader import data_loader
from strategy.single_MA import single_MA
from backtester import backtester
import time

start = time.time()
data = data_loader("/Users/nhna/coding/coding_roadmap/week4_backtester/data/AAPL.csv")
print(backtester(single_MA, data, 20, 1000))
end = time.time()
print(end - start)
