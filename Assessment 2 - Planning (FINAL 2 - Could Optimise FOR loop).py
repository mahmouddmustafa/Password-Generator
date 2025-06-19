print('Assessment 2 - Password Generator')

used_pass_file = open("used_passwords.txt", "r")            #Opens a file to read the contents of it and create a set out of the contents
used_pass = set()                                           
for line in used_pass_file:
    used_pass.add(line.strip())
    
import random                                               #imports random and string library, to be able to have an unbiased (random) password generated and to access all kinds of characters in a str
import string

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
special_c = string.punctuation
numbers = string.digits
all_characters = lower_case + upper_case + special_c + numbers          #assigns all_characters with all the possible str characters using ascii in the string library

length = range(18)

username = input('Please create a username: '"\n").strip()              #asks for a username to create an email out of, strip() function removes any blank spaces on either side of the input
email = username + "@gmail.com".strip()
print(f'Your email is: \n{email}')                                      #all the \n in the code (except line 30) are to create an aesthetic look, more pleasing to the eye

print('Please ensure the password has not been used across other programs before.')         #Ensures Criteria 4
while True:                                                                                                         #all conditions within the true will occur until the truth value is false
    password = input('Create a Password or type "random" to generate a password \ntype "quit" to exit: ').strip()
    if password == "quit".strip():                                                              #if the user wants to exit the program they inout "quit"
        exit()
    if password in used_pass and password != "random":                                                              #checks if the password has been used before in the file and ensures the word "random"
       print('ERROR - This password has been used before, please enter a new one.')                                 #^continuation is not added to the used passwords file 
    else:
        used_pass_file = open("used_passwords.txt", "a")                                            #if the password has not been used before, it is added to the used passwords file, using append 
        used_pass_file.write(password + "\n")                                                       #\n ensures passwords are not overlapping and on separate lines
        if password == "random":
                password = ''.join(random.choice(all_characters)for i in length)    #random.choice makes up a random string of all the possible ascii characters in the length of the variable length (assigned to range(18))
                print(f"Your Password is: {password}")
                used_pass_file.write(password)                                      #if random is typed by the user, the random password is stored in the used passwords file
                break
        special = any(not i.isalnum() for i in password)                    #boolean expression (T/F) if any character of the string input from the password is not alphaneumeric i.e. symbols it is true
        lower = any(i.islower() for i in password)                          #boolean expression (T/F) if any character of the string input from the password is lowercase it is true
        numbers = any(i.isdigit() for i in password)                        #boolean expression (T/F) if any character of the string input from the password is a digit it is true
        upper = any(i.isupper() for i in password)                          ##boolean expression (T/F) if any character of the string input from the password is uppercase it is true
        if special and lower and numbers and upper:                 #so if the password contains upper case, lower case, numbers and symbols - it is approved and then checks the length of the password after
            if 1 <= len(password) < 8:                                           #if the password is not equal to or greater than 8, it is not accepted and it loops until a pass >= 8 is created
                print(len(password)*'*')                                         #displays the length of the password using * for an aesthetic look and ranks the password's strength
                print('Password - Weak')
                print('Sorry, Password must be atleast 8 characters long.')
            elif 16 > len(password) >= 8:                                       #if length of password is 8 and greater, it is accepted and is ranked strong
                print(len(password)*'*')
                print('Password - Strong')
            elif len(password) >= 16:                                           #if length of password is 16 and greater, it is accepted and is ranked very strong
                print(len(password)*'*')
                print('Password - Very Strong')
            elif password == "":                                                #if the password is blank, it asks the user to create a password in a loop until a password is entered
                print('You must create a Password.')
            confirm_password = input('Confirm Password: '"\n").strip()          #asks for the user to confirm the password by re entering the password
            if confirm_password == password:                                    #if the password is equivalent to the confirmation password, the password is created successfully 
                print('Password Created Successfully!')
                break
            else:
                while confirm_password != password:                             #if the confirm password is not equivalent it continues asking until it is equivalent
                    print('Incorrect, Please try again.')
                    confirm_password = input('Confirm Password: '"\n").strip()
                else:
                    print(len(password)*'*')                                                #password is equivalent and displays a confirmation message
                    print('Password Confirmed, Congratulations on your new Password!')
                    break
        else:
            print('ERROR!')                     #refers to first condition about following the criteria of atleast 8 characters and containing upper, lower cases and digits and special characters
            print('Password must have atleast 8 characters and contain: UPPERCASE, lowercase, numbers and special characters.') #condition must be followed for the password to be created or will stay in loop
else:
    False
        
print('To keep your account more secure, Please answer the following security questions')       #security questions to boosten privacy and security (extra feature) later used when verifying identity
sq1 = input("What was the name of your first pet? ""\n").strip()
sq2 = input("In what city was your father born? ""\n").strip()
sq3 = input("What was your childhood nickname? ""\n").strip()

i = 0
while i < 4:                                                                                #gives the user a max of 3 attempts to verify identity 
    print('Please re-enter your information to verify your identity.')
    email_verify = input('re-enter your email: '"\n").strip()
    password_verify = input('re-enter your password: ').strip()
    i += 1
    if email_verify == email and password_verify == password:               #if the email and password are equivalent, the account is created
        print('Success! Account has been Successfully created.')
        break                                                               #breaks the loop if condition is met
    elif email_verify != email or password_verify != password:              #if they are not equivalent, the user has the option to retrieve password by saying yes and reanswering the security questions           
        print('ERROR. Your email or Password is incorrect.')                #^continuation - or to say no and renter the info with a max of 3 attempts before the program automatically quits for security
        forgot_password = input('Forgot Password? Type yes or no. ').strip()
        if forgot_password == 'yes':
            print('To retrieve your password, please answer the following security questions')
            sq1_verify = input("What was the name of your first pet? ""\n").strip()
            sq2_verify = input("In what city was your father born? ""\n").strip()
            sq3_verify = input("What was your childhood nickname? ""\n").strip()
            if sq1 == sq1_verify and sq2 == sq2_verify and sq3 == sq3_verify:
                print('Your Password is:', password)    
            else:
                print('Incorrect Answers. You have', 4 - i, 'Attempts Left.')
        else:
            print('You have', 4 - i, 'Attempts Left.')
else:
    print('ERROR! Too many incorrect verification attempts.')
    exit()
used_pass_file.close()                                              #closes the file to prevent corruption
    





