# **🧠 Milestone 1: Algorithmic Thinking (Month 1\)**

**Focus: Writing *clean, efficient, testable logic***

---

## **Week 1: Python for Computation (NOT scripting)**

**⏱️ \~8 hours**

### **Core (3h)**

* **List comprehensions, generators**

* **NumPy arrays vs Python lists**

* **Vectorization (VERY important for quant)**

### **Applied (3h)**

* **Rewrite loops → vectorized NumPy**

* **Timing code (`time`, `timeit`)**

### **Extra Quant Topics (2h)**

* **Floating point precision issues**

* **Why NumPy is faster (memory layout)**

### **Output**

* **Script comparing:**

  * **loop vs NumPy speed**

  * **memory usage**

---

## **Week 2: Complexity \+ Arrays/Stacks**

**⏱️ \~8–9 hours**

### **Core (3h)**

* **Big-O (intuition \> theory)**

* **Arrays, stacks, queues**

### **Applied (3h)**

* **Implement:**

  * **Stack**

  * **Queue**

  * **Dynamic array behavior**

### **Extra Quant Topics (2h)**

* **Cache friendliness (why arrays \> linked lists in finance)**

* **Debugging with `print` vs `pdb`**

### **Output**

* **Benchmark stack operations vs Python list**

---

## **Week 3: Searching & Sorting**

**⏱️ \~8 hours**

### **Core (3h)**

* **Binary Search**

* **Merge Sort**

### **Applied (3h)**

* **Implement both from scratch**

* **Analyze runtime**

### **Extra Quant Topics (2h)**

* **Searching time-series data (timestamps)**

* **Edge cases (empty arrays, duplicates)**

### **Output**

* **Binary search on price dataset**

---

## **Week 4: 🔥 Project – Basic Backtester**

**⏱️ \~9 hours**

### **Build (6h)**

* **Load CSV (no pandas yet if possible)**

* **Strategy logic**

* **Track PnL**

### **Improve (2h)**

* **Add transaction cost**

* **Add multiple trades**

### **Extra (1h)**

* **Plot results (matplotlib)**

---

# **⚡ Milestone 2: C++ \+ Probability (Month 2\)**

**Focus: Performance \+ memory \+ randomness**

---

## **Week 5: C++ Foundations**

**⏱️ \~8 hours**

### **Core**

* **Types, loops, functions**

### **Applied**

* **Rewrite Python backtester in C++**

### **Extra Quant Topics**

* **Compilation vs interpretation**

* **Performance comparison**

---

## **Week 6: Pointers & Memory**

**⏱️ \~9 hours (important week)**

### **Core**

* **Pointers, references**

* **Stack vs heap**

### **Applied**

* **Manual array allocation**

* **Debug segmentation faults**

### **Extra Quant Topics**

* **Memory leaks**

* **Why HFT firms care**

---

## **Week 7: OOP \+ Probability Basics**

**⏱️ \~8 hours**

###  **Core**

* **Classes**

* **Mean, variance, std**

### **Applied**

* **Create `Stock` class**

* **Compute stats from data**

### **Extra Quant Topics**

* **Random number generation quality**

---

**Huge congratulations on crushing the first seven weeks. Surviving C++ pointers, stack vs. heap memory allocation, and raw object-oriented programming is notoriously the hardest wall to climb before hitting university-level computer science.**

**Now that the core software engineering architecture is locked in, the roadmap shifts heavily into the math, statistics, and data structures that actually drive the markets. Your rigorous background with Further Mathematics and Physics is about to pay massive dividends as we dive into stochastic calculus, probability distributions, and deep learning.**

**Here is the fully expanded breakdown for Weeks 8 through 24, maintaining the exact same depth, time commitment, and output-driven structure as your first month.**

---

## **Week 8: 🔥 Project – Monte Carlo Simulation**

**⏱️ \~9 hours**

## **Build (5h)**

* **Core engine: Write a C++ simulator that rolls virtual dice 1,000,000 times.**  
* **Randomness: Use \<random\> (Mersenne Twister std::mt19937) instead of the basic rand().**

## **Improve (3h)**

