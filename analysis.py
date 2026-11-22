"""Student Marks Analysis
Analyses student marks using Pandas and Matplotlib.
Run:  python analysis.py
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

SUBJECTS = ["Python", "DBMS", "Data_Structures", "Networking", "Maths"]
PASS_MARK = 40
os.makedirs("images", exist_ok=True)

# 1. Load data
df = pd.read_csv("student_marks.csv")
print("Rows, Columns:", df.shape)
print("\nMissing values:\n", df[SUBJECTS].isnull().sum())

# 2. Clean data: fill missing marks with that subject's average
for sub in SUBJECTS:
    df[sub] = df[sub].fillna(round(df[sub].mean()))

# 3. Calculate total, percentage and grade
df["Total"] = df[SUBJECTS].sum(axis=1)
df["Percentage"] = (df["Total"] / (len(SUBJECTS) * 100) * 100).round(2)


def grade(p):
    if p >= 75:
        return "A"
    if p >= 60:
        return "B"
    if p >= 50:
        return "C"
    if p >= 40:
        return "D"
    return "Fail"


df["Grade"] = df["Percentage"].apply(grade)

# 4. Analysis
print("\n--- Subject-wise average ---")
subject_avg = df[SUBJECTS].mean().round(2)
print(subject_avg)

print("\n--- Top 5 students ---")
print(df.nlargest(5, "Percentage")[["Student_ID", "Name", "Percentage", "Grade"]].to_string(index=False))

print("\n--- Grade distribution ---")
grade_counts = df["Grade"].value_counts().reindex(["A", "B", "C", "D", "Fail"], fill_value=0)
print(grade_counts)

pass_pct = (df[SUBJECTS].ge(PASS_MARK).all(axis=1).mean() * 100).round(1)
print(f"\nStudents passing in ALL subjects: {pass_pct}%")

corr_att = df["Attendance"].corr(df["Percentage"]).round(2)
corr_study = df["Study_Hours"].corr(df["Percentage"]).round(2)
print(f"\nCorrelation: Attendance vs Percentage = {corr_att}")
print(f"Correlation: Study hours vs Percentage = {corr_study}")

# 5. Charts
plt.figure(figsize=(7, 4))
subject_avg.plot(kind="bar", color="#4c72b0")
plt.title("Subject-wise Average Marks")
plt.ylabel("Average marks")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("images/subject_average.png", dpi=120)
plt.close()

plt.figure(figsize=(6, 4))
grade_counts.plot(kind="bar", color="#55a868")
plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of students")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("images/grade_distribution.png", dpi=120)
plt.close()

plt.figure(figsize=(6, 4))
plt.scatter(df["Attendance"], df["Percentage"], alpha=0.7, color="#c44e52")
plt.title("Attendance vs Percentage")
plt.xlabel("Attendance (%)")
plt.ylabel("Percentage")
plt.tight_layout()
plt.savefig("images/attendance_vs_percentage.png", dpi=120)
plt.close()

plt.figure(figsize=(6, 4))
plt.scatter(df["Study_Hours"], df["Percentage"], alpha=0.7, color="#8172b2")
plt.title("Study Hours vs Percentage")
plt.xlabel("Study hours per day")
plt.ylabel("Percentage")
plt.tight_layout()
plt.savefig("images/study_hours_vs_percentage.png", dpi=120)
plt.close()

# 6. Save result
df.to_csv("results.csv", index=False)
print("\nCharts saved in the 'images' folder and results saved to results.csv")
