import streamlit as st
from utils.stats_helpers import calculate_power, calculate_sample_size
import matplotlib.pyplot as plt

st.title("🧪 A/B Test Power Simulator")

baseline = st.slider("Baseline Conversion Rate (%)", 1, 50, 10) / 100
lift = st.slider("Expected Lift (%)", 1, 50, 10) / 100
alpha = st.slider("Significance Level", 0.01, 0.1, 0.05)
power = st.slider("Desired Power", 0.5, 0.99, 0.8)

if st.button("Calculate Sample Size"):
    sample_size = calculate_sample_size(baseline, lift, power, alpha)
    st.success(f"Required Sample Size per Group: {int(sample_size)}")
