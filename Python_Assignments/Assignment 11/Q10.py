li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_li = []

print("Original List: ", li)

for i in li:
    if(i % 2 != 0):
        odd_li.append(i)

li = odd_li

print("List after removing even numbers: ", li)      