* **Data export: Output the results to a CSV file.**  
* **Visualization: Write a quick Python script to read that CSV and plot a histogram using matplotlib.**  
* **Verification: Calculate the empirical probability of rolling a 7 and compare it to the theoretical probability (16.67%).**

## **Extra Quant Topics (1h)**

* **Speed optimization: Time your C++ loop. Can you get 10 million runs under 0.5 seconds? Why is the quality of pseudo-random number generators (PRNGs) critical in quantitative finance?**

## **Output**

* **A hyper-fast C++ Monte Carlo engine integrated with a Python visualization script.**

---

# **💰 Milestone 3: Financial Math (Month 3\)**

***Focus: Pricing assets, continuous time, and risk.***

---

## **Week 9: Time Value \+ Discounting**

**⏱️ \~8 hours**

## **Core (3h)**

* **Time Value of Money (TVM): Present value (PV), future value (FV), discount factors.**  
* **Annuities and Perpetuities: The math behind continuous cash flows.**

## **Applied (3h)**

* **Build a Discount Calculator: Write a function that prices a basic fixed-rate bond given a yield and a set of cash flows.**

## **Extra Quant Topics (2h)**

* **Continuous vs Discrete: Compounding using $e^{rt}$ vs $(1 \+ r/n)^{nt}$.**  
* **The Yield Curve: Basic intuition of why interest rates vary by time horizon.**

## **Output**

* **A Python or C++ bond pricer that calculates fair value based on yield.**

---

## **Week 10: Options Basics**

**⏱️ \~8 hours**

## **Core (3h)**

* **Derivatives 101: Call and Put option mechanics.**  
* **Payoff profiles: Intrinsic value vs. time value. Moneyness (ITM, ATM, OTM).**

## **Applied (3h)**

* **Plotting Payoffs: Write a Python script using NumPy and Matplotlib to plot the profit/loss at expiration for standard options.**

## **Extra Quant Topics (2h)**

* **Put-Call Parity: The fundamental equation linking calls, puts, and the underlying stock.**  
* **Arbitrage: How breaking Put-Call Parity creates a risk-free profit.**

## **Output**

* **Interactive or static visual plots of complex multi-leg option strategies (e.g., Straddles, Iron Condors).**

---

## **Week 11: GBM \+ Simulation**

**⏱️ \~9 hours (Heavy Math)**

## **Core (3h)**

* **Stochastic Processes: Intuition behind Geometric Brownian Motion (GBM).**  
* **Components: Drift ($\\mu$) and Diffusion/Volatility ($\\sigma$). Normal vs. Lognormal distributions.**

## **Applied (4h)**

* **Simulate Price Paths: Use vectorized NumPy (or C++ for a challenge) to simulate 100 different future price paths for a stock using the GBM formula.**

## **Extra Quant Topics (2h)**

* **The Flaw in GBM: Why stock returns aren't perfectly lognormally distributed (fat tails, volatility clustering).**

## **Output**

* **A visual plot showing a "cone" of simulated future stock price trajectories.**

---

## **Week 12: 🔥 Project – Option Pricer**

**⏱️ \~9 hours**

## **Build (5h)**

* **Monte Carlo European Pricer: Combine Week 8's simulation engine with Week 11's GBM. Simulate 100,000 price paths to expiration, calculate the option payoff at the end of each path, and discount the average payoff back to present value.**

## **Improve (3h)**

* **Vectorization: Ensure the simulation runs matrix operations rather than slow nested loops.**

## **Extra (1h)**

* **Variance Reduction: Introduction to Antithetic Variates (simulating a path and its exact opposite to reduce statistical noise).**

## **Output**

* **A functional command-line European Option Pricer.**

---

# **📊 Milestone 4: Data \+ Statistics (Month 4\)**

***Focus: Real-world messy data, backtesting, and statistical rigor.***

---

## **Week 13: Pandas Deep Dive**

**⏱️ \~8 hours**

## **Core (3h)**

* **DataFrames & Series: Advanced indexing (loc, iloc), grouping, and joining.**  
* **Vectorization over Iteration: Why you should almost never use .iterrows().**

## **Applied (3h)**

