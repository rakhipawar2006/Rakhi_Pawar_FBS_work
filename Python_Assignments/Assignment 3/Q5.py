a = int(input("Enter first side of triangle: "))
b = int(input("Enter second side of triangle: "))
c = int(input("Enter third side of triangle: "))

if((a + b > c) and (a + c > b) and (b + c > a)):
    if(a == b == c):
        print("The triangle is Equilateral.")
    elif(a == b or a == c or b == c):
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("The triangle is not valid.")
