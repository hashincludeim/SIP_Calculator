# SIP Calculator and Investment Comparison Tool

This project is a web application built using Streamlit that provides tools for calculating Systematic Investment Plan (SIP) returns and comparing different investment scenarios. The application allows users to input their investment details and visualize the growth of their investments over time.

## Features

- **SIP Calculator**: Calculate the future value of your investments with monthly SIP contributions and compound interest.
- **Investment Comparison**: Compare two different investment scenarios side by side to make informed decisions.
- **Interactive Visualizations**: Visualize the growth of your investments over time using Plotly charts.
- **Customizable Inputs**: Adjust initial investment, monthly SIP amount, expected annual return, and investment period.

## Installation

To run this application locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**:
   Ensure you have Python 3.11 or higher installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Start the Streamlit server:
   ```bash
   streamlit run main.py
   ```

## Configuration

The application is configured to run on port 5000. You can modify the configuration in the `.streamlit/config.toml` file if needed.

## Usage

### SIP Calculator

1. Navigate to the SIP Calculator page.
2. Enter your initial investment amount, monthly SIP amount, expected annual return, and investment period.
3. Click "Calculate Returns" to view the future value of your investment and a detailed breakdown of your returns.

### Investment Comparison

1. Navigate to the Investment Comparison page.
2. Enter the investment details for two different scenarios.
3. Click "Compare Investments" to view a side-by-side comparison of the two scenarios, including total investment, future value, and returns breakdown.

## Code Structure

- **main.py**: Contains the main logic for the SIP Calculator.
  - SIP calculation function: `calculate_sip` (startLine: 18, endLine: 39)
  - Currency formatting function: `format_currency` (startLine: 41, endLine: 43)
  - User interface setup and visualization (startLine: 45, endLine: 195)

- **pages/01_Investment_Comparison.py**: Contains the logic for the Investment Comparison tool.
  - SIP calculation function: `calculate_sip` (startLine: 18, endLine: 39)
  - Currency formatting function: `format_currency` (startLine: 41, endLine: 43)
  - User interface setup and visualization (startLine: 45, endLine: 323)

- **.streamlit/style.css**: Custom CSS for styling the application.

## Dependencies

The project uses the following Python packages:
- numpy
- pandas
- plotly
- streamlit

These dependencies are specified in the `pyproject.toml` file (startLine: 6, endLine: 12).

## Deployment

The application is configured for deployment using Replit. The deployment settings are specified in the `.replit` and `replit.nix` files.


