import pandas as pd

df=pd.read_csv('Exceltask.csv')
print('='*50)
age=df[df['AGE']>20]
print(age)
print('='*50)

print('='*50)
print(df.head())
print('='*50)

print('='*50)
cgpa=df[df['CGPA']>=3.5]
print(cgpa)
print('='*50)

print('='*50)
result2=df[(df['CGPA']>3.2) & (df['AGE']>20)]
print(result2)
print('='*50)

print('='*50)
result1=df[(df['CGPA']>3.7) | (df['AGE']<20)]
print(result1)
print('='*50)

print('='*50)
des=df.sort_values('AGE')
print(des)
print('='*50)

print('='*50)
des=df.sort_values('AGE', ascending=False)
print(des)
print('='*50)

print('='*50)
print(df[["NAME","CGPA"]])
print('='*50)

print('='*50)
totalstudents=len(df)
print(totalstudents)
print('='*50)

print('='*50)
avg_age=df['AGE'].mean()
print(avg_age)
print('='*50)

print('='*50)
avg_cgpa=df['CGPA'].mean()
print(avg_cgpa)
print('='*50)

print('='*50)
avg_age=df['AGE'].max()
print(avg_age)
print('='*50)

print('='*50)
min_age=df['AGE'].min()
print(min_age)
print('='*50)

print('='*50)
higest_CGPA=df['CGPA'].max()
lowest_age=df['AGE'].min()
result=df[(df['CGPA']==higest_CGPA) & (df['AGE']==lowest_age)]
if not result.empty:
    print(result)
else:
    print("No student found with Highest CGPA and Lowest Age.")
print('='*50)