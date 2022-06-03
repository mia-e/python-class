#Mia Escoto 
from random import choice 

capital_dic={ 
'Alabama': 'Montgomery', 
'Alaska': 'Juneau', 
'Arizona':'Phoenix', 
'Arkansas':'Little Rock', 
'California': 'Sacramento', 
'Colorado':'Denver', 
'Connecticut':'Hartford',
'Delaware':'Dover', 
'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 
'Hawaii': 'Honolulu', 
'Idaho': 'Boise',
'Illinios': 'Springfield',
'Indiana': 'Indianapolis', 
'Iowa': 'Des Monies',
'Kansas': 'Topeka', 
'Kentucky': 'Frankfort', 
'Louisiana': 'Baton Rouge', 
'Maine': 'Augusta', 
'Maryland': 'Annapolis',
'Massachusetts': 'Boston', 
'Michigan': 'Lansing', 
'Minnesota': 'St. Paul', 
'Mississippi': 'Jackson', 
'Missouri': 'Jefferson City', 
'Montana': 'Helena',
'Nebraska': 'Lincoln', 
'Neveda': 'Carson City', 
'New Hampshire': 'Concord',
'New Jersey': 'Trenton', 
'New Mexico': 'Santa Fe', 
'New York': 'Albany', 
'North Carolina': 'Raleigh', 
'North Dakota': 'Bismarck', 
'Ohio': 'Columbus',
'Oklahoma': 'Oklahoma City', 
'Oregon': 'Salem', 
'Pennsylvania': 'Harrisburg', 
'Rhoda Island': 'Providence',
'South Carolina': 'Columbia', 
'South Dakoda': 'Pierre', 
'Tennessee': 'Nashville', 
'Texas': 'Austin', 
'Utah' : 'Salt Lake City', 
'Vermont': 'Montpelier',
'Virginia': 'Richmond', 
'Washington': 'Olympia', 
'West Virginia': 'Charleston', 
'Wisconsin': 'Madison', 
'Wyoming': 'Cheyenne'
}

States=list(capital_dic.keys())

while True:
  state = choice(States)
  capital = capital_dic[state]
  while True: 
    guess = input(f"Please guess the capital of {state}, If you give up enter exit\ncapital: ")
    if guess.lower() == capital.lower():
      print("Correct!")
      break
    elif guess.lower() == 'exit':
      print(f"The correct answer is {capital}")
      break
    else: 
      print("incorrect")
  while True:
    try: 
      replay = int(input("Press 1 to continue, press 0 to quit: "))
      if replay == 1 or replay == 0:
        break
    except ValueError: 
      print("Please enter a number")
  if replay == 0: 
    print("Goodbye")
    break
  else:
    print("New Round")