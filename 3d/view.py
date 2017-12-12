from settings import *

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from math import *

from model import GameModel

class GameView(object):
  def __init__(self, model):
    pygame.init()
    pygame.display.set_mode(screen_size, DOUBLEBUF|OPENGL)

    self.camera_rot = [150.0,35.0]

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)

    glEnable(GL_TEXTURE_2D)
    glTexEnvi(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_MODULATE)
    glTexEnvi(GL_POINT_SPRITE,GL_COORD_REPLACE,GL_TRUE)

    glHint(GL_PERSPECTIVE_CORRECTION_HINT,GL_NICEST)
    glEnable(GL_DEPTH_TEST)

    self.model = model

    pygame.display.set_caption('3d Tic Tac Toe')

    # List for X
    self.dl_x = glGenLists(1)
    glNewList(self.dl_x,GL_COMPILE)
    glColor4f(1.0,0.0,0.7,1)
    glBegin(GL_LINES)
    glVertex3f(0.1,0.0,0.1); glVertex3f(0.9,0.0,0.9)
    glVertex3f(0.1,0.0,0.9); glVertex3f(0.9,0.0,0.1)
    glEnd()
    glEndList()

    # List for O
    self.dl_o = glGenLists(1)
    glNewList(self.dl_o,GL_COMPILE)
    glColor4f(1,1,1,1)
    glBegin(GL_LINE_STRIP)
    for i in range(0,100+1,1):
      angle = radians(360.0*i/100.0)
      glVertex3f(0.5+0.4*cos(angle),0.0,0.5+0.4*sin(angle))
    glEnd()
    glEndList()

  def set_view_3D(self, rect):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(camera_fov,float(screen_size[0])/float(screen_size[1]), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

  def set_camera(self, rect=[0,0,screen_size[0],screen_size[1]], cen=camera_center, rad=camera_radius):
    self.set_view_3D(rect)
      
    camera_pos = [
        cen[0] + rad*cos(radians(self.camera_rot[0]))*cos(radians(self.camera_rot[1])),
        cen[1] + rad*sin(radians(self.camera_rot[1])),
        cen[2] + rad*sin(radians(self.camera_rot[0]))*cos(radians(self.camera_rot[1]))
    ]
    gluLookAt(
        camera_pos[0],camera_pos[1],camera_pos[2],
        cen[0],cen[1],cen[2],
        0,1,0
    )

  def draw_grid(self):
    glBegin(GL_LINES)
    for layer in range(4):
      glColor4f(*board_colors[layer])
      for i in range(4+1):
        glVertex3f(i,spacing*layer,0); glVertex3f(i,spacing*layer,4)
        glVertex3f(0,spacing*layer,i); glVertex3f(4,spacing*layer,i)
    glEnd()

  def draw_fill(self):
    for layer in range(4):
      glBegin(GL_QUADS)
      glVertex3f(0,spacing*layer,0)
      glVertex3f(4,spacing*layer,0)
      glVertex3f(4,spacing*layer,4)
      glVertex3f(0,spacing*layer,4)
      glEnd()

  def draw_square(self,x,y,z):
    glBegin(GL_QUADS)
    glVertex3f(x,  spacing*y,z  )
    glVertex3f(x+1,spacing*y,z  )
    glVertex3f(x+1,spacing*y,z+1)
    glVertex3f(x,  spacing*y,z+1)
    glEnd()

  def draw_pieces(self):
    for y in range(4):
      for z in range(4):
        for x in range(4):
          piece = self.model.data[y][z][x]
          if piece == None:
            continue

          glPushMatrix()
          glTranslatef(x,spacing*y,z)
          if piece == 'X':
            glCallList(self.dl_x)
          if piece == 'O':
            glCallList(self.dl_o)
          glPopMatrix()

  def rotate_camera(self):
    key = pygame.key.get_pressed()
    if key[K_LEFT]:
      self.camera_rot[0] += 2
    if key[K_RIGHT]:
      self.camera_rot[0] -= 2
    if key[K_UP]:
      self.camera_rot[1] += 2
    if key[K_DOWN]:
      self.camera_rot[1] -= 2