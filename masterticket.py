TICKET_PRICE = 10

tickets_remaining = 100

# Run this while tickets remain
while tickets_remaining:

    # Output how many tickets are remaining using the tickets_remaining variable
    print("There are {} tickets remaining!".format(tickets_remaining))

    # Gather the user's name and assign it to a new variable
    users_name = input("What is your name? ")

    # Prompt the user by name and ask how many tickets they would like
    try:
        req_tickets = int(input("Hello {}, How many tickets would you like to buy?".format(users_name)))
        if req_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue {}, please try again".format(err))
    else:

        # Calculate the price (number of tickets multiplied by the price) and assign it to a variable
        price_qt = req_tickets * TICKET_PRICE

        # Output the price to the screen
        print("Your price total is {}".format(price_qt))

        # Prompt user if htey want to proceed. Y/N?
        purch_conf = input("Would you like to proceed, Y/N?")
        # If they want to proceed
        if purch_conf.lower() == "y":

            # print out to the screen "SOLD!" to comfirm purchase
            # TODO: Gather credit card information and process it.
            print("SOLD!")
            # and then decrement the tickets remaining by the number of tickets purchased
            tickets_remaining -= req_tickets
        # Otherwise...
        else:

            # Thank them by name
            print("Thanks Anyways!")

# Notify user that the tickets are sold out
print("Sorry, all sold out!")