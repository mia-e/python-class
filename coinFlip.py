#Mia Escoto 
# Coin toss experiment 

import random
import statistics
import math

def coinToss():
 coin = ["heads", "tails"]
 flip = random.choice(coin)
 return flip 

def trial():
 global b 
 b = 0
 a = []
 while ("heads" and "tails") not in a:
  b+=1
  result = coinToss()
  a.append(result)
 return b

c = []
for i in range(0, 10000):
 trial()
 c.append(b)
print(round(statistics.mean(c)))