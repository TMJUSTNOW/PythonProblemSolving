def isMatch(string, pattern):
  """Determine if the string matches the pattern.

  The pattern supports the '.' character, meaning it can match anything, and
  the '*' operator, which means zero or more matches of the preceding character.
  The function works recursively by splitting off characters from the front
  of the string and the pattern as they are matched.

  Args:
    string: The string we are to match.
    pattern: The pattern to subject it to.

  Returns:
    Boolean true or false for whether the pattern matches the string.
  """
  if not string:
    # Only both being empty is a match.
    return not pattern
  elif not pattern:
    return False
  s0 = string[0]
  p0 = pattern[0]
  # Lookahead for '*'
  if len(pattern) >= 2 and pattern[1] == "*":
    # This is a wildcard match.
    if p0 == "." or s0 == p0:
      # The characters match.
      # Consider consuming this character in the string but keeping that
      # character of the pattern on the matching stack.
      if isMatch(string[1:], pattern):
        return True
      # Consider consuming the characer and the matching pattern, saying we
      # are done recognizing this.
      if isMatch(string[1:], pattern[2:]):
        return True
    # Either there was no match, or we're considering the hypothesis that
    # the wildcard pattern matched zero characters.
    return isMatch(string, pattern[2:])
  elif p0 == "." or s0 == p0:
    # It's a match.
    return isMatch(string[1:], pattern[1:])
  else:
    return False

def test(tuples):
  """Present the given tuples to the 'isMatch' function for testing.

  Prints 'Success' or '*** FAIL ***' for each test case.

  Args:
    tuples: A list of tuples containing a string, a pattern, and the desired
      return of the 'isMatch' function.
  """
  for t in tuples:
    print (t[0], t[1], t[2],
           "Success" if isMatch(t[0], t[1]) == t[2] else "*** FAIL ***")

test([
    ("aa", "a", False),
    ("aa", "aa", True),
    ("aaa", "a", False),
    ("aa", "a*", True),
    ("aa", ".*", True),
    ("ab", ".*", True),
    ("aab", "c*a*b", True),
    ("aa", ".", False),
])

