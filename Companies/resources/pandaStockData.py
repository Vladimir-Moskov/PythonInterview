"""
    Review of main Panda features

    https://pandas.pydata.org/
    Python Data Analytics: With Pandas, NumPy, and Matplotlib
"""
import pandas
import quandl
import matplotlib.pyplot as plt

quandl.ApiConfig.api_key = ''
apple = quandl.get('WIKI/AAPL')
ms = quandl.get('WIKI/MSFT')

print(ms.head())

# ms['Adj. Close'].plot()
# plt.show()
print(ms.index)

# ms['2018']['Adj. Close'].plot()
# ms['2018-03']['Adj. Close'].plot()
# ms.loc['2018-01-01': '2018-03-31']['Adj. Close'].plot()

ms_price = ms[['Adj. Close']]
apple_price = apple[['Adj. Close']]
ms_price.rename(columns={'Adj. Close': 'MSFT'}, inplace=True)
apple_price.rename(columns={'Adj. Close': 'AAPL'}, inplace=True)

both_stock = ms_price.join(apple_price, how='inner')
# both_stock.plot()
# both_stock.loc['2017'].plot()
# both_stock['2017'].rolling(min_periods=10, window=10, center=False).mean().plot()

both_stock['2017'].rolling(min_periods=10, window=10, center=False).std().plot()
plt.show()






