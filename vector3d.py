'''
basic vector3d class
'''

class Vec3(object):
  def __init__(self, *args):
    if len(args) == 1 and isinstance(args, Vec3):
      self.xyz = args.xyz
    else:
      self._components = [*args[:3]] + [0] * (3-min(len(args), 3))
  @property
  def x(self):
    return self._components[0]
  @property
  def y(self):
    return self._components[1]
  @property
  def z(self):
    return self._components[2]
  @property
  def xy(self):
    return self._components[0:2]
  @property
  def yz(self):
    return self._components[1:]
  @property
  def xyz(self):
    return self._components[:]
  @x.setter
  def x(self, value):
    self._components[0] = value
  @y.setter
  def y(self, value):
    self._components[1] = value
  @z.setter
  def z(self, value):
    self._components[2] = value
  @xy.setter
  def xy(self, value):
    assert len(value)==2
    self.x, self.y = value
  @yz.setter
  def yz(self, value):
    assert len(value)==2
    self.y, self.z = value
  @xyz.setter
  def xyz(self, value):
    assert len(value)==3
    self.x, self.y, self.z = value
  
  def magnitude(self):
    '''calculates the magnitude of the vector'''
    return sum(x*x for x in self.xyz) ** 0.5

  def __neg__(self):
    return Vec3(-self.x, -self.y, -self.z)

  def crossProduct(self, rhs):
    '''
    cx = aybz − azby
    cy = azbx − axbz
    cz = axby − aybx	
    '''
    return Vec3(
      self.y*rhs.z - self.z*rhs.y,
      self.z*rhs.x - self.x*rhs.z,
      self.x*rhs.y - self.y*rhs.x
    )

  def dotProduct(self, rhs):
    '''vector dot product'''
    assert isinstance(rhs, Vec3)
    return sum([a*b for a, b in zip(self.xyz, rhs.xyz)])

  def normalize(self):
    '''vector normalized'''
    self.xyz = (self/self.magnitude()).xyz

  def __mul__(self, rhs):
    '''vector scalar multiplication'''
    assert isinstance(rhs, (int, float))
    return Vec3(*[a*rhs for a in self.xyz])

  def __add__(self, rhs):
    if isinstance(rhs, Vec3):
      return Vec3(*[a+b for a,b in zip(self.xyz, rhs.xyz)])
    elif isinstance(rhs, (int, float)):
      return Vec3(*[a+rhs for a in self.xyz])

  def __iadd__(self, rhs):
    '''v += rhs'''
    self.xyz = (self + rhs).xyz

  def __sub__(self, rhs):
    if isinstance(rhs, Vec3):
      return Vec3(*[a-b for a,b in zip(self.xyz, rhs.xyz)])
    elif isinstance(rhs, (int, float)):
      return Vec3(*[a-rhs for a in self.xyz])
  
  def __isub__(self, rhs):
    self.xyz = (self - rhs).xyz

  def __truediv__(self, rhs):
    assert isinstance(rhs, (int, float))
    return Vec3(*[a/rhs for a in self.xyz])
  def __repr__(self):
    return f'Vec3({self._components})'
