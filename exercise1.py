# Define a function that accepts a list of numbers as an argument and
# returns the sum of the odd numbers in the list.


def sum_of_odd (list):
    total = 0
    for num in list:
        if num % 2 != 0:
            total += num
    return total

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

sum_of_odds = sum_of_odd(my_list)
print("This is your list: {}".format(my_list))
print("The sum of the odd numbers in the list is {}.".format(sum_of_odd(my_list)))
