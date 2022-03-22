# Start of loop

#initialise loops so that it runs at least ince
name = ""
count = 0
MAX_TICKETS = 5

while name != "X" and count < MAX_TICKETS:
    print("You have {} seats "
          "left".format(MAX_TICKETS-count))

    # Get details...
    name = input("Name : ")
    count += 1
    print()
    
if count == MAX_TICKETS:
    print("You had sold all the available tickets")
else:
    print("You have sold {} tickets.  \n"
          "There are {} places still available"
          .format(count,MAX_TICKETS - count))
