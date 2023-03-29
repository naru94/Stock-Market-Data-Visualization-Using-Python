# Import libraries
# pip install matplotlib
from matplotlib import pyplot as plt
# pip install seaborn
import seaborn as sb
# pip install statsmodels
from statsmodels.graphics.tsaplots import plot_acf
import pandas as pd
# pip install plotly
import plotly.express as px

# Load Dataset
df = pd.read_csv("https://raw.githubusercontent.com/naru94/Stock-Market-Data-Visualization-Using-Python/main/dataset/BAJAJFINSV.csv", parse_dates=["Date"])

# Preprocessing of the data
df.set_index("Date", drop=False, inplace=True)

new_idx = pd.date_range("2008-05-26", "2021-04-30", freq="1D")
df = df.reindex(new_idx)

# Date vs Volume plot
sb.set_theme()
sb.set(rc={'figure.figsize':(15,8)})
fig = px.line(df, x='Date', y="Volume")
fig.write_html("plots/date_vs_volume.html")

# Date vs High price of the day plot
fig = px.line(df, x='Date', y="High")
fig.write_html("plots/date_vs_high_price.html")

# Simple Moving Average (SMA) for 10 and 20 days
df_sma=df.copy()
df_sma['SMA_10']=df_sma.VWAP.rolling(10, min_periods=1).mean()
df_sma['SMA_20']=df_sma.VWAP.rolling(20, min_periods=1).mean()

plt.plot(df_sma['Date'], df_sma['VWAP'], color='blue')
plt.plot(df_sma['Date'],df_sma['SMA_10'], color='red')
plt.plot(df_sma['Date'],df_sma['SMA_20'], color='green')
plt.savefig("plots/simple_moving_average.png")

# Autocorrelation plot
df.isnull().sum()
df['VWAP'].interpolate(method='linear',axis=0,inplace=True)
plot_acf(df['VWAP'], lags=50)
plt.savefig("plots/autocorrelation.png")

# Heatmap
df_temp=df.copy()
df_temp['day'] = df_temp.index.day
df_temp['month'] = df_temp.index.month
df_temp['year'] = df_temp.index.year

df_m=df_temp.groupby(['month', 'year']).mean(numeric_only=True)
df_m=df_m.unstack(level=0)
fig, ax = plt.subplots(figsize=(11, 9))
sb.heatmap(df_m['VWAP'])
plt.savefig("plots/heatmap.png")