class Token(object):
  def __init__(self, symbol):
    self.__symbol__ = symbol

  def symbol(self):
    return self.__symbol__
