import random
import database

diamonds = {
    "red": {"hint": "Red diamond located in the city of love", "location": "Paris"},
    "blue": {"hint": "Blue diamond is in a city which hosted the 1952 Summer Olympics ", "location": "Helsinki"},
    "green": {"hint": "Green diamond is in a city which is the largest urban area in the Nordic countries", "location": "Stockholm"},
    "yellow": {"hint": "Yellow diamond is in a city that is the home to 29 companies of the Fortune Global 500 in Japan", "location": "Tokyo"},
    "purple": {"hint": "Purple diamond is in a city has the third greatest population", "location": "ShangHai"},
    "pink": {"hint": "Pink diamond is in a city has the most visited zoo in Europe", "location": "Berlin"},
    "white": {"hint": "White diamond is in a city that is the world's northernmost capital of a country", "location": "Reykjavik"},
}

def play_game():
    collected_diamonds = set()
    attempts = 0
    score = 0

    print("Welcome to the Diamond Hunt Game!")
    player_name = input("Enter your name: ")

    # Press enter to exit the game
    if not player_name:
        return

    while len(collected_diamonds) < len(diamonds) and attempts < 9:
        remaining_diamonds = set(diamonds.keys()) - collected_diamonds
        color = random.choice(list(remaining_diamonds))
        hint = diamonds[color]["hint"]
        location = diamonds[color]["location"]

        guess = input(f"Guess the location of the {color} diamond ({hint}): ")
        attempts += 1

        # Press enter to pre_exit the game anytime
        if guess == "":
            intend_exit = input(f"Do you want to exit the game? (yes/no)").lower()
            if intend_exit != "no":
                print(f"Sorry to see you go, {player_name}")
                break
        elif guess.lower() == location.lower():
            database.getairportsbycity(guess)
            print(f"Congratulations, {player_name}! You found the {color} diamond.")
            collected_diamonds.add(color)
            score += 1
        else:
            print("Incorrect guess, try again")


    if len(collected_diamonds) == len(diamonds):
        print(f"Congratulations, {player_name}! You've collected all seven diamonds in {attempts} attempts.")

    elif attempts > 9:
        print(f"Sorry, {player_name}. You've reached the maximum attempts. Try again later")


    database.storeplayerscores(player_name, score)