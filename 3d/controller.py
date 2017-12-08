class GameController(object):
  """controller for game"""
  def __init__(self, model):
    self.model = model
    self.done = False