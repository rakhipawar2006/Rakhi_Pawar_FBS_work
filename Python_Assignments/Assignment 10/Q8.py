li = [1,2,3,4,5,6,7,8,9,10]
n = len(li)
dup = [0] * n

for i in range(0, len(li)):
    dup[i] = li[i]
    
print("Original List: ",li)
print("Duplicate List: ", dup)

print("ID of Original list: ",id(li))
print("ID of Duplicate list: ",id(dup))