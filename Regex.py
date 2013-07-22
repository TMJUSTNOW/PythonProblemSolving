# practise  regex
import re
strs = [
    "8144658695",
    "812 673 5748",
    "812  453   6783",
    "812-348 7584",
    "(617) 536 6584",
    "834-674-8595",
    "(834 674 8595",
]
for str1 in strs:
  s = ''
  match = re.match(r'(\((?P<ac1>\d{3})\)|(?P<ac2>\d{3}))(\s*|-)(?P<m3>\d{3})(\s*|-)(?P<l4>\d{4})',str1)
  if match:
    # print match.groups(), match.group("last")
    s = (match.group("ac1") or match.group("ac2")) + ' ' + match.group("m3") + ' ' + match.group("l4")
    print s
  else:
    print "Does not match: ", str1

infos = [
  'Zaphod, Beeble, 23/12/1994',
  'Dent, Arthur, 05/04/1993',
  'Feynman, Richard, 18/02/1956'
]

for info in infos:
  newDate  = ''
  match  = re.search(r'(?P<month2>\d{2})/(?P<date2>\d{2})/(?P<year4>\d{4})',info)
  newDate = match.group('date2') + '/' +  match.group('month2') + '/' + match.group('year4')[2:]
  print newDate

text = """a@b.com A towel, @f.com it says, is about the most massively useful thing an
interstellar hitchhiker can have. Partly it has great practical value
- you can wrap it around you dent@vogon.com for warmth as you bound across the cold
moons of Jaglan Beta; you can lie on it on the brilliant marble-sanded
beaches of Santraginus V, foo@bar.bar.com inhaling the heady sea vapours; you can
sleep under it beneath the stars which shine so redly on the desert
world of Kakrafoon; use it john.smith@blah.org to sail a mini raft down the slow heavy
river Moth; wet it for use in hand-to- hand-combat; wrap it round your
head to ward off glom@flop.net noxious fumes or to avoid the gaze of the Ravenous
Bugblatter Beast of Traal (a mindboggingly stupid animal, it assumes
that if you can't see it, it can't see you - daft as a bush, but very
ravenous); you can wave your towel in emergencies as a distress
signal, and of course dry yourself off with it if it still seems to be
clean enough."""

# get all the email address
for m in re.finditer(r'\b\w[\w\d_-]*(\.\w[\w\d_-]*)*@(\w+\.)+\w+\b', text):
  print m.group(0)# entire match



