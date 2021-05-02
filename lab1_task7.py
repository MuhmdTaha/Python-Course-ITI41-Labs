
############################### LAB-01 TASK-07 ##############################################

# 7 - Ask the user for his name then confirm that he has entered his name
# (not an empty string/integers). then proceed to ask him for his email and
# print all this data
# - (Bonus) check if it is a valid email or not

############################### START  TASK 7 ################################################

import re

def validate_name_and_email(username):
    try:
        int(username)
        print("please enter a valid name")
    except:
        while len(username) <= 0:
            print("Please enter a valid name !!")
            username = input("please enter your name: ")

        else:
            email = input("Please enter your Email: ")
            regex = '^[a-z][a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if (re.search(regex, email)):
                print(f"This is your name {username}, and this is your email {email}")
            else:
                print("Invalid Email")
                validate_name_and_email(username)

username = input("please enter your name: ")
username = username.lower()
validate_name_and_email(username)

############################### END OF TASK 7 ################################################





