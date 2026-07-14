# Step 1: Import pandas
import pandas as pd

# Step 2: CSV load karo
# Make sure to replace 'Exceltask.csv' with the correct path to your CSV file
df = pd.read_csv('Exceltask.csv')

# Step 3: Print First 5 rows and Last 5 rows
print("="*50)
print("FIRST 5 ROWS:")
print("="*50)
print(df.head(5))
print("\n")

print("="*50)
print("LAST 5 ROWS:")
print("="*50)
print(df.tail(5))
print("\n")
print("High CGPA 3.5 above")
high_cgpa = df[df["CGPA"] > 3.5]
print(high_cgpa)

# Step 4: Print Number of rows and Number of columns
print("="*50)
print("DATASET INFORMATION:")
print("="*50)
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")
print("\n")

# Step 5: Print Column names
print("="*50)
print("COLUMN NAMES:")
print("="*50)
for i, col in enumerate(df.columns, 1):
    print(f"{i}. {col}")
print("\n")

# Step 6: Print Average CGPA
print("="*50)
print("AVERAGE CGPA:")
print("="*50)
# Assuming the column name is 'CGPA' - change if different
average_cgpa = df['CGPA'].mean()
print(f"Average CGPA: {average_cgpa:.2f}")
print("\n")

# Step 7: Highest CGPA
print("="*50)
print("HIGHEST CGPA:")
print("="*50)
highest_cgpa = df['CGPA'].max()
# Get the row(s) with highest CGPA
highest_cgpa_rows = df[df['CGPA'] == highest_cgpa]
print(f"Highest CGPA: {highest_cgpa}")
print("\nDetails of student(s) with highest CGPA:")
print(highest_cgpa_rows)
print("\n")

# Step 8: Lowest CGPA with code
print("="*50)
print("LOWEST CGPA:")
print("="*50)
lowest_cgpa = df['CGPA'].min()
# Get the row(s) with lowest CGPA
lowest_cgpa_rows = df[df['CGPA'] == lowest_cgpa]
print(f"Lowest CGPA: {lowest_cgpa}")
print("\nDetails of student(s) with lowest CGPA:")
print(lowest_cgpa_rows)


