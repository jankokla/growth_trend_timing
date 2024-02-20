# Growth Trend Timing

Applying the idea of market timing from [Philosophical Economics](http://www.philosophicaleconomics.com/2016/01/gtt/) (PE). In addition to using 
moving average, it involves economic indicators as second layer for the final decisions.

## Theory

Growth Trend Timing combines trend following strategies with economic indicators in order to avoid losses. As PE puts it:

> It systematically does what any human trend-following market timer would have to do in order to be successful – 
> distinguish between negative price trends that will give way to large downturns that support profitable 
> exits and reentries, and negative price trends that will prove to be nothing more than short-term noise.

In this case, [the Industrial Production Index](https://fred.stlouisfed.org/graph/?g=3atC) and 
[Advance Real Retail and Food Services Sales](https://fred.stlouisfed.org/graph/?g=2aF7) is used as economic indicators. 
The ETF in focus is [Vanguard FTSE All-World UCITS ETF](https://finance.yahoo.com/quote/VWRL.AS/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAJHakSVXDGrM4cEoP1m0HdVZJNa93_Px2wP2P__pVyqfkRnkUZJqgOU9m_Ioy9Gh7r7-y60OKgTsWv_IwWOhYYDXMWtYw5doMNaE4RO-HYrErGFpIRxlCVIhzjXPp_zpClqzaFwLm1XZtWDLsvk1FI2dAY-j0aVrS9dtF9lXRZTA)
and 10-month moving average is used as a trend following indicator.

## Installation 

1. Clone the repository to your preferred destination.
2. Manually run or use cron jobs to periodically plot the results using Plotly.
