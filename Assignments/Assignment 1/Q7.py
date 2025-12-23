a = float(input('Enter coefficient of a: '))
b = float(input('Enter coefficient of b: '))
c = float(input('Enter coefficient of c: '))

r1 = (-b + (b*b - 4*a*c)**0.5) / 2*a
r2 = (-b - (b*b - 4*a*c)**0.5) / 2*a

print(f'Roots of Quadratic Equation is {r1} and {r2} .')
