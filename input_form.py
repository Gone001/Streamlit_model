import streamlit as st

st.title("Placement Outlook")

specialization = st.selectbox("Specialization",
    ["Data Science", "Cybersecurity", "Cloud Computing",
     "Web Development", "Networking"])
attendance = st.selectbox("Attendance", ["High", "Medium", "Low"])
internship = st.selectbox("Internship done?", ["Yes", "No"])
backlogs = st.number_input("Backlogs", min_value=0, max_value=10, step=1)
cgpa = st.slider("CGPA", min_value=0.0,max_value=10.0, value=5.0, step=0.1)
comm = st.slider("Communication score", min_value=0.0,max_value=10.0, value=5.0, step=0.5)

st.write("You entered:", specialization, attendance, internship,
         backlogs, cgpa, comm)
