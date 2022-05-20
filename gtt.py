import yfinance as yf
import pandas as pd
import plotly.express as px


def get_stock_data(ticker: str, ma_window: int) -> pd.DataFrame:
    stock = yf.Ticker(ticker)
    stock_data = stock.history(period='5y')
    stock_data['MA10'] = stock_data['Close'].rolling(window=ma_window).mean()
    return stock_data


def plot(stock_data: pd.DataFrame):
    fig = px.line(
        stock_data,
        x=stock_data.index,
        y=['Close', 'MA10'],
        title="Vanguard FTSE All-World ETF (VWRL.AS)")

    fig.update_layout(
        legend_title="Variables",
        yaxis_title="Price (EUR)")
    fig.show()


if __name__ == '__main__':
    _ticker = "VWRL.AS"
    _ma_window = 300
    _stock_data = get_stock_data(_ticker, _ma_window)
