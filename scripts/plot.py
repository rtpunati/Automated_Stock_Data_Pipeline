import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load and preprocess the data
data = pd.read_csv('C://Users//ratan//automated_data_pipeline//output//MSI_stock_data.csv')
data.rename(columns={'Unnamed: 0': 'Date'}, inplace=True)
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Forward-fill to handle missing values
data = data.asfreq('D').fillna(method='ffill')

# Use all available data for training
train_data = data

# Fit ARIMA model on the training data
model = ARIMA(train_data['Close'], order=(5, 1, 0))  # Adjust order as needed
model_fit = model.fit()

# Forecast the next 5 days (27th onward)
forecast_steps = 7
forecast = model_fit.forecast(steps=forecast_steps)

# Correct forecast index to start from the next day
forecast.index = pd.date_range(start=data.index[-1] + pd.Timedelta(days=1),
                               periods=forecast_steps,
                               freq='D')

# Plot the actual data and forecast
plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Actual Data', color='blue')
plt.plot(forecast.index, forecast, label='Forecast', color='orange', linestyle='--')
plt.axvline(x=data.index[-1], color='gray', linestyle='--', label='Forecast Start')

# Add labels and legend
plt.title("Stock Price Forecast (Starting from 27th)")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.legend()
plt.grid()

# Show plot
plt.show()

# Print forecasted values
print("Forecasted Values:")
print(forecast)
