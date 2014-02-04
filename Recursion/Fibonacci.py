'''write a method to generate the nth fibonacci number
1,1,2,3,5,8...
'''

FIB_CALCULATIONS = 0

def fibonacci(n):
  if n == 1 or n== 2:
    return 1
  elif n < 1:
    return None
  else:
    global FIB_CALCULATIONS
    FIB_CALCULATIONS += 1
    return fibonacci(n - 1) + fibonacci(n - 2)


CACHED_FIB_CALCULATIONS = 0

FIB_CACHE = {}

@memoize.Memoize()
def cached_fibonacci(n):
  if n == 1 or n== 2:
    return 1
  elif n < 1:
    return None
  else:
    global FIB_CACHE
    if n in FIB_CACHE:
      return FIB_CACHE[n]
    else:
      global CACHED_FIB_CALCULATIONS
      CACHED_FIB_CALCULATIONS += 1
      result = cached_fibonacci(n - 1) + cached_fibonacci(n - 2)
      FIB_CACHE[n] = result
      return result


def fib3(n):
  if n == 1 or n== 2:
    return 1
  elif n < 1:
    return None
  else:
    return fib3(n - 1) + fib3(n - 2)


      


# def main():
#   print fibonacci(6)
#   print fibonacci(1)
#   print fibonacci(2)
#   print fibonacci(0)

# main()

print fibonacci(20)
print "Made %d calculations" % FIB_CALCULATIONS
print cached_fibonacci(20)
print "Made %d calculations" % CACHED_FIB_CALCULATIONS
print FIB_CACHE
