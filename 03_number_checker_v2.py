# function goes here


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


#main routine goes here
low_num = 12

high_num = 130

age = int_check("Age: ")
