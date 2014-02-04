'''
max points on a line
Given n points on a 2D plane, 
find the maximum number of points that lie on the same straight line.

y = kx + b
save k, b = > two points

'''

class Point(object):
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def __str__(self):
    return 'x: ' +  str(self.x) + '_'+ 'y: '+ str(self.y)
  
def MaxPoints(points):
  # calculate line for every two points, save the k and a in hashmap
  # accumulate the points with the same k and a
  # math formulation : y - y1 = (y2-y1)/(x2-x1)(x-x1)
  length = len(points)
  map = {}
  num_max_points = 0
  # get all the unique pairs for points in the list
  for i in range(length):
    j = i + 1 
    for j in range(j,length):
      point1 = points[i]
      point2 = points[j]
      k = 0.0
      b = 0.0
      # slope k and intercept b
      if point2.y != point1.y and point2.x != point1.x:
        k = float(point2.y - point1.y) / float(point2.x - point1.x)
        b = point1.y - k * point1.x
        print ('points: {},{} -- k :{} and b : {}'.format(str(point1),str(point2),k,b))
      #  y = b
      elif point2.y == point1.y:
        k = 0
        b = point1.y
      #  x = b
      elif point2.x == point1.x:
        k = float('inf')
        b = point1.x

      if (k,b) not in map:
        map[(k,b)] = [point1,point2]
      elif point1 not in map[(k,b)]:
        map[(k,b)].append(point1)
      elif point2 not in map[(k,b)]:
        map[(k,b)].append(point2)

  for key,values in map.iteritems():
    print key
    for value in values:
      print str(value)
  
  for m in map:
    if len(map[m]) > num_max_points :
      num_max_points = len(map[m])

  return num_max_points
 
p1 = Point(3,2)
p2 = Point(2,4)
p3 = Point(4,5)
p4 = Point(1,6)
points  = []
points.extend((p1,p2,p3,p4))
print points

MaxPoints(points)


