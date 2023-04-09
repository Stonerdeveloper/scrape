import yfinance as yf
import pandas as pd
import numpy as np
import ta
import matplotlib.pyplot as plt
#import sklearn.linear_model

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2022-3-27')

# Calculate technical indicators
tickerDf['sma20'] = ta.trend.sma_indicator(tickerDf['Close'], window=20)
tickerDf['sma50'] = ta.trend.sma_indicator(tickerDf['Close'], window=50)
tickerDf['rsi'] = ta.momentum.RSIIndicator(tickerDf['Close']).rsi()

# Create a chart with analysis
fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(tickerDf.index, tickerDf['Close'], label='Close')
ax.plot(tickerDf.index, tickerDf['sma20'], label='SMA20')
ax.plot(tickerDf.index, tickerDf['sma50'], label='SMA50')
ax.legend()

ax2 = ax.twinx()
ax2.plot(tickerDf.index, tickerDf['rsi'], label='RSI', color='purple')
ax2.axhline(y=30, color='red', linestyle='--')
ax2.axhline(y=70, color='green', linestyle='--')
ax2.fill_between(tickerDf.index, y1=30, y2=70, color='#adccff', alpha=0.2)

ax2.legend()

#plt.plot(macd)
plt.title(tickerSymbol +'Historical Price')
plt.savefig('macd.png')
plt.show()


