__author__ = '''nwilsontech'''
__ver__ = (1, 0, 0, 'Initial')
'''
Simple python file testing out classes and relation of users.
'''


class UserPrivilege:
  ''' User Privilege Class'''
  def __init__(self, access):
    self.__access = access
  
  def __repr__(self):
    return f'{self.__access.title()}'
  
  @property
  def valid(self):
    return self.__access.lower() in self.Options
  
  @property
  def code(self):
    return self.Options.index(self.__access.lower())
  
  @property
  def Options(self):
    return ['visitor','staff','engineer','admin']


class User:
  ''' User Base Class '''
  def __init__(self, Name, access, *_ignore):
    self._name = Name
    self._priv = UserPrivilege(access)
  
  @property
  def Access(self):
    return self._priv
  
  def __repr__(self):
    return f'{self._name} (Access Granted: {self.Access()})'

class VisitorUser(User):
  ''' User Derived Class with Vistor Access '''
  def __init__(self, Name):
    super().__init__(Name, 'visitor')

class StaffUser(User):
  ''' User Derived Class with Staff Access '''
  def __init__(self, Name):
    super().__init__(Name, 'staff')

class EngineerUser(User):
  ''' User Derived Class with Engineer Access '''
  def __init__(self, Name):
    super().__init__(Name, 'engineer')

class AdminUser(User):
  ''' User Derived Class with Admin Access '''
  def __init__(self, Name):
    super().__init__(Name, 'admin')

class Users:
    ''' User Collection Class '''
    def __init__(self, members):
        self.__count = 0 # not utilizing yet
        self.__members = []
        for m in members:
          if isinstance(m, str):
            self.createVisitor(m)
          elif isinstance(m, User):
            self.add(m)
          else:
            raise TypeError(m)
    
    def add(self, uac):
      if isinstance(uac, User):
        self.__members.append(uac)
      else:
        raise TypeError(uac)
    
    def __len__(self):
        return len(self.__members)
    
    def createVisitor(self, Name):
      self.add(VisitorUser(Name))
    
    def __contains__(self, member):
        return member in self.__members
    
    def __repr__(self):
      nlu = '\n'.join(map(str,self.__members))
      return 'Users Accounts:\n%s' % nlu

''' Start UnitTesting '''
db = Users(['James','Eli',AdminUser('Victor')])

print(db)
print()

test_a = VisitorUser('James')
test_b = StaffUser('Blake')
test_c = EngineerUser('William')
test_d = AdminUser('Elliot')

print(test_a)
print(test_b)
print(test_c)
print(test_d)
