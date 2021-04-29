################Importing modules################
import json  # for database files
import re  # for regex pattern
import datetime  # for date and time
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
email_regix = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
