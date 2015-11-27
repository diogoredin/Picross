def cria_coordenada(linha, coluna):
    return coordenada (linha, coluna)

def coordenada_linha(coord):
    return coordenada.linha(coord)

def coordenada_coluna(coord):
    return coordenada.coluna(coord)

def e_coordenada(elemento):
    return isinstance(elemento, coordenada)

def coordenadas_iguais(coord1, coord2):
    linha1 = coordenada_linha(coord1)
    coluna1 = coordenada_coluna(coord1)
    linha2 = coordenada_linha(coord2)
    coluna2 = coordenada_coluna(coord2)
    return (linha1 == linha2 and coluna1 == coluna2)

def coordenada_para_cadeia(coord):
    linha = str(coordenada_linha(coord))
    coluna = str(coordenada_coluna(coord))
    return '(' + linha + ' : ' + coluna + ')'
