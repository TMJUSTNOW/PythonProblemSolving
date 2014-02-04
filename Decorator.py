
# class Decorator(object):

#   def __init__(self):
#     self.func = func
#     print "Created a decorator with: %s" % func

# @Decorator()
# def Foo(n):
#   print "Foo: %d" % n
#   return 2 * n

# Foo(2)


class double_it(object):

    def __init__(self, f):
        print "__init__()"
        self.f = f

    def __call__(self, *args):
        print "__call__()"
        return 2 * self.f(*args)

@double_it
def multiply(x, y):
  return x * y

print multiply(3, 4)


class cacher(object):

  def __init__(self, func):
    # print "__init__()"
    self.cache = {}
    self.func = func

  def __call__(self, n):
    # print "__call__(%d)" % n
    if n in self.cache:
      return self.cache[n]
    else:
      result = self.func(n)
      self.cache[n] = result
      return result

NUM_CALCS = 0

@cacher
def fibonnaci(n):
  if n == 1 or n== 2:
    return 1
  elif n < 1:
    return None
  else:
    global NUM_CALCS
    NUM_CALCS += 1
    return fibonnaci(n - 1) + fibonnaci(n - 2)

print fibonnaci(20)
print "# calcs: %d" % NUM_CALCS
