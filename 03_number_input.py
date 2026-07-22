"""CONTROL 3 of 10 -- st.number_input: collect a number, not text.
New here: min_value/max_value/step guard against bad input BEFORE your
code ever sees it -- the box itself refuses to go out of range.
"""
import streamlit as st

backlogs = st.number_input("Backlogs", min_value=0, max_value=10, step=1)
st.write("backlogs:", backlogs, "| type:", type(backlogs).__name__)

cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
st.write("cgpa:", cgpa, "| type:", type(cgpa).__name__)

# Expected behaviour:
#   Two boxes with up/down arrows. "backlogs" only ever shows whole
#   numbers (type int) because step=1 is a whole number; "cgpa" allows
#   decimals (type float) because step=0.1 is not. Try typing 11 or -1
#   into either box -- it snaps back inside the min/max range.
