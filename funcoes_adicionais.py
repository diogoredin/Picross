##############################################################
#
#   FUNCOES ADICIONAIS
#   - le_tabuleiro
#	- pede_jogada
#	- jogo_picross
#	- tabuleiro_celulas_vazias
#	- linha_completa
#
##############################################################

# Funcao le tabuleiro
def le_tabuleiro(espec):
	'''le_tabuleiro : cad. caracteres -> tuplo
       le_tabuleiro(espec) recebe como argumento uma cadeia de caracteres que corresponde ao nome do 
       ficheiro com os dados de especificacao do jogo, e devolve um tuplo de dois tuplos com a 
       especificacao das linhas e colunas.'''

# Funcao pede jogada
def pede_jogada(tab):
	'''pede_jogada : tabuleiro -> jogada
       le_tabuleiro(tab) recebe como argumento o tabuleiro do jogo e devolve a jogada que o jogador 
       pretende executar.'''

# Funcao jogo picross
def jogo_picross(espec):
	'''jogo_picross : cad. caracteres -> logico
       jogo_picross(espec) recebe como argumento uma cadeia de caracteres representando o nome do 
       ficheiro com a especificacao do tabuleiro, e devolve True caso o tabuleiro resultante do jogo 
       esteja completo (quadro completo e de acordo com as especificacoes) e False caso contrario.'''

# Funcao tabuleiro celulas vazias
def tabuleiro_celulas_vazias(tab, lista):
	'''tabuleiro_celulas_vazias : tabuleiro -> lista
       tabuleiro_celulas_vazias(espec) recebe como recebe como argumento um elemento do tipo tabuleiro e 
       devolve uma lista com as coordenadas das celulas do tabuleiro que estao vazias.'''

# Funcao linha completa
def linha_completa(tab, lista):
	'''tabuleiro_celulas_vazias : tabuleiro -> lista
       tabuleiro_celulas_vazias(espec) recebe como argumento um tuplo com a especificacao de uma linha 
       ou coluna, e uma lista com os conteudos das celulas de uma linha / coluna, e verifica se a linha / 
       coluna em questao satisfaz a especificacao recebida.'''