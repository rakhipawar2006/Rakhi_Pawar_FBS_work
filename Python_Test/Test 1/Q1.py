length = int(input("Enter the length : "))
breadth = int(input("Enter the breadth : "))
radius = int(input("Enter the radius : "))

rect_area = length * breadth
semi_circle_area = (3.14 * radius * radius) / 2

total_area = rect_area + semi_circle_area

print(f"Area of given figure is {total_area}")

rect_peri = 2 * length + breadth
semi_circle_peri = 3.14 * radius

total_peri = rect_peri + semi_circle_peri

print(f"Perimeter of given figure is {total_peri}")


