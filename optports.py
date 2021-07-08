import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sys import argv

return_stocks = pd.read_csv(argv[1], delimiter=';', index_col=0, parse_dates=True)
stocks = list(return_stocks.columns)

portfolio_returns = []
portfolio_risk = []
sharpe_ratio_port = []
portfolio_weights = []
ann_returns = []

number_of_portfolios = 5
RF = 0.01

for portfolio in range(number_of_portfolios):
    weights = np.random.random_sample((len(stocks)))
    weights = weights / np.sum(weights)

    annualize_return = np.sum((return_stocks.mean() * weights) * 252)
    ann_returns.append(annualize_return)
    portfolio_returns.append(annualize_return)
    matrix_covariance_portfolio = (return_stocks.cov() * 252)
    portfolio_variance = np.dot(weights.T,np.dot(matrix_covariance_portfolio, weights))
    portfolio_standard_deviation= np.sqrt(portfolio_variance) 
    portfolio_risk.append(portfolio_standard_deviation)
    sharpe_ratio = ((annualize_return- RF)/portfolio_standard_deviation)
    sharpe_ratio_port.append(sharpe_ratio)

    portfolio_weights.append(weights)  

portfolio_risk = np.array(portfolio_risk)
portfolio_returns = np.array(portfolio_returns)
sharpe_ratio_port = np.array(sharpe_ratio_port)

porfolio_metrics = [portfolio_returns,portfolio_risk,sharpe_ratio_port, portfolio_weights] 
portfolio_dfs = pd.DataFrame(porfolio_metrics)
portfolio_dfs = portfolio_dfs.T
portfolio_dfs.columns = ['Port Returns','Port Risk','Sharpe Ratio','Portfolio Weights']

for col in ['Port Returns', 'Port Risk', 'Sharpe Ratio']:
    portfolio_dfs[col] = portfolio_dfs[col].astype(float)

Highest_sharpe_port = portfolio_dfs.iloc[portfolio_dfs['Sharpe Ratio'].idxmax()]
min_risk = portfolio_dfs.iloc[portfolio_dfs['Port Risk'].idxmin()]
Highest_sharpe_port.to_csv('output.csv')

plt.figure(figsize=(10, 5))
plt.scatter(portfolio_risk, portfolio_returns, c=(portfolio_returns-RF) / portfolio_risk)
plt.scatter(Highest_sharpe_port['Port Risk'], Highest_sharpe_port['Port Returns'], marker='*', color='r', linewidths=3, label='Max Sharpe ratio')
plt.xlabel('Portfolio Standard deviation')
plt.ylabel('Portfolio Return')
axes = plt.gca()
axes.set_xlim(0)
axes.set_ylim()
plt.colorbar(label='Sharpe ratio')
plt.savefig('output.png')
