# Main function / Written by Mengna Deng

import database
import game_logic

while True:
    game_logic.play_game()
    play_again = input("Would you like to play again? (yes/no): ").lower()

    if play_again != "yes":

        # Print all the players scores to the user state before exit
        database.allplayerscores()
        break
