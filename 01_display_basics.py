"""CONTROL 1 of 10 -- The "display" family: things that show text, but
never collect anything back from the user.
New here: st.title, st.header, st.subheader, st.caption, st.write,
st.markdown -- six ways to put text on the page, each a different size
or job.
"""
import streamlit as st

st.title("This is st.title -- the biggest, one per page")
st.header("This is st.header -- for a major section")
st.subheader("This is st.subheader -- for a smaller section")
st.write("This is st.write -- the all-purpose one. Give it text, a "
         "number, a DataFrame, even a chart -- it displays whatever "
         "you hand it.")
st.caption("This is st.caption -- small, grey, for a footnote or hint.")
st.markdown("This is **st.markdown** -- like st.write, but always reads "
            "its text as Markdown, so `**bold**` and `*italic*` work.")

# Expected behaviour (in the browser):
#   Six lines of text stacked top to bottom, each visibly a different
#   size/weight -- title biggest, caption smallest and grey. Run with:
#   streamlit run 01_display_basics.py
