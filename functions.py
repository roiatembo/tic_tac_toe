import random

winning_combinations = [
[1,2,3],
[4,5,6],
[7,8,9],
[1,4,7],
[2,5,8],
[3,6,9],
[1,5,9],
[3,5,7]
]

mini_gameboard = [
    ["-","|","-","|","-"],
    ["-","|","-","|","-"],
    ["-","|","-","|","-"]
]


available_boxes = [1,2,3,4,5,6,7,8,9]
player_1_boxes = []
player_2_boxes = []

class GamePlay(object):
    """This class defines how the game would be played"""

    def __init__(self, player_choice):
        self.player_choice = player_choice

    def is_winning(self, boxes):
        win = 0
        for combination in winning_combinations:
            if combination[0] in boxes:
                win += 1
            if combination[1] in boxes:
                win += 1
            if combination[2] in boxes:
                win += 1
            if win == 3:
                win = 0
                return True
            else:
                win = 0

    def computer_play(self):
        """
        makes sure that the computer picks random numbers from 1-9
        and only picks those numbers that haven't been picked
        :return:
        """
        pick_number = True
        while pick_number:
            box = random.randint(1,9)
            if box not in available_boxes:
                continue
            else:
                pick_number = False
            available_boxes.remove(box)
            return box

    def is_valid(self, box):
        """
        takes the number chosen and checks if its available and then removes it from
        the available boxes
        :param box: the number picked
        :return:
        """
        if box not in available_boxes:
            print("Your input is invalid please try again")
            return False
        else:
            available_boxes.remove(box)

    def player_input(self, condition, player, boxes, box=0):
        """
        takes a players input and perfoms validations
        :param condition: is always true
        :param player: player number
        :param boxes: players choices so far
        :param box: is zero when the computer's turn to pick
        :return:
        """
        input_cond = condition
        while input_cond == "correct":
            box = int(input(f"Player {player} enter a box number between 1-9: "))
            if self.is_valid(box) == False:
                continue
            else:
                input_cond = "incorrect"
        boxes.append(box)
        print(f"Player {player} choices so far are {boxes}")
        if self.is_winning(boxes):
            print(f"Game over Player {player} has won")
            return 1
        elif len(available_boxes) == 0:
            print("Game over it is a draw")
            return 1
        else:
            return 0

    def play(self):
        """
        method that controls the play of the game
        :return:
        """
        box = 0
        while True:
            condition = "correct"
            player = "1"
            continue_play = self.player_input(condition, player, player_1_boxes)
            if continue_play == 1:
                break

            player = "2"
            if self.player_choice == "f":
                continue_play = self.player_input(condition, player, player_2_boxes)
            else:
                condition = "incorrect"
                choosen_box = self.computer_play()
                continue_play = self.player_input(condition, player, player_2_boxes, box=choosen_box)
            if continue_play == 1:
                break

for row in mini_gameboard:
    pretty_row = ""
    for item in row:
        pretty_row += item
    print(pretty_row)