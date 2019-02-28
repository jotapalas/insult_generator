from markov_python.cc_markov import MarkovChain
from fetch_data import get_insults

import sys
from getopt import getopt

def format(str):
  out = str[0].capitalize()
  for i in range(1, len(str)):
    if str[i] == str[i-1]:
      out += ','
    out += ' ' + str[i]
  return out

mc_insults = MarkovChain()
mc_comebacks = MarkovChain()
insults = get_insults()

for insult in insults:
  mc_insults.add_string(insult[0])
  mc_comebacks.add_string(insult[1])

count = 1
optlist, args = getopt(sys.argv[1:], 'c:')
for arg in optlist:
  if arg[0] == '-c':
    count = int(arg[1])
    break;
else:
  if len(args) > 0:
    count = int(args[0])

while count > 0:
  generated_insult = mc_insults.generate_text(100)
  generated_comeback = mc_comebacks.generate_text(100)
  print ("- %s\n- %s\n" % (format(generated_insult), format(generated_comeback)))
  count -= 1