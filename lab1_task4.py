
############################### LAB-01 TASK-04 ##############################################

# 4 - write a function that takes a number as an argument and if the number
# divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# divisible by both return "FizzBuzz"


############################### START  TASK 4 ################################################

def fizz_buzz(number):

    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        print(f"your number doesn't fit! try another number")
        return 0


print(fizz_buzz(int(input("Please enter a number: "))))


############################### END OF TASK 4 ################################################