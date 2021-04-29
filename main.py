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

################Logic Starts Here################
while True:
    ################First User Choice Registeration################
    if select == "1":
        print("Registeration")
        print("----------------")
        first_name = input("Please Enter Your First Name : ")
        new_user["first_name"] = first_name

        last_name = input("Please Enter Your Last Name : ")
        new_user["last_name"] = last_name

        while True:
            user_emial = input("Please Enter Your Email : ")
            if re.search(email_regix, email):
                new_user["email"] = email
                break
            print("Email not valid try again")

        while True:
            user_password = input("Please Enter Your Password : ")
            confirm_user_password = input("Enter Confirm Password : ")
            if user_password == confirm_password:
                new_user["password"] = password
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
################Second User Choice Login################
    elif select == "2":
        print("Login")
        print("="*50)

        user_emial = input("Please Enter Your Email : ")
        user_password = input("Please Enter Your Password : ")

        db = open("users.json", 'r')
        data = db.read()
        db.close()

        users = json.loads(data)

        for user in users:

            if user['email'] == user_emial and user['password'] == user_password:
                print("="*50)
                print(f"Wellcome {user['first_name']} {user['last_name']}")
                print("="*50)
                is_logged = True
                author = user['email']

                print("Choose which sub process do you want?")
                print("1 -> Create Project")
                print("2 -> View All Projects")
                print("3 -> Edit Project")
                print("4 -> Delete Project")
                print("5 -> Search for a Project using Date")
                print("6 -> Exit")

                sub_menu_select = input("Please Enter Your Number: ")

                while True:
                    if sub_menu_select == "1":
                        print("Create Project")
                        print("="*20)

                        print("="*20)
                        title = input("Enter Project Title: ")
                        new_project["title"] = title

                        details = input("Enter Project Details: ")
                        new_project["details"] = details

                        total_target = input("Enter Project Total Target: ")
                        new_project["total_target"] = total_target

                        while True:
                            start_time = input("Enter Project Start Time: ")
                            try:
                                datetime.datetime.strptime(
                                    start_time, '%Y-%m-%d')
                                new_project["start_time"] = start_time
                                break
                            except ValueError:
                                print("Incorrect data format, should be YYYY-MM-DD")

                        while True:
                            end_time = input("Enter Project End Time: ")
                            try:
                                datetime.datetime.strptime(
                                    end_time, '%Y-%m-%d')
                                new_project["end_time"] = end_time
                                break
                            except ValueError:
                                print("Incorrect data format, should be YYYY-MM-DD")

                        new_project['author'] = author

                        print("="*50)

                        db = open("projectsdb.json", 'r')
                        data = db.read()
                        db.close()

                        projects = json.loads(data)
                        projects.append(new_project)

                        db = open("projectsdb.json", 'w')
                        db.write(json.dumps(projects))
                        db.close()

                        break
                    elif sub_menu_select == "2":
                        print("View All Projects")
                        print("="*50)
                        db = open("projectsdb.json", 'r')
                        data = db.read()
                        db.close()

                        projects = json.loads(data)

                        for project in projects:

                            print("="*50)
                            print(f"Title: {project['title']}")
                            print(f"Details: {project['details']}")
                            print(f"Total Target: {project['total_target']}")
                            print(f"Start Time: {project['start_time']}")
                            print(f"End Time: {project['end_time']}")
                            print(f"author: {project['author']}")
                            print("="*50)

                        break
                    elif sub_menu_select == "3":
                        print("Edit Project")
                        print("="*50)

                        project_title = input("Enter Project Title To Edit: ")

                        db = open("projectsdb.json", 'r')
                        data = db.read()
                        db.close()

                        projects = json.loads(data)

                        for project in projects:

                            if project['title'] == project_title and project['author'] == author:

                                is_exist = True

                                print("="*50)
                                title = input(
                                    "Enter New Title or press enter to skip it: ")
                                if title:
                                    project["title"] = title

                                details = input(
                                    "Enter New Details or press enter to skip it: ")
                                if details:
                                    project["details"] = details

                                total_target = input(
                                    "Enter New Total Target or press enter to skip it: ")
                                if total_target:
                                    project["total_target"] = total_target

                                start_time = input(
                                    "Enter New Start Time or press enter to skip it: ")
                                if start_time:
                                    while True:
                                        try:
                                            datetime.datetime.strptime(
                                                start_time, '%Y-%m-%d')
                                            project["start_time"] = start_time
                                            break
                                        except ValueError:
                                            print(
                                                "Incorrect data format, should be YYYY-MM-DD")

                                        start_time = input(
                                            "Enter New Start Time or press enter to skip it: ")

                                        if not start_time:
                                            break

                                end_time = input(
                                    "Enter New End Time or press enter to skip it: ")
                                if end_time:
                                    while True:
                                        try:
                                            datetime.datetime.strptime(
                                                end_time, '%Y-%m-%d')
                                            project["end_time"] = end_time
                                            break
                                        except ValueError:
                                            print(
                                                "Incorrect data format, should be YYYY-MM-DD")

                                        end_time = input(
                                            "Enter New End Time or press enter to skip it: ")

                                        if not end_time:
                                            break

                                print("="*50)

                                db = open("projectsdb.json", 'w')
                                db.write(json.dumps(projects))
                                db.close()
                                print("Project Edited successfully")
                                break

                        if is_exist == False:
                            print("This Product Doesn't Exists")

                        break
                    elif sub_menu_select == "4":
                        print("Delete Project")
                        print("="*50)

                        project_title = input(
                            "Enter Project Title To Delete: ")

                        db = open("projectsdb.json", 'r')
                        data = db.read()
                        db.close()

                        projects = json.loads(data)

                        for index, project in enumerate(projects):

                            if project['title'] == project_title and project['author'] == author:

                                is_exist = True

                                projects.pop(index)

                                db = open("projectsdb.json", 'w')
                                db.write(json.dumps(projects))
                                db.close()
                                print("Project Deleted successfully")
                                break

                        if is_exist == False:
                            print("This Product Doesn't Exists")

                        break
                    elif sub_menu_select == "5":
                        print("Search for a Project using Start Date")
                        print("="*50)

                        while True:
                            project_start_date = input(
                                "Enter Project Start Date to Search: ")
                            try:
                                datetime.datetime.strptime(
                                    project_start_date, '%Y-%m-%d')

                                db = open("projectsdb.json", 'r')
                                data = db.read()
                                db.close()

                                projects = json.loads(data)

                                for project in projects:

                                    if project['start_time'] == project_start_date and project['author'] == author:

                                        is_exist = True

                                        print("="*50)
                                        print(f"Title: {project['title']}")
                                        print(f"Details: {project['details']}")
                                        print(
                                            f"Total Target: {project['total_target']}")
                                        print(
                                            f"Start Time: {project['start_time']}")
                                        print(
                                            f"End Time: {project['end_time']}")
                                        print(f"author: {project['author']}")
                                        print("="*50)
                                        break

                            except ValueError:
                                print("Incorrect data format, should be YYYY-MM-DD")

                            if is_exist == False:
                                print("This Product Doesn't Exists")

                            break

                    elif sub_menu_select == "6":
                        break

        if is_logged == False:
            print("your email or password not correct please try again")
        break
################If user didn't choose either to login nor register ################
    elif select == "3":
        break
    else:
        select = input("You have to choose between 1 , 2 , or 3: ")

################Logic ends Here################
