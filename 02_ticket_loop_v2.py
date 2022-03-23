# Start of loop

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
    name = input("Name : ")
    count += 1
    print()
    
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
