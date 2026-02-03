li = [50, 20, 34, 12, 80, 97, 25, 10]

max = li[0]
sec_max = 0

for i in range(1, len(li)):
    if(li[i] > max):
        sec_max = max
        max = li[i]
        
    elif(li[i] > sec_max):
        sec_max = li[i]
        
print(f"Second largest element in list is: {sec_max}")
        