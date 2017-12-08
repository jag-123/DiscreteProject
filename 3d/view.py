from settings import *

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from math import *

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
        cen[1] + rad                     *sin(radians(self.camera_rot[1])),
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

  def draw(self):
    self.set_camera()
    
    glClear(GL_DEPTH_BUFFER_BIT)

    # self.draw_fill()

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    self.draw_grid()

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