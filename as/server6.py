class Player:
  def __init__(self):
    self.x = None
    self.y = None
    self.z = None
    self.nickname = None

class Moderator(Player):
  def __init__(self):
    super().__init__()
    self.nickname = 'Moderator'
