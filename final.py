#######   Diogo Redin 84711 . Diogo Vilela 84710 . G027   ######
#
#
#   JOGO PICROSS - PROJETO II FP
#   https://en.wikipedia.org/wiki/Nonogram
#
#
################################################################

################################################################
#
#   INDEX
#
#   1. Coordenada
#     1.1. cria_coordenada
#     1.2. coordenada_linha
#     1.3. coordenada_coluna
#     1.4. e_coordenada
#     1.5. coordenadas_iguais
#     1.6. coordenada_para_cadeia
#
#   2. Jogada
#     2.1. cria_jogada
#     2.2. jogada_coordenada
#     2.3. jogada_valor
#     2.4. e_jogada
#     2.5. jogadas_iguais
#     2.6. jogada_para_cadeia
#
################################################################

################################################################
#
#   COORDENADA
#   - Utilizado para indexar as celulas do tabuleiro. Cada
#     celula e indexada atraves da linha (um inteiro entre 1 
#     e o numero de linhas do tabuleiro) e da coluna respetiva
#     (um inteiro entre 1 e o numero de colunas do tabuleiro) 
#     em que a celula (1 : 1) corresponde ao canto superior 
#     esquerdo do tabuleiro.
#
#   - Repr. Interna -> Criada a estrutura de dados 'coordenada'.
#
################################################################

# Cria tipo coordenada
class coordenada:

    # Iniciador
    def __init__(self, lin, col):

        # Testa se sao inteiros positivos
        if not(isinstance(lin, (int)) and isinstance(col, (int)) and ((lin > 0) and (col > 0))):
            raise ValueError('cria_coordenada: argumentos invalidos')

        # Acede a coluna e linha
        self.linha = lin
        self.coluna = col

    # Atributo
    def get_linha(self):
        return self.linha

    # Atributo
    def get_coluna(self):
        return self.coluna

# Construtor
def cria_coordenada(lin, col): 
    '''cria_coordenada  : int x int -> coordenada
       cria_coordenada(lin, col) recebe dois argumentos positivos do tipo inteiro, linha e coluna respetivamente e 
       devolve um elemento do tipo coordenada correspondete a celula (l : c).'''
    return coordenada(lin, col)

# Seletor
def coordenada_linha(coord):
    '''coordenada_linha : coordenada -> inteiro
       coordenada_linha(coord) recebe como argumento um elemento do tipo coordenada e devolve a linha respetiva.'''
    
    # Testa se recebe uma coordenada
    if not( e_coordenada(coord) ):
        raise ValueError('coordenada_linha: argumentos invalidos')

    return coord.get_linha()

# Seletor
def coordenada_coluna(coord):
    '''coordenada_coluna : coordenada -> inteiro
       coordenada_coluna(coord) recebe como argumento um elemento do tipo coordenada e devolve a coluna respetiva.'''
    
    # Testa se recebe uma coordenada
    if not( e_coordenada(coord) ):
        raise ValueError('coordenada_coluna: argumentos invalidos')

    return coord.get_coluna()

# Reconhecedor
def e_coordenada(elem):
    '''e_coordenada : universal -> logico
       e_coordenada(elem) recebe um unico argumento e devolve True caso seja do tipo coordenada e False caso contrario.'''
    return isinstance(elem, (coordenada))

# Teste
def coordenadas_iguais(coord1, coord2):
    '''coordenadas_iguais : coordenada x coordenada -> logico
       coordenadas_iguais(coord1, coord2) recebe como argumento dois elementos do tipo coordenada e devolve True caso 
       esses elementos correspondam a mesma coordenada, e False caso contrario.'''

    # Testa se recebe uma coordenada
    if not( e_coordenada(coord1) and e_coordenada(coord2) ):
        raise ValueError('coordenadas_iguais: argumentos invalidos')

    return ( ( coordenada_linha(coord1) == coordenada_linha(coord2) ) and ( coordenada_coluna(coord1) == coordenada_coluna(coord2) ) )

