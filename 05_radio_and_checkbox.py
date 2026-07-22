"""CONTROL 5 of 10 -- st.radio and st.checkbox: two other ways to choose.
New here: same JOB as st.selectbox (collect a choice), different FEEL --
radio shows every option at once, checkbox is a plain yes/no switch.
"""
import streamlit as st

internship = st.radio("Internship done?", ["Yes", "No"])
st.write("internship:", internship)

show_details = st.checkbox("Show extra details")
st.write("show_details:", show_details, "| type:", type(show_details).__name__)
if show_details:
    st.write("Here are the extra details you asked to see.")

# Expected behaviour:
#   st.radio shows both "Yes"/"No" as clickable dots, all options visible
#   at once -- no dropdown to open. st.checkbox is a single tickbox;
#   show_details is always exactly True or False, never anything else.
#   Ticking it reveals the extra sentence -- unticking it hides it again.
