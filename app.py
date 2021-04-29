################Importing modules################
import json         # for database files
import re           # for regex pattern
import datetime     # for date and time
################User Starting Menu################
print("~~~Welcome to Crowdfunding App~~~\nChoose which process do you want?\n")
print("1 --> Registeration\n2 --> Login\n3 --> Exit")

select = input("Please Please Enter Your Choice: ")

new_user = {}
new_project = {}
is_logged = False
is_exist = False
author = ''
################Phone and Email Pattern################
phone_regex = '^01[0125][0-9]{8}'
email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

################Logic Starts Here################
while True:
    ################First User Choice Registeration################
    if select == "1":
        print("Registeration")
        print("="*50)
        first_name = input("Please Enter Your First Name: ")
        new_user["first_name"] = first_name

        last_name = input("Please Enter Your Last Name: ")
        new_user["last_name"] = last_name

        while True:
            user_email = input("Please Enter Your Email: ")
            if re.search(email_regex, user_email):
                new_user["email"] = user_email
                break
            print("Email not valid try again")

        while True:
            user_password = input("Please Enter Your Password : ")
            confirm_user_password = input("Enter Confirm Password : ")
            if user_password == confirm_user_password:
                new_user["password"] = user_password
                break
            print("password not match try again")

        while True:
            phone = input("Please Enter Your Mobile Phone : ")
            if re.search(phone_regex, phone):
                new_user["phone"] = phone
                break
            print("Phone not valid try again")

        db = open("users.json", 'r')
        data = db.read()
        db.close()

        users = json.loads(data)
        users.append(new_user)

        db = open("users.json", 'w')
        db.write(json.dumps(users))
        db.close()

        break
################end of User Choice Registeration################
################################################################