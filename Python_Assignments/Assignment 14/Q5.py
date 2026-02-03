# 5. Write a Python program to find the longest common prefix of all
# strings. Use the Python set.

strings = ["flower", "flow", "floor", "flour"]

prefix = " "

for i in range(len(min(strings, key=len))):
    s = set()
    
    for word in strings:
        s.add(word[i])
        
    if len(s) == 1:
        prefix += s.pop()
    else:
        break

print("Longest Commom Prefix: ",prefix)   