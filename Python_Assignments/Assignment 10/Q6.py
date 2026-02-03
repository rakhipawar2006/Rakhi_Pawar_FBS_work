li = [1, 2, 3, 2, 4, 1, 5, 3]
unique_list = []

# Loop through the original list
for i in li:
    if i not in unique_list:
        unique_list = unique_list + [i]

print("Original list:", li)
print("List without duplicates:", unique_list)
