def areaRect(l, b):
    area = l * b
    return area

length = int(input('Enter the length of Rectangle: '))
breadth = int(input('Enter Breadth of Reactangle: '))

result = areaRect(length, breadth)

print(f'Area of Rectangle = {result}.')