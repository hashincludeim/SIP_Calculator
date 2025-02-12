import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="SIP Calculator with Investment Comparison",
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
st.markdown('<h1 class="main-header">SIP Calculator with Investment Comparison</h1>', unsafe_allow_html=True)

# Create tabs for different scenarios
tab1, tab2 = st.tabs(["Scenario 1", "Scenario 2"])

# Initialize session state for both scenarios
if 'scenario1' not in st.session_state:
    st.session_state.scenario1 = {
        'principal': 10000,
        'monthly_sip': 5000,
        'interest_rate': 12.0,
        'years': 10
    }

if 'scenario2' not in st.session_state:
    st.session_state.scenario2 = {
        'principal': 10000,
        'monthly_sip': 7500,
        'interest_rate': 15.0,
        'years': 10
    }

# Input fields for Scenario 1
with tab1:
    st.markdown("### Investment Details - Scenario 1")

    st.session_state.scenario1['principal'] = st.number_input(
        "Initial Investment Amount (₹)",
        min_value=0,
        value=st.session_state.scenario1['principal'],
        step=1000,
        help="Enter your initial investment amount",
        key='s1_principal'
    )

    st.session_state.scenario1['monthly_sip'] = st.number_input(
        "Monthly SIP Amount (₹)",
        min_value=0,
        value=st.session_state.scenario1['monthly_sip'],
        step=500,
        help="Enter the amount you want to invest monthly",
        key='s1_monthly_sip'
    )

    st.session_state.scenario1['interest_rate'] = st.number_input(
        "Expected Annual Return (%)",
        min_value=1.0,
        max_value=30.0,
        value=st.session_state.scenario1['interest_rate'],
        step=0.5,
        help="Enter your expected annual return rate",
        key='s1_interest_rate'
    )

    st.session_state.scenario1['years'] = st.number_input(
        "Investment Period (Years)",
        min_value=1,
        max_value=40,
        value=st.session_state.scenario1['years'],
        step=1,
        help="Enter the number of years you plan to invest",
        key='s1_years'
    )

# Input fields for Scenario 2
with tab2:
    st.markdown("### Investment Details - Scenario 2")

    st.session_state.scenario2['principal'] = st.number_input(
        "Initial Investment Amount (₹)",
        min_value=0,
        value=st.session_state.scenario2['principal'],
        step=1000,
        help="Enter your initial investment amount",
        key='s2_principal'
    )

    st.session_state.scenario2['monthly_sip'] = st.number_input(
        "Monthly SIP Amount (₹)",
        min_value=0,
        value=st.session_state.scenario2['monthly_sip'],
        step=500,
        help="Enter the amount you want to invest monthly",
        key='s2_monthly_sip'
    )

    st.session_state.scenario2['interest_rate'] = st.number_input(
        "Expected Annual Return (%)",
        min_value=1.0,
        max_value=30.0,
        value=st.session_state.scenario2['interest_rate'],
        step=0.5,
        help="Enter your expected annual return rate",
        key='s2_interest_rate'
    )

    st.session_state.scenario2['years'] = st.number_input(
        "Investment Period (Years)",
        min_value=1,
        max_value=40,
        value=st.session_state.scenario2['years'],
        step=1,
        help="Enter the number of years you plan to invest",
        key='s2_years'
    )

calculate_button = st.button("Compare Investments")

