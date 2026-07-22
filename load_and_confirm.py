import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

clf = joblib.load("placement_model.pkl")
reg = joblib.load("package_model.pkl")

# rebuild the same test sets to check against (this script never fit anything)
df8 = pd.read_csv("student_placement_history.csv")
X8 = pd.get_dummies(df8.drop(columns=["StudentID", "Placed"]))
y8 = df8["Placed"]
_, X8_test, _, y8_test = train_test_split(X8, y8, test_size=0.2, random_state=42)

df9 = pd.read_csv("student_package_prediction.csv")
X9 = pd.get_dummies(df9.drop(columns=["StudentID", "PackageLPA"]))
y9 = df9["PackageLPA"]
_, X9_test, _, y9_test = train_test_split(X9, y9, test_size=0.2, random_state=42)

print("reloaded classifier accuracy:", clf.score(X8_test, y8_test))
print("reloaded regressor MAE:", mean_absolute_error(y9_test, reg.predict(X9_test)))