__NOTES__ = '''
Random Initial Singleton / Processor Implementation
'''
__AUTHOR__ = '''
Nathaniel Wilson
'''


class Application:
  _instance = None
  _functions = []
  _reg_funcs = {}
  _reg_vals = {'regA':None, 'regB': None, 'regC': None}
  def __init__(self,*args, **kwargs):
    self._args = args
    self._kwargs = kwargs
  def Execute(self):
    # do stuff
    print(f'Application Executing with:\n\t {self._args} && {self._kwargs}')
    for fn in self._functions:
      fn()
  def RegisterFunction(self, func_name:str, func_args:int, func_def:callable):
    self._reg_funcs[func_name]={'argc':func_args, 'func_def':func_def}
  def InvokeFunction(self, func_name:str, *args):
    result = self._reg_funcs[func_name]['func_def'](*args)
    print(f'output> {result}')
  
  def Finalize(self):
    # do clean up
    pass
  @staticmethod
  def GetApp():
    if Application._instance is None:
      print('Initializing Application instance')
      Application._instance = Application(1)
    return Application._instance



if __name__ == '__main__':
  a = Application.GetApp()
  a.Execute()
  a.RegisterFunction('add',2, lambda x, y: x+y)
  a.InvokeFunction('add',1,2)
  b = Application.GetApp()
  b.Execute()
