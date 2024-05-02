# Mortgage Rates Tracker
## Author: Alfredo Macias
## Contact: www.linkedin.com/in/alfredo-j-macias-952b55123

## Introduction
The Mortgage Rates Tracker is a Python application designed to fetch, analyze, and compare mortgage rates using data from an external API. It's ideal for financial analysts, mortgage brokers, and individuals interested in the housing market trends.

## Key Features
The application includes several features to help you understand and predict mortgage rates:

- **API Integration**: Fetches mortgage rates data from a specified API.
- **Data Validation**: Ensures that the data fetched from the API is in the correct format.
- **Rate Analysis**: Analyzes current and historical rate data to predict today's mortgage rate.
- **Rate Comparison**: Compares current rates with historical averages to provide buying recommendations.

## Getting Started
To run this application, ensure you have Python installed along with the necessary libraries:

### Prerequisites
- Python 3.6 or higher
- Libraries: `requests`, `pandas`, `sklearn`

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/mortgage-rates-tracker.git
   cd mortgage-rates-tracker
   ```
2. **Install Dependencies**:
   ```bash
   pip install requests pandas scikit-learn
   ```

### Running the Application
To execute the program, run the following command in your terminal:
   ```bash
   python mortgage_rates_tracker.py
   ```

## Code Explanation
This section provides a detailed explanation of key components in the source code:

### API Integration
- **Method**: `fetch_rates`
- **Functionality**: Sends a GET request to the specified API URL and returns the JSON response containing mortgage rates.
- **Error Handling**: Includes robust error handling to manage potential request failures or bad responses.

### Data Validation
- **Method**: `validate_data`
- **Purpose**: Checks if the received data contains a 'rates' key, ensuring it conforms to the expected format.
- **Output**: Returns True if valid, otherwise prints an error message and returns False.

### Rate Analysis
- **Method**: `analyze_rates`
- **Components**: 
  - Uses `pandas` to convert the rates data into a DataFrame and computes a timestamp for each date.
  - Fits a linear regression model to predict today's mortgage rate based on historical data.
  - Outputs the predicted rate for today.

### Rate Comparison
- **Method**: `compare_rates`
- **Functionality**: Calculates the historical average of the rates and compares it with the current rate, providing a recommendation based on this comparison.

## Usage Examples
Use this tool to:
- **Monitor Mortgage Trends**: Keep track of how mortgage rates change over time and predict future trends.
- **Financial Planning**: Use the insights from the application to plan financial actions like buying a house or refinancing a mortgage.

## Contributing
Contributions to improve the Mortgage Rates Tracker are welcomed. Please ensure to fork the repository and submit pull requests for any enhancements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or support, please open an issue in this repository, and we will assist you as soon as possible.
