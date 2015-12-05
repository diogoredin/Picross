class tabuleiro:
    def __init__(self, t):
        # Se o argumento e um tuplo
        if not( isinstance(t, (tuple))
                # Se o tuplo contem dois tuplos
                and len(t) == 2
                # Se os elementos do tuplo sao tuplos
                and all( isinstance(tuplos, (tuple)) for tuplos in t )
                # Se esses tuplos nao sao vazios
                and all( len(tuplos) > 0 for tuplos in t )
                # Se as especificacoes sao inteiras
                and all( isinstance(elem, (int)) for tuplos in t for espec in tuplos for elem in espec ) 
                # Se as especificacoes sao positivas
                and all( (elem > 0) for tuplos in t for espec in tuplos for elem in espec )):
    
            raise ValueError('cria_tabuleiro: argumentos invalidos')

        # Acede as linhas, colunas e celulas
        self.linhas = t[0]
        self.colunas = t[1]
        self.celulas = [[0 for x in range (len(self.colunas))] for y in range (len(self.linhas))]

    # Atributo
    def get_linhas (self):
        return self.linhas

    # Atributo
    def get_colunas (self):
        return self.colunas

    # Atributo
    def get_celulas (self):
        return self.celulas

    # Igualdade
    def __eq__ (self, tab):
            spec1 = tabuleiro_especificacoes(self)
            spec2 = tabuleiro_especificacoes(tab)
            celulas1 = tabuleiro_celulas(self)
            celulas2 = tabuleiro_celulas(tab)
            return (spec1 == spec2 and celulas1 == celulas2)


# Construtor
def cria_tabuleiro(spec):
    '''cria_tabuleiro : tuple -> tabuleiro 
    cria_tabuleiro(spec) recebe como argumento um tuplo composto 
    por dois tuplos de tuplos de inteiros, em que o primeiro tuplo corresponde
    a especificacao das linhas e o segundo a especificacao das colunas
    cria_tabuleiro devolve um objeto do tipo tabuleiro'''

    if not( isinstance(t, (tuple))
                # Se o tuplo contem dois tuplos
                and len(t) == 2
                # Se os elementos do tuplo sao tuplos
                and all( isinstance(tuplos, (tuple)) for tuplos in t )
                # Se esses tuplos nao sao vazios
                and all( len(tuplos) > 0 for tuplos in t )
                # Se as especificacoes sao inteiras
                and all( isinstance(elem, (int)) for tuplos in t for espec in tuplos for elem in espec ) 
                # Se as especificacoes sao positivas
                and all( (elem > 0) for tuplos in t for espec in tuplos for elem in espec )):
    
            raise ValueError('cria_tabuleiro: argumentos invalidos')
    
    return tabuleiro(spec)

# Reconhecedor
def e_tabuleiro(elem):
    '''e_tabuleiro : universal -> logico
    e_tabuleiro(elem) recebe um unico argumento e devolve
    True se o argumento for do tipo tabuleiro e False caso contrario'''
    return isinstance(elem, tabuleiro)

# Seletor
def tabuleiro_especificacoes(tab):
    '''tabuleiro_especificacoes : tabuleiro -> tuple 
    cria_tabuleiro(tab) recebe como argumento um objeto do tipo tabuleiro e
    devolve um tuplo com as especificacoes do tabuleiro '''

    # Testa se o argumento e do tipo tabuleiro
    if not e_tabuleiro(tab):
        raise ValueError('tabuleiro_especificacoes: argumentos invalidos')

    # Se for tabuleiro:
    # Obtem as especificacoes das linhas
    spec_linhas = tab.get_linhas()
    # Obtem as especificacoes das colunas
    spec_colunas = tab.get_colunas()
    # Junta as especificacoes das linhas e das colunas num tuplo
    spec = (spec_linhas, spec_colunas)
    # Devolve o tuplo criado
    return spec

# Seletor
def tabuleiro_celulas(tab):
    '''tabuleiro_celulas : tabuleiro -> list 
    tabuleiro_celulas(tab) recebe como argumento um objeto do tipo tabuleiro e
    devolve uma lista constituida por listas com os valores que estao 
    em cada celula do tabuleiro'''
    # Testa se o argumento e do tipo tabuleiro
    if not e_tabuleiro(tab):
        raise ValueError('tabuleiro_celulas: argumentos invalidos')
   
    # Se for tabuleiro:
    # Obtem a lista com os valores das celulas
    celulas = tab.get_celulas()
    # Devolve a lista obtida
    return celulas