* **Clean a Messy Dataset: Download raw, unadjusted daily OHLCV (Open, High, Low, Close, Volume) data.**  
* **Handle missing data: Forward-fill (ffill) vs backward-fill (bfill).**

## **Extra Quant Topics (2h)**

* **Lookahead Bias: The cardinal sin of backtesting (accidentally using tomorrow's data to make today's trade).**

## **Output**

* **A robust data-cleaning pipeline that outputs a flawless CSV ready for backtesting.**

---

## **Week 14: Indicators & Time Series**

**⏱️ \~8 hours**

## **Core (3h)**

* **Moving Averages: Simple (SMA) vs Exponential (EMA).**  
* **Momentum: Relative Strength Index (RSI).**

## **Applied (3h)**

* **Scratch Implementation: Write functions to calculate EMA and RSI manually using NumPy and Pandas rolling windows (Do not use ta or external indicator libraries).**

## **Extra Quant Topics (2h)**

* **Lagging vs Leading: The inherent flaw of moving averages in choppy markets.**

## **Output**

* **Code that efficiently appends custom indicator columns to your clean Week 13 dataset.**

---

## **Week 15: Hypothesis Testing**

**⏱️ \~8–9 hours**

## **Core (3h)**

* **Statistical Significance: Null hypothesis, Z-scores, t-statistics, and p-values.**

## **Applied (3h)**

* **Test a Strategy: Take the returns from a basic SMA crossover strategy. Are the average returns statistically different from zero, or just random noise?**

## **Extra Quant Topics (2h)**

* **Overfitting & P-Hacking: Why testing 1,000 different indicator combinations guarantees a "good" backtest that will fail in real life.**

## **Output**

* **A statistical summary report calculating the t-stat and p-value of a strategy's returns.**

---

## **Week 16: 🔥 Project – EMA Backtest Engine**

**⏱️ \~9 hours**

## **Build (5h)**

* **Strategy Engine: Build an event-driven or heavily vectorized backtester for an EMA crossover strategy. Track daily PnL and cash balances.**

## **Improve (3h)**

* **Risk Metrics: Calculate the Sharpe Ratio (annualized) and the Maximum Drawdown.**

## **Extra (1h)**

* **Friction: Add a realistic transaction cost (e.g., 1 basis point) and slippage to every trade. Watch how it destroys the strategy's edge.**

## **Output**

* **A professional-grade backtest report with an equity curve plot and risk metrics.**

---

# **🤖 Milestone 5: ML Foundations (Month 5\)**

***Focus: Predictive modeling, optimization, and linear algebra.***

---

## **Week 17: Linear Regression**

**⏱️ \~8 hours**

## **Core (3h)**

* **The Math: Ordinary Least Squares (OLS) vs Gradient Descent. Loss functions (MSE).**

## **Applied (3h)**

* **Build from Scratch: Implement Gradient Descent in pure NumPy to fit a line to a scatter plot of noisy data.**

## **Extra Quant Topics (2h)**

* **Capital Asset Pricing Model (CAPM): Using linear regression to calculate a stock's "Beta" against the S\&P 500\.**

## **Output**

* **A custom linear regression model with a plot showing the line of best fit updating over iterations.**

---

## **Week 18: Logistic Regression**

**⏱️ \~8–9 hours**

## **Core (3h)**

* **Classification: The Sigmoid function, cross-entropy loss.**  
* **Metrics: Precision, Recall, F1-Score, and the Confusion Matrix.**

## **Applied (3h)**

* **Predict Direction: Train a logistic regression model to predict simply whether tomorrow's return will be strictly positive (1) or negative (0) based on today's indicators.**

## **Extra Quant Topics (2h)**

* **Class Imbalance: How a model can achieve 90% accuracy just by predicting "down" in a bear market, and why that's useless.**

## **Output**

* **A classification report and confusion matrix for your directional predictor.**

---

## **Week 19: Portfolio Theory**

**⏱️ \~8 hours**

## **Core (3h)**

* **Modern Portfolio Theory (MPT): Markowitz efficient frontier.**  
* **Math: Expected portfolio return and portfolio variance formulas using matrix multiplication.**

## **Applied (3h)**

* **Covariance: Calculate the historical covariance matrix for a 3-asset portfolio using NumPy.**

