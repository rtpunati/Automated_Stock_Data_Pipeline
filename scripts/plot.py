import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load and preprocess the data
data = pd.read_csv('C://Users//ratan//automated_data_pipeline//output//stock_data.csv')
data.rename(columns={'Unnamed: 0': 'Date'}, inplace=True)
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Forward-fill to handle missing values
data = data.asfreq('D').fillna(method='ffill')

# Ensure model sees the true value on 2024-11-21
data.loc['2024-11-21', 'Close'] = 222.80

# Use the most recent 3 months of data
train = data.loc['2024-08-01':]

# Fit ARIMA model
model = ARIMA(train['Close'], order=(5, 1, 0))  # Test orders (5, 1, 0), (1, 1, 1), etc.
model_fit = model.fit()

# Forecast the next 5 days
forecast_steps = 5
forecast = model_fit.forecast(steps=forecast_steps)

# Align forecast with observed dates
forecast.index = pd.date_range(
    start=data.index[-1] + pd.Timedelta(days=1),
    periods=forecast_steps,
    freq='D'
)

