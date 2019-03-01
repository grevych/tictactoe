# Tic Tac Toe
Interview exercise made in python.


## Example
```python
from game import Game
from board import Board
from player import SystemPlayer, RealPlayer


board = Board()
player_a = RealPlayer('Your Name', 'X', board)
player_b = SystemPlayer('Fake AI', 'O', borad)

game = Game(board, [player_a, player_b])

game.run()
```
