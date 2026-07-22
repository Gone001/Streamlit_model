import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("student_package_prediction (1).csv")
X = pd.get_dummies(df.drop(columns=["StudentID", "PackageLPA"]))
y = df["PackageLPA"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
print("MAE:", mean_absolute_error(y_test, model.predict(X_test)))

joblib.dump(model, "package_model.pkl")
joblib.dump(list(X.columns), "package_columns.pkl")
print("saved package_model.pkl and package_columns.pkl")