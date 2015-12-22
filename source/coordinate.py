################################################################
#
#   COORDENADA

#   - Used to index the board cells. Each cell is indexed 
#     by the line (an integer between 1 and the number of 
#     lines in the board) and the column (an integer between 
#     1 and the number of colums in the board) in wich the
#     cell (1 : 1) match with with the superior left corner
#     of the board.
#
# # - Repr. Interna -> Criada a estrutura de dados 'coordenada'.
#
################################################################

# Create coordinate type
class coordinate:

    # Inicializer
    def __init__(self, line, column):

        # Access to line and column
        self.line = line
        self.column = column

    # Atribute
    def get_line(self):
        return self.line

    # Atribute
    def get_column(self):
        return self.column

# Creator
def create_coordinate(line, column): 
    '''create_coordinate  : int x int -> coordinate
       create_coordinate(line, column) recieves two posite integers as arguments, line and column
       respectively and returns a coordinate type element coorespondent to the cell (line : column).'''

    # Test if the argument are two positive integers
    if not(isinstance(line, (int)) and isinstance(column, (int)) and ((line > 0) and (column > 0))):
        raise ValueError('create_coordinate: invalid arguments')

    return coordinate(line, column)

# Selector
def coordinate_line(coord):
    '''coordinate_line : coordenada -> integer
       coordinate_line(coord) recieves as argument a cell and returns the coorespondent line.'''
    
    # Test if the argument is a coordinate
    if not(is_coordinate(coord)):
        raise ValueError('coordinate_line: invalid argument')

    return coord.get_line()

# Selector
def coordinate_column(coord):
    '''coordinate_column : coordinate -> inteiro
       coordinate_column(coord) recieves as argument a cell and returns the coorespondent column.'''
    
    # Test if the argument is a coordinate
    if not(is_coordinate(coord)):
        raise ValueError('coordinate_column: invalid argument')

    return coord.get_column()

# Recognizer
def is_coordinate(element):
    '''is_coordinate : universal -> logic
       is_coordinate(element) recieves an argument and returns True if the element is a coordinate
       and return False otherwise.'''

    return isinstance(element, (coordinate))

# Test
def same_coordinates(coord1, coord2):
    '''same_coordinates : coordinate x coordinate -> logic
       same_coordinates(coord1, coord2) recieves as arguments two coordinates and returns two if
       the coordinates represent the same cell on the board and False otherwise'''

    # Test if the arguments are two coordinates
    if not( is_coordinate(coord1) and is_coordinate(coord2) ):
        raise ValueError('same_coordinates: invalid arguments')

    return ( ( coordinate_line(coord1) == coordinate_line(coord2) ) and 
             ( coordinate_column(coord1) == coordinate_column(coord2) ) )

# Funcao
def coordenada_para_cadeia(coord):
    '''coordenada_para_cadeia : coordenada -> cad. caracteres
       coordenada_para_cadeia(coord) recebe como argumento um elemento do tipo coordenada e devolve 
       uma cadeia de caracteres que a representa.'''

    # Testa se recebe coordenada
    if not( e_coordenada(coord) ):
        raise ValueError('coordenada_para_cadeia: argumentos invalidos')

    # Acedemos a linha e coluna
    return ( '(' + str( coordenada_linha(coord) ) + ' : ' + str( coordenada_coluna(coord) ) + ')' )