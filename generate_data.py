"""Generate a sample student marks dataset (student_marks.csv).

You can skip this file if you use your own dataset (e.g. from Kaggle).
"""
import numpy as np
import pandas as pd

np.random.seed(42)
N = 100

first = ["Aarav", "Riya", "Neha", "Rahul", "Priya", "Karan", "Sneha", "Aman", "Pooja", "Vikas",
         "Isha", "Rohan", "Anjali", "Mohit", "Kavya", "Nikhil", "Simran", "Harsh", "Divya", "Yash"]
last = ["Sharma", "Patel", "Singh", "Verma", "Shah", "Mehta", "Gupta", "Joshi", "Yadav", "Kushwaha"]

names = [f"{np.random.choice(first)} {np.random.choice(last)}" for _ in range(N)]
attendance = np.clip(np.random.normal(78, 12, N), 40, 100).round(1)
study_hours = np.clip(np.random.normal(3, 1.2, N), 0.5, 7).round(1)

# Marks depend a little on attendance and study hours (so the analysis shows real patterns)
base = 48 + (attendance - 60) * 0.4 + study_hours * 4.5

def marks(shift=0, spread=10):
    m = base + shift + np.random.normal(0, spread, N)
    return np.clip(m, 10, 100).round().astype(int)

df = pd.DataFrame({
    "Student_ID": [f"MCA{1000 + i}" for i in range(N)],
    "Name": names,
    "Attendance": attendance,
    "Study_Hours": study_hours,
    "Python": marks(5),
    "DBMS": marks(0),
    "Data_Structures": marks(-5),
    "Networking": marks(-2),
    "Maths": marks(-8),
})

# Add a few missing values on purpose, to practise data cleaning
for col in ["Python", "DBMS", "Maths"]:
    df.loc[np.random.choice(N, 2, replace=False), col] = np.nan

df.to_csv("student_marks.csv", index=False)
print("student_marks.csv created with", len(df), "rows")
