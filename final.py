##############################################################
#
#   JOGO PICROSS - PROJETO II FP
#   https://en.wikipedia.org/wiki/Nonogram
#
#   - Diogo Redin 84711
#   - Diogo Vilela 84710
#
##############################################################

##############################################################
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
##############################################################

##############################################################
#
#   COORDENADA
#   - Utilizado para indexar as celulas do tabuleiro. Cada
#     celula e indexada atraves da linha (um inteiro entre 1 
#     e o numero de linhas do tabuleiro) e da coluna respetiva
#     (um inteiro entre 1 e o numero de colunas do tabuleiro) 
#     em que a celula (1 : 1) corresponde ao canto superior 
#     esquerdo do tabuleiro.
#
##############################################################

# Cria tipo coordenada
class coordenada:

    # Iniciador
    def __init__(self, lin, col):

        # Testa se sao inteiros positivos
        if not(isinstance(lin, (int)) and isinstance(col, (int)) and (lin > 0) and (col > 0)):
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

    # Igualdade
    def __eq__(self, coord):

        # Testa se recebe dois elementos do tipo coordenada
        if not(isinstance(self, (coordenada)) and isinstance(coord, (coordenada))):
            raise ValueError('coordenadas_iguais: argumentos invalidos')

        # Igual quando as linhas e colunas são iguais
        return ( ( self.get_linha() == coord.get_linha() ) and ( self.get_coluna() == coord.get_coluna()) )

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
    return (coord1 == coord2)

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

##############################################################
#
#   JOGADA
#   - Representa uma jogada a efetuar sobre um tabuleiro
#     Cada jogada e composto por uma coordenada e um valor
#     igual a 1 ou dois que representa o conteudo de uma
#     celula de um tabuleiro de picross.
#
##############################################################

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

    # Igualdade
    def __eq__(self, jog):

        # Testa se recebe dois elementos do tipo jogada
        if not(isinstance(self, (jogada)) and isinstance(jog, (jogada))):
            raise ValueError('jogadas_iguais: argumentos invalidos')

        # Igual quando as coordenadas e valor de ambos sao iguais
        return ( ( self.get_coordenada() == jog.get_coordenada() ) and ( self.get_celula() == jog.get_celula() ) )

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

    # Se recebe testa igualdade
    return (jog1 == jog2)

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