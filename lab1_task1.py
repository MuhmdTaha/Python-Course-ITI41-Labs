
############################### LAB-01 TASK-01 ######################################

# 1 - Write a program that counts up the number of vowels [a, e, i, o, u]
# contained in the string

############################### START  TASK 1  #######################################

def count_vowels(string):

    number_of_vowels = 0
    list_of_vowels = ["a", "e", "i", "o", "u"]
    for char in string:
        if char in list_of_vowels:
            number_of_vowels += 1

    print(f"your string has {str(number_of_vowels)} vowels ! ")

usr_input = input("Please enter a string: ")
count_vowels(usr_input)

############################### END OF TASK 1  #########################################