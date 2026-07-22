import streamlit as st
st.title("Placement Outlook")
name=st.text_input("Student_name")
if st.button("Say hello"):
    st.write(f"hello : {name}")