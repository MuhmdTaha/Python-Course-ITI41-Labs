
############################### LAB-01 TASK-02 ##############################################

# 2 - Write a function that accepts two arguments (length, start) to generate
# an array of a specific length filled with integer numbers increased by one
# from start.

############################### START  TASK 2 ###############################################

def generate_arr(length, start):
    result_arr = []
    for counter in range(length):
        result_arr.append(start)
        start += 1
    return result_arr

user_length = 4
user_start = 15
print(generate_arr(user_length, user_start))

############################### END OF TASK 2 ###############################################



