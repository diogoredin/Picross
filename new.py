############################################
#
# Projeto 2 - Picross
#
############################################

############################################
#
# Classe Coordenadas:
# 	- Cria Coordenada (cria_coordenada)
#	- Coordenada Linha (coordenada_linha)
#	- Coordenada Coluna (coordenada_coluna)
#
############################################

############################################
# COORDENADA
############################################
class coordenada:
	
	########################################
	# CONSTRUTOR
	########################################
	def __init__(self, l, c):

		# Testa se são inteiros positivos
		if not(isinstance(l, (int)) and isinstance(c, (int)) and (l > 0) and (c > 0)):
			raise ValueError('cria_coordenada: argumentos invalidos')
		self.linha = l
		self.coluna = c

	########################################
	# COORDENADA LINHA
	########################################
	def coordenada_linha(self):
		return self.linha

	########################################
	# COORDENADA COLUNA
	########################################
	def coordenada_coluna(self):
		return self.coluna

############################################
#
# Classe Tabuleiro:
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
	
		# Acede linhas e colunas
		self.linhas = t([0])
		self.colunas = t([1])

	########################################
	# TABULEIRO DIMENSOES
	########################################
	def tabuleiro_dimensoes(self):
	
		# Qtd linhas & colunas
		linhas = len(self.linhas())
		colunas = len(self.colunas())
	
		# Devolve dimensoes num tuplo
		return (linhas, colunas)

	########################################
	# TABULEIRO ESPECIFICACOES
	########################################
	def tabuleiro_especificacoes(self):
	
		# Linhas & colunas
		linhas = self.linhas()
		colunas = self.colunas()
	
		# Devolve dimensoes num tuplo
		return (linhas, colunas)

	########################################
	# TABULEIRO CELULA
	########################################
	def tabuleiro_celula(self, c, n):
		
		# Testa a coordenada e o inteiro
		if not( isinstance(c, (coordenada)) and isinstance(n, (int)) ):
			raise ValueError('tabuleiro_celula: argumentos invalidos')
	
		# Vai buscar coordenadas
		linha = coordenada(c).coordenada_linha
		coluna = coordenada(c).coordenada_coluna
		
		return (self