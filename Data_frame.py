'''
import pandas as pd
import joblib
df=pd.read_csv("student_placement_history.csv")

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
'''

#here is a problem that model has a different sequence and we are giving a different sequence of data to our modle so we need to reindex our data or 
#we have to make the order that aligned to our trained fetaures 

import pandas as pd
import joblib

model = joblib.load("placement_model.pkl")
columns = joblib.load("placement_columns.pkl")

row = pd.DataFrame([{
    "Specialization": "Cloud Computing", "AttendanceBand": "High",
    "InternshipDone": "No", "Backlogs": 0, "CGPA": 8.4,
    "CommunicationScore": 7.5,
}])
row_encoded = pd.get_dummies(row)
row_fixed = row_encoded.reindex(columns=columns, fill_value=False)

print("shape after reindex:", row_fixed.shape)
print("prediction:", "Placed " if model.predict(row_fixed)[0]==1 else "Not placed")