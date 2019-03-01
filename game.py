import token


class GameException(Exception):
  pass
 
class DrawGame(GameException):
  def __init__(self):
    GameException.__init__(self, '__DRAW__')


class EndGame(GameException):
  def __init__(self, player):
    message = 'Player {0} wins!'.format(player.name())
    GameException.__init__(self, message)


class Game(object):
  def __init__(self, board, players=[]):
    self.__board__ = board
    self.__turns__ = players
  
  def add_player(self, player):
    if len(self.__turns__) == 2:
      raise Exception('Two players at most!')
    
    self.__turns__.append(player)

  def run(self):
    while True:
      try:
        if self.__board__.has_winner():
          winner = self.__turns__.pop()
          raise EndGame(winner)

        if self.__board__.is_full():
          raise DrawGame()

        turn = self.__turns__.pop(0)

        print('It is player {0}\'s turn!'.format(turn.name()))

        coordinate = turn.make_move()
        player_token = token.Token(turn.token_symbol())
        self.__board__.add_token(player_token, coordinate)
      except GameException as error:
        print(error)
        exit(0)
      except Exception as error:
        print(error)
        self.__turns__.insert(0, turn)
      
      self.__turns__.append(turn)
      self.__board__.render()
