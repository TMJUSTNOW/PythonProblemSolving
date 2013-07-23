# given a string, return all the permutations based on the characters of the string
# abc:a 
def PermutationStr(string, chars_stack=None, used_chars=None):
  if chars_stack is None:
    chars_stack = []
  if used_chars is None:
    used_chars = [False for _ in range(len(string))]
  if all(used_chars):
    yield "".join(chars_stack)
  else:
    for i in range(len(string)):
      if not used_chars[i]:
        used_chars[i] = True
        chars_stack.append(string[i])
        for string1 in PermutationStr(string,
                                      chars_stack=chars_stack,
                                      used_chars=used_chars):
          yield string1
        used_chars[i] = False
        chars_stack.pop()

for perm in PermutationStr("abcd"):
  print perm

for a in [1,2,3]:
  for b in ['a','b','c']:
    for c in [10,11,12]:
      for d in ['z', 'y', 'x']:
        for e in ['q', 'r', 't']:
          print a, b, c, d, e

arrays = [
    [1,2,3],
    ['a','b','c'],
    [10,11,12],
    ['z', 'y', 'x'],
    ['q', 'r', 't'],
    [3, 4, 5]
]
def Foo(arrays, values=None):
  if values is None:
    values = []
  if not arrays:
    print ", ".join(str(v) for v in values)
  else:
    array = arrays.pop(0)
    for a in array:
      values.append(a)
      Foo(arrays, values=values)
      values.pop()
    arrays.append(array)
Foo(arrays)