# Funcao
def coordenada_para_cadeia(coord):
    '''coordenada_para_cadeia : coordenada -> cad. caracteres
       coordenada_para_cadeia(coord) recebe como argumento um elemento do tipo coordenada e devolve uma cadeia de 
       caracteres que a representa.'''

    # Testa se recebe coordenada
    if not( e_coordenada(coord) ):
        raise ValueError('coordenada_para_cadeia: argumentos invalidos')

    # Acedemos a linha e coluna
    return ( '(' + str( coordenada_linha(coord) ) + ' : ' + str( coordenada_coluna(coord) ) + ')' )

################################################################
#
#   JOGADA
#   - Representa uma jogada a efetuar sobre um tabuleiro
#     Cada jogada e composto por uma coordenada e um valor
#     igual a 1 ou dois que representa o conteudo de uma
#     celula de um tabuleiro de picross.
#
#   - Repr. Interna -> Criada a estrutura de dados 'jogada'.
#
################################################################

# Cria tipo jogada
class jogada:

    # Iniciador
    def __init__(self, coord, cel):

        # Testa se recebe um elemento do tipo coordenada e um inteiro com valor 1 ou 2, correspondente a celula
        if not(isinstance(coord, (coordenada)) and isinstance(cel, (int)) and (cel == 1 or cel == 2)):
            raise ValueError('cria_jogada: argumentos invalidos')

        # Acede a coordenada e celula
        self.coordenada = coord
        self.celula = cel

    # Atributo
    def get_coordenada(self):
        return self.coordenada

    # Atributo
    def get_celula(self):
        return self.celula

# Construtor
def cria_jogada(coord, cel):
    '''cria_joagada : coordenada x {1,2} -> jogada
       cria_jogada(coorde, cel) recebe como argumento um elemento do tipo coordenada e um inteiro com valor 1 ou 2
       e verfica a validade dos seus argumentos.'''
    return jogada(coord, cel)

# Seletor
def jogada_coordenada(jog):
    '''jogada_coordenada : jogada -> coordenada
       jogada_coordenada(jog) recebe como argumento um elemento do tipo jogada e devolve a coordenada respetiva.'''

    # Testa se recebe uma joagda
    if not( e_jogada(jog) ):
        raise ValueError('jogada_coordenada: argumentos invalidos')

    # Se for devolve coordenada
    return jog.get_coordenada()

# Seletor
def jogada_valor(jog):
    '''jogada_valor : jogada -> {1,2}
       jogada_valor(jog) recebe como argumento um elemento do tipo jogada e devolve o valor respetivo.'''

    # Testa se recebe uma jogada
    if not( e_jogada(jog) ):
        raise ValueError('jogada_valor: argumentos invalidos')

    # Se for devolve celula
    return jog.get_celula()

# Reconhecedor
def e_jogada(elem):
    '''e_jogada : universal -> logico
       e_jogada(elem) recebe um unico argumento e devolve True caso seja do tipo jogada e False caso contrario.'''
    return isinstance(elem, (jogada))

# Teste
def jogadas_iguais(jog1, jog2):
    '''jogadas_iguais : jogada x jogada -> logico
       jogadas_iguais(jog1, jog2) recebe como argumento dois elementos do tipo jogada e devolve True caso esses elementos
       correspondam a mesma jogada, e False caso contrario.'''

    # Testa se recebe dois elementos do tipo jogada
    if not(isinstance(jog1, (jogada)) and isinstance(jog2, (jogada))):
        raise ValueError('jogadas_iguais: argumentos invalidos')

    return ( ( jogada_coordenada(jog1) == jogada_coordenada(jog2) ) and ( jogada_valor(jog1) == jogada_valor(jog2) ) )

# Funcao
def jogada_para_cadeia(jog):
    '''jogada_para_cadeia : jogada -> cad. caracteres
       jogada_para_cadeia(jog) recebe como argumento um elemento do tipo jogada e devolve uma cadeia de caracteres que
       a representa.'''

    # Testa se recebe duas jogadas
    if not( e_jogada(jog) ):
        raise ValueError('jogada_para_cadeia: argumentos invalidos')

    # Primeiro acedemos a coordenada da jogada e transformamos numa cadeia de caracteres e depois acedemos a 
    # celula da jogada
    return ( str( coordenada_para_cadeia( jogada_coordenada(jog) ) ) + ' --> ' + str( jogada_valor(jog) ) )

