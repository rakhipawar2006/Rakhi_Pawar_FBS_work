li = ["apple", "banana", "kiwi", "cherry", "fig"]

for i in range(0, len(li)):
    for j in range(i + 1, len(li)):
        if(len(li[i]) > len(li[j])):
            li[i], li[j] = li[j], li[i]
            
print("Sorted list according to length:", li)