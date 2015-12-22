################################################################
#
#   TABULEIRO
#   - Representa um tabuleiro de picross.
#
#   - Repr. Interna -> Criada a estrutura de dados 'tabuleiro'.
#
################################################################

from coordinate import *

# Cria tipo tabuleiro
class tabuleiro:

    # Iniciador
    def __init__(self, t):

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
                # se o tuplo t contem dois tuplos
                and len(t) == 2
                # se os elementos do tuplo sao tuplos
                and all( isinstance(tuplos, (tuple)) for tuplos in t )
                # se esses tuplos nao sao vazios
                and all( len(tuplos) > 0 for tuplos in t )
                # se as especificacoes sao tuplos
                and all( isinstance(espec, (tuple)) for tuplos in t for espec in tuplos )
                # se as especificacoes sao inteiras
                and all( isinstance(elem, (int)) for tuplos in t for espec in tuplos for elem in espec )
                # se as especificacoes sao positivas
                and all( (elem > 0) for tuplos in t for espec in tuplos for elem in espec )):
    
            raise ValueError('cria_tabuleiro: argumentos invalidos')

        # Criamos linhas, colunas e celulas conforme o tuplo recebido
        self.linhas = tuple(t[0])
        self.colunas = tuple(t[1])
        self.celulas = [[0 for linha in range(len(t[0]))] for coluna in range(len(t[1]))]

    # Atributo
    def get_linhas(self):
        return self.linhas

    # Atributo
    def get_colunas(self):
        return self.colunas

    # Atributo
    def get_celulas(self):
        return self.celulas

    # Modificador
    def preenche_celula(self, linha, coluna, e):
        self.celulas[linha-1][coluna-1] = e
        return self

# Construtor
def cria_tabuleiro(t):
    '''cria_tabuleiro : tuplo -> tabuleiro
       cria_tabuleiro(t) recebe como argumento um elemento t do tipo tuplo descrevendo a 
       especificacao das linhas e das colunas do tabuleiro, e devolve um elemento do tipo 
       tabuleiro.'''
    return tabuleiro(t)

# Seletor
def tabuleiro_especificacoes(t):
    '''tabuleiro_especificacoes : tabuleiro -> tuplo
       tabuleiro_especificacoes(t) recebe como argumento um elemento t do tipo tabuleiro e 
       devolve um tuplo composto por dois tuplos de tuplos de inteiros, cujo primeiro elemento 
       corresponde a especificacao das linhas e o segundo a especificacao das colunas.'''

    # Testa se recebe argumentos corretos
    if not( e_tabuleiro(t) ):
        raise ValueError('tabuleiro_especificacoes: argumentos invalidos')

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
       tabuleiro_celulas(t) recebe como argumento um elemento t do tipo tabuleiro e devolve uma 
       lista composta por tantas listas quantas linhas o tabuleiro tiver. Cada lista contem o 
       valor das celulas correspondentes a respetiva linha.'''
    
    # Testa se recebe argumentos corretos
    if not( e_tabuleiro(t) ):
        raise ValueError('tabuleiro_celulas: argumentos invalidos')

    # Acede celulas do tabuleiro
    celulas = t.get_celulas()

    # Retorna lista com celulas
    return [[elemento for elemento in linha] for linha in celulas]

# Seletor
def tabuleiro_dimensoes(t):
    '''tabuleiro_dimensoes : tabuleiro -> tuplo
       tabuleiro_dimensoes(t) recebe como argumento um elemento t do tipo tabuleiro e devolve 
       um tuplo com dois elementos, cujo primeiro elemento e o numero de linhas do tabuleiro e 
       o segundo o numero de colunas do mesmo.'''

    # Testa se recebe argumentos corretos
    if not( e_tabuleiro(t) ):
        raise ValueError('tabuleiro_dimensoes: argumentos invalidos')

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
       tipo coordenada e devolve um elemento do tipo inteiro entre 0 e 2, que corresponde ao valor 
       contido na celula do tabuleiro referente a coordenada c. 0 - celula vazia / 1 - celula 
       branca / 2 - celula preenchida.'''

    # Testa se recebe tabuleiro e coordenada
    if not( e_tabuleiro(t) and is_coordinate(c) ):
        raise ValueError('tabuleiro_celula: argumentos invalidos')

    linha_max = tabuleiro_dimensoes(t)[0]
    coluna_max = tabuleiro_dimensoes(t)[1]

    linha = coordinate_line(c)
    coluna = coordinate_column(c)

    # Testa se coordenada esta dentro do tabuleiro
    if not( 0 < linha < linha_max+1 and 0 < coluna < coluna_max+1 ):
        raise ValueError('tabuleiro_celula: argumentos invalidos')

    # Cria lista com celulas do tabuleiro
    celulas = tabuleiro_celulas(t)

    # Acede ao valor da celula no tabuleiro na linha e coluna especificadas
    valor_celula = celulas[linha-1][coluna-1]

    return valor_celula

