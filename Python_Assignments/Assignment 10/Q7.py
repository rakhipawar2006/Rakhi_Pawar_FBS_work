li = [1,2,3,4,5,6,7,8,9,10]
n = len(li)
cube = [0] * n

for i in range(0, len(li)):
    cube[i] = li[i] ** 3

print("Original List: ", li)
print("List of Cubes: ", cube)