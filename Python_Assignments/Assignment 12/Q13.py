str = input('Enter String: ')

digit_cnt = 0
letter_cnt = 0

for ch in str:
    if ch.isdigit():
        digit_cnt += 1
    elif ch.isalpha():
        letter_cnt += 1

print(f'Original String = {str}')       
print(f'Total Digits = {digit_cnt}')
print(f'Total Letters = {letter_cnt}')