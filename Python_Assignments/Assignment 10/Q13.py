li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_list = []

print("Original list:", li)

for num in li:
    if num % 2 != 0:  
        odd_list = odd_list + [num] 

li = odd_list
print("List after removing even numbers:", li)
