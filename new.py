############################################
#
# Projeto 2 - Picross
#
############################################

############################################
# CLASSE COORDENADA
############################################
class coordenada:

	# Inicia os objetos da classe
	def __init__(self, l, c):

		# Testa se são inteiros positivos
		if not(isinstance(c, (int)) and isinstance(l, (int)) and (c > 0) and (l > 0)):
			raise ValueError('cria_coordenada: argumentos invalidos')
		
		# Define linha e coluna da coordenada
		self.linha = l
		self.coluna = c
	
	# Redefine igualdade para coordenadas
	def __eq__(self, c):
	
		# Testa se estamos a trabalhar com coordenadas
		if not isinstance(c, coordenada):
			raise ValueError('cria_coordenada: argumentos invalidos')
		return (self.linha == c.linha and self.coluna == c.coluna)

	# Retorna a linha na coordenada
	def coordenada_linha(self):
		return self.linha

	# Retorna a coluna na coordenada
	def coordenada_coluna(self):
		return self.coluna

############################################
# FUNCOES DA COORDENADA
############################################

# Testa se as cordenadas são iguais
def coordenadas_iguais(c1,c2):

	# Testa se estamos a trabalhar com coordenadas
	if not(isinstance(c1, (coordenada)) and isinstance(c2, (coordenada))):
		raise ValueError('coordenadas_iguais: argumentos invalidos')
	return (c1 == c2)
	
# COORDENADA PARA CADEIA
def coordenada_para_cadeia(c):

	# Testa se estamos a trabalhar com coordenadas
	if not(isinstance(c, (coordenada))):
		raise ValueError('coordenada_para_cadeia: argumentos invalidos')
	return( '(' . c.linha . ':' . c.coluna . ')' )

# CRIA COORDENADA
def cria_coordenada(c):
	return (coordenada(c))

# E COORDENADA
def e_coordenada(c):
	return (isinstance(c, (coordenada)))

############################################
# CLASSE TABULEIRO
############################################
class tabuleiro:
	
	# CONSTRUTOR
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

# TABULEIRO DIMENSOES
def tabuleiro_dimensoes(t):
	
	# Qtd linhas & colunas
	linhas = len(self.linhas())
	colunas = len(self.colunas())
	
	# Devolve dimensoes num tuplo
	return (linhas, colunas)

# TABULEIRO ESPECIFICACOES
def tabuleiro_especificacoes(self):
	
	# Linhas & colunas
	linhas = self.linhas()
	colunas = self.colunas()
	
	# Devolve dimensoes num tuplo
	return (linhas, colunas)

# TABULEIRO CELULA
def tabuleiro_celula(self, c, n):
		
	# Testa a coordenada e o inteiro
	if not( isinstance(c, (coordenada)) and isinstance(n, (int)) ):
		raise ValueError('tabuleiro_celula: argumentos invalidos')
	
	# Vai buscar coordenadas
	linha = coordenada(c).coordenada_linha
	coluna = coordenada(c).coordenada_coluna