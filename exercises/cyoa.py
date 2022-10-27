"""EX06 - Doggy Daycare Adventure."""


__author__ = 730579449


import random
player: str = ""
DOG: str = "\U0001F415"
health: int = 10
happiness: int = 10
points: int = 0 
dog_name: str = ""


def main() -> None: 
    """Runs the game."""
    global points, player
    greet()
    print("Now that you have a dog to take care of you have a couple options to choose from:")
    print("(1) Walk, (2) Feed, (3) Train, (4) Check Stats, (5) Mystery Objective or (6) Log Out.")
    choice: str = input("Enter your choice: ")
    while choice != "6":
        if choice == "1":
            walk_dog()
        if choice == "2":
            feed_dog()
        if choice == "3":
            train_dog()
        if choice == "4":
            check_stats()
        if choice == "5":
            points = dog_adventure(points)
        print("(1) Walk, (2) Feed, (3) Train, (4) Check Stats, (5) Mystery Objective, or (6) Log Out.")
        choice: str = input("Enter your choice: ")
    print("Thank you for playing Doggie Daycare!") 
    print(f"You finished your shift with {points} point(s), {health} health, and {happiness} on the happiness scale for {dog_name}.")


def random_dog_name() -> str:
    """Gives the user a dog name."""
    global dog_name
    num = random.randint(1, 5)
    if num == 1:
        dog_name = "Timmy"
    elif num == 2:
        dog_name = "Joy"
    elif num == 3:
        dog_name = "Apollo"
    elif num == 4:
        dog_name = "Lucky"
    elif num == 5:
        dog_name = "Rose"
    return dog_name
    

def greet() -> None:
    """Welcomes the user."""
    global player, DOG
    username: str = input("Greetings, what is your name? ")
    player = username
    print(f"Welcome {player} to Doggy Daycare!")
    name = random_dog_name()
    print(f"{player} we have selected {name} {DOG} as your first dog under your care!")


def walk_dog() -> None:
    """Walks the dog and awards points to owner."""
    global DOG, dog_name, points, health, happiness
    print(f"You have chosen to walk {dog_name} {DOG}!")
    health -= 3
    points += 1 
    happiness += 3
    print(f"You have successfuly walked {dog_name} {DOG}!")


def feed_dog() -> None:
    """Feeds the user's dog and increases health."""
    global DOG, dog_name, points, health, happiness
    print(f"You have chosen to feed {dog_name} {DOG}!")
    health += 5
    points += 1
    happiness += 3
    print(f"You have fed {dog_name} {DOG} their kibble!")


def train_dog() -> None: 
    """Trains dog and increases happiness."""
    global DOG, dog_name, points, health, happiness
    print(f"You have chosen to train {dog_name} {DOG}!")
    health -= 4
    points += 2
    happiness += 1
    print(f"You successfully taught {dog_name} a new trick!")


def dog_adventure(dog_venture_points: int) -> int: 
    """Mini doggie adventure."""
    global player, DOG
    print(f"{player} it looks like {dog_name} {DOG} ventured off while you weren't paying attention ")
    print(f"Let's see how long it takes you to find {dog_name}.")
    find: str = input("Do you want to check the (1) kitchen, the (2) backyard, the (3) garage, or the (4) bedroom?")
    if find == "1":
        print(f"Looks like {dog_name} was drinking water!")
        print(f"You found {dog_name} in 5 dog minutes.")
        dog_venture_points += 2
    if find == "2":
        print(f"Looks like {dog_name} is running around.")
        print(f"It took you 35 dog minutes to catch {dog_name}.")
        dog_venture_points -= 2
    if find == "3":
        print(f"Looks like {dog_name} is not here.")
        print("Try again later.")
        dog_venture_points -= 5
    if find == "4":
        print(f"{dog_name} is not here but looks like they made a mess in here.")
        print("Clean it up or get fired!")
        dog_venture_points -= 4
    dog_venture_points += 1
    return dog_venture_points


def check_stats() -> None:
    """Checks stats."""
    global points, health, happiness, player 
    print(f"{player} , {dog_name} {DOG} has {health} health, {points} point(s) and {happiness} happiness!")   


if __name__ == "__main__":
    main()