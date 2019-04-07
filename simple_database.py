from random import randint
import names

op_table = {
  'has':lambda a, b: b in a,
  '>':lambda a, b: a > b,
  '>=':lambda a, b: a >= b,
  '<':lambda a, b: a < b,
  '<=':lambda a, b: a <= b,
  '!=':lambda a, b: a != b,
  '==':lambda a, b: a == b,
}

class Database:
  def __init__(self):
    self.tbl_collection = {}
  def CreateTable(self, tbl):
    assert tbl.name not in self.tbl_collection, "Collection Already Exist"
    self.tbl_collection[tbl.name] = tbl
  def Get(self,lookup):
    return None if lookup not in self.tbl_collection else self.tbl_collection[lookup]

class CExpr:
  def __init__(self, test, expr, val):
    self.test = test
    self.expr = expr
    self.val  = val
  def res(self, tval):
    return op_table[self.expr](tval, self.val)

class Table:
  def __init__(self, name):
    self.name = name
    self.rows = []
  def insert(self, **data):
    self.rows.append(data)
  def select(self, columns=[], condition=[]):
    ret = []
    for row in self.rows:
      ev = 0
      for cond in condition:
        if cond.res(row[cond.test]):
          ev += 1
        else:
          #print(row[cond.test],cond.res(row[cond.test]),'skipping')
          continue
      if ev == len(condition):
        ret += [{k:v for (k,v) in row.items() if k in columns}]
    print(f'results from query: {len(ret)}')
    
    for r in ret:
      print(r)
  def dump(self):
    for i, row in enumerate(self.rows):
      print(f'Row {i}:', row)

db = Database()
db.CreateTable(Table('users'))
for i in range(100):
  db.Get('users').insert(fname=names.get_first_name(),
                         lname=names.get_last_name(),
                         age=randint(16,67),
                         notes='nada')
db.Get('users').dump()
db.Get('users').select(columns=['fname','lname','notes'],condition=[CExpr('age','<=',32)])
