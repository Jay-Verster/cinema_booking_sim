## Coding by: Jay Verster | Date: 26/05/2021 | Python

# PROJECT: CINEMA BOOKING SIMULATOR

films = {
    "Fidning Nemo": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 5],
    "Ghost Busters": [12, 5]
}

film_list = list(films.keys())

print("""\nWelcome to Jay's Cinema Booking Simulator!""")

while True:
    print("\nAvailable Films:\n")
    for elem in film_list:
        print(elem)
    choice = input("\nPlease type in the name of the film you would like to see below.\nChoice: ").strip().title()
    if choice in films:
        age = int(input("\nGreat! Now we'll just need to verify if you are old enough to see the film. Please enter your age below.\nAge: ").strip())
        if age>= films[choice][0]:
            print("\nAwesome, you're old enough to see the film!")
            num_seats = int(input("\nHow many seats would you like to book? Maximum of 5 per film.\nAmount: ").strip())
            if films[choice][1] >= num_seats:
                print("\nYour booking has been successful. Enjoy the film!\n")
                films[choice][1] = films[choice][1] - num_seats
                break
            else:
                print("\nUnortunately we do not have enough available seats, please choose a different film.")
        else:
            print("\nOof, unfortunately you are not not old enough to see this film! Please choose a different film.")
    else:
        print("\nHmm, we don't seem to have that film. Please check your spelling or choose a different film from the list.")