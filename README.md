# Technical Analysis Indicators Library

This repository contains a Python class for calculating various technical analysis indicators on financial time series data. The class leverages pandas_ta to compute popular indicators such as the Relative Strength Index (RSI), Exponential Moving Average (EMA), Moving Average Convergence/Divergence (MACD), Volume Weighted Average Price (VWAP), Average True Range (ATR), Bollinger Bands, and more. It also includes a method to detect crossovers between two time series.

### Features

RSI Calculation: Compute the Relative Strength Index (RSI) over a specified window.
EMA Calculation: Calculate the Exponential Moving Average (EMA) for a series.
MACD Calculation: Derive the MACD line, signal line, and histogram.
VWAP Calculation: Compute the Volume Weighted Average Price (VWAP) from high, low, close, and volume data.
ATR Calculation: Determine the Average True Range (ATR) over a given period.
Crossover Detection: Identify crossover events between two time series.
Bollinger Bands: Generate Bollinger Bands including the lower, middle, upper bands, as well as band width and range.

---

### Dependencies

This library requires the following Python packages:

- numpy
- pandas
- pandas_ta
- yfinance (for sample data usage)
- matplotlib (for visualization in the example)

Install the dependencies via pip:

`bash`
pip install numpy pandas pandas-ta yfinance matplotlib

---

### Usage

Below is an example of how to use the TechnicalAnalysis class:

python

```
import yfinance as yf
import matplotlib.pyplot as plt
from technical_analysis import TechnicalAnalysis # Adjust the import based on your file name

# Download sample data for AAPL using yfinance

df = yf.download("AAPL", period="6mo", interval="1d")

# Create an instance of TechnicalAnalysis

ta = TechnicalAnalysis()

# Calculate various technical indicators

df["RSI"] = ta.get_RSI(df["Close"])
df["EMA_20"] = ta.get_EMA(df["Close"], window=20)
macd_df = ta.get_MACD(df["Close"])
df = df.join(macd_df)
df["VWAP"] = ta.get_VWAP(df["High"], df["Low"], df["Close"], df["Volume"])
df["ATR"] = ta.get_ATR(df["High"], df["Low"], df["Close"])
df["BBands_lower"] = ta.get_BBands(df["Close"])["Lower_Band"]
```

---

### File Structure

technical_analysis.py: Contains the TechnicalAnalysis class with methods to calculate technical indicators.
README.md: This file.

### License

MIT License

Author: William Kruta

Github: Primitive-Coding
