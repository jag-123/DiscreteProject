import pygame
from model import GameModel
from view import GameView

from OpenGL.GL import *
from OpenGL.GLU import *

from settings import *

class GameController(object):
  """controller for game. When a key is pressed, does specific action """
  def __init__(self, model):
    self.model = GameModel()
    self.view = GameView(self.model)

    self.done = False

    self.solution = None

    self.mouse_pos = [0,0,0]
    self.mouse_valid = False

  def select_square(self):
      #if pygame.mouse.get_pressed()[0]:
      mouse_position = list(pygame.mouse.get_pos())
      mouse_position[1] = screen_size[1] - mouse_position[1]
      mouse_rel = pygame.mouse.get_rel()

      self.view.draw_fill()

      self.mouse_pos = self.get_pos_at(mouse_position,False)
      self.mouse_pos[0] = int(self.mouse_pos[0])
      self.mouse_pos[1] = int(round(self.mouse_pos[1]/spacing))
      self.mouse_pos[2] = int(self.mouse_pos[2])

      print(self.mouse_pos)
      #self.solution = self.model.check_if_empty()

  def get_pos_at(self, windowcoord,flip=True):
    viewport = glGetIntegerv(GL_VIEWPORT)
    winX = windowcoord[0]
    if flip: winY = viewport[3]-windowcoord[1]
    else: winY = windowcoord[1]
    winZ = glReadPixels(winX,winY,1,1,GL_DEPTH_COMPONENT,GL_FLOAT)[0][0]
    return list(gluUnProject(winX,winY,winZ))#,modelview,projection,viewport)