"""CONTROL 9 of 10 -- st.metric and simple built-in charts.
New here: st.metric highlights ONE number big and bold, optionally with
a delta arrow; st.bar_chart/st.line_chart plot a DataFrame with zero
matplotlib code.
"""
import pandas as pd
import streamlit as st

st.metric("Estimated Package (LPA)", 6.59, delta=0.6)
st.metric("Backlogs", 0, delta=-1, delta_color="inverse")

chart_data = pd.DataFrame(
    {"Package (LPA)": [6.59, 5.99]}, index=["This student", "Dataset average"])
st.bar_chart(chart_data)

trend = pd.DataFrame({"AvgPackageLPA": [4.5, 4.9, 5.5, 6.5, 6.7]})
st.line_chart(trend)

# Expected behaviour:
#   Two big number tiles -- the first with a GREEN up-arrow "+0.6" (a
#   rise is good here), the second with a GREEN down-arrow because
#   delta_color="inverse" flips the usual red/green meaning (fewer
#   backlogs is good, so a drop shows green, not red). Below them, a
#   2-bar chart, then a 5-point line chart -- both drawn from nothing
#   but a DataFrame, no plt.plot() anywhere.
