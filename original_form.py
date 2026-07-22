import pandas as pd
import joblib
import streamlit as st

st.title("Placement Outlook")

clf = joblib.load("placement_model.pkl")
clf_columns = joblib.load("placement_columns.pkl")
reg = joblib.load("package_model.pkl")
reg_columns = joblib.load("package_columns.pkl")

specialization = st.selectbox("Specialization",
    ["Data Science", "Cybersecurity", "Cloud Computing",
     "Web Development", "Networking"])
attendance = st.selectbox("Attendance", ["High", "Medium", "Low"])
internship = st.selectbox("Internship done?", ["Yes", "No"])
backlogs = st.number_input("Backlogs", min_value=0, max_value=10, step=1)
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
comm = st.number_input("Communication score",
                        min_value=0.0, max_value=10.0)

if st.button("Predict"):
    row = pd.DataFrame([{
        "Specialization": specialization, "AttendanceBand": attendance,
        "InternshipDone": internship, "Backlogs": backlogs,
        "CGPA": cgpa, "CommunicationScore": comm,
    }])
    row_encoded = pd.get_dummies(row)

    placed = clf.predict(row_encoded.reindex(columns=clf_columns, fill_value=False))[0]
    package = reg.predict(row_encoded.reindex(columns=reg_columns, fill_value=False))[0]

    st.write("Will Placed" if  placed ==1 else "Will Not Placed")
    st.write("predicted package:", round(package, 2))