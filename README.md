
# Automated Data Pipeline for Stock Market Forecasting

## Overview
This project implements an automated data pipeline that fetches stock market data, processes it, and generates forecasts using an ARIMA model. The pipeline is scheduled to run daily using Windows Task Scheduler. The data is fetched from the Alpha Vantage API, transformed into a structured format, and forecasted using historical stock data.

## Project Structure

```markdown
automated_data_pipeline/
│
├── data/
│   └── stock_data.csv           # CSV containing the processed stock data
│    
├── scripts/
│   ├── extract_data.py            # Script to fetch and preprocess stock data
│   └── plot.py                    # Script to plot historical and forecasted data
│   └── runpipeline.bat                # Batch file to run the pipeline 
│
├── output/                        # Folder to store the output CSV files
│   └── stock_data.csv             # CSV containing the processed stock data
│
└── README.md                      # This file

```
```

## Features

- **Data Extraction**: Fetches daily stock data from Alpha Vantage API for a specified stock symbol (e.g., IBM).
- **Data Transformation**: Converts the raw data into a clean, structured Pandas DataFrame, fills missing values, and adds new features like `Daily Range`.
- **ARIMA Forecasting**: Uses ARIMA to forecast future stock prices based on historical data.
- **Plotting**: Generates plots to visualize the historical stock prices and forecasted values.
- **Task Scheduling**: The pipeline is scheduled to run daily using Windows Task Scheduler.

## Prerequisites

- **Python** (Anaconda recommended)
- **Required Python Libraries**:  
  - `requests` (for making HTTP requests to Alpha Vantage API)
  - `pandas` (for data manipulation and analysis)
  - `matplotlib` (for plotting data)
  - `statsmodels` (for ARIMA model implementation)

To install the required libraries, run:

```bash
pip install requests pandas matplotlib statsmodels
```

## Setup

### 1. Get Alpha Vantage API Key
- Sign up for a free API key on [Alpha Vantage](https://www.alphavantage.co/support/#api-key).
- Replace `YOUR_API_KEY` in the `extract_data.py` script with your actual API key.

### 2. Configure the Batch File
- Ensure that the batch file `runpipeline.bat` points to the correct Python executable and script paths. By default, it uses the Anaconda Python path:
  ```batch
  C:\Users\*****\anaconda3\python.exe C:\Users\*****\automated_data_pipeline\scripts\extract_data.py
  ```
  Adjust these paths if necessary.

### 3. Schedule the Task Using Windows Task Scheduler
- The batch file `runpipeline.bat` can be scheduled to run daily using Windows Task Scheduler:
  - Open Task Scheduler and create a new task to run the batch file at a set time each day.
  
## How It Works

1. **Data Extraction**:  
   The `extract_data.py` script fetches stock data for a given symbol (e.g., IBM) from the Alpha Vantage API.

   The raw data is processed into a clean format, filling missing values and adding a new feature, `Daily Range`, which calculates the difference between the high and low prices for each day.

3. **ARIMA Forecasting & Visualization**:  
   The `plot.py` script uses the historical data to train an ARIMA model and forecast the next 5 days of stock prices and generates a plot to compare historical stock prices and the forecasted values.

5. **Task Scheduling**:  
   The batch file `runpipeline.bat` is scheduled to run daily using Windows Task Scheduler to automate the pipeline execution.

## Running the Pipeline Manually

To manually run the pipeline:

1. Open a command prompt.
2. Navigate to the folder containing the batch file.
3. Execute the batch file:
   ```bash
   runpipeline.bat
   ```

## Output

- The processed stock data is saved as `stock_data.csv` in the `output/` folder.

## Troubleshooting

- **API Key Issues**: If you encounter errors related to the API key, ensure you have replaced `YOUR_API_KEY` with your valid key in the `extract_data.py` script.
- **Missing Data**: If the pipeline fails due to missing data, check the console output for error details.
- **Task Scheduler Errors**: Ensure the paths in the batch file are correct and that the Python executable is available in your system's PATH.

