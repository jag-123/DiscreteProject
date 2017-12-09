from OpenGL.GL import *
from OpenGL.GLU import *

from math import *

class GameModel(object):
  """ Model for game """
  def __init__(self):
    self.data = []
    for y in range(4):
      layer = []
      for z in range(4):
        row = []
        for x in range(4):
          row.append(None)
        layer.append(row)
      self.data.append(layer)