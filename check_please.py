import math

def split_check(total, num_of_people):
    if num_of_people <= 1:
        raise ValueError("More than 1 person is requried to split the check")
    return math.ceil(total / num_of_people)

try:
    total_due = float(input("What is the total? "))
    number_of_people = int(input("How many people? "))
    amount_due = split_check(total_due, number_of_people)
except ValueError as err:
    print("Oh no! That's not a valid value. Try again...")
    print("({})".format(err))
else:
    print("Each person owers ${}".format(amount_due))