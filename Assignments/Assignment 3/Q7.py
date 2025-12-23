correct_userid = 'xyz'
correct_password = '1234'

user_id = input('Enter user ID: ')
password = input('Enter password: ')

if user_id == correct_userid and password == correct_password:
    print("User enter correct user ID and password.")
    print("Login Successful...!")
elif(user_id != correct_userid):
    print("Invalid user ID.")
elif(password != correct_password):
    print("Invalid Password.")
else:
    print("Invalid user ID and password.")
    
