import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [ rock , paper , scissors ]
your_turn = int ( input ( "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.") )
if your_turn >= 3 or your_turn < 0:
    print ( "You typed invalid number. You lost!" )
else:
    print ( game_images[ your_turn ] )

    computer_turn = random.randint ( 0 , 2 )
    print ( f"Computer choice is {computer_turn}" )
    print ( game_images[ computer_turn ] )

    if your_turn == 0 and computer_turn == 2 :
        print ( "You Win!" )
    elif computer_turn == 0 and your_turn == 2 :
        print ( "You Lost!" )
    elif computer_turn > your_turn :
        print ( "You Lost!" )
    elif your_turn > computer_turn :
        print ( "You Win!" )
    elif computer_turn == your_turn :
        print ( "It is a draw!" )
