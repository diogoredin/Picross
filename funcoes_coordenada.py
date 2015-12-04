class coordenada:

    def __init__ (self, l, c):

        # Testa se sao inteiros positivos
        if not(isinstance(l, (int)) and isinstance(c, (int)) and (l > 0) and (c > 0)):
            raise ValueError('cria_coordenada: argumentos invalidos')
        self.linha = l
        self.coluna = c

def cria_coordenada(l, c):    
    return coordenada (l, c)

def coordenada_linha(c):
    return c.linha()

def coordenada_coluna(c):
    return c.coluna()

def e_coordenada(e):
    return isinstance(e, coordenada)

def coordenadas_iguais(c1, c2):
    linha1 = coordenada_linha(c1)
    coluna1 = coordenada_coluna(c1)
    linha2 = coordenada_linha(c2)
    coluna2 = coordenada_coluna(c2)
    return (linha1 == linha2 and coluna1 == coluna2)

def coordenada_para_cadeia(c):
    linha = str(coordenada_linha(c))
    coluna = str(coordenada_coluna(c))
    return '(' + linha + ' : ' + coluna + ')'
