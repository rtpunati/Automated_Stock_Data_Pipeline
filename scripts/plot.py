import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.model_selection import train_test_split

# Load the data into a pandas DataFrame
data = pd.read_csv('C://Users//ratan//automated_data_pipeline//output//stock_data.csv')
# Rename 'Unnamed: 0' to 'Date' and set it as the index
data.rename(columns={'Unnamed: 0': 'Date'}, inplace=True)
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Check if the data is stationary
# You can perform a Dickey-Fuller test or visualize the data to assess stationarity

# Split the data into training and test sets (e.g., last 30 days for testing)
train, test = train_test_split(data, test_size=0.1, shuffle=False)

# Fit an ARIMA model (you might need to tune the p, d, q parameters)
# For simplicity, we are using (p=5, d=1, q=0), but you may want to optimize this
model = ARIMA(train['Close'], order=(5, 1, 0))
model_fit = model.fit()

# Forecast the next 30 days
forecast_steps = len(test)
forecast = model_fit.forecast(steps=forecast_steps)

# Plot the actual vs forecasted values
plt.figure(figsize=(10, 6))
plt.plot(train.index, train['Close'], label='Training Data')
plt.plot(test.index, test['Close'], label='Actual Data')
plt.plot(test.index, forecast, label='Forecast', color='red')
plt.title('ARIMA Model Forecasting')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()