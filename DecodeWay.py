'''
decode numbers into characters
return the number of ways to decode a number
'''
A 1
B 2
C 3

# DICT = {}
# for i in range(26):
#   DICT[i+1] = chr(ord('A') + i)
DICT = dict((i + 1, chr(ord('A') + i)) for i in range(26))
print DICT

'''
check whether the string can be decoded
Args: string
Return: whether it can bew found in the dictionary
'''
def is_valid(str1):
  str_int = int(str1)
  return str_int >= 0 and str_int <= 26 and DICT[str_int]

'''
Return how many ways that you can decode a number based on existing dictionary

Args: Integer number
Return: number of ways to decode the number
'''
def decode_ways1(num):
  # cover the integer number to string
  num_str = str(num)
  # number of ways for decoding the number
  num_ways = 0
  for i in range(len(num_str)):
    # if the substring from index 0 to i are valid,
    # recursively check the rest of the string
    if is_valid(num_str[0:i+1]):
      # get the rest of the string
      rest = num_str[i+1:]
      # the rest of the string is an empty string
      #  the number of ways increase one
      if not rest:
        num_ways += 1
      #  recursively call the function if the rest of the string can be decoded
      else:
        num_ways += decode_ways1(rest)

  return num_ways

'''
given integer number,
return all the ways that you can decode
'''
def decode_ways2(num):
  pass
'''
given the integer in string format,
return whether it can be decoded from the dictionary
'''
def valid(char):
  char_int = int(char)
  return char_int <= 26 and char_int > 0 and DICT[char_int]
'''
given a number and the dictionary
return how many ways the number can be decoded
'''
def decode_number(num):
  num_str = str(num)
  num_ways = 0
  for i in range(len(num_str)):
    # Check all substrings to see if they're valid.
    if valid(num_str[0:i+1]):
      rest_of_string = num_str[i+1:]
      # See if the rest of the string can be decoded.
      if not rest_of_string:
        num_ways += 1
      else:
        num_ways += decode_number(rest_of_string)
    else:
      break
  return num_ways

print decode_ways1(123123)