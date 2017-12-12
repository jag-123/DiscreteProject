import pygame
from pygame.locals import *
from settings import *

from OpenGL.GL import *
from OpenGL.GLU import *

from view import GameView
from model import GameModel
from controller import GameController

from tictactoe4x4 import TicTacToe3D
from minimax import AI

class GameMain(object):
  def __init__(self):
    self.model = GameModel()
    self.view = GameView(self.model)
    self.controller = GameController(self.model)

    self.board = TicTacToe3D()
    self.AI = AI(self.board)

  def GameLoop(self):
    """ Game Loop """
    done = False

    while not done:
      self.view.set_camera()
      self.view.rotate_camera()
      glClear(GL_DEPTH_BUFFER_BIT)
      
      self.view.draw_fill()

      self.controller.detect_square()

      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          if ((self.controller.mouse_pos[0])+(self.controller.mouse_pos[1]*16)+(self.controller.mouse_pos[2]*4)) in self.board.available_moves():
            self.controller.select_square()
            player_move = self.controller.mouse_pos
            player_move2 = ((player_move[0])+ (player_move[1]*16)+(player_move[2]*4))


            player = 'X'

            self.board.make_move(player_move2, player)

            if self.board.complete():
              print('done')
              pygame.time.wait(1000)
              done = True
              break

            player = self.AI.get_enemy(player)
            computer_move = self.AI.determineMove(self.board, player)
            self.board.make_move(computer_move, player)

            a = divmod(computer_move,16)
            b = divmod(a[1],4)
            self.model.data[a[0]][b[0]][b[1]] = 'O'

            print(self.model.data)

            print(player_move)
            print(player_move2)
            print(b[1],a[0],b[0])
            print(computer_move)

            print(self.board.show())

        elif event.type == pygame.QUIT:
          pygame.quit()
          quit()

      glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

      self.mouse_valid =\
      self.controller.mouse_pos[0]>=0 and self.controller.mouse_pos[0]<=3 and\
      self.controller.mouse_pos[1]>=0 and self.controller.mouse_pos[1]<=3 and\
      self.controller.mouse_pos[2]>=0 and self.controller.mouse_pos[2]<=3

      if self.mouse_valid:
        c = board_colors[self.controller.mouse_pos[1]]
        glColor4f(c[0],c[1],c[2],0.4)
        self.view.draw_square(*self.controller.mouse_pos)


      self.view.draw_pieces()
      self.view.draw_grid()

      pygame.display.flip()
      pygame.time.wait(10)

    print ("winner is", self.board.winner())

if __name__ == '__main__':
  MainWindow = GameMain()
  MainWindow.GameLoop()