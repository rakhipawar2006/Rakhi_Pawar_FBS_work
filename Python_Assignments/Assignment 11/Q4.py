li = [10, 25, 15, 45, 70, 80, 60, 35]
#n = len(li)
def bubbleSort(li):
    size = len(li)
    for i in range(1, size):
        for j in range(0, size - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                
print("Original List: ", li)
bubbleSort(li)
print(li)
#sec_max = li[n - 2]
sec_max = li[-2]
print("Second Largest Number in list is = ",sec_max)