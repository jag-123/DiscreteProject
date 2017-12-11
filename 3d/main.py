import pygame
from pygame.locals import *
from settings import *

from OpenGL.GL import *
from OpenGL.GLU import *

from view import GameView
from model import GameModel
from controller import GameController

class GameMain(object):
  def __init__(self):
    self.model = GameModel()
    self.view = GameView(self.model)
    self.controller = GameController(self.model)

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
          self.controller.select_square()
          print(self.controller.mouse_pos)
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


if __name__ == '__main__':
  MainWindow = GameMain()
  MainWindow.GameLoop()