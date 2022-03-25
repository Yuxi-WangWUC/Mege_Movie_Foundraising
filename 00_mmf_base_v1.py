#import statements

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

#""""""""""Main Routine""""""""""

#Set up directions / lists needed to hold data

#Ask user if they have used the program before & show instruction if necessary

#Loop to get ticket details

#initialise loops so that it runs at least ince
name = ""
count = 0
MAX_TICKETS = 5

while name != "X" and count < MAX_TICKETS:
    #tell user how many seats are left
    if count < MAX_TICKETS - 1:
        print("You have {} seats "
              "left".format(MAX_TICKETS - count)) 
    # Warns users that only one seat is left
    else:
         print("You have one seat left")
         
    # Get details...
    
    #Get name (can't be blank)
    name = not_blank("Name: ")

    # end the loop if the exit code is entered
    if name == "X":
        break
   
    
    #Get age between 12 and 130
    age = int_check("Age: ")

    #check that age is valid...
    if age < 12:
        print("Sorry you are too young for this movie")
        continue
    elif age > 130:
        print("This is very old - it looks like a mistake")
        continue

    count += 1  

    
#End of tickets loop

#calculate profit etc:
if count == MAX_TICKETS:
    print("You had sold all the available tickets")
elif count == MAX_TICKETS - 1:
    print("You had sold {} tickets.  \n"
          "There one {} place still available"
          .format(count,MAX_TICKETS - count))
else:
    print("You have sold {} tickets.  \n"
          "There are {} places still available"
          .format(count,MAX_TICKETS - count))
            

    #Get age (between 12 and 130)


    #Calculte ticket price

    #Loop to ask for snacks

    #Calculate snack price

    #Ask for payment method (and apply surcharge if necessary)

#Calculater total sales and profit

#Output data to text file
