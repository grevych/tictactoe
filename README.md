# Tic Tac Toe
Interview exercise made in python.


## Example
```python
from game import Game
from board import Board
from player import SystemPlayer, RealPlayer


board = Board()
player_a = RealPlayer('Your Name', 'X')
player_b = SystemPlayer('Fake AI', 'O', board)

game = Game(board, [player_a, player_b])

game.run()
```
