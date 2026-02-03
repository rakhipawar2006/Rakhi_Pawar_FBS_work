str = input("Enter the String: ")
cnt = 0 

for ch in str:
    if ch in 'AEIOUaeiou':
        cnt += 1
        
print(f"Total Number of Vowels in String are: {cnt}")
        