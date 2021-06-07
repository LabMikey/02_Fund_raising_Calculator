# Functions go here


# Checks that user has entered yes / no to a question
def yes_no(question):
  error = "please answer yes / no"

  valid = False
  while not valid:
    # ask question and put response in lowercase
    response = input(question).lower()

    if response == "yes" or response == "y":
      return "yes"
    elif response == "no" or response == "n":
      return "no"
    else:
        print(error)



def profit_goal(total_costs):

    # Intialise variable and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:

        # ask for profit goal...
        response = input("What is your profit goal (eg $500 or 50%) ")

        # check if forst character is $
        if response [-1] == "$":
            profit_type = "$"
            # Get amount (everything before the $)
            amount = response[:-1]

        # check if last charcter is %
        elif response[-1] == "%":
            profit_type = "%"
            # Get amount (everything before the %)
            amount = response[:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # Check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no("Do you mean ${:.2f}. " "ie {:.2f} dollars? ," "y / n ".format(amount, amount))

            # Set profit type based on user anwser above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no("Do youy mean {}%? , y / n".format(amount))
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # if return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal






