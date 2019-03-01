import random

class InvalidCoordinateError(Exception):
  def __init__(self, coordinate):
    message = 'Invalid coordiante: {0}'.format(coordinate)
    Exception.__init__(self, message)


class CoordinateTakenError(Exception):
  def __init__(self, coordinate):
    message = 'Coordinate {0} is already occupied'.format(coordinate)
    Exception.__init__(self, message)


class Board(object):
  EMPTY_SYMBOL = '-'

  def __init__(self):
    self.__board__ = []
    self.__taken__ = set()
    self.__untaken__ = set()

    for x in range(3):
      self.__board__.append([])
      for y in range(3):
        self.__board__[x].append(None)
        self.__untaken__.add((x, y))

  def __is_coordinate_valid__(self, coordinate):
    x, y = coordinate

    if x < 0 and x >= len(self.__board__):
      return False

    if y < 0 and y >= len(self.__board__[0]):
      return False

    return True

  def __has_equals_in_rows__(self):
    for index_x in range(len(self.__board__)):
      row_set = set()

      for index_y in range(len(self.__board__)):
        element = self.__board__[index_x][index_y]

        symbol = element.symbol() if element else self.EMPTY_SYMBOL
        row_set.add(symbol)

      if len(row_set) == 1:
        if self.EMPTY_SYMBOL not in row_set:
          return True
    
    return False

  def __has_equals_in_columns__(self):
    for index_x in range(len(self.__board__)):
      row_set = set()

      for index_y in range(len(self.__board__)):
        element = self.__board__[index_y][index_x]

        symbol = element.symbol() if element else self.EMPTY_SYMBOL
        row_set.add(symbol)

      if len(row_set) == 1:
        if self.EMPTY_SYMBOL not in row_set:
          return True
  
    return False
  
  def __has_equals_in_diagonals__(self):
    row_set = set()

    for index in range(len(self.__board__)):
      element = self.__board__[index][index]

      symbol = element.symbol() if element else self.EMPTY_SYMBOL
      row_set.add(symbol)

    if len(row_set) == 1:
      if self.EMPTY_SYMBOL not in row_set:
        return True

    row_set = set()

    for index in range(len(self.__board__) - 1, -1, -1):
      element = self.__board__[index][index]

      symbol = element.symbol() if element else self.EMPTY_SYMBOL
      row_set.add(symbol)

    if len(row_set) == 1:
      if self.EMPTY_SYMBOL not in row_set:
        return True

    return False 

  def is_full(self):
    untaken_length = len(self.__taken__)
    board_length = len(self.__board__) * len(self.__board__[0])

    return untaken_length == board_length 

  def add_token(self, token, coordinate):
    if not self.__is_coordinate_valid__(coordinate):
      raise InvalidCoordinateError(coordinate)

    if coordinate in self.__taken__:
      raise CoordinateTakenError(coordinate)

    x, y = coordinate
    self.__board__[x][y] = token
    self.__taken__.add(coordinate)
    self.__untaken__.remove(coordinate)

  def render(self):
    output = ''

    for row in self.__board__:
      for element in row:
        if element:
          output += element.symbol()
        else:
          output += self.EMPTY_SYMBOL
        output += '|'
      output = output[:-1] + '\n'
    
    print(output)

  def random_untaken_coordinate(self):
    return random.choice(tuple(self.__untaken__))

  def has_winner(self):
    if self.__has_equals_in_rows__():
      return True

    if self.__has_equals_in_columns__():
      return True

    if self.__has_equals_in_diagonals__():
      return True

    return False