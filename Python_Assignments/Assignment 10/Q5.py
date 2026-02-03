li = [50, 12, 34, 12, 80, 97, 25, 10, 12]

num = int(input("Enter Number to be search: "))
count = 0

for i in range(0, len(li)):
    if(num == li[i]):
        count += 1
        
if(count > 0):
    print(f"The number {num} present in list {count} times.")
else:
    print(f"The number {num} is not present in list.")