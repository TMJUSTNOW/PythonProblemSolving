

def _ConsumeString(str_value, last, has_jumped):
  """Consumes the string value.

  Args:
    last: The last number that was read.
    has_jumped: Whether we have skipped a number.

  Returns:
    A tuple of a success boolean (for whether we have read the whole string),
    and the missing number.
  """
  next1 = str(last + 1)
  if str_value.startswith(next1):
    return _ConsumeString(str_value[len(next1):], last + 1, has_jumped)
  elif not has_jumped:
    next2 = str(last + 2)
    if str_value.startswith(next2):
      success, _ = _ConsumeString(str_value[len(next2):], last + 2, True)
      return success, last + 1 if success else None
    else:
      return False, None
  else:
    return not str_value, None


def FindMissing(str_value):
  """Finds the missing consecutive number in the string value."""
  for i in range(1, len(str_value) / 2):
    try:
      first = int(str_value[0:i])
      success, jumped = _ConsumeString(str_value[i:], first, False)
      if success:
        return jumped
    except ValueError:
      continue
  return -1


print FindMissing("12345689101112")
print FindMissing("9991000100110021004")
# There's no missing number, so it should return -1.
print FindMissing("123456789101112")
