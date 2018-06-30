class Thing:
  def __init__(self, name):
    self.name = name

t = Thing("clint")
# v = getattr(t, 'age', 'no name')
# print(v)
print(t.__class__.__name__)
