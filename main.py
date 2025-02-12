import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="SIP Calculator with Compound Interest",
    page_icon="💰",
    layout="wide"
)

# Load custom CSS
with open('.streamlit/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def calculate_sip(principal, monthly_investment, interest_rate, years):
    """
    Calculate SIP returns with compound interest
    """
    monthly_rate = interest_rate / (12 * 100)
    num_payments = years * 12
    
    # Calculate future value
    future_value = principal
    investment_data = []
    running_investment = principal
    
    for month in range(num_payments):
        running_investment += monthly_investment
        future_value = (future_value + monthly_investment) * (1 + monthly_rate)
        
        investment_data.append({
            'Month': month + 1,
            'Investment Amount': running_investment,
            'Future Value': future_value
        })
    
    return future_value, investment_data

def format_currency(amount):
    """Format amount as currency"""
    return f"₹{amount:,.2f}"

# Header
st.markdown('<h1 class="main-header">SIP Calculator with Compound Interest</h1>', unsafe_allow_html=True)

# Create two columns for input and results
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### Investment Details")
    
    # Input fields
    principal = st.number_input(
        "Initial Investment Amount (₹)",
        min_value=0,
        value=10000,
        step=1000,
        help="Enter your initial investment amount"
    )
    
    monthly_sip = st.number_input(
        "Monthly SIP Amount (₹)",
        min_value=0,
        value=5000,
        step=500,
        help="Enter the amount you want to invest monthly"
    )
    
    interest_rate = st.number_input(
        "Expected Annual Return (%)",
        min_value=1.0,
        max_value=30.0,
        value=12.0,
        step=0.5,
        help="Enter your expected annual return rate"
    )
    
    years = st.number_input(
        "Investment Period (Years)",
        min_value=1,
        max_value=40,
        value=10,
        step=1,
        help="Enter the number of years you plan to invest"
    )

    calculate_button = st.button("Calculate Returns")

# Calculate results when button is clicked
if calculate_button:
    future_value, investment_data = calculate_sip(principal, monthly_sip, interest_rate, years)
    df = pd.DataFrame(investment_data)
    
    total_investment = principal + (monthly_sip * years * 12)
    total_interest = future_value - total_investment
    
    with col2:
        st.markdown("### Investment Summary")
        
        # Display metrics in cards
        metrics_col1, metrics_col2 = st.columns(2)
        
        with metrics_col1:
            st.markdown(
                f"""
                <div class="metric-container">
                    <h4>Total Investment</h4>
                    <h2>{format_currency(total_investment)}</h2>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        with metrics_col2:
            st.markdown(
                f"""
                <div class="metric-container">
                    <h4>Future Value</h4>
                    <h2>{format_currency(future_value)}</h2>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        st.markdown(
            f"""
            <div class="results-card">
                <h4>Returns Breakdown</h4>
                <p>Total Interest Earned: {format_currency(total_interest)}</p>
                <p>Initial Investment: {format_currency(principal)}</p>
                <p>Total SIP Investment: {format_currency(monthly_sip * years * 12)}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Create visualization
        st.markdown("### Investment Growth Visualization")
        
        fig = go.Figure()
        
        # Add investment amount line
        fig.add_trace(
            go.Scatter(
                x=df['Month'],
                y=df['Investment Amount'],
                name='Total Investment',
                line=dict(color='#83C5BE', width=2)
            )
        )
        
        # Add future value line
        fig.add_trace(
            go.Scatter(
                x=df['Month'],
                y=df['Future Value'],
                name='Future Value',
                line=dict(color='#006D77', width=2)
            )
        )
        
        # Update layout
        fig.update_layout(
            title='Investment Growth Over Time',
            xaxis_title='Month',
            yaxis_title='Amount (₹)',
            template='plotly_white',
            hovermode='x unified',
            showlegend=True,
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01
            ),
            margin=dict(l=0, r=0, t=30, b=0)
        )
        
        st.plotly_chart(fig, use_container_width=True)

# Add explanatory notes
st.markdown("""
<div class="results-card">
    <h4>About SIP Calculator</h4>
    <p>This calculator helps you estimate the returns on your Systematic Investment Plan (SIP) with compound interest. Here's how it works:</p>
    <ul>
        <li>Initial Investment: The amount you start with</li>
        <li>Monthly SIP: Regular monthly investment amount</li>
        <li>Expected Return: Annual return rate on your investment</li>
        <li>Time Period: Duration of your investment in years</li>
    </ul>
    <p>The calculator considers monthly compounding and regular SIP investments to give you an estimate of your future wealth.</p>
</div>
""", unsafe_allow_html=True)
