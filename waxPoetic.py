#Mia Escoto 
#Wax Poetic 
import random

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrand", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalixingly", "furiously", "sensuously"]
p_nouns = []
p_verbs = []
p_adj = []
p_prep = []
p_adv = []

def choice(list):
  random_element = random.choice(list)
  return random_element

for i in range(3):
  p_nouns.append(choice(nouns))
  p_verbs.append(choice(verbs))
  p_adj.append(choice(adjectives))
  for i in range(2):
    p_prep.append(choice(prepositions))
    p_adv.append(choice(adjectives))
  if p_adj[0].startswith('a' or 'e' or 'i' or 'u' or 'o'):
    p_article = "an"
  else:
    p_article = "a"

print(f"""{p_article} {p_adj[0]} {p_nouns[0]}. {p_verbs[0]} {p_prep[0]} the {p_adj[1]}
{p_nouns[1]} {p_adv[0]} the {p_nouns[0]} {p_verbs[1]}
the {p_nouns[1]} {p_verbs[2]} {p_prep[1]} a {p_adj[2]} {p_nouns[2]}""")