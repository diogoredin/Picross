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
class coordenada:

	def __init_ (self, l, c):

		# Testa se são inteiros positivos
		if not(isinstance(l, (int)) and isinstance(c, (int)) and (l > 0) and (c > 0)):
			raise ValueError('cria_coordenada: argumentos invalidos')
		self.linha = l
		self.coluna = c

############################################
# COORDENADA LINHA
############################################

	def coordenada_linha(self, coord):
		return self.linha

############################################
# COORDENADA COLUNA
############################################

	def coordenada_coluna(self, coord):
		return self.coluna

############################################
#
# Funcoes Tabuleiro:
# 	- Cria Tabuleiro (cria_tabuleiro)
#	- Dimensoes Tabuleiro (tabuleiro_dimensoes)
#	- Especificacoes Tabuleiro (tabuleiro_especificacoes
#
############################################

############################################
# CRIA TABULEIRO
############################################

class tabuleiro:

	def __init__ (self, t):

		# Testa o tuplo
		if not( isinstance(t, (tuple))
		        # se o tuplo contem dois tuplos
		        and len(t) == 2
		        # se o os dois elementos sao tuplos
		        and all( isinstance(tuplos, (tuple)) for tuplos in t )
		        # se esses tuplos nao sao vazios
		        and all( len(tuplos) > 0 for tuplos in t )
		        # se as especificacoes sao positivas
		        and all( elem > 0 for tuplos in t for espec in tuplos for elem in espec )
		        # se as especificacoes sao inteiras
		        and all( isinstance(elem, (int)) for tuplos in t for espec in tuplos for elem in espec )
		        # se a qtdd especificacoes sao a msm
		        and len (t[0]) == len(t[1])):

			raise ValueError('cria_tabuleiro: argumentos invalidos')

		# Cria lista com as celulas (com uma linha)
		cell = [[]]

		# Para cada linha
		for x in range (len (t[0])):

			# Para cada coluna
			for y in range (len (t[1])):


				# Coloca a 0 a coordenada correspondente
				cell[x].append (0)

			# Adiciona nova linha
			cell.append ([])

		self.espec_linhas = t[0]
		self.espec_colunas = t[1]
		self.celulas = cell

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

		#    z = tabuleiro (((2)
