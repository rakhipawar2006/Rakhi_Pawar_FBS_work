str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

len_str1 = 0
len_str2 = 0

for ch in str1:
    len_str1 += 1
    
for ch in str2:
    len_str2 += 1
    
if(len_str1 == len_str2):
    print(f"Length of {str1} and {str2} is same.")
elif(len_str1 > len_str2):
    print(f"Larger String is = {str1}")   
else:
    print(f"Larger String is = {str2}")
    