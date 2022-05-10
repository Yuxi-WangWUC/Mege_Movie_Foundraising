# import statements
import re
import pandas


# functions go here

# check the tickets names are not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)
        # if the name is not blank, the program continues
        if response != "":
            return response
        # if the name is blank, show error and repeat the question
        else:
            print("Sorry, this can't be blank,"
                  "please enter your name")




# check for an integer bewteen 2 values:
def int_check(question):

    error = "Please enter a whole number that is more than 0 "

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        #if an integer is not entered, display an error
        except ValueError:
            print(error)


# check number of tickets lefe and warns user
# if maximum is being approached
def check_tickets(tickets_sold, ticket_limit):
    #tell user how many seats are left
    if ticket_count < MAX_TICKETS - 1:
        print("You have {} seats "
              "left".format(MAX_TICKETS - ticket_count))

    # Warns users that only one seat is left
    else:
         print("There is only one seat left")

    return ""


# gets ticket price based on age
def get_ticket_price():

    # Get age between 12 and 130
    age = int_check("Age: ")

    # check that age is valid...
    if age < 12:
        print("Sorry you are too young for this movie")
        return "invalid ticket price"
    elif age > 130:
        print("This is very old - it looks like a mistake")
        return "invalid ticket price"

    if age < 16:
        ticket_price = 7.5
    elif 16 <= age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    return ticket_price


def string_check(choice, options):

    is_valid = ""
    chosen = ""

    for var_list in options:

        # if the snack is in one of the lists, return the full response
        if choice in var_list:

            # get full name of snack and put it in
            # title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        print("Please enter a valid option")
        print()
        return "invalid choice"


#get list of snacks
def get_snack():
    #regular expression to find if desired_snack starts with a number
    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    # Each item in valid snacks is a list with
    # valid options for each snack <full name, letter code (a - e)
    # , and possible abbreviations etc>

    valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&Ms", "m&m's", "mms", "m", "b"],    # first desired_snack is M&Ms for inclusion in output
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["orange juice", "oj", "o", "juice", "e"]
]

    # LIST holds snack order for a single user
    snack_order = []

    desired_snack = ""
    while desired_snack != "x":

        snack_row = []

        # ask user for desired snack and put it in lowercase
        desired_snack = input("Snack (type x to exit choices): ").lower()

        if desired_snack == "x":
            return snack_order

        # if desired_snack has a number, separate it into two (number / desired_snack)
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        # remove white space around snack
        desired_snack = desired_snack.strip()

        # check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)

        # check snack amount is valid (less than 5)
        if amount >= 5:
            print("Sorry - we have a four snack maximum")
            snack_choice = "invalid choice"

        # add snack and amount to list...

        snack_row.append(amount)
        snack_row.append(snack_choice)

        # check that snack is not the exit code before adding
        if snack_choice != "x" and snack_choice != "invalid choice":
            snack_order.append(snack_row)


# """"""""""Main Routine""""""""""

# Set up directions / lists needed to hold data

# list of valid yes / no responses
yes_no = [
    ["yes", "y"],
    ["no", 'n']
]

# list of valid responses for payment method
pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

#initialise loops so that it runs at least ince
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

#initialise lists (ti make data-frame in due course)
all_names = []
all_tickets = []

# snack lists...
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# store surcharge multiplier
surcharge_mult_list = []

# lists to store summary data...
summary_headings = ["Popcorn", "M&M's", "Pita Chips", "Water",
                    "Orange Juice", "Snack Profit", "Ticket Profit",
                    "Total Profit"]
summary_data = []

# Data Frame Dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
    'Surcharge_Multiplier': surcharge_mult_list
}

# Summary Dictionary
summary_data_dict = {
    'Item': summary_headings,
    'Amount': summary_data
}
# cost of each snack
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice':3.25
}

# Ask user if they have used the program before & show instruction if necessary

# Loop to get ticket details
while name != "x" and ticket_count < MAX_TICKETS:

    #check numbers of ticket limit has been exceeded...
    check_tickets(ticket_count, MAX_TICKETS)

    # ***** Get details...******

    #Get name (can't be blank)
    name = not_blank("Name: ")

    # end the loop if the exit code is entered
    if name == "x":
        break

    #get ticket price based on age
    ticket_price = get_ticket_price()
    #if age is invalid, restart loop (and get name again)
    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price

    #add name and ticket price to lists
    all_names.append(name)
    all_tickets.append(ticket_price)

    #get snacks
    #ask user if they want a snack
    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you want to order snack?").lower()
        check_snack = string_check(want_snack, yes_no)

    # if they say yes, ask what snacks they want
    if check_snack == "Yes":
        snack_order = get_snack()

    else:
        snack_order = []

    # assume no snacks have been bought..
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

    # ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash or credit card)").lower()
        how_pay = string_check(how_pay, pay_method)

    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0

    surcharge_mult_list.append(surcharge_multiplier)

#End of tickets loop*

#print details ...
#create dataframe and set index to name column
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

#create column called 'sub Total'
#fill it price for snacks and ticket
movie_frame["Snacks"] = \
    movie_frame['Popcorn']*price_dict["Popcorn"] + \
    movie_frame['Water']*price_dict['Water'] + \
    movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
    movie_frame['M&Ms']*price_dict['M&Ms'] + \
    movie_frame['Orange Juice']*price_dict['Orange Juice']

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame["Snacks"]

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + \
    movie_frame["Surcharge"]

# shorten column names
movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ',
                                          'Pita Chips': 'Chips',
                                          'Surcharge_Multiplier': 'SM'})

# Set up summary dataframe
# populate snack items...
for item in snack_lists:
    # sum items in each snack list
    summary_data.append(sum(item))

# Get snack profit
# Get snack total from panda
snack_total = movie_frame['Snacks'].sun()
snack_profit = snack_total * 0.2
summary_data.append(snack_profit)

# Get Ticket profit and add to list
ticket_profit = ticket_sales - (5 * ticket_count)
summary_data.append(ticket_profit)

# Work out total profit and add to list
total_profit = snack_profit + ticket_profit
summary_data.append(total_profit)

# set up columns to be printed
pandas.set_option('display.max_columns', None)

# display numbers to 2 dp...
pandas.set_option('precision', 2)

print_all = input("Print all the columns?? (y) for yes")
if print_all == "y":
    print(movie_frame)
else:
    print(movie_frame[['Ticket', 'Sub Total',
                       'Surcharge', 'Total']])
print(movie_frame)


#Tell users if they have unsold ticket
if ticket_count == MAX_TICKETS:
    print("You had sold all the available tickets")

elif ticket_count == MAX_TICKETS - 1:
    print("You had sold {} tickets.  \n"
          "There one {} place still available"
          .format(ticket_count,MAX_TICKETS - ticket_count))

else:
    print("You have sold {} tickets.  \n"
          "There are {} places still available"
          .format(ticket_count,MAX_TICKETS - ticket_count))

    #Get age (between 12 and 130)


    #Calculte ticket price

    #Loop to ask for snacks

    #Calculate snack price

    #Ask for payment method (and apply surcharge if necessary)

#Calculater total sales and profit

#Output data to text file

