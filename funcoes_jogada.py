##############################################################
#
#	JOGADA
#	- Representa uma jogada a efetuar sobre um tabuleiro
#	  Cada jogada e composto por uma coordenada e um valor
#	  igual a 1 ou dois que representa o conteudo de uma
#	  celula de um tabuleiro de picross.
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

    # Igualdade
    def __eq__(self, jog1, jog2):

    	# Testa se recebe dois elementos do tipo jogada
        if not(isinstance(jog1, (jogada)) and isinstance(jog2, (jogada))):
            raise ValueError('jogadas_iguais: argumentos invalidos')

        # Igual quando as coordenadas e valor de ambos sao iguais
        return ( (jog1.coordenada() == jog2.coordenada()) and (jog1.celula() == jog2.celula()) )

    # Seletor
    def coordenada(self):
    	return self.coordenada

   	# Seletor
    def celula(self):
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
	return jog.coordenada()

# Seletor
def jogada_valor(jog):
	'''jogada_valor : jogada -> {1,2}
	   jogada_valor(jog) recebe como argumento um elemento do tipo jogada e devolve o valor respetivo.'''

	# Testa se recebe uma jogada
	if not( e_jogada(jog) ):
		raise ValueError('jogada_valor: argumentos invalidos')

	# Se for devolve celula
	return jog.celula()

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
    return ( coordenada_para_cadeia( jog.coordenada() ) + ' --> ' + jog.celula() )