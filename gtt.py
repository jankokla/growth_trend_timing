from typing import List

import yfinance as yf
import pandas as pd
import pandas_datareader as pdr
from plotly.subplots import make_subplots
import plotly.express as px
import datetime


def get_stock_data(ticker: str, ma_window: int) -> pd.DataFrame:
    """Return the daily stock data with moving average."""
    stock = yf.Ticker(ticker)
    stock_data = stock.history(period='5y')
    stock_data['MA10'] = stock_data['Close'].rolling(window=ma_window).mean()
    return stock_data


def get_economics_data(year_count: int, data_points: List[str]) -> pd.DataFrame:
    """
    Return the DataFrame of the economics data.

    :param year_count: how many years back we look
    :param data_points: list of identifiers for indicators
    :return: df with the indicator data
    """
    df = pdr.DataReader(data_points,
                        'fred',
                        (datetime.datetime.today() - datetime.timedelta(days=year_count * 365)).strftime('%Y-%m-%d'),
                        datetime.datetime.today().strftime('%Y-%m-%d'))

    for data_point in data_points:
        df[data_point] = (df[data_point].div(df[data_point].shift(12)) - 1) * 100

    return df


def plot(stock_df: pd.DataFrame, economics_df: pd.DataFrame):
    """
    Plot two subplots with:
        1. stock data with moving average;
        2. economics data for the Industrial Production Index and Advance Real Retail and Food Services Sales.
    """
    fig = make_subplots(rows=2, cols=1,
                        subplot_titles=('Vanguard FTSE All-World ETF (VWRL.AS)', 'FRED Economic Data'))

    fig_up = px.line(
        stock_df,
        x=stock_df.index,
        y=['Close', 'MA10'])

    fig_down = px.line(
        economics_df,
        x=economics_df.index,
        y=economics_df.columns.values.tolist(),
        color_discrete_map={
            'INDPRO': "green",
            'RRSFS': "goldenrod"
        })

    for i in range(2):
        fig_down.data[i].update(mode='markers+lines')
        fig.add_trace(fig_up['data'][i], row=1, col=1)
        fig.add_trace(fig_down['data'][i], row=2, col=1)

    fig.show()


if __name__ == '__main__':
    _ticker = 'VWRL.AS'
    _ma_window = 300
    _stock_data = get_stock_data(_ticker, _ma_window)

    production_identifier = 'INDPRO'
    retail_sales_identifier = 'RRSFS'
    _economics_data = get_economics_data(5, [production_identifier, retail_sales_identifier])

    plot(_stock_data, _economics_data)
