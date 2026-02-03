# 4. Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.

numbers = [2, 4, 3, 5, 7, 8, 9, 3, 5, 2]

target_sum = int(input("Enter the value to check sum: "))

num_set = set(numbers)

set1 = set()

print("Pairs with sum", target_sum, "are:")

for num in num_set:
    diff = target_sum - num
    if diff in set1:
        print(f"{num} , {diff}")
    set1.add(num)
    
# for num1 in num_set:
#     for num2 in num_set:
#         if num1 < num2 and num1 + num2 == target_sum:
#             print(f"{num1}, {num2}")
