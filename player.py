import sys

class Player(object):
  def __init__(self, name, token_symbol):
    self.__name__ = name
    self.__token_symbol__ = token_symbol

  def name(self):
    return self.__name__

  def token_symbol(self):
    return self.__token_symbol__
  
  # Must return a coordiante
  def make_move(self):
    raise Exception('Method not implemented!')


class RealPlayer(Player):
  def make_move(self):
    player_input = sys.stdin.readline()
    player_input = player_input.split()

    x, y = player_input[:2]
    return int(x), int(y)


class SystemPlayer(Player):
  def __init__(self, name, token_symbol, board):
    Player.__init__(self, name, token_symbol)

    self.__board__ = board

  def make_move(self):
    return self.__board__.random_untaken_coordinate()
