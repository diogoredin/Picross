class tabuleiro:
    def __init__(self, t):
        # se o argumento e um tuplo
        if not( isinstance(t, (tuple))
                # se o tuplo contem dois tuplos
                and len(t) == 2
                # se os elementos do tuplo sao tuplos
                and all( isinstance(tuplos, (tuple)) for tuplos in t )
                # se esses tuplos nao sao vazios
                and all( len(tuplos) > 0 for tuplos in t )
                # se as especificacoes sao inteiras
                and all( isinstance(elem, (int)) for tuplos in t for espec in tuplos for elem in espec ) 
                # se as especificacoes sao positivas
                and all( (elem > 0) for tuplos in t for espec in tuplos for elem in espec )):
    
            raise ValueError('cria_tabuleiro: argumentos invalidos')

        # Qtd linhas & colunas
        self.linhas = t[0]
        self.colunas = t[1]
        self.celulas = [[0 for x in range (len(self.colunas))] for y in range (len(self.linhas))]

    def linhas (self):
        return self.linhas

    def colunas (self):
        return self.colunas

    def celulas (self):
        return self.celulas



# t e o tuplo com as especificacoes
def cria_tabuleiro(t):
    return tabuleiro(t)

# t e o tabuleiro
def tabuleiro_especificacoes(t):
    spec_linhas = t.linhas
    spec_colunas = t.colunas
    spec = (spec_linhas, spec_colunas)
    return spec

def tabuleiro_celulas(t):               # funcao opcional
    return t.celulas

# t e o tabuleiro
def tabuleiro_dimensoes(t):
    # Vai buscar as especificacoes do tabuleiro
    # spec vai ser um tuplo com as especificacoes das linhas na
    # primeira entrada e com especificacoes das colunas na segunda entrada
    spec = tabuleiro_especificacoes(t)

    # Vai buscar o tamanho das especificacoes das linhas
    dim_linhas = len(spec[0])

    # Vai buscar o tamanho das especificacoes das linhas
    dim_colunas = len(spec[1])

    # Cria um tuplo com as dimensoes
    dim = (dim_linhas, dim_colunas)

    return dim

# t e o tabuleiro, c e a coordenada
def tabuleiro_celula(t, c):
    linha = coordenada_linha(c)
    coluna = coordenada_coluna(c)
    celulas = tabuleiro_celulas(t)
    valor_celula = celulas[linha[coluna]]

    return valor_celula

# t e o tabuleiro, c e a coordenada, e e o valor a preencher
def tabuleiro_preenche_celula(t, c, e):
    linha = coordenada_linha(c)
    coluna = coordenada_coluna(c)
    celulas = tabuleiro_celulas(t)
    celulas = e
    return t

def e_tabuleiro(t):
    return isinstance(t, tabuleiro)

# def tabuleiro_completo

def tabuleiros_iguais(t1, t2):
    spec1 = tabuleiro_especificacoes(t1)
    spec2 = tabuleiro_especificacoes(t2)
    celulas1 = tabuleiro_celulas(t1)
    celulas2 = tabuleiro_celulas(t2)
    return (spec1 == spec2 and celulas1 == celulas2)

