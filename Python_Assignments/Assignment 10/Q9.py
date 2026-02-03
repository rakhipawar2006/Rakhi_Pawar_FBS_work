# n = int(input("Enter how many element you want enter in list: "))

# li = [0] * n
# even = []
# odd = []

# for i in range(0, n):
#     li[i] = int(input(f"Enter the element {i+1}: "))
#     if(li[i] % 2 == 0):
#         even = even + [li[i]]
#     else:
#         odd = odd + [li[i]]
          
# print(f"Original List: {li}") 
# print(f"Odd List: {odd}")
# print(f"Even List: {even}")


n = int(input("Enter how many element you want enter in list: "))

li = [0] * n
even_li = []
odd_li = []

for i in range(0, n):
    li[i] = int(input(f"Enter the element {i+1}: "))
    
for ele in li:
    if(ele % 2 == 0):
        even_li.append((ele))
    else:
        odd_li.append(ele)
          
print(f"Original List: {li}") 
print(f"Odd List: {odd_li}")
print(f"Even List: {even_li}")
