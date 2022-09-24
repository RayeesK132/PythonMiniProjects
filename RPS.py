import random
from sre_constants import REPEAT
from timeit import repeat
R = 'Rock'
P = 'Paper'
S = 'Siccors'

AIScore = 0
PlayerScore = 0
choices = [R, P, S]

print('What is your username?')

Player_name = input('')
AI_name = 'Computer'
print('\nWelcome to RPS ' + str.upper(Player_name) + '!')

while True:
    print('\nWould you like to pick Rock, paper or Sciccors?\n [Type: R, P or S]')
    answer_player = input('')
    AIChoice = random.choice(choices)

    Tie = AI_name + ' chooses ' + AIChoice + '\n It\'s a tie!'
    Winner = AI_name + ' chooses ' + AIChoice + '\n' + Player_name + ' Wins!'
    Loser = AI_name + ' chooses ' + AIChoice + '\n' + AI_name + 'Wins!'

    if str.upper(answer_player) == ('R'):
        print('\n' + Player_name + ' chooses ' + R)
        if AIChoice == (R):
            print(Tie)
        elif AIChoice == (S):
            print(Winner)
            PlayerScore = PlayerScore + 1
        else:
            print(Loser)
            AIScore = AIScore + 1
        
    if str.upper(answer_player) == ('P'):
        print('\n' + Player_name + ' chooses ' + P)
        if AIChoice == (P):
            print(Tie)
        elif AIChoice == (R):
            print(Winner)
            PlayerScore = PlayerScore + 1
        else:
            print(Loser)
            AIScore = AIScore + 1

    if str.upper(answer_player) == ('S'):
        print('\n' + Player_name + ' chooses ' + S)
        if AIChoice == (S):
            print(Tie)
        elif AIChoice == (P):
            print(Winner)
            PlayerScore = PlayerScore + 1
        else:
            print(Loser)
            AIScore = AIScore + 1
    
    print('\n' + Player_name + ' has won ', PlayerScore, 'times!')
    print('' + AI_name + ' has won ',  AIScore,  'times!')

    print('\n Would you like to play again?\n [Y or N]')
    Repeat = input('')
    if str.upper(Repeat) == ('Y'):
        Repeat = REPEAT
    else:
        break
    Repeat
    
