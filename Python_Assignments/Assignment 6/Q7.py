for i in range(1, 6):
    k = 65
    for j in range(1, 6 - i):
        print(' ', end = ' ')
        
    for j in range(1, 2 * i):
        print(chr(k), end= ' ')
        k += 1
       
    print()
    
    
#         A
#       A B C       
#     A B C D E
#   A B C D E F G
# A B C D E F G H I    