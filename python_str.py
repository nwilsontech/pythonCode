def srot(s:str, offset=0)->str:
  ''' Simple String Rotation'''
  offset %= len(s)
  return s[offset:]+s[:offset]
