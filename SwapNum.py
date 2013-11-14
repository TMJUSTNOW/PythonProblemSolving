def SwapNum(a,b):
  """
  Swap two numbers without temporary variable
  Arguments: two numbers a and b
  Output: a and b after swap
  """
  a = b - a
  b = b -a 
  a = a + b
  print "a : %d, b: %d" % (a,b)

def SwapNum1(a,b):
  print a,b
  a = a^b
  print a,b
  b = a^b
  print a,b
  a = a^b
  print a,b

SwapNum1(1,2)