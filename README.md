# Stock Price Data Pipeline

This project demonstrates the creation of a data pipeline that fetches historical stock price data from the Alpha Vantage API, processes the data to calculate daily returns, stores it in a SQLite database, and generates visualizations of the stock's closing prices. The project showcases skills in API integration, financial data analysis, and database management using Python and SQL.

## Project Structure

stock_price_pipeline/
├── main.py
├── README.md
├── requirements.txt
└── venv/


## Features

- **API Integration:** Fetches historical stock price data using the Alpha Vantage API.
- **Data Processing:** Transforms raw data to calculate daily returns and cleans it.
- **Database Management:** Stores the processed data in a SQLite database.
- **Data Visualization:** Generates a plot for daily closing prices.

## Setup Instructions

### Prerequisites

- Python 3.x
- A valid Alpha Vantage API key

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/stock_price_pipeline.git
    cd stock_price_pipeline
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # For Windows
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Add your Alpha Vantage API key:**
   - Open `main.py` in a text editor.
   - Replace `'your_alpha_vantage_api_key'` with your actual API key:
     ```python
     API_KEY = 'your_actual_alpha_vantage_api_key'  # Replace with your actual Alpha Vantage API key
     ```

### Running the Project

1. **Run the script:**
    ```bash
    python main.py
    ```

2. **Expected Output:**
    - A CSV file named `AAPL.csv` containing the fetched stock data.
    - A SQLite database file named `stock_data.db` with the processed data.
    - A plot of the daily closing prices displayed.

## Project Details

### Extract

- The `fetch_data` function fetches historical stock price data from Alpha Vantage API and saves it as a CSV file.

### Transform

- The `transform_data` function processes the raw data to calculate daily returns, sets the date as the index, and removes missing values.

### Load

- The `load_data_to_db` function loads the transformed data into a SQLite database.

### Visualize

- The `plot_data` function generates a plot for daily closing prices.

## Dependencies

- pandas
- requests
- sqlalchemy
- matplotlib

These dependencies are listed in `requirements.txt`.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Alpha Vantage](https://www.alphavantage.co/) for providing the stock price data API.
- [Python](https://www.python.org/) for providing an excellent programming language.
