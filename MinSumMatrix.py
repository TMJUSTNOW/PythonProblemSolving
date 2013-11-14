
import time

matrix = [[1,2,3,4,4],[4,5,6,7,5],[7,8,9,10,5],[3,4,7,2,5],[3,4,7,2,10]]

# saves the minimum cost to reach each node on the matrix
minPathCache = [[None,None,None,None,None] for _ in range(5)]
# saves the best move to reach each node on the matrix
bestMoveCache = [[None,None,None,None,None] for _ in range(5)]

'''
get the minium sum of the path from (0,0) to (n,n) in the matrix
'''
def minPath(x,y):
  if minPathCache[x][y] is not None:
    return minPathCache[x][y]
  else:
    # all the previous places we could have come from
    previous = []
    if x > 0:
      previous.append( (minPath(x - 1, y), "U",) )
    if y > 0:
      previous.append( (minPath(x, y - 1), "L",) )

    bestTuple = min(previous) if previous else (0, "*",)
    minPathCache[x][y] = bestTuple[0] + matrix[x][y]
    bestMoveCache[x][y] = bestTuple[1]
    return minPathCache[x][y]

start = time.time()
print start
print minPath(4,4)
stop = time.time()
print stop
print "Elapsed: %.02f us" % ((stop - start) * 1000000)
print "\n".join([str(row) for row in bestMoveCache])