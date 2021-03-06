# CINEMA BOOKING SIMULATOR
## By: Jeandre Verster
### Date: 21/06/2021
### Language: Python
#
This is a basic cinema booking simulator with a few simple functions. The user will be able to do/see the following:

- Upon running the program, a welcome message will be displayed along with a list of available films to book.
- The user will be required to type the name of a film from the list that they'd like to book tickets for.
- Once they have chosen a film, the program will verify wether they are old enough to see the film before proceeding with booking the tickets.
- Once verified, the user will be asked how many tickets they would like to book.
- When the tickets are booked, the program will display a sucess message and automatically terminate.
#
In any of the following cases, a programmed error message will be displayed and the program will restart:

- If there is a misspelling of the film name.
- If the film is not in the list (db).
- If the user is underage.
- If there aren't sufficient seats available.

The program will ONLY terminate once a booking has been sucessfully completed.
#
Take note that this is a very basic program that is meant to be viewed from a coding perspective as opposed to a UI/UE perspective.
The program was merely designed to showcase my abilities in the following:

- Python Programming; dictionaries, loops, lists, logical programming.
- Logical program structuring.
- Basic DB creation which could be translated to a basic SQL DB.
- Creating readable and collaborative-friendly code with sufficient notes that can be used by other programmers to understand the logic and reasoning of the code.
#
## SNAPSHOT OF RAW CODE W/OUT NOTES
```python
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
```
#
## EXAMPLE: Program running sucessfully without any errors.

![1](https://user-images.githubusercontent.com/69165459/126515911-c2d2f94b-f671-4333-9881-07d8ab25cf22.jpg)
#
## EXAMPLE: User entering an invalid input, a programmed error message is displayed and the program resets.

![2](https://user-images.githubusercontent.com/69165459/126516384-731d5256-376d-4d09-91b1-a9b554641030.jpg)
#
## EXAMPLE: The user is underage, a programmed error message is displayed and the program resets.

![3](https://user-images.githubusercontent.com/69165459/126517003-175f9486-3d35-4659-b17f-414581a2f131.jpg)
#
## EXAMPLE: There aren't enough seats available, a programmed error message is displayed and the program resets.

![4](https://user-images.githubusercontent.com/69165459/126517382-0a62c6aa-aa29-44af-8a14-960c2d24037d.jpg)
