#6. Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.

numbers = [1, 10, 20, 3, 5, 4, 11, 20]

unique_numbers = list(set(numbers))

max_product = 0
pair = ()

for i in range(len(unique_numbers)):
    for j in range(i + 1, len(unique_numbers)):
        product = unique_numbers[i] * unique_numbers[j]
        if product > max_product:
            max_product = product
            pair = (unique_numbers[i], unique_numbers[j])

print("Pair with maximum product:", pair, "with product =", max_product)
