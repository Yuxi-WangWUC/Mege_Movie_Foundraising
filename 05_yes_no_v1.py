def yes_no (question):

    error = "Please answer yes / no"

    valid = False

    while not valid:
        # ask question and put response in lowercase
        response = input(question).lower().strip()
        
        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"
        else:
            print(error)



#main routine goes here

for item in range(0,6):
    want_snacks = yes_no("Do you want snacks?")
    print("Answer Ok, you said: ",want_snacks)
    print()
