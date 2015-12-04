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
    def __init__ (self, lin, col):

        # Testa se sao inteiros positivos
        if not(isinstance(lin, (int)) and isinstance(col, (int)) and (lin > 0) and (col > 0)):
            raise ValueError('cria_coordenada: argumentos invalidos')

        # Acede a coluna e linha
        self.linha = lin
        self.coluna = col

    # Igualdade
    def __eq__(self, coord1, coord2):

        # Testa se recebe dois elementos do tipo jogada
        if not(isinstance(coord1, (coordenada)) and isinstance(coord2, (coordenada))):
            raise ValueError('coordenadas_iguais: argumentos invalidos')

        # Igual quando as linhas e colunas são iguais
        return ( (coord1.linha() == coord2.linha()) and (coord1.coluna() == coord2.coluna()) )

    # Seletor
    def coluna(self):
        return self.coluna

    # Seletor
    def linha(self):
        return self.linha

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
    return coord.linha()

# Seletor
def coordenada_coluna(coord):
    '''coordenada_coluna : coordenada -> inteiro
       coordenada_coluna(coord) recebe como argumento um elemento do tipo coordenada e devolve a coluna respetiva.'''
    return coord.coluna()

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
    return ( '(' + coord.linha() + ' : ' + coord.coluna + ')' )