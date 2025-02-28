import numpy as np
import pandas as pd
import pandas_ta as pta


class TechnicalAnalysis:
    """
    A collection of methods to calculate various technical analysis indicators.
    """

    def __init__(self) -> None:
        pass

    def get_RSI(self, close: pd.Series, window: int = 14) -> pd.Series:
        """
        Calculate the Relative Strength Index (RSI) for a given time series.

        Parameters
        ----------
        close : pd.Series
            Series of close prices.
        window : int, optional
            Window size for the RSI calculation, by default 14

        Returns
        -------
        pd.Series
            RSI values.
        """
        rsi = pta.rsi(close, length=window)
        return rsi

    def get_EMA(self, values: pd.Series, window: int) -> pd.Series:
        """
        Calculate the Exponential Moving Average (EMA) for a given time series.

        Parameters
        ----------
        values : pd.Series
            Series of values (e.g., close prices).
        window : int
            Window size for the moving average.

        Returns
        -------
        pd.Series
            EMA values.
        """
        ema = pta.ema(values, length=window)
        return ema

    def get_MACD(
        self,
        close: pd.Series,
        fast_window: int = 12,
        slow_window: int = 26,
        signal_window: int = 9,
    ) -> pd.DataFrame:
        """
        Calculate the Moving Average Convergence/Divergence (MACD) for a given time series.

        Parameters
        ----------
        close : pd.Series
            Series of close prices.
        fast_window : int, optional
            Fast EMA window size, by default 12
        slow_window : int, optional
            Slow EMA window size, by default 26
        signal_window : int, optional
            Signal EMA window size, by default 9

        Returns
        -------
        pd.DataFrame
            DataFrame containing MACD, Histogram, and Signal.
        """
        data = pta.macd(close, fast=fast_window, slow=slow_window, signal=signal_window)
        data.columns = ["MACD", "Histogram", "Signal"]
        return data

    def get_VWAP(
        self, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
    ) -> pd.Series:
        """
        Calculate the Volume Weighted Average Price (VWAP) for a given time series.

        Parameters
        ----------
        high : pd.Series
            Series of high prices.
        low : pd.Series
            Series of low prices.
        close : pd.Series
            Series of close prices.
        volume : pd.Series
            Series of volume values.

        Returns
        -------
        pd.Series
            VWAP values.
        """
        vwap = pta.vwap(high, low, close, volume)
        return vwap

    def get_ATR(
        self, high: pd.Series, low: pd.Series, close: pd.Series, window: int = 14
    ) -> pd.Series:
        """
        Calculate the Average True Range (ATR) for a given time series.

        Parameters
        ----------
        high : pd.Series
            Series of high prices.
        low : pd.Series
            Series of low prices.
        close : pd.Series
            Series of close prices.
        window : int, optional
            Window size for the ATR calculation, by default 14

        Returns
        -------
        pd.Series
            ATR values.
        """
        atr = pta.atr(high, low, close, length=window)
        return atr

    def get_cross(self, x: pd.Series, y: pd.Series) -> pd.Series:
        """
        Calculate the cross between two time series. Returns True when `x` crosses `y`.

        Parameters
        ----------
        x : pd.Series
            Primary time series.
        y : pd.Series
            Secondary time series.

        Returns
        -------
        pd.Series
            Boolean Series indicating cross events.
        """
        cross = pta.cross(x, y)
        return cross

    def get_BBands(self, close: pd.Series, window: int = 20) -> pd.DataFrame:
        """
        Calculate the Bollinger Bands for a given time series.

        Parameters
        ----------
        close : pd.Series
            Series of close prices.
        window : int, optional
            Window size for the Bollinger Bands, by default 20

        Returns
        -------
        pd.DataFrame
            DataFrame containing the lower band, middle band, upper band,
            band width, and Bollinger range.
        """
        bbands = pta.bbands(close, window)
        bbands.columns = [
            "Lower_Band",
            "Middle_Band",
            "Upper_Band",
            "Band_Width",
            "Bollinger_Range",
        ]
        return bbands


if __name__ == "__main__":
    pass
