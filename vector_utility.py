__AUTHOR__ = 'nwilsontech'

class Point:
  def __init__(self, x=0, y=0, z=0):
    self.x = x
    self.y = y
    self.z = z
  def __repr__(self):
    return str(tuple((self.x, self.y, self.z)))

def lerp_translate(p_src, p_dst, amt):
  assert 0 <= amt <= 1.0
  return Point(p_src.x*(1.0 - amt) - p_dst.x*amt,
               p_src.y*(1.0 - amt) - p_dst.y*amt,
               p_src.z*(1.0 - amt) - p_dst.z*amt)
