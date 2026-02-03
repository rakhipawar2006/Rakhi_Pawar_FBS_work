li = [50, 20, 34, 12, 80, 97, 25, 10]

max = li[0]
min = li[0]

for i in range(1, len(li)):
    if(li[i] > max):
        max = li[i]
    
    if(li[i] < min):
        min = li[i]
        
print(f"Maximum element of list = {max}")
print(f"Minimum element of list = {min}")      