import pygame
from pygame.locals import *

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

      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          self.controller.select_square()
        elif event.type == pygame.QUIT:
          pygame.quit()
          quit()

      self.view.rotate_camera()
      glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
      self.view.draw()
      pygame.display.flip()
      pygame.time.wait(10)


if __name__ == '__main__':
  MainWindow = GameMain()
  MainWindow.GameLoop()