"""CONTROL 8 of 10 -- The coloured "feedback" family.
New here: st.success, st.error, st.warning, st.info -- four coloured
message boxes, each with a conventional meaning worth respecting.
"""
import streamlit as st

st.success("Placed -- green means a positive/expected result.")
st.error("Not Placed -- red means a negative result, NOT a code error.")
st.warning("Borderline case -- yellow means proceed with caution.")
st.info("This app is a planning tool, not a verdict. -- blue means neutral info.")

# Expected behaviour:
#   Four coloured boxes stacked top to bottom: green, red, amber/yellow,
#   blue. Note st.error's red does NOT mean the code crashed -- it's
#   just a colour convention, easy to mix up with a real Python error.
