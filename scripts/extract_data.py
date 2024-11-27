import os
import requests
import pandas as pd
import json

# Function to fetch data from Alpha Vantage API
def fetch_data():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSI&apikey=YOUR_API_KEY'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "Time Series (Daily)" in data:
            return data["Time Series (Daily)"]
        elif "Note" in data:
            print("Note:", data["Note"])
        elif "Information" in data:
            print("Information:", data["Information"])
        else:
            print("Unexpected response format.")
    else:
        print(f"Failed to fetch data. HTTP {response.status_code}.")
    return None

# Function to transform raw data into a Pandas DataFrame
def transform_data(raw_data):
    if not raw_data:
        print("No raw data to process.")
        return None
    
    try:
        df = pd.DataFrame.from_dict(raw_data, orient="index")
        df.columns = ["Open", "High", "Low", "Close", "Volume"]
        df.index = pd.to_datetime(df.index)
        
        # Convert columns to numeric values
        for col in ["Open", "High", "Low", "Close", "Volume"]:
            df[col] = pd.to_numeric(df[col])
        
        # Add Daily Range as the difference between High and Low
        df['Daily Range'] = df['High'] - df['Low']
        
        df.sort_index(inplace=True)
        return df
    except Exception as e:
        print(f"Error during data transformation: {e}")
        return None

# Function to save the DataFrame as a CSV file in the 'output' folder
def load_data_to_csv(df, filename="MSI_stock_data.csv"):
    if df is None:
        print("No data to save.")
        return
    
    output_folder = "output"  # Specify the output folder
    os.makedirs(output_folder, exist_ok=True)  # Create folder if it doesn't exist
    file_path = os.path.join(output_folder, filename)  # Combine folder and filename
    df.to_csv(file_path)
    print(f"Data saved successfully to {file_path}")

# Main script to execute the ETL pipeline
if __name__ == "__main__":
    raw_data = fetch_data()
    if raw_data:
        transformed_data = transform_data(raw_data)
        if transformed_data is not None:
            load_data_to_csv(transformed_data)


