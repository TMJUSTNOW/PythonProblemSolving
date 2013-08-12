'''
Given a number, return the squre root for the number
using binary search to find the mid, then compare the number with mid^2 
'''
def SqureRoot(num,start,end,precision):
  mid = (start + end) / 2.0
  midSqure = mid * mid
  if abs(midSqure - num) <= precision:
    print mid
  elif midSqure > num:
    SqureRoot(num,start,mid,precision)
  elif midSqure < num:
    SqureRoot(num,mid,end,precision)

SqureRoot(35.0,0.0,35.0,0.001)