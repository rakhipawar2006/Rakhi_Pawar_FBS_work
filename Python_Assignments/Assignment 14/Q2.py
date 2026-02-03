#2. Write a Python program to remove the intersection of a second set with a first set.

s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 60}

s1.difference_update(s2)
#s1 -= s2

print("Set1 after removing intersection with Set2:", s1)
