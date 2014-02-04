#!/usr/bin/env python


'''
Given a string containing only digits, 
restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''
ips = []
def restore_ip(ip_str, num_segment):
  '''
    Args:
      ip_str:a string represent ip
      num_segment: number segments of the ip
    Return: 
      list of possible ip
  '''
  solutions = []
  if not num_segment:
    raise Exception("Should never happen")
 
  for i in range(1, len(ip_str) + 1):
    segment = ip_str[0:i]
    segment_value = int(segment)
    if segment_value > 255:  # like '2551'
      break
    elif len(segment) >= 2 and segment.startswith('0'):  # like '01'
      break
    else:
      if num_segment == 1:
        if not ip_str[i:]:
          # It's empty, so this is a solution.
          solutions.append(segment)
      else:
        sub_segments = restore_ip(ip_str[i:], num_segment - 1)
        if sub_segments:
          solutions.extend([segment + "." + s for s in sub_segments])
  return solutions


print restore_ip("25525511135", 4)
print restore_ip("21111", 4)
