li1 = [1, 2, 3, 4, 5, 10, 6]
li2 = [1, 3, 4, 5, 6, 7, 9]

intersection_li = []

for i in li1:
    if i in li2 and i not in intersection_li:
        intersection_li.append(i)

print("List 1: ", li1)
print("List 2: ", li2)
      
print("Intersection of the two lists: ", intersection_li)