from markov_python.cc_markov import MarkovChain
from fetch_data import get_insults

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

generated_insult = mc_insults.generate_text(100)
generated_comeback = mc_comebacks.generate_text(100)

print ("- %s\n- %s" % (format(generated_insult), format(generated_comeback)))