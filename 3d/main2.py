import pygame
from pygame.locals import *
from settings import *

from OpenGL.GL import *
from OpenGL.GLU import *

from view import GameView
from model import GameModel
from controller import GameController

from tictactoe4x4 import TicTacToe3D
# from minimax import AI
from minimax2 import AI

class GameMain2(object):
  def __init__(self):
    self.model = GameModel()
    self.view = GameView(self.model)
    self.controller = GameController(self.model)
    self.spectate = True
    self.board = TicTacToe3D()
    self.AI = AI(self.board)

  def GameLoop(self):
    """ Game Loop """
    done = False
    player = "O"

    while not done:
      self.view.set_camera()
      self.view.rotate_camera()
      glClear(GL_DEPTH_BUFFER_BIT)

      self.view.draw_fill()

      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          if not self.board.complete():

            player = self.AI.get_enemy(player)

            #make x smarter...
            if player == "X":
              self.board.difficulty = 2
            else:
              self.board.difficulty = 1

            computer_move = self.AI.determineMove(self.board, player)
            self.board.make_move(computer_move, player)

            a = divmod(computer_move,16)
            b = divmod(a[1],4)
            self.model.data[a[0]][b[0]][b[1]] = player
            
            # print(self.model.data)
            # print(self.board.show())

        elif event.type == pygame.QUIT:
          pygame.quit()
          quit()

      glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

      self.view.draw_pieces()
      self.view.draw_grid()

      if self.board.complete():
        for square in self.board.win:
          a = divmod(square,16)
          b = divmod(a[1],4)
          glColor4f(1,1,0,0.5)
          self.view.draw_square(b[1],a[0],b[0])

      pygame.display.flip()
      pygame.time.wait(10)

    print ("winner is", self.board.winner())

if __name__ == '__main__':
  MainWindow = GameMain2()
  MainWindow.GameLoop()