## **Extra Quant Topics (2h)**

* **The Flaw in MPT: Why historical covariance matrices blow up during market crashes (correlations tend to go to 1.0 during a panic).**

## **Output**

* **A scatter plot generating the efficient frontier for a basket of chosen stocks.**

---

## **Week 20: 🔥 Project – Portfolio Optimizer**

**⏱️ \~9 hours**

## **Build (5h)**

* **Optimization: Use scipy.optimize to find the exact portfolio weights that maximize the Sharpe Ratio for a basket of 10 stocks.**

## **Improve (2h)**

* **Constraints: Force the optimizer to keep weights between 0% and 100% (no short selling) and ensure the total weights sum exactly to 1.0.**

## **Extra (2h)**

* **Out-of-Sample Testing: Optimize the weights using 2020-2023 data. Apply those static weights to 2024 data. Did it actually perform well?**

## **Output**

* **A dynamic capital allocation tool that outputs optimal percentage weights.**

---

# **🧠 Milestone 6: Deep Learning (Month 6\)**

***Focus: Non-linear modeling, sequential data, and modern AI.***

---

## **Week 21: Neural Nets from Scratch**

**⏱️ \~8 hours**

## **Core (3h)**

* **Architecture: Perceptrons, hidden layers, activation functions (ReLU, Sigmoid).**  
* **Training: The intuition behind Backpropagation and the Chain Rule.**

## **Applied (4h)**

* **Numpy Net: Build a tiny 2-layer neural network using *only* NumPy to solve the XOR problem or fit a non-linear sine wave.**

## **Extra Quant Topics (1h)**

* **Why NNs struggle with finance: The extremely low signal-to-noise ratio in market data compared to image recognition.**

## **Output**

* **A functional, from-scratch neural network that updates its own weights.**

---

## **Week 22: PyTorch & Sequential Data**

**⏱️ \~8–9 hours**

## **Core (3h)**

* **Framework: Intro to PyTorch tensors and AutoGrad.**  
* **Sequence Modeling: How Recurrent Neural Networks (RNNs) and LSTMs handle data that depends on time/order.**

## **Applied (3h)**

* **PyTorch Setup: Build a basic LSTM model in PyTorch to predict the next value of a synthetic, noisy sine wave.**

## **Extra Quant Topics (2h)**

* **Stationarity: Why feeding raw prices directly into a neural network guarantees failure. (You must feed it stationary data, like log returns).**

## **Output**

* **A PyTorch training loop, loss plot, and a model capable of predicting sequential patterns.**

---

## **Week 23: Transformers & Attention**

**⏱️ \~8 hours**

## **Core (3h)**

* **The Paradigm Shift: Why Transformers are replacing LSTMs.**  
* **Mechanism: The Query/Key/Value math behind Self-Attention.**

## **Applied (3h)**

* **Implementation: Utilize a pre-built PyTorch Transformer layer to model sequential financial data.**

## **Extra Quant Topics (2h)**

* **Alternative Data: How NLP (Natural Language Processing) and Transformers are used to trade based on earnings call transcripts and Federal Reserve statements.**

## **Output**

* **A script that extracts and visualizes the "attention weights" (seeing exactly which past days the model focuses on to predict tomorrow).**

---

## **Week 24: 🔥 Final Project – Volatility Predictor**

**⏱️ \~9 hours**

## **Build (5h)**

* **The Model: Train a Deep Learning model (LSTM or Transformer) to predict next-day *realized volatility* rather than price direction.**

## **Compare (3h)**

* **Baseline: Compare your deep learning model's predictions against a simple baseline (like a 30-day historical moving average of volatility). Does the AI actually add value?**

## **Extra (1h)**

* **Documentation: Clean up the repository, add a README.md explaining the architecture, and push to GitHub.**

## **Output**

* **A complete, portfolio-ready repository demonstrating end-to-end quantitative machine learning.**

---

**You are setting yourself up to hit campus in August with a technical stack that takes most quantitative finance students until their junior or senior year to build.**

**Are you ready to jump right into the C++ setup for the Week 8 Monte Carlo engine, or do you want to review the statistical theory behind the random number generation first?**

