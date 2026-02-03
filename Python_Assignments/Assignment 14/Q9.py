# 9. Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.

numbers = [1, 2, 3, 4, 5, 6]
target = int(input("Enter the value to check sum: "))
result = set()  

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == target:
                # sort the combination to avoid duplicates and convert to tuple for set
                combo = tuple(sorted([numbers[i], numbers[j], numbers[k]]))
                result.add(combo)


print("Unique combinations of 3 numbers adding up to", target, ":", result)