# Calculate results when button is clicked
if calculate_button:
    # Calculate for both scenarios
    future_value1, investment_data1 = calculate_sip(
        st.session_state.scenario1['principal'],
        st.session_state.scenario1['monthly_sip'],
        st.session_state.scenario1['interest_rate'],
        st.session_state.scenario1['years']
    )

    future_value2, investment_data2 = calculate_sip(
        st.session_state.scenario2['principal'],
        st.session_state.scenario2['monthly_sip'],
        st.session_state.scenario2['interest_rate'],
        st.session_state.scenario2['years']
    )

    df1 = pd.DataFrame(investment_data1)
    df2 = pd.DataFrame(investment_data2)

    total_investment1 = st.session_state.scenario1['principal'] + (st.session_state.scenario1['monthly_sip'] * st.session_state.scenario1['years'] * 12)
    total_investment2 = st.session_state.scenario2['principal'] + (st.session_state.scenario2['monthly_sip'] * st.session_state.scenario2['years'] * 12)

    total_interest1 = future_value1 - total_investment1
    total_interest2 = future_value2 - total_investment2

    # Display comparison metrics
    st.markdown("### Investment Comparison")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Scenario 1")
        st.markdown(
            f"""
            <div class="metric-container">
                <h4>Total Investment</h4>
                <h2>{format_currency(total_investment1)}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            f"""
            <div class="results-card">
                <h4>Returns Breakdown</h4>
                <p>Total Interest Earned: {format_currency(total_interest1)}</p>
                <p>Initial Investment: {format_currency(st.session_state.scenario1['principal'])}</p>
                <p>Total SIP Investment: {format_currency(st.session_state.scenario1['monthly_sip'] * st.session_state.scenario1['years'] * 12)}</p>
                <p>Future Value: {format_currency(future_value1)}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown("#### Scenario 2")
        st.markdown(
            f"""
            <div class="metric-container">
                <h4>Total Investment</h4>
                <h2>{format_currency(total_investment2)}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            f"""
            <div class="results-card">
                <h4>Returns Breakdown</h4>
                <p>Total Interest Earned: {format_currency(total_interest2)}</p>
                <p>Initial Investment: {format_currency(st.session_state.scenario2['principal'])}</p>
                <p>Total SIP Investment: {format_currency(st.session_state.scenario2['monthly_sip'] * st.session_state.scenario2['years'] * 12)}</p>
                <p>Future Value: {format_currency(future_value2)}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Comparison Analysis
    difference = future_value2 - future_value1
    percentage_difference = (difference / future_value1) * 100

    st.markdown(
        f"""
        <div class="results-card">
            <h4>Scenario Comparison</h4>
            <p>Difference in Future Value: {format_currency(abs(difference))} ({abs(percentage_difference):.2f}% {'higher' if difference > 0 else 'lower'} in Scenario 2)</p>
            <p>Additional Investment Required: {format_currency(abs(total_investment2 - total_investment1))}</p>
            <p>Difference in Returns: {format_currency(abs(total_interest2 - total_interest1))}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Create visualization
    st.markdown("### Investment Growth Comparison")

    fig = go.Figure()

    # Add investment amount lines
    fig.add_trace(
        go.Scatter(
            x=df1['Month'],
            y=df1['Investment Amount'],
            name='Investment (Scenario 1)',
            line=dict(color='#83C5BE', width=2, dash='dot')
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df2['Month'],
            y=df2['Investment Amount'],
            name='Investment (Scenario 2)',
            line=dict(color='#EE6C4D', width=2, dash='dot')
        )
    )

    # Add future value lines
    fig.add_trace(
        go.Scatter(
            x=df1['Month'],
            y=df1['Future Value'],
            name='Returns (Scenario 1)',
            line=dict(color='#006D77', width=2)
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df2['Month'],
            y=df2['Future Value'],
            name='Returns (Scenario 2)',
            line=dict(color='#E29578', width=2)
        )
    )

    # Update layout
    fig.update_layout(
        title='Investment Growth Comparison',
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
    <h4>About Investment Comparison</h4>
    <p>This calculator helps you compare two different investment scenarios side by side. You can analyze:</p>
    <ul>
        <li>Different monthly SIP amounts</li>
        <li>Various expected return rates</li>
        <li>Different investment horizons</li>
        <li>Impact of changing initial investments</li>
    </ul>
    <p>Use this tool to make informed decisions about your investment strategy by comparing different scenarios.</p>
</div>
""", unsafe_allow_html=True)