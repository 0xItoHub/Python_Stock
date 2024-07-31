import yfinance as yf
import matplotlib.pyplot as plt

# データを取得したい銘柄のティッカーシンボルを指定
ticker = 'AAPL'

# yfinanceを使ってデータを取得
data = yf.download(ticker, start="2023-01-01", end="2023-07-31")

# 株価チャートを表示
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['Close'], label='Close Price')
plt.title(f'{ticker} Stock Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
