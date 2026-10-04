import random
choices = ['rock','paper','scissor']
comp = random.choice(choices)
player = ""
while player not in choices:
    player = input("enter choice(rock/paper/scissor):").lower()
    print(f"computer chose {comp},player chose {player}")
    if player == comp:
        print("it's a TIE!!!!!!!!!!!!!!!!!")
    elif player == 'rock':
        if comp ==  'paper':
            print("paper covers rock,computer wins")
        else:
            print("rock beats scissor,player wins")
    elif player == 'paper':
        if comp == 'scissor':
            print("computer wins,scissor cuts paper")
        else:
            print("paper covers rock,player wins")
    elif player == 'scissor':
        if comp == 'rock':
            print("rock beats scissor ,comp wins")
        else:
            print("scissor cuts paper,player wins")
                  