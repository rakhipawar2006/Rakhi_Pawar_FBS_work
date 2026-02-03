li1 = [1, 7, 10, 8, 5]
li2 = [6, 2, 4, 9, 3]

li = []

for i in li1:
    li.append(i)
    
for j in li2:
    li.append(j)

def bubbleSort(li):
    size = len(li)
    for i in range(1, size):
        for j in range(0, size - i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]

print("List 1: ", li1)
print("List 2: ", li2)   
bubbleSort(li)         
print("Merged and Sorted List:", li)
        