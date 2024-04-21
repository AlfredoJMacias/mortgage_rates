import requests
import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime

class MortgageRatesTracker:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_rates(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching mortgage rates: {e}")
            return None

    def validate_data(self, data):
        if "rates" in data:
            return True
        else:
            print("Invalid data format received from API.")
            return False

    def analyze_rates(self, data):
        df = pd.DataFrame(data['rates'])
        df['date'] = pd.to_datetime(df['date'])
        today = datetime.now().strftime('%Y-%m-%d')

        # Simple Prediction Model
        model = LinearRegression()
        df['timestamp'] = df['date'].map(pd.Timestamp.timestamp)
        X = df[['timestamp']]  # Feature
        y = df['rate']  # Target

        model.fit(X, y)
        prediction = model.predict([[pd.Timestamp(today).timestamp()]])
        print(f"Predicted mortgage rate for today ({today}): {prediction[0]:.2f}%")

    def compare_rates(self, current_rate, historical_rates):
        historical_avg = historical_rates.mean()
        print(f"Current rate: {current_rate}%")
        print(f"Average historical rate: {historical_avg:.2f}%")
        if current_rate < historical_avg:
            print("Good time to consider a mortgage, as current rates are below the historical average.")
        else:
            print("Current rates are above the historical average. Caution advised.")

if __name__ == "__main__":
    tracker = MortgageRatesTracker("https://api.example.com/mortgage_rates")
    rates_data = tracker.fetch_rates()

    if rates_data and tracker.validate_data(rates_data):
        tracker.analyze_rates(rates_data)
        current_rate = rates_data['rates'][-1]['rate']
        historical_rates = pd.Series([rate['rate'] for rate in rates_data['rates']])
        tracker.compare_rates(current_rate, historical_rates)
