#Mia Escoto 
#casino games
from random import choice
from typing import Counter 

#symbols = ["cherry", "lemon", "orange", "bananna", "[bar] [bar]", "bell", "LUCKY7", "horseshoe", "WILD", "*scatter*", "STACK", "double diamond"]

def playSlot(userMoney):

  def slotType():
    while True:
      try:
        type = int(input("What type of slot would you like to play? Enter 1 for small win, 2 for medium win, 3 for big win? "))
        if type != 1 and type !=2 and type!=3:
          print("Please enter a number 1-3")
          continue
      except ValueError:
        print("Please enter a number 1-3")
        continue
      break
    return type

  def smallSlot():
    prize = 0
    print("To win you need to land all 3 numbers, if you land all three 7 you have a bonous ")
    symbols = ["  7  ", "  8  ", "  9  ", "  6  ", "  1  ", "  3  ", "  2  "]
    slot1 = choice(symbols)
    slot2 = choice(symbols)
    slot3 = choice(symbols)
    print(f"""
          ---------------------
          |{slot1}| {slot2}| {slot3}|
          ---------------------""")
    if slot1 == slot2 and slot1 == slot3:
      prize += 100
      if slot1 == "  7  ":
        prize+=100
    if int(slot1) == int(slot2)-1 and int(slot2) == int(slot3)-1:
      prize +=200
    if prize!=0:
      print(f"YOU WON ${prize}")
    else:
      print(f"you did not win.")
    return prize


  def midSlot():
    prize = 0
    symbols = [" Cherry  ", "  Apple  ", "  Orange ", "Blueberry", " Bananna ", "  Grape  ", "  Lemon  ", "  Melon  ", "  Mango  ", "  Lime   ", " Tomato  "]
    slots = [choice(symbols), choice(symbols), choice(symbols), choice(symbols), choice(symbols), choice(symbols), choice(symbols), choice(symbols), choice(symbols)]
    print(f"""  
            -------------------------------
            |{slots[0]}|{slots[1]}|{slots[2]}|
            -------------------------------
            |{slots[3]}|{slots[4]}|{slots[5]}|
            -------------------------------
            |{slots[6]}|{slots[7]}|{slots[8]}|
            -------------------------------""")

    if (slots[0] == slots[1] and slots[2] == slots[0]) or (slots[6] == slots[7] and slots[6] == slots[8]):
      if slots[0] == slots[6]:
        prize += 600
      else:
        prize+=300
    if (slots[0] == slots[3] and slots[6] == slots[0]) or (slots[2] == slots[5] and slots[2] == slots[8]):
      if slots[0] == slots[2]:
        prize += 600
      else:
        prize+=300
    if (slots[0] == slots[4] and slots[0] == slots[8]) or (slots[2] == slots[4] and slots[2] == slots[6]):
      if slots[0] == slots[2]:
        prize += 600
      else:
        prize+=300
    if (slots[1] == slots[4] and slots[1] == slots[7]) or (slots[3] == slots[4] and slots[3] == slots[5]):
      if slots[1] == slots[3]:
        prize += 1000
      else:
        prize+=500

    if prize != 0:
      print(f"YOU WON ${prize}")
    else:
      print("you did not win.")
    return prize

#    symbols = [" cherry  ", "blueberry", " bananna ", "  grape  ", "  lemon  ", "  melon  ", "  mango  ", "  lime   ", " tomato  ", " cracker ",   "  juice  ", "   red   ", "  apple  ", "  orange ",  "   blue  ", "    7    ", "  WILD   ", "  fruit  ", ]

  def bigSlot():
    win = 0
    symbols = [" cherry  ", "blueberry", " bananna ", "  grape  ", "  lemon  ", "  melon  ", "  mango  ",   "  juice  ", "   red   ", "  apple  ", "  WILD   " ]
    slots = [choice(symbols), choice(symbols), choice(symbols), choice(symbols), choice(symbols), choice(symbols), choice(symbols), choice(symbols), choice(symbols), choice(symbols), choice(symbols), choice(symbols), choice(symbols), choice(symbols), choice(symbols)]
    print(f"""  
            ---------------------------------------------------
            |{slots[0]}|{slots[1]}|{slots[2]}|{slots[3]}|{slots[4]}|
            ---------------------------------------------------
            |{slots[5]}|{slots[6]}|{slots[7]}|{slots[8]}|{slots[9]}|
            ---------------------------------------------------
            |{slots[10]}|{slots[11]}|{slots[12]}|{slots[13]}|{slots[14]}|
            ---------------------------------------------------""")
    def slotAcross(index, prize):
      win = 0
      counter=0
      for i in range(4):
        if slots[index] == slots[index+1]:
          counter +=1
          index +=1
      if counter == 4:
        win+= prize
      return win

    def slotDown(index):
      win = 0
      counter=0
      for i in range(2):
        if slots[index] == slots[index+5]:
          counter +=1
          index +=5
      if counter == 2:
        win+= 3000
      return win

    def slotDiagRight(index):
      win = 0
      counter=0
      for i in range(2):
        if slots[index] == slots[index+6]:
          counter +=1
          index +=6
      if counter == 2:
        win+= 1500
      return win



    def slotDiagLeft(index):
      win = 0
      counter=0
      for i in range(2):
        if slots[index] == slots[index+4]:
          counter +=1
          index +=4
      if counter == 2:
        win+= 1500
      return win


    symbol = [i.strip() for i in symbols]
    for i in range(15):
      if slots[i] == "  WILD   ":
        while True:
          wild = input(f"What would you like the WILD in slot {i+1} to be?").strip()
          if wild not in symbol:
            print("Please chose a slot")
            continue
          break
        for j in range(len(symbols)):
          if wild == symbols[j].strip():
            wild = symbols[j]
        slots[i] = wild
        print(slots[j])
        print(f"""  
              ---------------------------------------------------
              |{slots[0]}|{slots[1]}|{slots[2]}|{slots[3]}|{slots[4]}|
              ---------------------------------------------------
              |{slots[5]}|{slots[6]}|{slots[7]}|{slots[8]}|{slots[9]}|
              ---------------------------------------------------
              |{slots[10]}|{slots[11]}|{slots[12]}|{slots[13]}|{slots[14]}
              ---------------------------------------------------""")


    #Adding across wins

    win += slotAcross(0, 5000) + slotAcross(5, 10000)  + slotAcross(10, 5000)
    #Adding down wins
    win += slotDown(0) + slotDown(1) +slotDown (2) + slotDown(3) + slotDown(4)
    #Adding right diagnal wins
    win += slotDiagRight(0) + slotDiagRight(1) + slotDiagRight(2)
    #Adding left diagnal wins
    win += slotDiagLeft(4) +slotDiagLeft(3) +slotDiagLeft(2)
    if win !=0:
      print(f"YOU WON ${win}")
    else:
      print("You did not win.")
    return win


  while False:
    x = bigSlot()
    if x > 1:
      break
    
  while True:
    type = slotType()
    if type == 1:
      userMoney -=5
      userMoney += smallSlot()
    if type == 2:
      userMoney -= 50
      userMoney += midSlot()
    if type == 3:
      userMoney -= 150
      userMoney += bigSlot()
    while True:
      try:
        playAgain = int(input(f"You have ${userMoney} left. Would you like to play again? enter 1 for yes and any number for no. "))
        break
      except ValueError: 
        print("Please enter a number")
        continue
    if playAgain !=1:
      break




playSlot(5000)