"""CONTROL 7 of 10 -- st.button, and PROOF of the rerun behaviour from
the "Meet Streamlit" briefing.
New here: a random number printed with NO button anywhere near it --
watch it change when you click a totally unrelated button below it.
"""
import random
import streamlit as st

st.write("A random number, printed with no button involved:", random.randint(1, 1000))

if st.button("Click me (does nothing related to the number above)"):
    st.write("You clicked the button.")

# Expected behaviour:
#   The random number is different EVERY time you click the button --
#   even though the button has nothing to do with random numbers. That's
#   because clicking ANY widget reruns the ENTIRE script from the top.
#   This is the single most important thing to see with your own eyes
#   before building a real app.
