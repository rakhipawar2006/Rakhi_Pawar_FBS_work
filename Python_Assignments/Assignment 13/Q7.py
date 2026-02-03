dict = {1: "Red", 2: "Black", 3: "Pink", 4: "Yellow"}

key = int(input('Enter the key to remove: '))

dict.pop(key)

print(f"Dictionary after removing key {key} : {dict}")