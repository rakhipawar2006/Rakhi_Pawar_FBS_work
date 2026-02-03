li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_li = []
odd_li = []

for ele in li:
    if ele % 2 == 0:
        even_li.append(ele)
    else:
        odd_li.append(ele)
        
print("Original List: ", li)
print("Even List: ",even_li)
print("Odd List: ",odd_li)