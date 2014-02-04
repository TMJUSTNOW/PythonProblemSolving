'''
Given an integer n,
generate a square matrix filled with elements from 1 to n^2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

def spiral_matrix(n):
  # create the empty matrix
  matrix  = [[None]*n for i in range(n)]
  # starting position (x,y)
  x,y = 0,0
  # the direction of the increment of x and y
  dx,dy = 1,0

  for j in range(n**2):
    matrix[y][x] = j + 1
    nx,ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < n and matrix[ny][nx] == None:
      x,y = nx,ny
    else:
      # changing the direction of x and y 
      # magic part!!!!
      dx,dy = -dy,dx
      x,y = x + dx,y + dy

  return matrix


matrix = spiral_matrix(3)
for row in matrix:
  print row


'''
Given a matrix of m x n elements (m rows, n columns), 
return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

'''
def spiral_matrix2(matrix,m,n):
  nums = []
  x_bounds = [0, m]
  y_bounds = [0, n]
  sx,sy = 0,0
  dx,dy = 1,0
  for _ in range(m * n):
    nums.append(matrix[sy][sx])
    nx,ny = sx + dx, sy + dy
    if x_bounds[0] <= nx < x_bounds[1] and y_bounds[0] <= ny < y_bounds[1]:
      sx,sy = nx,ny
    else:
      dx,dy = -dy,dx 
      sx,sy = sx + dx, sy + dy

  return nums

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print spiral_matrix2(matrix,3,3)
'''
given you a list of number, print the matrix in spiral order
'''
