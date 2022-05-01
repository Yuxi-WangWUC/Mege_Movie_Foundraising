#import statements
import re
import pandas


#functions go here

  #check the tickets names are not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)
        #if the name is not blank, the program continues
        if response != "":
            return response
        #if the name is blank, show error and repeat the question
        else:
            print("Sorry, this can't be blank,"
                  "please enter your name")




#check for an integer bewteen 2 values:
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


#check number of tickets lefe and warns user
#if maximum is being approached
def check_tickets(tickets_sold, ticket_limit):
    #tell user how many seats are left
    if ticket_count < MAX_TICKETS - 1:
        print("You have {} seats "
              "left".format(MAX_TICKETS - ticket_count))

    # Warns users that only one seat is left
    else:
         print("There is only one seat left")

    return ""


#gets ticket price based on age
def get_ticket_price():

    #Get age between 12 and 130
    age = int_check("Age: ")

    #check that age is valid...
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

        #if the snack is in one of the lists, return the full response
        if chosen in var_list:

            #get full name of snack and put it in
            #title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        #if the chosen option is not valid, set is_valid to
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

#get list of snacks
def get_snack():

#""""""""""Main Routine""""""""""

#Set up directions / lists needed to hold data

#list of valid yes / no responses
yes_no = [
    ["yes", "y"],
    ["no", 'n']
]

#list of valid responses for payment method
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
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]



#Date Frame Dictornary
movie_date_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice':orange_juice
}

#cost of each snack
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice':3.25
}



#Ask user if they have used the program before & show instruction if necessary

#Loop to get ticket details
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

    #if they say yes, ask what snacks they want
    if check_snack == "Yes":
        get_snack = get_snack()
    else:
        get_snack = []

    #show snack orders
    print()
    if len(snack_order) == 0:
        print("Snacks Ordered: None")
        
    else:
        print("Snacks Ordered: ")
        print(snack_order)

    #get payment method (ie: work out if surcharge is needed)
        #ask for payment method
    how_pay = "invalid chosen"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash or credit card)").lower()
        how_pay = string_check(how_pay, pay_method)

    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0
#End of tickets loop*

#print details ...
movie_frame = pandas.DataFrame(movie_date_dict)
print(movie_frame)

#calculate ticket profit
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

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

