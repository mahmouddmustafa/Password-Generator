print('Assessment 2 - Password Generator')

used_pass_file = open("used_passwords.txt", "r")
used_pass = set()
for line in used_pass_file:
    used_pass.add(line.strip())
    
import random
import string

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
special_c = string.punctuation
numbers = string.digits
all_characters = lower_case + upper_case + special_c + numbers

length = range(25)

username = input('Please create a username: '"\n").strip()
email = username + "@gmail.com".strip()
e = f'Your email is: \n{email}'
print(e)

print('Please ensure the password has not been used across other programs before.')
while True:
    password = input('Create a Password or type "random" to generate a password: ').strip()
    if password in used_pass:
       print('ERROR - This password has been used before, please enter a new one.')
    else:
        used_pass_file = open("used_passwords.txt", "a")
        used_pass_file.write(password + "\n")
        special = lower = numbers = upper = False
        for i in password:
            if not i.isalnum():
                special = True
            elif i.islower():
                lower = True
            elif i.isdigit():
                numbers = True
            elif i.isupper():
                upper = True
            if special and lower and numbers and upper:
                break
        if special and lower and numbers and upper:
            if password == "random":
                password = ''.join(random.choice(all_characters)for i in length)
                p = f"Your Password is: {password}"
                print(p)
                used_pass_file.write(password)
                break
            elif 1 < len(password) < 8:
                print(len(password)*'*')
                print('Password - Weak')
                print('Sorry, Password must be atleast 8 characters long.')
            elif 16 > len(password) >= 8:
                print(len(password)*'*')
                print('Password - Strong')
                confirm_password = input('Confirm Password: '"\n").strip()
                if confirm_password == password:
                    print('Password Created Successfully!')
                    break
                else:
                    while confirm_password != password:
                        print('Incorrect, Please try again.')
                        confirm_password = input('Confirm Password: '"\n").strip()
                    else:
                        print(len(password)*'*')
                        print('Password Confirmed, Congratulations on your new Password!')
                        break
            elif len(password) >= 16:
                print(len(password)*'*')
                print('Password - Very Strong')
                confirm_password = input('Confirm Password: '"\n").strip()
                if confirm_password == password:
                    print('Password Created Successfully!')
                    break
                else:
                    while confirm_password != password:
                        print('Incorrect, Please try again.')
                        confirm_password = input('Confirm Password: '"\n").strip()
                    else:
                        print(len(password)*'*')
                        print('Password Confirmed, Congratulations on your new Password!')
                        break
            elif password == "":
                print('You must create a Password.')
        else:
            print('ERROR!')
            print('Password must contain: UPPERCASE, lowercase, numbers and special characters.')
else:
    False
        
print('To keep your account more secure, Please answer the following security questions')
sq1 = input("What was the name of your first pet? ""\n").strip()
sq2 = input("In what city was your father born? ""\n").strip()
sq3 = input("What was your childhood nickname? ""\n").strip()

while True:
    print('Please re-enter your information to verify your identity.')
    email_verify = input('re-enter your email: '"\n").strip()
    password_verify = input('re-enter your password: ').strip()
    if email_verify == email and password_verify == password:
            print('Success! Account has been Successfully created.')
            break
    elif email_verify != email or password_verify != password:
        print('ERROR. Your email or Password is incorrect.')
        forgot_password = input('Forgot Password? Type yes or no. ').strip()
        if forgot_password == 'yes':
            print('To retrieve your password, please answer the following security questions')
            sq1_verify = input("What was the name of your first pet? ""\n").strip()
            sq2_verify = input("In what city was your father born? ""\n").strip()
            sq3_verify = input("What was your childhood nickname? ""\n").strip()
            if sq1 == sq1_verify and sq2 == sq2_verify and sq3 == sq3_verify:
                print('Your Password is:', password)    
                email_verify = input('re-enter your email: '"\n").strip()
                password_verify = input('re-enter your password: ').strip()
                if password_verify == password:
                    print('Password Verified Successfully!')
                    break
                else:
                    while password_verify != password:
                        print('Incorrect, Please try again.')
                        password_verify = input('Verify Password: '"\n").strip()
                    else:
                        print(len(password_verify)*'*')
                        print('Password Verified!')
                        break
                print('Success! Account has been Successfully created.')
                break
            else:
                print('Incorrect Answers.')
                exit()
        else:
            False
used_pass_file.close()






