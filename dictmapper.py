class DictionaryMappingProxy(type):
  '''
  Metaclass used to wrap dict
  '''
  def __init__(cls, name, bases, dict):
    super(DictionaryMappingProxy, cls).__init__(name, bases, dict)
    setattr(cls, '__setattr__', DictionaryMappingProxy.__metasetattr)
    setattr(cls, '__getattr__', DictionaryMappingProxy.__metagetattr)

  @staticmethod
  def __metagetattr(obj, attr):
    try:
      return obj[attr]
    except KeyError:
      raise AttributeError(attr)
  
  @staticmethod
  def __metasetattr(obj, attr, value):
    try:
      obj[attr] = value
      return obj[attr]
    except KeyError:
      raise AttributeError(attr)

# Example

class Settings(dict, metaclass=DictionaryMappingProxy):
  pass


internal = Settings()
internal['Name'] = 'James'
print(internal.Name)
internal.Name='Frank'
print(internal.Name)
