li1 = [1, 2, 3, 4, 5, 8]
li2 = [3, 4, 5, 6, 7, 9]

union_li = []

for i in li1:
    if i not in union_li:
        union_li.append(i)
        
for i in li2:
    if i not in union_li:
         union_li.append(i)

print("List 1: ", li1)
print("List 2: ", li2)
print("Union of the two lists: ", union_li)