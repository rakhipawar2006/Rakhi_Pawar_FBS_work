n = int(input('Enter the no. of students: '))
tot_per = 0

for i in range(1, n+1):
    total = 0
    print(f'Enter Marks of 5 Subjects of Student {i} : ')
    for j in range(1, 6):
        marks = int(input(f'Enter Marks of Subject {j} : '))
        total += marks #total = total + marks
        
    percentage = (total / 500) * 100
    tot_per += percentage
    
    print(f'Percentage of Student {i} is : {percentage}%.')
    
avg = tot_per / n
print(f'Average Percentage of all Students is: {avg}%.')     