################################################################
#
#   TABULEIRO
#   - Representa uma jogada a efetuar sobre um tabuleiro
#     Cada jogada e composto por uma coordenada e um valor
#     igual a 1 ou dois que representa o conteudo de uma
#     celula de um tabuleiro de picross.
#
#   - Repr. Interna -> Criada a estrutura de dados 'tabuleiro'.
#
################################################################

# Cria tipo tabuleiro
class tabuleiro:

    # Iniciador
    def __init__(self, t, cel):

        # exemplo do t - ( ( (0,0),(0,0),(0,0) ), ( (0,0),(0,0),(0,0) ) )
        # corresponde a especificacoes do tabuleiro em cada tuplo
        # dentro do tuplo principal corresponde a linhas e colunas
        # respetivamente. Cada tuplo dentro do tuplo das linhas / colunas
        # corresponde as especificacoes para essa linha / coluna.

        # exemplo do cel - [[0,0,0],[0,0,0],[0,0,0]] 
        # corresponde a celulas do tabuleiro em que cada lista corresponde a 
        # uma linha do tabuleiro e cada elemento dessa lista contem o valor das
        # celulas dessa linha. Existem tantas celulas numa linha quanto colunas.

        # se o argumento t e um tuplo
        if not( isinstance(t, (tuple))
                # se as celulas sao lista
                and isinstance(cel, (list))
                # se as linhas sao lista
                and all( isinstance(linhas, (list)) for linhas in cel )
                # se as celulas sao 0, 1, 2
                and all( celulas in (0,1,2) for linhas in cel for celulas in linhas )
                # se o numero de listas construidos e o correto (uma lista por cada linha)
                and len(cel) == len(t[0])
                # se o numero de celulas construidos e o correto (uma celula por cada coluna)
                and all( len(linhas) == len(t[1]) for linhas in cel )
                # se o tuplo t contem dois tuplos
                and len(t) == 2
                # se os elementos do tuplo sao tuplos
                and all( isinstance(tuplos, (tuple)) for tuplos in t )
                # se esses tuplos nao sao vazios
                and all( len(tuplos) > 0 for tuplos in t )
                # se as especificacoes sao inteiras
                and all( isinstance(espec, (tuple)) for tuplos in t for espec in tuplos )
                # se as especificacoes sao inteiras
                and all( isinstance(elem, (int)) for tuplos in t for espec in tuplos for elem in espec )
                # se as especificacoes sao positivas
                and all( (elem > 0) for tuplos in t for espec in tuplos for elem in espec )):
    
            raise ValueError('cria_tabuleiro: argumentos invalidos')

        # Criamos linhas, colunas e celulas conforme o tuplo recebido
        self.linhas = tuple(t[0])
        self.colunas = tuple(t[1])
        self.celulas = cel

    # Atributo
    def get_linhas(self):
        return self.linhas

    # Atributo
    def get_colunas(self):
        return self.colunas

    # Atributo
    def get_celulas(self):
        return self.celulas

# Construtor
def cria_tabuleiro(t):
    '''cria_tabuleiro : tuplo -> tabuleiro
       cria_tabuleiro(t) recebe como argumento um elemento t do tipo tuplo descrevendo a especificacao das 
       linhas e das colunas do tabuleiro, e devolve um elemento do tipo tabuleiro.'''

    # Cria lista para cada linha, e cria um elemento a 0 por cada coluna (tabuleiro vazio)
    # exemplo de tabuleiro 3x3: [[0,0,0],[0,0,0],[0,0,0]]
    cel = [[0 for linha in range(len(t[0]))] for coluna in range(len(t[1]))]

    return tabuleiro(t, cel)