# Seletor
def tabuleiro_celulas_linha(tab, line):
    '''tabuleiro_celulas_linha : tabuleiro x int -> list
    tabuleiro_celulas_linha(tab, line) recebe como argumentos um objeto do 
    tipo tabuleiro e um argumeno do tipo inteiro correspondente a uma linha
     e devolve uma lista com os valores das celulas da linha'''
    
    # Testa se o argumento tab e do tipo tabuleiro
    if not e_tabuleiro(tab)
        raise ValueError('tabuleiro_celulas_linha: tabuleiro invalido')

    # Testa se o argumento line e do tipo int    
    if not (isinstance(line, int)):
        raise ValueError('tabuleiro_celulas_linha: linha invalida')

    # Testa se a linha introduzida esta contida no tabuleiro indicado
    dimensoes = tabuleiro_dimensoes(tab)
    qtd_linhas = dimensoes[0]
    if not (line => 0)
        and ((qtd_linhas - 1) => line):
        raise ValueError('tabuleiro_celulas_linha: linha fora do tabuleiro')

    # Se os argumentos introduzidos sao validos:
    # Obtem os valores de todas as celulas do tabuleiro
    celulas = tabuleiro_celulas (tab)
    # Dos valores obtidos, obtem os valores das celulas da linha selecionada
    valores_linha = celulas[line]
    # Devolve a lista com os valores obtidos
    return preenchimento_linha

# Seletor
def tabuleiro_dimensoes(tab):
    '''tabuleiro_dimensoes : tabuleiro -> tuple
    tabuleiro_dimensoes(tab) recebe como argumento um objeto do
    tipo tabuleiro e devolve um tuplo constituido por dois
    inteiros com o numero de linhas no primeiro elemento e 
    com o numero de colunas no segundo'''
    # Testa se o argumento tab e do tipo tabuleiro
    if not e_tabuleiro(tab)
        raise ValueError('tabuleiro_celulas_linha: tabuleiro invalido')

    spec = tabuleiro_especificacoes(tab)
    dimensao_linhas = len(spec[0])
    dimensao_colunas = len(spec[1])
    dimensoes = (dimensao_linhas, dimensao_colunas)
    return dimensoes

# t e o tabuleiro, c e a coordenada
def tabuleiro_celula(tab, coord):
    linha = coordenada_linha(coord)
    coluna = coordenada_coluna(coord)
    celulas = tabuleiro_celulas(tab)
    valor_celula = celulas[linha[coluna]]

    return valor_celula

# t e o tabuleiro, c e a coordenada, e e o valor a preencher
def tabuleiro_preenche_celula(tab, coord, value):
    linha = coordenada_linha(coord)
    coluna = coordenada_coluna(coord)
   # tabuleiro_celulas(tab) = value
    return t



def tabuleiro_completo(tab):
    celulas_vazias = tabuleiro_celulas_vazias(tab)
    if celulas_vazias != []:
        return False
    dimensoes = tabuleiro_dimensoes (tab)
    qtd_linha = dimensoes[0]
    especificacoes = tabuleiro_especificacoes (tab)
    especificacoes_linhas = especificacoes[0]

    for linha in range (len(qtd_linha)):
        espec_linha = especificacoes_linhas[linha]
        conteudo_linha = tabuleiro_celulas_linha(tab, linha)

        if not linha_completa(espec_linha, conteudo_linha):
            return False

    return True

def tabuleiros_iguais(tab1, tab2):
    spec1 = tabuleiro_especificacoes(t1)
    spec2 = tabuleiro_especificacoes(t2)
    celulas1 = tabuleiro_celulas(t1)
    celulas2 = tabuleiro_celulas(t2)
    return (spec1 == spec2 and celulas1 == celulas2)


def tabuleiro_celulas_vazias(tab):
    celulas = tabuleiro_celulas(tab)
    dimensoes = tabuleiro_dimensoes(tab)
    qtd_linhas = dimensoes[0]
    qtd_colunas = dimensoes[1]
    celulas_vazias = []
    for linha in range (qtd_linhas):
        for coluna in range (qtd_colunas):
            conteudo = celulas[linha][coluna]
            print (conteudo)
            if conteudo == 0:
                coord = coordenada(linha + 1, coordenada + 1)
                celulas_vazias.append (coord)
    return celulas_vazias
