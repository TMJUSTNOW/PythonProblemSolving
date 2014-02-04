def factorial(a):
  if a <= 1:
    return a
  else:
    return a * factorial(a - 1)


def sorted1(v):
  arr = []
  for _v in v:
    arr.append(_v)
  arr.sort()
  return arr
