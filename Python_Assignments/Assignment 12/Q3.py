def chkAnagram(str1, str2):
    dict1 = {}
    dict2 = {}
    
    if(len(dict1) != len(dict2)):
        return("Strings are not Anagram.")
    
    for ch in str1:
        if ch in dict1:
            dict1[ch] = dict[ch] + 1
        else:
            dict1[ch] = 1
            
    for ch in str2:
        if ch in dict2:
            dict2[ch] = dict2[ch] + 1
        else:
            dict2[ch] = 1
            
    if dict1 == dict2:
        return("Strings are Anagram.")
    else:
        return("Strings are not Anagram.")
            

str1 = input('Enter the first string: ')
str2 = input('Enter the second string: ')
print(chkAnagram(str1, str2))

# str1 = input('Enter the first string: ')
# str2 = input('Enter the second string: ')

# if(sorted(str1) == sorted(str2)):
#     print("Strings are Anagram.")
# else:
#     print("Strings are not Anagram.")