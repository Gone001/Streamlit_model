"""CONTROL 2 of 10 -- st.text_input: collect a short line of text.
New here: a widget that RETURNS a value -- whatever the user typed is
sitting in the `name` variable on every single rerun, automatically.
"""
import streamlit as st

name = st.text_input("What's your name?")
st.write("You typed:", name)

favourite = st.text_input("Favourite subject", value="Machine Learning")
st.write("Favourite subject:", favourite)

# Expected behaviour:
#   An empty box; "You typed:" shows nothing until you type something,
#   then updates on every keystroke -- no button needed. The second box
#   starts pre-filled with "Machine Learning" (the `value=` default).
