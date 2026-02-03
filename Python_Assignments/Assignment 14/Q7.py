# 7. Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.

set1 = {1, 2, 3, 4, 5, 8, 9}
set2 = {3, 4, 5, 6, 7, 9, 10}

missing_in_set2 = set1 - set2 #set1.difference(set2)
missing_in_set1 = set2 - set1 #set2.difference(set1)

print("Set 1: ",set1)
print("Set 2: ",set2)
print()
print("Missing in set2:", missing_in_set2)
print("Missing in set1:", missing_in_set1)
