## Coding by: Jay Verster | Date: 26/05/2021 | Python

## Skills Displayed: Python Coding with Dictionaries, Lists and Loops | Database Creation | Basic Database Management

## ------------------------------ ##

# PROJECT: CINEMA BOOKING SIMULATOR

# Welcome to my Cinema Booking Simulator. The objective of this program would be to allow a user
# to book seats to a movie within the systems' database should they meet the age requirements.

# Notes: Creating a dictionary called 'films' that will contain the available films in the cinema,
# as well as their age restriction at index [0] and available seats at index [1].

films = {
    "Fidning Nemo": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 5],
    "Ghost Busters": [12, 5]
}

# Notes: Below I am creating a list from the above dictionary. This will later be used to display the
# available films in the cinema to the user. This piece of code is merely to ease and improve the
# user experience.

film_list = list(films.keys())

# Notes: The below code will display a welcome message to the user.

print("""\nWelcome to Jay's Cinema Booking Simulator!""")

# Notes: Creating a while loop to run the program

while True:
    # Notes: The below print statement will create a caption to improve the user experience, and will run each time the loop is repeated. 
    print("\nAvailable Films:\n")

    # Notes: The below for loop will display the available films showing in the cinema by printing each element from the list film_list on a seperate line.
    for elem in film_list:
        print(elem)

    # Notes: The below code will capture input from the user for their choice of film. The strip() function is used to strip user-entered whitespace, and the title() function
    # is used to capatilise each word entered by the user. These functions are used in order for the data to be read correctly from the dictionary.
    choice = input("""\nPlease type in the name of the film you would like to see below.\nChoice:""").strip().title()

    # Notes: If the user entered an available item found in the dictionary, the below code will run. If not, then a programmed error message is displayed to the user and the loop will restart
    if choice in films:

        #Notes: The user's age is captured through user input. The input is automatically cast to an integer format, and the strip() function is used to remove any whitespace.
        age = int(input("\nGreat! Now we'll just need to verify if you are old enough to see the film. Please enter your age below.\nAge:").strip())

        # Notes: The user's age is compared to the age restriction in the films dictionary. If the user's age is equal to or higher than the restriction, the below code will run.
        # If not, then the else statement will come into effect, print a programmed message and restart the loop in order for the user to choose a more appropriate film.
        if age>= films[choice][0]:
            print("\nAwesome, you're old enough to see the film!")

            # Notes: The number of seats the user wants to book is captured through user input, which is stripped of whitespace using the strip() function and cast into an integer
            # in order to run the data correctly through the dictionary.
            num_seats = int(input("\nHow many seats would you like to book? Maximum of 5 per film.\nAmount:").strip())

            # Notes: The amount is compared to the available seats. If there are seats available, the below code will run by printing a programmed success message to the user confirming their
            # booking and subtracting the booked seats from the available seats in the dictionary, thus updating it. This then enacts the break function and the program ends.
            # If there aren't enough seats available when compared to the dictionary, then a programmed error message is displayed to the user and the loop restarts.
            if films[choice][1] >= num_seats:
                print("Your booking has been successful. Enjoy the film!\n")
                films[choice][1] = films[choice][1] - num_seats
                break
            else:
                print("\nUnortunately we do not have enough available seats, please choose a different film.")
        else:
            print("\nOof, unfortunately you are not not old enough to see this film! Please choose a different film.")
    else:
        print("\nHmm, we don't seem to have that film. Please check your spelling or choose a different film from the list.")      
