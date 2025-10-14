import yfinance as yf

tickers = ["MSFT", "AAPL", "GOOGL", "AMZN", "TSLA"]

for ticker in tickers:
    dat = yf.Ticker(ticker)
    history = dat.history(period='1y')
    history.to_csv(f'{ticker}_history.csv')
    print(f"Downloaded {ticker}")