# Seletor
def tabuleiro_especificacoes(t):
    '''tabuleiro_especificacoes : tabuleiro -> tuplo
       tabuleiro_especificacoes(t) recebe como argumento um elemento t do tipo tabuleiro e devolve um tuplo composto 
       por dois tuplos de tuplos de inteiros, cujo primeiro elemento corresponde a especificacao das linhas 
       e o segundo a especificacao das colunas.'''

    # Acede linhas e colunas do tabuleiro
    spec_linhas = t.get_linhas()
    spec_colunas = t.get_colunas()

    # Cria tuplo com as especificacoes das linhas e colunas
    spec = (spec_linhas, spec_colunas)

    # Devolve especificacoes
    return spec

# Seletor
def tabuleiro_celulas(t):
    '''tabuleiro_celulas : tabuleiro -> lista
       tabuleiro_celulas(t) recebe como argumento um elemento t do tipo tabuleiro e devolve uma lista composta 
       por tantas listas quantas linhas o tabuleiro tiver. Cada lista contem o valor das celulas correspondentes a
       respetiva linha.'''
    return t.get_celulas()

# Seletor
def tabuleiro_dimensoes(t):
    '''tabuleiro_dimensoes : tabuleiro -> tuplo
       tabuleiro_dimensoes(t) recebe como argumento um elemento t do tipo tabuleiro e devolve um tuplo 
       com dois elementos, cujo primeiro elemento e o numero de linhas do tabuleiro e o segundo o numero 
       de colunas do mesmo.'''

    # Vai buscar as especificacoes do tabuleiro
    # spec vai ser um tuplo com as especificacoes das linhas na
    # primeira entrada e com especificacoes das colunas na segunda entrada
    spec = tabuleiro_especificacoes(t)

    # Calcula dimensao das especificacoes das linhas
    dim_linhas = len(spec[0])

    # Calcula dimensao das especificacoes das linhas
    dim_colunas = len(spec[1])

    # Cria um tuplo com as dimensoes
    dim = (dim_linhas,dim_colunas)

    # Devolve dimensoes
    return dim

# Seletor
def tabuleiro_celula(t, c):
    '''tabuleiro_celula : tabuleiro x coordenada -> {0, 1, 2}
       tabuleiro_celula(t) recebe como argumentos um elemento t do tipo tabuleiro e um elemento c do 
       tipo coordenada e devolve um elemento do tipo inteiro entre 0 e 2, que corresponde ao valor contido na 
       celula do tabuleiro referente a coordenada c. 0 - celula vazia / 1 - celula branca / 2 - celula preenchida.'''

    # Testa se recebe argumentos corretos
    if not( e_tabuleiro(t) and e_coordenada(c) ):
        raise ValueError('tabuleiro_celula: argumentos invalidos')

    # Acede a linha e coluna da coordenada dada
    linha = coordenada_linha(c)
    coluna = coordenada_coluna(c)

    # Cria lista com celulas do tabuleiro
    celulas = tabuleiro_celulas(t)

    # Acede ao valor da celula no tabuleiro na linha e coluna especificadas
    valor_celula = celulas[linha-1][coluna-1]

    return valor_celula

# Modificador
def tabuleiro_preenche_celula(t, c, e):
    '''tabuleiro_preenche_celula :  tabuleiro × coordenada × {0, 1, 2} -> tabuleiro
       tabuleiro_preenche_celula(t, c, e) recebe como argumentos um elemento t do tipo tabuleiro, um elemento c do tipo 
       coordenada e um inteiro e entre 0 e 2, e modifica o tabuleiro t, preenchendo a celula referente a coordenada c 
       com o elemento e, que pode ser 0, 1 ou 2. 0 - celula vazia / 1 - celula branca / 2 - celula preenchida. Devolve
       o tabuleiro modificado na celula especificada.'''

    # Testa se recebe argumentos corretos
    if not( e_tabuleiro(t) and e_coordenada(c) and e in (0,1,2) ):
        raise ValueError('tabuleiro_preenche_celula: argumentos invalidos')

    # Acede a linha e coluna da coordenada dada
    linha = coordenada_linha(c)
    coluna = coordenada_coluna(c)

    # Cria lista com celulas do tabuleiro
    celulas = tabuleiro_celulas(t)

    # Guarda na posicao especificada o novo elemento
    celulas[linha-1][coluna-1] = e

    # Cria novo tabuleiro com as mesmas especificacoes e celula alterada
    return tabuleiro(tabuleiro_especificacoes(t), celulas)

