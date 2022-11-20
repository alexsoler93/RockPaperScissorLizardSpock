from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

def make__gesture(self,):
    
    gesture = input("Make your choice!")

    if gesture == '1':
        print('You chose Rock!')
    elif gesture == '2':
        print('You chose Paper!')
    elif gesture == '3':
        print('You chose Scissors!')
    elif gesture == '4':
        print('You chose Lizard!')
    elif gesture == '5':
        print('You chose Spock!')
    else:
        print('Input not valid')
    


