c_userid = 'abc'
c_password = '1234'

count = 1

while count <= 3:
    user_id = input('Enter User ID: ')
    password = input('Enter Password: ')

    if user_id == c_userid and password == c_password:
        print('Login Successful...!')
        break
    else:
        print(f'Wrong credentials. Attempt {count} of 3')
    
    count += 1