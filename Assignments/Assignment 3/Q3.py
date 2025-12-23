a = int(input("Enter first angle of triangle: "))
b = int(input("Enter second angle of triangle: "))
c = int(input("Enter third angle of triangle: "))

#The sum of angles of triangle must be 180°
sum = a + b + c

if(sum == 180):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
