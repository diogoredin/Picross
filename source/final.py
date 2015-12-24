#######   Diogo Redin 84711 . Diogo Vilela 84710 . G027   ######
#
#
#   GAME PICROSS - PROJECT II FP
#   https://en.wikipedia.org/wiki/Nonogram
#
#
################################################################

################################################################
#
#   INDEX
#
#   1. Coordinate
#     1.1. create_coordinate
#     1.2. coordinate_line
#     1.3. coordinate_column
#     1.4. is_coordinate
#     1.5. same_coordinates
#     1.6. coordinate_to_string
#
#   2. Move
#     2.1. create_move
#     2.2. move_coordinate
#     2.3. move_value
#     2.4. is_move
#     2.5. same_moves
#     2.6. move_to_string
#
#   3. Board
#     3.1. create_board
#     3.2. board_dimensions
#     3.3. board_specifications
#     3.4. board_cell
#     3.5. fill_board_cell
#     3.6. is_board
#     3.7. complete_board
#     3.8. same_board
#     3.9. print_board
#
#   4. Adictional Funcions
#     4.1. read_board
#     4.2. ask_move
#     4.3. empty_board_cells
#     4.4. complete_line
#     4.5. picross_game
#
################################################################


from coordinate import *
from move import *
from board import *
import subprocess as sp
import os
import platform

################################################################
#
#   FUNCOES ADICIONAIS
#   - le_tabuleiro
#   - pede_jogada
#   - tabuleiro_celulas_vazias
#   - linha_completa
#   - jogo_picross
#
################################################################

# Funcao le tabuleiro
def le_tabuleiro(level, nr_gm):
    '''le_tabuleiro : cad. caracteres -> tuplo
       le_tabuleiro(espec) recebe como argumento uma cadeia de caracteres que corresponde ao nome do 
       ficheiro com os dados de especificacao do jogo, e devolve um tuplo de dois tuplos com a 
       especificacao das linhas e colunas.'''

    # Importa modulo ast que permite avaliar a string contida no ficheiro sem riscos. Apenas sao
    # avaliadas funcoes python do tipo tuplo, lista, dicionario, booleano, string, numero e None. 
    # https://docs.python.org/2/library/ast.html#ast.literal_eval
    from ast import literal_eval
    
    # Abre ficheiro, le e fecha
    f1 = open('../resources/Levels/Level_'+str(level)+'/'+str(nr_gm)+'.txt', 'r')
    l1 = f1.readline()
    f1.close()

    # E usada a funcao cria_tabuleiro para testar a validade dos argumentos
    return tabuleiro_especificacoes(cria_tabuleiro(literal_eval(l1)))

# Funcao pede jogada
def pede_jogada(t):
    '''pede_jogada : tabuleiro -> jogada
       le_tabuleiro(tab) recebe como argumento o tabuleiro do jogo e devolve a jogada que o jogador 
       pretende executar.'''

    # Testa se recebe tabuleiro
    if not(e_tabuleiro(t)):
        raise ValueError('pede_jogada: argumentos invalidos')

    linha_max = tabuleiro_dimensoes(t)[0]
    coluna_max = tabuleiro_dimensoes(t)[1]
    coordenada_min = coordinate_to_string(create_coordinate(1,1))
    coordenada_max = coordinate_to_string(create_coordinate(linha_max,coluna_max))

    # Pede jogada ao utilizador
    print('Introduza a jogada')
    coordenada = input('- coordenada entre ' + coordenada_min + ' e ' + coordenada_max + ' >> ')
    valor = input('- valor >> ')

    # Se for introduzida jogada
    if (coordenada != '' and valor != ''):

        # Extrai numeros introduzidos para a coordenada
        arg1 = list(filter(lambda x: x.isdigit(), coordenada.rsplit(' : ', 1)[0]))
        arg2 = list(filter(lambda x: x.isdigit(), coordenada.rsplit(' : ', 1)[1]))
        valor = int(valor)
        lin = int(''.join(n for n in arg1 if n.isdigit()))
        col = int(''.join(n for n in arg2 if n.isdigit()))

        # Se for valida para o tabuleiro criamos jogada
        if ( 0 < lin < linha_max+1 and 0 < col < coluna_max+1 ):
            return cria_jogada(create_coordinate(lin,col),valor)
        else:
            return False

