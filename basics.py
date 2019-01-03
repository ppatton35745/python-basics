first_name = input("WHat is your first name? ")
print("Hello,", first_name)
if first_name == "Phil":
    print(first_name, "is learning Python")
elif first_name == "Maximiliane":
    print(first_name, "is learning with fellow students in the Community! me topo!")
else:
    # This is just in case we have a younger user who can't yet read
    age = int(input("How old are you? "))
    if age <= 6:
        print("Wow you're {}! If you're confident with your reading already...".format(age))
    print("You should totally learn Python, {}!".format(first_name))
print("Have a great day {}!".format(first_name))

# print(first_name)
# print("These", "will be", "seperated by spaces")

# print("Hello, Phil")
# print("Phil is learning Python")
# print(first_name, "is using the variable")