# Modificador
def tabuleiro_preenche_celula(t, c, e):
    '''tabuleiro_preenche_celula :  tabuleiro × coordenada × {0, 1, 2} -> tabuleiro
       tabuleiro_preenche_celula(t, c, e) recebe como argumentos um elemento t do tipo tabuleiro, um 
       elemento c do tipo coordenada e um inteiro e entre 0 e 2, e modifica o tabuleiro t, preenchendo 
       a celula referente a coordenada c com o elemento e, que pode ser 0, 1 ou 2. 0 - celula vazia / 
       1 - celula branca / 2 - celula preenchida. Devolve o tabuleiro modificado na celula 
       especificada.'''

    # Testa se recebe argumentos corretos
    if not( e_tabuleiro(t) and is_coordinate(c) and e in (0,1,2) ):
        raise ValueError('tabuleiro_preenche_celula: argumentos invalidos')

    linha_max = tabuleiro_dimensoes(t)[0]
    coluna_max = tabuleiro_dimensoes(t)[1]

    linha = coordinate_line(c)
    coluna = coordinate_column(c)

    # Testa se coordenada esta dentro do tabuleiro
    if not( 0 < linha < linha_max+1 and 0 < coluna < coluna_max+1 ):
        raise ValueError('tabuleiro_preenche_celula: argumentos invalidos')

    return t.preenche_celula(linha,coluna,e)

# Reconhecedor
def e_tabuleiro(t):
    '''e_tabuleiro : universal -> logico
       e_tabuleiro(t) recebe um argumento e devolve True caso seja do tipo tabuleiro e False caso 
       contrario.'''
    return isinstance(t, tabuleiro)

# Reconhecedor
def tabuleiro_completo(t):
    '''tabuleiro_completo : tabuleiro -> logico
       tabuleiro_completo(t) recebe como argumento um tabuleiro e devolve True caso esteja totalmente 
       preenchido de acordo com as suas especificacoes e False caso contrario.'''

    # Testa se recebe tabuleiro
    if not( e_tabuleiro(t) ):
        raise ValueError('tabuleiro_completo: argumentos invalidos')

    # Cria lista com celulas do tabuleiro
    celulas = tabuleiro_celulas(t)

    # Cria lista com o conteudo das celulas de cada coluna
    colunas = [[0 for elemento in linha] for linha in celulas]

    # Percorre todas as linhas
    for linha in range(0, len(celulas)):

        # Percorre as celulas dessa linha
        for celula in range(0, len(celulas[linha])):

            # Coloca valor da celula na lista no indice igual ao indice em que o valor foi encontrado
            colunas[celula][linha] = celulas[linha][celula]

    if ( # Se o tabuleiro nao tem nenhuma celula vazia
         len(tabuleiro_celulas_vazias(t)) == 0 and
         # Testa se as linhas estao corretas
         all(linha_completa(tabuleiro_especificacoes(t)[0][linha],celulas[linha]) 
            for linha in range(0, len(celulas))) and
         # Testa se as colunas estao corretas
         all(linha_completa(tabuleiro_especificacoes(t)[1][coluna],colunas[coluna]) 
            for coluna in range(0, len(colunas)))
        ):
        return True
    else:
        return False

# Teste
def tabuleiros_iguais(t1, t2):
    '''tabuleiros_iguais : tabuleiro x tabuleiro -> logico
       tabuleiros_iguais(t1, t2) recebe como argumento dois elementos do tipo tabuleiro e devolve 
       True caso esses elementos correspondam ao mesmo tabuleiro, e False caso contrario.'''

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
       escreve_tabuleiro(t) recebe como argumento um elemento t do tipo tabuleiro e escreve para o 
       ecra a representacao externa de um tabuleiro de Picross.'''

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
                especificacoes_das_colunas[linha_de_especificacoes] = (
                    especificacoes_das_colunas[linha_de_especificacoes] + 
                    str(nova_especificacao[linha_de_especificacoes]) + '    ' )
            else:
                especificacoes_das_colunas[linha_de_especificacoes] = (
                    especificacoes_das_colunas[linha_de_especificacoes] + '     ' )

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
            if tabuleiro_celula(t, create_coordinate(linha, coluna)) == 0:
                conteudo = '?'

            # Branco
            elif tabuleiro_celula(t, create_coordinate(linha, coluna)) == 1:
                conteudo = '.'

            # Preenchido
            elif tabuleiro_celula(t, create_coordinate(linha, coluna)) == 2:
                conteudo = 'x'

            # Escreve celula
            nova_linha = nova_linha + '[ ' + conteudo + ' ]'

        # ESPECIFICACOES DAS LINHAS
        # Existem tantas especificacoes por linha quanto colunas. Percorremos todas, por 
        # ordem crescente.
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