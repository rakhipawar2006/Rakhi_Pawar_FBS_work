li = [1, 2, 3, 2, 4, 5, 2, 3, 5]
new_li = []

remove_ele = int(input('Enter the element to remove all occurences: '))

for i in li:
    if i != remove_ele:
        new_li = new_li + [i]
        
print(f'Original list: {li}')
print(f'List after removing {remove_ele} :  {new_li}')
    
