print('Assessment 2 - Password Generator')

import random
import string

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
special_c = string.punctuation
numbers = string.digits
all_characters = lower_case + upper_case + special_c + numbers

length = range(25)

while True:
    password = input('Create a Password or type "random" to generate a password: ')
    if password == "random":
        password = ''.join(random.choice(all_characters)for i in length)
        p = f"Your Password is: {password}"
        print(p)
        print('GoodBye!')
        break
    elif 1 < len(password) < 8:
        print(len(password)*'*')
        print('Password - Weak')
        print('Sorry, Password must be atleast 8 characters long.')
    elif 16 > len(password) >= 8:
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
            print(len(password)*'*')
            print('Password - Strong')
            confirm_password = input('Confirm Password: ')
            if confirm_password == password:
                print('Password Created Successfully!')
                break
            else:
                while confirm_password != password:
                    print('Incorrect, Please try again.')
                    confirm_password = input('Confirm Password: ')
                else:
                    print(len(password)*'*')
                    print('Password Confirmed, Congratulations on your new Password!')
                    break
        else:
            print('ERROR!')
            print('Password must contain: UPPERCASE, lowercase, numbers and special characters.')
    elif len(password) >= 16:
        special = lower = numbers = upper = False
        for i in password:
            if not i.isalnum():
                special = True
            if i.islower():
                lower = True
            if i.isdigit():
                numbers = True
            if i.isupper():
                upper = True
            if special and lower and numbers and upper:
                break
        if special and lower and numbers and upper:
            print(len(password)*'*')
            print('Password - Very Strong')
            confirm_password = input('Confirm Password: ')
            if confirm_password == password:
                print('Password Created Successfully!')
                break
            else:
                while confirm_password != password:
                    print('Incorrect, Please try again.')
                    confirm_password = input('Confirm Password: ')
                else:
                    print(len(password)*'*')
                    print('Password Confirmed, Congratulations on your new Password!')
                    break
    elif password == "":
        print('You must create a Password.')
    else:
        False
   











