###############################################################
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

    # Testa se sao inteiros positivos
    if not(isinstance(lin, (int)) and isinstance(col, (int)) and ((lin > 0) and (col > 0))):
        raise ValueError('cria_coordenada: argumentos invalidos')

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
