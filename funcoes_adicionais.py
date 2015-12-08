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
def le_tabuleiro(espec):
    '''le_tabuleiro : cad. caracteres -> tuplo
       le_tabuleiro(espec) recebe como argumento uma cadeia de caracteres que corresponde ao nome do 
       ficheiro com os dados de especificacao do jogo, e devolve um tuplo de dois tuplos com a 
       especificacao das linhas e colunas.'''

    # Importa modulo ast que permite avaliar a string contida no ficheiro sem riscos. Apenas sao avaliadas funcoes python do tipo
    # tuplo, lista, dicionario, booleano, string, numero e None. https://docs.python.org/2/library/ast.html#ast.literal_eval
    from ast import literal_eval
    
    # Abre ficheiro, le e fecha
    f1 = open(espec, 'r')
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
    coordenada_min = coordenada_para_cadeia(cria_coordenada(1,1))
    coordenada_max = coordenada_para_cadeia(cria_coordenada(linha_max,coluna_max))

    # Pede jogada ao utilizador
    print('Introduza a jogada')
    coordenada = input('- coordenada entre ' + coordenada_min + ' e ' + coordenada_max + ' >> ')
    valor = input('- valor >> ')

    # Se for introduzida jogada
    if (coordenada != '' and valor != ''):

        # Extrai numeros introduzidos para a coordenada
        argumentos = list(filter(lambda x: x.isdigit(), coordenada))
        valor = int(valor)
        lin = int(argumentos[0])
        col = int(argumentos[1])

        # Se for valida para o tabuleiro criamos jogada
        if ( 0 < lin < linha_max+1 and 0 < col < coluna_max+1 ):
            return cria_jogada(cria_coordenada(lin,col),valor)
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

    qtd_linhas = tabuleiro_dimensoes(t)[0]
    qtd_colunas = tabuleiro_dimensoes(t)[1]

    lista = []

    # Percorre todas as celulas
    for l, c in zip(range(1,qtd_linhas+1), range(1,qtd_colunas+1)):

        # Testa celula
        coordenada = cria_coordenada(l, c)
        if tabuleiro_celula(t, coordenada) == 0:
            lista.append(coordenada)

    return lista

# Funcao linha completa
def linha_completa(especificacoes,celulas):
    '''linha_completa : tuplo x lista -> logico
       linha_completa(t) recebe como argumento um tuplo com a especificacao de uma linha ou coluna, e 
       uma lista com os conteudos das celulas de uma linha / coluna, e verifica se a linha / coluna em 
       questao satisfaz a especificacao recebida.'''

# Funcao jogo picross
def jogo_picross(espec):
    '''jogo_picross : cad. caracteres -> logico
       jogo_picross(espec) recebe como argumento uma cadeia de caracteres representando o nome do 
       ficheiro com a especificacao do tabuleiro, e permite jogar um jogo de Picross. Devolve True 
       caso o tabuleiro resultante do jogo esteja completo (quadro completo e de acordo com as 
       especificacoes) e False caso contrario.'''

    print('JOGO PICROSS')

    # Le ficheiro e cria tabuleiro
    especificacoes = le_tabuleiro(espec)
    tabuleiro = cria_tabuleiro(especificacoes)

    # Enquanto o tabuleiro estiver com celulas por preencher
    while not(len(tabuleiro_celulas_vazias(tabuleiro)) == 0):

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
    if tabuleiro_completo(tabuleiro):
        escreve_tabuleiro(tabuleiro)
        print('JOGO: Parabens, encontrou a solucao!')
        return True
    else:
        escreve_tabuleiro(tabuleiro)
        print('JOGO: O tabuleiro nao esta correto!')
        return False
