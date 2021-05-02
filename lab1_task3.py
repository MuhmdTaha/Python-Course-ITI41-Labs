
############################### LAB-01 TASK-03 ##############################################

# 3 - Fill an array of 5 elements from the user, Sort it in descending and
# ascending orders then display the output

############################### START  TASK 3  ###############################################

def sort_array(array):
    asc_sorted_array = array[:]
    asc_sorted_array.sort()

    desc_sorted_array = array[:]
    desc_sorted_array.sort(reverse=True)
    print(f"Array in asc order   {asc_sorted_array}")
    print(f"Array in desc order  {desc_sorted_array}")

user_array = list(map(int, input("Please enter your array of numbers: ").split()))
print(user_array)
sort_array(user_array)

############################### END OF TASK 3  ###############################################



