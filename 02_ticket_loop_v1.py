# Start of loop

#initialise loops so that it runs at least ince
name = ""
count = 0
MAX_TICKETS = 5

while name != "X" and count < MAX_TICKETS:

    # Get details...
    name = input("Name : ")
    count += 1
    if count == MAX_TICKETS:
        print("You had sold all the available tickets")
    if name == "X":
        print("You have ",count," tickets left")
