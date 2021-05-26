import pandas


def num_check(question, error, num_type):
    valid = False

    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def not_blank(question, error):
    valid = False

    while not valid:
        response = input(question)

        # If name is not blank, program continues
        if response != "":
            return response

        # If name is blank, show error (& repeat loop)
        else:
            print("Sorry - this can’t be blank, "
                 "please enter your name")


def currency(x):
    return "${:.2f}".format(x)


# *** Main routine starts here ***

# Set up dictionaries and lists

item_list = []
quantity_list = []
price_list = []

variable_dict ={
    "Item": item_list,
    "Quantity": quantity_list,
    "Price": price_list
}

# Get user data
product_name = not_blank("Produce name: ",
                         "The product name can't be blank.")

# Loop to get component, quantity and price
item_name = ""
while item_name.lower() != "xxx":

    print()
    # get name, quantity and item
    item_name = not_blank("Item name: ",
                          "The component name can't be "
                          "blank.")
    if item_name.lower() == "xxx":
        break
    quantity = num_c