# Stock-Market-Data-Visualization-Using-Python
Stock markets are constantly changing. It is difficult to predict the stock market’s fluctuations because of the many factors at play. Similarly, it is difficult to create models to consider such variability. However, due to recent advances in machine learning and computing, machines can now process large amounts of data. This enables us to use stock exchange data from the past to analyze trends and predict future changes.

This project will leverage Python to analyze stock data from the last 13 years. Our focus will be on the NIFTY-50 stock market (2008–2021) dataset publicly available on Kaggle. However, because there are around 50 different files and stocks available in the dataset, we’ll only select one file to visualize in this project.

## Project Overview
In this project, we will use Python libraries and tools to visualize stock market data. 
There are various data visualization libraries available in Python. The top five are shown below:

* Matplotlib
* Pandas
* NumPy
* Plotly Express
* Seaborn 

Specifically, we'll use Matplotlib in combination with the Pandas library to visualize the data. The project will involve analyzing stock market data from the 26th of May, 2008 to the 30th of April, 2021, which will be updated monthly with the latest information.
Python has a significant collection of libraries that are useful for statistical computation and visualization. We use Python tools and techniques to visualize stock market data.

## Data Description
The stock market data sets are at a day-level, with pricing and trading values split across them. There are CSV files for each stock and a metadata file with some macro-information about the stocks themselves.

* The **“High”** column represents the highest price in a day.
* The **“Low”** column represents the lowest price in a day.
* The **“VWAP”** column represents the volume-weighted average price.

The **Volume-Weighted Average Price** (VWAP) is a commonly used benchmark for traders and investors to evaluate the price at which a stock or other security is trading. It takes into account both the price and the trading volume of the security over a given period of time.

The formula for calculating VWAP is:

> VWAP = ∑ (Price × Volume) / ∑ Volume

where:

Price is the price of the security at a particular time interval
Volume is the volume of the security traded at that same time interval
To calculate VWAP, you need to first determine the time interval you want to use for the calculation (e.g., one day, one hour, or one minute). Then, you would need to collect the price and volume data for that time interval and plug the values into the formula to calculate the VWAP for that interval. You would repeat this process for each interval to get a VWAP for the entire period.

**Dataset link:**

https://www.kaggle.com/datasets/rohanrao/nifty50-stock-market-data?select=BAJAJFINSV.csv

## Data Preprocessing
To preprocess the data, we'll set the "Date" column as an index, and filter the dates from 2008-05-26 to 2021-04-30. We can then convert an index to an ordinary column of the data frame.

## Data Visualization
We'll use **Seaborn** and **Plotly Express libraries** to plot the volume of each day and the highest price for each day. Additionally, we'll calculate the **Simple Moving Average (SMA)** to identify trends and potential buy/sell signals by smoothing out the price data over a specific time period.

In a moving average, we consider a subset of data and calculate its average. In stock market analysis, the moving average smooths out short-term price fluctuations, and filters out the noise (outlier data that could confuse the model). This results in a clearer picture of the price trend as compared to the raw data.

A **Simple Moving Average (SMA)** is a popular technical analysis tool that helps traders and investors to identify trends and potential buy/sell signals by smoothing out the price data over a specific time period. In stock market analysis, the moving average smooths out short-term price fluctuations, and filters out the noise (outlier data that could confuse the model). This results in a clearer picture of the price trend as compared to the raw data. The formula for calculating the SMA is straightforward:

> SMA = (Sum of Prices for N periods) / N

where:

N is the number of periods in the time frame you want to analyze
Sum of Prices for N periods is the sum of the closing prices of the asset over the chosen time frame.

To calculate the SMA, you would need to add up the closing prices of the asset over the specified time period, and then divide the sum by the number of periods. For example, to calculate a 10-day SMA for a stock's closing prices, you would add up the closing prices for the past 10 days and then divide the sum by 10.

As new data becomes available, you would recalculate the SMA by dropping the oldest price and adding the newest price, and then dividing the sum by the number of periods again. This way, the SMA will continue to reflect the most recent price movements.

## Autocorrelation Analysis
We'll analyze the prices from the past to the recent time frame using the **Autocorrelation function (ACF)** at lag k. The ACF is used to measure the correlation between a time series and its lagged values, with lag k indicating the number of time periods by which the series is shifted. We can use it to check whether the elements in the time series data are positively correlated, negatively correlated, or independent of each other.

**Autocorrelation function (ACF)** at lag k, denoted as ρk, is:

> ρk = sk/ s0

Here, sk is the sample autocovariance at lag k, and s0 is the sample variance of the time series. The sample autocovariance at lag k is calculated as:

> sk = (1/n) ∑(t=k+1 to n)[(yt – ȳ) * (yt–k – ȳ)]

where yt is the value of the time series at time t, ȳ is the sample mean of the time series, k is the number of time periods by which the series is lagged, and n is the total number of observations in the time series.

The ACF is used to measure the correlation between a time series and its lagged values, with lag k indicating the number of time periods by which the series is shifted. The ACF plot, or correlogram, is a plot of the autocorrelation coefficients against the lag values.

A **correlogram** can be used to identify patterns and trends in the time series, including seasonality and periodicity. It can also be used to inform the selection of appropriate models for forecasting future values of the series, such as autoregressive integrated moving average (ARIMA) models.

Here, 

> sk = cov (si, si + k) for any i

The variance of the time series is s0. A plot of ρk against k is known as a **correlogram**.

## Heat maps
Heat maps use colored cells at different time frames to represent the intensity of the first variable of interest, such as price, temperature, rainfall, and so on. In this plot, analyze the prices of the stock at different time frames.

## Conclusion
In conclusion, this project provides a comprehensive overview of using Python tools and techniques to visualize stock market data. We used various libraries and techniques like data preprocessing, data visualization, simple moving averages, and autocorrelation analysis to gain insights into the stock market data.