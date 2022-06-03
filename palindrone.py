def isPal(str):
  str = purge(str)
  p_letters = 0
  for i in range(len(str)):
    if str[i] == str[len(str) - (i+1)]:
      p_letters+=1
  if p_letters == len(str):
    return True
  else: 
    return False

def isAlmostPal(str):
  if isPal(str) == True:
    return False
  else:
    str = purge(str.lower())
    p_letters = 0
    for i in range(len(str)):
      if str[i] == str[len(str) - (i+1)]:
        p_letters+=1
    if p_letters == len(str):
      return True


def purge(str):
  stringList = []
  for i in str: 
    if isLetter(i):
      stringList.append(i)
  purged_string = ''.join(stringList)
  return purged_string

def isLetter(x): 
  if (ord(x)) in range(96, 122) or (ord(x)) in range(64, 91):
    return True
  else:
    return False



while True: 
  user_string = input("Enter String: ")
  print(f"Palidrome: {isPal(user_string)}")
  print(f"Almost Palidrome: {isAlmostPal(user_string)}")
  while True:
    try:
      repeat = int(input("Do you wish to repeat this function? if so enter 1 if not, enter 0.\n: "))
      if repeat !=1 and repeat !=0:
        print("please enter an integer 0-1.")
      else:
        break
    except ValueError:
      print("please enter an integer 0-1.")
  if repeat == 0:
    break 
  elif repeat == 1:
    continue