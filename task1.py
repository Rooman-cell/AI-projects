# Program to take user's name and age, calculate future age, and check eligibility

# Step 1: Take user's name as input
name = input("Enter your name: ")

# Step 2: Take user's age as input
age = int(input("Enter your age: "))

# Step 3: Calculate age after 10 years
future_age = age + 10

# Step 4: Check eligibility for internship
if age >= 18:
    eligibility = "Eligible for Internship"
else:
    eligibility = "Keep Learning"

# Display the results
print("\n--- Results ---")
print("Name:", name)
print("Current Age:", age)
print("Age after 10 years:", future_age)
print("Status:", eligibility)