import pandas as pd

df = pd.read_csv("/Users/tanish/Downloads/Assignment_3/python-assignment-part4:/students.csv")

# Task 1.1

print("First five rows:")
print(df.head())

# Task 1.2

print("\nShape (rows, columns): ", df.shape)
print("\nData types: ")
print(df.dtypes)

# Task 1.3

print("\nSummary Statistics: ")
print(df.describe())

# Task 1.4

print("\nCount of students passed & failed: ")
print(df['passed'].value_counts())

# Task 1.5

subject_cols = ['math', 'science', 'english', 'history', 'pe']

print("\nAverage scores (Passed students): ")
print(df[df['passed'] == 1][subject_cols].mean())

print("\nAverage scores (Failed students): ")
print(df[df['passed'] == 0][subject_cols].mean())

# Task 1.6

df['average'] = df[subject_cols].mean(axis=1)

top_student = df.loc[df['average'].idxmax()]

print("\nTop student (highest average):")
print(top_student)

# Task 2

import matplotlib.pyplot as plt

subject_cols = ['math', 'science', 'english', 'history', 'pe']
df['avg_score'] = df[subject_cols].mean(axis=1)

# Task 2.1 Bar Chart

avg_scores = df[subject_cols].mean()

plt.figure()
plt.bar(subject_cols, avg_scores)
plt.title("Average score per subject")
plt.xlabel("Subjects")
plt.ylabel("Average Score")
plt.savefig("plot1_bar.png")
plt.show()

# Task 2.2 Histogram

plt.figure()
plt.hist(df['math'], bins = 5)
mean_math = df['math'].mean()
plt.axvline(mean_math, linestyle='dashed', label=f"Mean: {mean_math:.2f}")
plt.title("Distribution of math scores")
plt.xlabel("Math Score")
plt.ylabel("Frequency")
plt.legend()
plt.savefig("plot2_hist.png")
plt.show()

# Task 2.3 Scatter Plot

plt.figure()
pass_df = df[df['passed'] == 1]
fail_df = df[df['passed'] == 0]
plt.scatter(pass_df['study_hours_per_day'], pass_df['avg_score'], label="Pass")
plt.scatter(fail_df['study_hours_per_day'], fail_df['avg_score'], label="Fail")
plt.title("Study Hours vs Average Score")
plt.xlabel("Study Hours per Day")
plt.ylabel("Average Score")
plt.legend()
plt.savefig("plot3_scatter.png")
plt.show()

# Task 2.4 Box Plot

pass_attendance = pass_df['attendance_pct'].tolist()
fail_attendance = fail_df['attendance_pct'].tolist()
plt.figure()
plt.boxplot([pass_attendance, fail_attendance], labels= ['Pass', 'Fail'])
plt.title("Attendance Distribution (Pass vs Fail)")
plt.ylabel("Attendance Percentage")
plt.savefig("plot4_box.png")
plt.show()

# Task 2.5 Line Plot

plt.figure()
plt.plot(df['name'], df['math'], marker = 'o', label = 'Math')
plt.plot(df['name'], df['science'], marker='s', label="Science")
plt.title("Math vs Science Scores per Student")
plt.xlabel("Student Name")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.legend()
plt.savefig("plot5_line.png")
plt.show()

# Task 3

import seaborn as sns

# Task 3.1 Bar Plot

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

sns.barplot(data = df, x = 'passed', y='math', ax=ax1)
ax1.set_title("Average Math Score (Pass vs Fail)")
ax1.set_xlabel("Passed")
ax1.set_ylabel("Math Score")

sns.barplot(data=df, x='passed', y='science', ax=ax2)
ax2.set_title("Average Science Score (Pass vs Fail)")
ax2.set_xlabel("Passed")
ax2.set_ylabel("Science Score")

plt.tight_layout()
plt.savefig("seaborn_barplots.png")
plt.show()

# Task 3.2 Scatter Plot

plt.figure()

sns.scatterplot(data=df, x='attendance_pct', y='avg_score', hue= 'passed')
sns.regplot(data=df[df['passed']==1], x='attendance_pct', y='avg_score', scatter=False, label='Pass')
sns.regplot(data=df[df['passed']==0], x='attendance_pct', y='avg_score', scatter=False, label='Fail')

plt.title("Attendance vs Average Score")
plt.xlabel("Attendance Percentage")
plt.ylabel("Average Score")
plt.legend()

plt.savefig("seaborn_scatter.png")
plt.show()

# Seaborn made plotting easier with the help of groupping and styling.
# Matplotlib offers more granular control for extensive customisation.

# Task 4

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Task 4.1 Prepare Data

feature_cols = ['math', 'science', 'english', 'history', 'pe', 'attendance_pct', 'study_hours_per_day']
X = df[feature_cols]
y = df['passed']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# Task 4.2 Train a Model

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

print("Training Accuracy:", model.score(X_train_scaled, y_train))

# Task 4.3 Evaluate the Model

y_pred = model.predict(X_test_scaled)
print("Test Accuracy:", accuracy_score(y_test, y_pred))

names = df.loc[X_test.index, 'name']

for name, actual, pred in zip(names, y_test, y_pred):
    status = "✅ correct" if actual == pred else "❌ wrong"
    print(f"{name} | Actual: {actual} | Predicted: {pred} | {status}")

# Task 4.4 Feature Importance

coeffs = model.coef_[0]
feat_importance = sorted(zip(feature_cols, coeffs), key=lambda x: abs(x[1]), reverse=True)

for feat, coef in feat_importance:
    print(f"{feat}: {coef:.4f}")

features = [f[0] for f in feat_importance]
values = [f[1] for f in feat_importance]
colors = ['green' if v > 0 else 'red' for v in values]

plt.figure()
plt.barh(features, values, color=colors)
plt.title("Feature Coefficients")
plt.xlabel("Coefficient Value")
plt.ylabel("Features")
plt.savefig("feature_importance.png")
plt.show()

# Task 4.5

new_student = [[75, 70, 68, 65, 80, 82, 3.2]]
new_scaled = scaler.transform(new_student)

pred = model.predict(new_scaled)[0]
prob = model.predict_proba(new_scaled)[0]

print("Prediction:", "Pass" if pred == 1 else "Fail")
print("Probabilities [Fail, Pass]:", prob)
