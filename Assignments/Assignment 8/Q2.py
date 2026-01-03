def areaCir(r):
    area = 3.142 * r * r
    return area

radius = float(input('Enter the radius of circle: '))

result = areaCir(radius)

print(f'Area of Circle = {result}.')