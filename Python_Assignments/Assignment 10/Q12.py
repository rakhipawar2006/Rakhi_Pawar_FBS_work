li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(li)
square = [0] * n
cube = [0] * n

for i in range(0, n):
    square[i] = li[i] ** 2
    cube[i] = li[i] ** 3
    
print("The Original List : ", li)
print("Square of List: ", square)
print("Cube of List: ", cube)