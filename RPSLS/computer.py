import random
from player import Player

gestures = ['1', '2', '3', '4', '5']

class Commputer(Player):
    def __init__(self):
        super().__init__()

    def ran_gesture(self):

        com_gesture = random.choice(gestures)

        if com_gesture == '1':
            print('I chose Rock!')
        elif com_gesture == '2':
            print('I chose paper!')
        elif com_gesture == '3':
            print('I chose Scissors!')
        elif com_gesture == '4':
            print('I chose Lizard!')
        elif com_gesture == '5':
            print('I chose Spock!')
        else:
            ()