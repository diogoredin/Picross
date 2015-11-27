############################################
#
# Projeto 2 - Picross
#
############################################

############################################
#
# Funcoes Coordenadas:
# 	- Cria Coordenada (cria_coordenada)
#	- Coordenada Linha (coordenada_linha)
#	- Coordenada Coluna (coordenada_coluna)
#
############################################

############################################
# COORDENADA
############################################

def cria_coordenada(l, c):

	# Testa se são inteiros positivos
	if not(isinstance(l, (int)) and isinstance(c, (int)) and (l > 0) and (c > 0)):
		raise ValueError('cria_coordenada: argumentos invalidos')

	# Devolve a coordenada num dicionario
	return {'linha' : l, 'coluna' : c}

############################################
# COORDENADA LINHA
############################################

def coordenada_linha(coord):

	# Testa se e coordenada
	if not e_coordenada():
		raise ValueError('coordenada_linha: argumentos invalidos')

	# Devolve a linha se for
	return coord['linha']

############################################
# COORDENADA COLUNA
############################################

def coordenada_coluna(coord):

	# Testa se e coordenada
	if not e_coordenada():
		raise ValueError('coordenada_coluna: argumentos invalidos')

	# Devolve a coluna se for
	return coord['coluna']

############################################
#
# Funcoes Tabuleiro:
# 	- Cria Tabuleiro (cria_tabuleiro)
#	- Dimensoes Tabuleiro (tabuleiro_dimensoes)
#	- Especificacoes Tabuleiro (tabuleiro_especificacoes
#
############################################

############################################
# CLASSE TABULEIRO
############################################
class tabuleiro:
	
	########################################
	# CONSTRUTOR
	########################################
	def __init__(self, t):
	
		# Testa o tuplo
		if not( isinstance(t, (tuple))
				# se o tuplo contem dois tuplos
				and all( isinstance(tuplos, (tuple)) for tuplos in t )
				# se esses tuplos nao sao vazios
				and all( len(tuplos) > 0 for tuplos in t )
				# se as especificacoes sao positivas
				and all( elem > 0 for tuplos in t for espec in tuplos for elem in espec )
				# se as especificacoes sao inteiras
				and all( isinstance(elem, (int)) for tuplos in t for espec in tuplos for elem in espec ) ):
	
			raise ValueError('cria_tabuleiro: argumentos invalidos')
	
		# Qtd linhas & colunas
		self.linhas = t([0])
		self.colunas = t([1])

	########################################
	# TABULEIRO DIMENSOES
	########################################
	def tabuleiro_dimensoes(self):
	
		# Qtd linhas & colunas
		linhas = len(self[0])
		colunas = len(self[1])
	
		# Devolve dimensoes num tuplo
		return (linhas, colunas)

	############################################
	# TABULEIRO ESPECIFICACOES
	############################################
	
	def tabuleiro_especificacoes(self):
	
		# Qtd linhas & colunas
		linhas = self[0]
		colunas = self[1]
	
		# Devolve dimensoes num tuplo
		return (linhas, colunas) #teste atributo

	############################################
	# TABULEIRO CELULA
	############################################
	
	def tabuleiro_celula(self, coordenada, inteiro):
	
		# Qtd linhas & colunas
		linhas = tab['linhas']
		colunas = tab['colunas']
	
		# Devolve dimensoes num tuplo
		return (linhas, colunas) #teste atributo