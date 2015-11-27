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
#
############################################

def cria_tabuleiro(t):
	
	# Testa se recebe dois tuplos
	for tuplos in t:
		list[tuplos] = isinstance(t[tuplos], (tuple))
		
	# Testa o tuplo
	if not( isinstance(t, (tuple))
			# se o tuplo contem dois tuplos
			and all( isinstance(tuplos, (tuple)) for tuplos in t )
			# se esses tuplos nao sao vazios
			and all( len(tuplos) > 0 for tuplos in t )
			# se as especificacoes sao positivas
			and all( elem > 0 for elem in espec for espec in tuplos for tuplos in t )
			# se as especificacoes sao inteiras
			and all( isinstance(elem, (int)) for elem in espec for espec in tuplos for tuplos in t )
			
		raise ValueError('cria_tabuleiro: argumentos invalidos')
		
	# Devolve o tabuleiro num dicionario (com as especificacoes dentro de tuplos)
	return {'linhas' : t[0], 'colunas' : t[1]}
