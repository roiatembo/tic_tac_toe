from ascii_art import logo, game_board
from functions import GamePlay

continue_play = True
print(logo)
print(game_board)
print("""
Instructions

use the above board and numbers as reference to which square you want to play
and enter the number of the square you want to play
""")

player_choice = input("Who do you want to play with? type 'f' for friend, 'c' for computer: ").lower()

if player_choice == "f" or player_choice == "c":
    GamePlay = GamePlay(player_choice)
    GamePlay.play()
else:
    print("Hey that is not fair, you picked an option that i dont have")
    print("Game over try again next time")