# Funcao tabuleiro celulas vazias
def tabuleiro_celulas_vazias(t):
    '''tabuleiro_celulas_vazias : tabuleiro -> lista
       tabuleiro_celulas_vazias(t) recebe como recebe como argumento um elemento do tipo tabuleiro e 
       devolve uma lista com as coordenadas das celulas do tabuleiro que estao vazias.'''

    # Testa se recebe tabuleiro
    if not(e_tabuleiro(t)):
        raise ValueError('tabuleiro_celulas_vazias: argumentos invalidos')

    # Dimensoes
    qtd_linhas = tabuleiro_dimensoes(t)[0]
    qtd_colunas = tabuleiro_dimensoes(t)[1]
    # Lista celulas vazias
    lista = []

    # Percorre todas as celulas
    for linha in range(1,qtd_linhas+1):
        for coluna in range(1,qtd_colunas+1):

            # Testa celula
            coordenada = create_coordinate(linha,coluna)
            if tabuleiro_celula(t, coordenada) == 0:
                lista.append(coordenada)

    return lista

# Funcao linha completa
def linha_completa(especificacoes,celulas):
    '''linha_completa : tuplo x lista -> logico
       linha_completa(t) recebe como argumento um tuplo com a especificacao de uma linha ou coluna, e 
       uma lista com os conteudos das celulas de uma linha / coluna, e verifica se a linha / coluna em 
       questao satisfaz a especificacao recebida.'''

    # Lista com o numero de blocos seguidos de celulas preenchidas ("especificacoes")
    lista_ocorrencias = []

    somador = 0

    # Por cada celula dada
    for celula in range(0, len(celulas)):

        # Se a celula esta preenchida registamos a ocorrencia num somador
        if celulas[celula] == 2:
            somador += 1

        # Se a celula nao esta preenchida fazemos reset ao somador e registamos o valor que tinha
        # (que corresponde ao numero de celulas preenchidas seguidas que encontramos)
        else:
            if somador != 0:
                lista_ocorrencias.append(somador)
                somador = 0
        
    # Caso fossem todas preenchidas temos de passar o somador na mesma
    if somador != 0:
        lista_ocorrencias.append(somador)

    # Se ha celulas vazias a linhas nao esta completa
    if not(any(celulas[celula] == 0 for celula in range(0, len(celulas)))):

        # Se os blocos de celulas preenchidas sao iguais as especificacoes, a linha / coluna esta correta
        return (especificacoes == tuple(lista_ocorrencias))

    else:
        return False


def continue_game(game):
    from ast import literal_eval
    
    # Abre ficheiro, le e fecha
    f1 = open('../resources/Saved_games/'+ game +'.txt', 'r')
    spec = f1.readline()
    cells = f1. readline()
    f1.close()
    board = cria_tabuleiro(literal_eval(spec))
    board = tabuleiro_preenche_celulas(board, literal_eval(cells))
    return board

# Funcao jogo picross
def jogo_picross(level, nr_gm, choice, game):
    '''jogo_picross : cad. caracteres -> logico
       jogo_picross(espec) recebe como argumento uma cadeia de caracteres representando o nome do 
       ficheiro com a especificacao do tabuleiro, e permite jogar um jogo de Picross. Devolve True 
       caso o tabuleiro resultante do jogo esteja completo (quadro completo e de acordo com as 
       especificacoes) e False caso contrario.'''

    # Verifica o sistema em que o jogo esta a correr
    system = platform.system()

    if choice == ('n'):
        # Le ficheiro e cria tabuleiro
        especificacoes = le_tabuleiro(level, nr_gm)
        tabuleiro = cria_tabuleiro(especificacoes)
    else:
        tabuleiro = continue_game(game)
        
    # Enquanto o tabuleiro estiver com celulas por preencher
    while len(tabuleiro_celulas_vazias(tabuleiro)) != 0:

        if system == 'Linux':
            # Limpa a shell Linux
            tmp = sp.call('clear',shell=True)
        elif system == 'Darwin':
            # Limpa a shell Mac
            tmp = sp.call('cls',shell=True)
        elif system == 'Windows':
            # Limpa a shell Windows
            os.system('cls')

        print('JOGO PICROSS')

        # Mostra no ecra o tabuleiro
        escreve_tabuleiro(tabuleiro)

        # Pede jogada
        jogada = pede_jogada(tabuleiro)

        # Enquanto nao houver jogada valida pede jogada
        while e_jogada(jogada) == False:
            if jogada == False:
                print('Jogada invalida.')
                jogada = pede_jogada(tabuleiro)

        # Atualiza tabuleiro
        coordenada = jogada_coordenada(jogada)
        valor = jogada_valor(jogada)

        tabuleiro_preenche_celula(tabuleiro, coordenada, valor)

    # Testa se esta resolvido corretamente
    if tabuleiro_completo(tabuleiro) == True and len(tabuleiro_celulas_vazias(tabuleiro)) == 0:
        escreve_tabuleiro(tabuleiro)
        print('JOGO: Parabens, encontrou a solucao!')
        return True
    elif tabuleiro_completo(tabuleiro) == False and len(tabuleiro_celulas_vazias(tabuleiro)) == 0:
        escreve_tabuleiro(tabuleiro)
        print('JOGO: O tabuleiro nao esta correto!')
        return False
