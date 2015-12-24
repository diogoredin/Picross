# Loader of the game

import random
from final import *

choice = 0
valid_choice = False

while (choice != 'y' and choice != 'n'):
    print ('PICROSS GAME \n \n')
    choice = input ('Do you wish to continue a game?\n>>> (Y/N): ').lower()

if choice == 'n':
    while not valid_choice:
        print ('PICROSS GAME \n \n')
        print ('3x3   --> Level 1\n5x5   --> Level 2\n10x10 --> Level 3')
        level = (input ('Chose a level --> '))
        try:
            level = int(level)
            if (level > 0 and level < 4):
                valid_choice = True
        except ValueError:
            pass
            
    f1 = open('../resources/Levels/lv_qt.txt', 'r')
    for i in range (level):
        lv_qt = int(f1.readline())
    f1.close()

    nr_gm = random.randint(1,lv_qt)
    jogo_picross(level, nr_gm, choice, '')

else:
    print ('PICROSS GAME \n \n')
    f1 = open('../resources/Saved_games/Saved_games_list.txt')
    name = f1.readline()
    f1.close()
    if name == '':
        print ('There are no saved games')

    else:
        list_games = []
        game = ''
        while not ((game + '\n') in list_games):
            f1 = open('../resources/Saved_games/Saved_games_list.txt')
            name = f1.readline() 
            print ('Which game you want to continue?')
            while name != '':
                print ('   '+ name, end ='')
                list_games.append (name)
                name = f1.readline()
            f1.close()
            print ('\n')
            game = input ('>>> ')
        jogo_picross (0, 0, choice,  game)
