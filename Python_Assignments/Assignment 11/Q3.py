li = [[10, 5], [5, 1], [7, 4], [9, 2], [2, 3]]

def selectionSort(li):
    size = len(li)
    for i in range(0, size - 1):
        min = i
        for j in range(i + 1, size):
            if(li[min][1] > li[j][1]):
                min = j
        li[i], li[min] = li[min], li[i]

print("Original List: ", li)
selectionSort(li)
print("Sorted List According to the Second Element in Sublist is: ",li)