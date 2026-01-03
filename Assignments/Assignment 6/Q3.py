for i in range(1, 5):
    num = 1
    for j in range(1, 5 - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print(num, end="   ")
        num = num * (i - j) // j
    print()

#       1   
#     1   1   
#   1   2   1
# 1   3   3   1