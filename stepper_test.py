__version__ = (1, 1, 0)
__author__ = 'Nathaniel Wilson'
__email__ = 'unlisted'

class Stepper:
  def __init__(self, scale):
    self._current = 0
    self._limit = scale
    self._loop = False
  def step(self, by=1):
    if (self._current + by) <= self._limit:
      self._current += by
    elif self._loop:
      self.reset()
  def reset(self, default=0):
    self._current = default
  @property
  def inprogess(self):
    return not self.finished
  @property
  def finished(self):
    return self._current == self._limit
  @property
  def value(self):
    return self._current
  @property
  def as_per(self):
    return self._current / self._limit
  

class Point2D:
  def __init__(self, x, y):
    self.components = {'x': x, 'y': y}
  @property
  def x(self):
    return self.components['x']
  @x.setter
  def x(self, val):
    self.components['x'] = val
  @property
  def y(self):
    return self.components['y']
  @y.setter
  def y(self, val):
    self.components['y'] = val
  def lerp(self, otherPoint, time_division):
    assert 1.0 >= time_division >= 0
    tX = (1 - time_division) * self.x + otherPoint.x*time_division
    tY = (1 - time_division) * self.y + otherPoint.y*time_division
    return Point2D(int(tX), int(tY))
  def self_lerp(self, otherPoint, time_division):
    self = self.lerp(otherPoint, time_division)
  @property
  def as_array(self):
    return [ self.components[x] for x in self.components]
  
  @as_array.setter
  def as_array(self, val):
    assert len(val) == len(self.components)
    for i, k in enumerate(self.components):
      self.components[k] = val[i]


  def findDistance(self, otherPoint):
    dX = (self.x - otherPoint.x) ** 2
    dY = (self.y - otherPoint.y) ** 2
    return (dX + dY) ** 0.5
  def __repr__(self):
    return str(self.components)


class Point3D:
  def __init__(self, x, y, z, w):
    self.components = {'x': x, 'y': y, 'z': z}
  @property
  def x(self):
    return self.components['x']
  @x.setter
  def x(self, val):
    self.components['x'] = val
  @property
  def y(self):
    return self.components['y']
  @y.setter
  def y(self, val):
    self.components['y'] = val
  @property
  def z(self):
    return self.components['z']
  @z.setter
  def z(self, val):
    self.components['z'] = val
  def lerp(self, otherPoint, time_division):
    assert 1.0 >= time_division >= 0
    tX = (1 - time_division) * self.x + otherPoint.x*time_division
    tY = (1 - time_division) * self.y + otherPoint.y*time_division
    tZ = (1 - time_division) * self.z + otherPoint.z*time_division
    return Point3D(tX, tY, tZ)
  def self_lerp(self, otherPoint, time_division):
    self = self.lerp(otherPoint, time_division)

  def findDistance(self, otherPoint):
    dX = (self.x - otherPoint.x) ** 2
    dY = (self.y - otherPoint.y) ** 2
    dZ = (self.z - otherPoint.z) ** 2
    return (dX + dY + dZ) ** 0.5
  def __repr__(self):
    return str(self.components)



AA = Point2D(0, 0)
BB = Point2D(100,0)
step = Stepper(100)
while step.inprogess:
  tmp = AA.lerp(BB,step.as_per)
  print(step.value, tmp)
  step.step()
else:
  tmp = AA.lerp(BB,step.as_per)
  print(step.value, tmp)
