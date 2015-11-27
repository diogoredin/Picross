def cria_tabuleiro(spec):
    return tabuleiro(spec)

def tabuleiro_dimensoes(tab):
    # Vai buscar as especificacoes do tabuleiro
    # spec vai ser um tuplo com as especificacoes das linhas na
    # primeira entrada e com especificacoes das colunas na segunda entrada
    spec = tabuleiro_especificacoes(tab)

    # Vai buscar o tamanho das especificacoes das linhas
    dim_linhas = len(spec[0]

    # Vai buscar o tamanho das especificacoes das linhas
    dim_colunas = len(spec[1])

    # Cria um tuplo com as dimensoes
    dim = (dim_linhas, dim_colunas)

    return dim

def tabuleiro_especificacoes(tab):
    spec_linhas = tabuleiro.linhas(tab)
    spec_colunas = tabuleiro.colunas(tab)
    spec = (spec_linhas, spec_colunas)
    return spec

# def tabuleiro_celula(tab, coord): YET TO FINISH
