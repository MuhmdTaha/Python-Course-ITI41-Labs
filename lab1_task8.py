
############################### LAB-01 TASK-08 ##############################################

# 8 - Write a program that prints the number of times the string 'iti' occurs in

############################### START  TASK 8  ##############################################

def search_for_iti(string):
    number_of_iti_word = 0
    for index in range(len(string) - 2):
        word = string[index] + string[index+1] + string[index+2]
        if word == "iti":
            number_of_iti_word += 1

    print(f"This is the number of iti word in your string: {number_of_iti_word}")

string_input = input("please enter a string which contain an iti word: ")
search_for_iti(string_input)


str.count("iti")



############################### END OF TASK 8  ##############################################





