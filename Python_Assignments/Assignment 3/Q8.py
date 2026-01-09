import random

correct_userid = 'xyz'
correct_password = '1234'

user_id = input('Enter user ID: ')
password = input('Enter password: ')

if user_id == correct_userid and password == correct_password:
    
    captcha = random.randint(1000,9999)
    print(f'Captcha = {captcha}')

    num = int(input("Enter the same number: "))

    if(captcha == num):
        print("Login Successful...!")
    else:
        print("Failed! Captcha does not match.")

#elif(user_id != correct_userid):
    #print("Invalid user ID.")
#elif(password != correct_password):
#     print("Invalid Password.")
else:
    print("Invalid user ID and password.")
    
