import requests
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

API_KEY = 'LD2L8APXXQCXS8SP'  # Replace with your actual Alpha Vantage API key
SYMBOL = 'AAPL'

def fetch_data(symbol, api_key):
    """Fetches historical stock price data from Alpha Vantage API."""
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=full&datatype=csv'
    response = requests.get(url)
    with open(f'{symbol}.csv', 'w') as f:
        f.write(response.text)

def transform_data(df):
    """Transforms the raw stock price data."""
    df['date'] = pd.to_datetime(df['timestamp'])
    df.set_index('date', inplace=True)
    df['daily_return'] = df['close'].pct_change()
    df.dropna(inplace=True)
    return df

def load_data_to_db(df, db_name):
    """Loads the transformed data into a SQLite database."""
    engine = create_engine(f'sqlite:///{db_name}')
    df.to_sql('stocks', engine, if_exists='replace', index=False)

def plot_data(df):
    """Generates a plot for daily closing prices."""
    df['close'].plot(title='Daily Closing Price')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.show()

def main():
    fetch_data(SYMBOL, API_KEY)
    df = pd.read_csv(f'{SYMBOL}.csv')
    df = transform_data(df)
    load_data_to_db(df, 'stock_data.db')
    plot_data(df)

if __name__ == "__main__":
    main()
