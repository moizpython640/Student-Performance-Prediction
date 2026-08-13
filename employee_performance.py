# بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّحِيمِ

import numpy as np
import pandas as pd

employees = ["Ali", "Ahmed", "Sara", "Ayesha", "Usman"]
performance = [92, 76, 88, 65, 81]

df = pd.DataFrame({
    "Employee": employees,
    "Performance Score": performance
})

average = np.mean(performance)
highest = np.max(performance)
lowest = np.min(performance)

rating = []

for score in performance:
    if score >= 90:
        rating.append("Excellent")
    elif score >= 75:
        rating.append("Good")
    elif score >= 60:
        rating.append("Average")
    else:
        rating.append("Needs Improvement")

df["Rating"] = rating

print("=" * 50)
print("EMPLOYEE PERFORMANCE MANAGEMENT SYSTEM")
print("=" * 50)

print(df)

print("\nAverage Score :", average)
print("Highest Score :", highest)
print("Lowest Score  :", lowest)

