n = int(input("Enter the how many elements you want to enter in list: "))

li = []
square_li = []
cube_li = []

for i in range(0, n):
    num = int(input(f"Enter the number {i+1}: "))
    li.append(num)
    
for i in li:
    square_li.append(i ** 2)
    cube_li.append(i ** 3)
    
print("Number List: ", li)
print("Square List: ", square_li)
print("Cube  List: ", cube_li)