# Reconhecedor
def e_tabuleiro(t):
    '''e_tabuleiro : universal -> logico
       e_tabuleiro(t) recebe um argumento e devolve True caso seja do tipo tabuleiro e False caso contrario.'''
    return isinstance(t, tabuleiro)

# Reconhecedor
def tabuleiro_completo(t):
    '''tabuleiro_completo : tabuleiro -> logico
       tabuleiro_completo(t) recebe como argumento um tabuleiro e devolve True caso esteja totalmente preenchido de 
       acordo com as suas especificacoes e False caso contrario.'''

    # Testa se recebe tabuleiro
    if not( e_tabuleiro(t) ):
        raise ValueError('tabuleiro_completo: argumentos invalidos')

    # Cria lista com celulas do tabuleiro
    celulas = tabuleiro_celulas(t)

    # Especificacoes linhas e colunas
    linhas = tabuleiro_especificacoes(t)[0]
    colunas = tabuleiro_especificacoes(t)[1]

    qtd_linhas = tabuleiro_dimensoes(t)[0]
    qtd_colunas = tabuleiro_dimensoes(t)[1]

    if not( # Testa se ha celulas vazias
            len(tabuleiro_celulas_vazias(t)) == 0
            ):
        return False
    else:
        return True

# Teste
def tabuleiros_iguais(t1, t2):
    '''tabuleiros_iguais : tabuleiro x tabuleiro -> logico
       tabuleiros_iguais(t1, t2) recebe como argumento dois elementos do tipo tabuleiro e devolve True caso esses elementos
       correspondam ao mesmo tabuleiro, e False caso contrario.'''

    # Testa se recebe tabuleiro
    if not( e_tabuleiro(t1) and e_tabuleiro(t2)):
        raise ValueError('tabuleiros_iguais: argumentos invalidos')

    # Igual quando as linhas, colunas e celulas sao iguais
    return ( ( tabuleiro_especificacoes(t1)[0] == tabuleiro_especificacoes(t2)[0] ) and
             ( tabuleiro_especificacoes(t1)[1] == tabuleiro_especificacoes(t2)[1] ) and 
             ( tabuleiro_celulas(t1) == tabuleiro_celulas(t2) ) )

