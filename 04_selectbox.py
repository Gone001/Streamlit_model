"""CONTROL 4 of 10 -- st.selectbox: pick exactly one option from a list.
New here: this is how a text COLUMN (like Specialization) becomes a
form field -- the list you pass in should be the exact categories the
model was trained on, spelled exactly the same way.
"""
import streamlit as st

specialization = st.selectbox("Specialization",
    ["Data Science", "Cybersecurity", "Cloud Computing",
     "Web Development", "Networking"])
st.write("chosen:", specialization)

attendance = st.selectbox("Attendance", ["High", "Medium", "Low"], index=1)
st.write("chosen:", attendance)

# Expected behaviour:
#   Two dropdowns. The first defaults to "Data Science" (the first item
#   in the list, since no index= was given). The second defaults to
#   "Medium" because index=1 points at the list's 2nd item (index 0 is
#   "High"). Changing either updates its "chosen:" line immediately.
