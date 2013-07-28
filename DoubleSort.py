
class Person(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age

persons = [
  Person("Emma", 25),
  Person("Adam", 29),
  Person("Adam", 61),
  Person("Adam", 30),
  Person("Emma", 10),
  Person("Paul", 29),
]
persons.sort(key=lambda x: (x.name, -x.age))
print "\n".join(["%s %d" % (p.name, p.age) for p in persons])
