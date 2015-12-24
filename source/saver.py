def saver(t, flag):
    cleaning()
    print ('Picross \n \n ')

    if flag == 'Empty':
        print('Name can\'t be empty')

    if flag = 'Space':
        print('Name can\'t have spaces')
    
    game = input('Name your game')
    if game == '':
        flag = 'Empty'
        saver (t, flag)

    if ' ' in game:
        flag = 'Space'
        saver (t, flag)

    else:
        file = open(game + '.txt', 'w')
        spec = tabuleiro_especificacoes(t)
        cells = tabuleiro_celulas(t)
        f.write (spec)
        f.write (cells)
        f.close
        
