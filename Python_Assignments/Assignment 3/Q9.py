m1 = int(input('Enter marks of subject 1: '))
m2 = int(input('Enter marks of subject 2: '))
m3 = int(input('Enter marks of subject 3: '))
m4 = int(input('Enter marks of subject 4: '))
m5 = int(input('Enter marks of subject 5: '))

total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100

if(percentage >= 75):
    grade = 'First Class with Distinction.'
elif(percentage >= 60):
    grade = 'First Class.'
elif(percentage >= 50 ):
    grade = 'Second Class.'
elif(percentage >= 40):
    grade = 'Third Class.'
else:
    grade = 'Fail.'

print(f'Percentage = {percentage}%')
print(f'Grade = {grade}')