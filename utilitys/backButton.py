def back(message):

    while True:
        answer = input(message).lower().strip()

        if answer == "y":
            return True
        elif answer == "n":
            return False
        
        print("lotfan dorst vared kon (Y/N)")

    