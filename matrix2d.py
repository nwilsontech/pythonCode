__APPNAME__ = 'Python Test'
__AUTHOR__ = 'nwilsontech'
__VERSION__ = {'Major':0,
               'Minor':1,
               'Revision':1,
               'Release':'Alpha'}

class AppTesting:
  def __runmessage(self, message):
    self.__print(__APPNAME__+message)
  def __print(self,message,align='^'):
    print('{:={}56}'.format(message, align))
  def __enter__(self):
    self.__print('Release:'+\
                 '.'.join(\
                     list(str(v) for k, v in __VERSION__.items())))
    self.__runmessage(': Started')
  def __exit__(self, exc_type, exc_val, exc_tb):
    self.__runmessage(': Finished')

app = AppTesting()

class Matrix:
  def __init__(self, rows, cols, defaultValue=None):
    assert rows >= 1 and cols >= 1, 'Min Size: 1 X 1'
    self._rows = rows
    self._cols = cols
    self._cells = [[defaultValue] * cols] * rows
  def __repr__(self):
    result = '\n'.join([str(self.row(i)) for i in range(self._rows)])
    return result
  def __len__(self):
    '''returns the product of rows & cols'''
    return self._rows*self._cols
  def __getitem__(self, index):
    '''provides subscriptable notation'''
    return self.row(index)
  def flatten(self):
    '''returns our N by M array as a single array'''
    return [cel for row in self._cells for cel in row]
  def fill(self, value):
    '''flood fills our cells with {value}'''
    self._cells = [[value] * self._cols] * self._rows
  def auto_fill(self):
    '''fills cells with corresponding index value'''
    for index, row in enumerate(self._cells):
      self._cells[index] = [(x+self._cols*(index)) for x in range(self._cols)]
    return self
  def row(self, index):
    '''returns entire row'''
    assert 0 <= index < self._rows, f'{index}: Index Out of Bounds'
    return self._cells[index]
  def col(self, index):
    '''returns entire column'''
    assert 0 <= index < self._cols, 'Index Out of Bounds'
    return [r[index] for r in self._cells]
  def update(self, row, col, val):
    self._cells[col + row*self._cols] = val
    return self
  def cell(self, row, col):
    return self._cells[col + row*self._cols]
  @property
  def dim(self):
    return (self._rows, self._cols)

if __name__ == '__main__':
  ''' Simple Test '''
  with app:
    g = Matrix(4,5, defaultValue=1)
    g.auto_fill()
    print(g[3][1])
    print(g.dim)
