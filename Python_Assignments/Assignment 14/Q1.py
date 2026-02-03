# 1. Write a Python program to find elements in a given set that are not in another set.

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 6}

difference = s1.difference(s2)
#difference = set1 - set2

print("Elements in set1 that are not in set2:", difference)