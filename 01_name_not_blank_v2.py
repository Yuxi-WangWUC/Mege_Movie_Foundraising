#funtions go here

def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)
        #if name is not blank, program continues
        if response != "":
            return response
        #if name is blank, show error (& repeat loop)
        else:
            print(error_message)

#Main Routine goes here
name = not_blank("Name: ",
                 "Sorry, this can't be blank, "
                 "please enter your name" )
