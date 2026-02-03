str = input('Enter the String: ')

words = str.split()

word_cnt = {}

for word in words:
    if word in word_cnt:
        word_cnt[word] += 1
    else:
        word_cnt[word] = 1

print(f'Original String: {str}')      
print('Frequency of word: ')
print(word_cnt)