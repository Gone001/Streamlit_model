import pandas as pd
import joblib

model = joblib.load("placement_model.pkl")
# One brand-new student, exactly as a Streamlit form would hand it over.
row = pd.DataFrame([{
    "Specialization": "Cloud Computing", "AttendanceBand": "High",
    "InternshipDone": "No", "Backlogs": 0, "CGPA": 8.4,
    "CommunicationScore": 7.5,
}])
row_encoded = pd.get_dummies(row)
print(row_encoded)
print("columns produced:", list(row_encoded.columns))
print("count:", row_encoded.shape[1])

model.predict(row_encoded)