"""CONTROL 10 of 10 -- st.columns and st.sidebar: arranging widgets,
not creating new ones.
New here: everything used today (title, selectbox, metric, ...) can be
placed side by side instead of stacked, or moved into a side panel.
"""
import streamlit as st

st.title("Layout Demo")

left, right = st.columns(2)
with left:
    st.metric("Placed Students", 381)
with right:
    st.metric("Not Placed", 219)

st.sidebar.title("Filters")
spec_filter = st.sidebar.selectbox("Specialization", ["All", "Data Science", "Networking"])
st.write("Sidebar filter chosen:", spec_filter)

# Expected behaviour:
#   The two metrics appear SIDE BY SIDE, not stacked -- st.columns(2)
#   splits the page into two equal panels. A separate panel appears on
#   the left edge of the browser window with its own title and dropdown
#   -- st.sidebar puts a widget there instead of the main page, useful
#   for filters/settings that shouldn't crowd the main form.
