"""CONTROL 6 of 10 -- st.slider: another way to get a number.
New here: contrast with Control 3's st.number_input -- same job (get a
number in a range), a dragging motion instead of typed digits.
"""
import streamlit as st

comm_score = st.slider("Communication score", min_value=0.0,
                        max_value=10.0, value=5.0, step=0.5)
st.write("comm_score:", comm_score)

backlogs_range = st.slider("Backlogs between", 0, 10, (0, 3))
st.write("backlogs_range:", backlogs_range)

# Expected behaviour:
#   A draggable bar starting at 5.0 for comm_score. The second slider
#   has TWO handles (because value=(0, 3) is a tuple, not a single
#   number) -- dragging either end returns a (low, high) pair, useful
#   for "show me students with backlogs between X and Y."
