# clone a graph
class Vertex(object):
  def __init__(self, name="", neighbors=None):
    self.name = name
    self.neighbors = neighbors if neighbors else []

  def Print(self):
    # Print the graph.
    printed = set()
    queue = [self]
    while queue:
      front = queue.pop(0)
      if front in printed:
        continue
      print "Node: %s, %s" % (front.name, ",".join([n.name for n in front.neighbors]))
      printed.add(front)
      queue.extend(front.neighbors)

def CloneGraph(vertex):
  old_to_new_verts = {}
  # Clone all the nodes then attach the neighbors using bfs
  queue = [vertex]
  while queue:
    front = queue.pop(0)
    if front in old_to_new_verts:
      continue
    old_to_new_verts[front] = Vertex(name=front.name + "'")
    queue.extend(front.neighbors)

  # Fill in their neighbors using the map
  for old_vertex, new_vertex in old_to_new_verts.iteritems():
    new_vertex.neighbors = [old_to_new_verts[n] for n in old_vertex.neighbors]
  return old_to_new_verts[vertex]

a = Vertex(name="A")
b = Vertex(name="B")
c = Vertex(name="C")
a.neighbors = [b, c]
b.neighbors = [a, c]
c.neighbors = [a, b]
a.Print()

print "\n"
aprime = CloneGraph(a)
aprime.Print()