# Funcao
def escreve_tabuleiro(t):
    '''escreve_tabuleiro : tabuleiro -> {}
       escreve_tabuleiro(t) recebe como argumento um elemento t do tipo tabuleiro e escreve para o ecra a representacao 
       externa de um tabuleiro de Picross.'''

    # Testa se recebe tabuleiro
    if not( e_tabuleiro(t) ):
        raise ValueError('escreve_tabuleiro: argumentos invalidos')

    # Elementos do Tabuleiro
    spec = tabuleiro_especificacoes(t)
    linhas = spec[0]
    colunas = spec[1]

    # Dimensoes do Tabuleiro
    dim = tabuleiro_dimensoes(t)
    qtd_linhas = dim[0]
    qtd_colunas = dim[1]

    # ESPECIFICACOES DAS COLUNAS
    # Criamos lista para colocar as 'linhas' que vamos criar com as especificacoes das colunas
    # Esta lista tem tantas 'linhas' quantas especificacoes tiver a coluna com mais especificacoes
    # exemplo de uma linha '2 2 2 3 3' ou '    1    '. A linha e uma string.
    especificacoes_das_colunas = ['  ']*len(max(colunas, key=len))

    # Percorremos cada par de especificacoes ex: (1,2)
    for especificacao in range(0, qtd_colunas):

        # Invertemos as especificacoes para as ler por ordem de escrita no ecra ex: (2,1)
        nova_especificacao = colunas[especificacao][::-1]

        # Por cada linha criada escrevemos a especificacao se existir
        for linha_de_especificacoes in range(0, len(especificacoes_das_colunas)):

            # Existe se o indice da lista for menor que o numero de elementos na especificacao
            # Se for maior nao existe especificacao a escrever
            if linha_de_especificacoes < len(colunas[especificacao]):
                especificacoes_das_colunas[linha_de_especificacoes] = especificacoes_das_colunas[linha_de_especificacoes] + str(nova_especificacao[linha_de_especificacoes]) + '    '
            else:
                especificacoes_das_colunas[linha_de_especificacoes] = especificacoes_das_colunas[linha_de_especificacoes] + '     '

    # Mostra para o ecra a(s) linha(s) criada(s) por ordem inversa
    for linha_de_especificacoes in reversed(range(0, len(especificacoes_das_colunas))):
        print(especificacoes_das_colunas[linha_de_especificacoes])

    # CONTEUDO DAS CELULAS
    # Para cada linha que contem as celulas respetivas
    for linha in range(1, qtd_linhas+1):

        nova_linha = ''
        # Acedemos a celula de cada linha
        for coluna in range(1, qtd_colunas+1):
 
            # Vazio
            if tabuleiro_celula(t, cria_coordenada(linha, coluna)) == 0:
                conteudo = '?'

            # Branco
            elif tabuleiro_celula(t, cria_coordenada(linha, coluna)) == 1:
                conteudo = '.'

            # Preenchido
            elif tabuleiro_celula(t, cria_coordenada(linha, coluna)) == 2:
                conteudo = 'x'

            # Escreve celula
            nova_linha = nova_linha + '[ ' + conteudo + ' ]'

        # ESPECIFICACOES DAS LINHAS
        # Existem tantas especificacoes por linha quanto colunas. Percorremos todas, por ordem crescente.
        for especificacao in range(0, len(linhas[linha-1])):

            # Se houver especificacoes nessa posicao
            if linhas[linha-1][especificacao] > 0:
                nova_linha = nova_linha + ' ' + str(linhas[linha-1][especificacao])

        # Espacos brancos
        espacos = len(max(linhas, key=len))-len(linhas[linha-1])
        for espaco in range(0, espacos):
            nova_linha = nova_linha + '  '

        # Proxima linha
        print(nova_linha + '|')

    print('')

################################################################
#
#   FUNCOES ADICIONAIS
#   - le_tabuleiro
#   - pede_jogada
#   - jogo_picross
#   - tabuleiro_celulas_vazias
#   - linha_completa
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

    coordenada_min = coordenada_para_cadeia(cria_coordenada(1,1))
    coordenada_max = coordenada_para_cadeia(cria_coordenada(tabuleiro_dimensoes(t)[0],tabuleiro_dimensoes(t)[1]))

    print('Introduza a jogada')
    coordenada = input('- coordenada entre ' + coordenada_min + ' e ' + coordenada_max + ' >> ')
    valor = input('- valor >> ')

    while coordenada == '' or valor == '' or int(valor) not in (1,2):
        print('Jogada invalida.\nIntroduza a jogada')
        coordenada = input('- coordenada entre ' + coordenada_min + ' e ' + coordenada_max + ' >> ')
        valor = input('- valor >> ')

    # Extrai numeros introduzidos para a coordenada
    argumentos = list(filter(lambda x: x.isdigit(), coordenada))
    coordenada = cria_coordenada(int(argumentos[0]),int(argumentos[1]))

    return cria_jogada(coordenada,int(valor))

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

    # Enquanto o tabuleiro nao estiver completo
    while not(tabuleiro_completo(tabuleiro)):

        # Mostra no ecra o tabuleiro
        escreve_tabuleiro(tabuleiro)

        # Pede jogada
        jogada = pede_jogada(tabuleiro)

        # Atualiza tabuleiro
        coordenada = jogada_coordenada(jogada)
        valor = jogada_valor(jogada)

        tabuleiro = tabuleiro_preenche_celula(tabuleiro, coordenada, valor)

    # Mostra tabuleiro resolvido
    escreve_tabuleiro(tabuleiro)

    print('JOGO: Parabens, encontrou a solucao!')
    return True