
#Caesar Cipher 

def show_menu():
  while True:
    try:
      menu_response = int(input(""" Please input the following number for what you would like to do.
    1) encrypt 
    2) decrypt 
    3) quit
    : """))
      if menu_response != 1 and menu_response != 2 and menu_response !=3:
        print("Please enter a number 1-3")
      else: 
        break
    except ValueError:
      print("Please enter a number 1-3.")
  return menu_response

def decrypt():
  message = get_message()
  key = get_key()
  decrypted_list = []
  for char in message:
    if char.islower():
      decrypted_list.append(chr((ord(char) - 97 - key) % 26 + 97))
    elif char.isupper():
      decrypted_list.append(chr((ord(char) - 65 - key) % 26 + 65))
    else:
      decrypted_list.append(char)
    decrypted_message = ''.join(decrypted_list)
  print(decrypted_message)

def encrypt():
  message = get_message()
  key = get_key()
  encrypted_list = []
  for char in message:
    if char.islower():
      encrypted_list.append(chr((ord(char) - 97 + key) % 26 + 97))
    elif char.isupper():
      encrypted_list.append(chr((ord(char) - 65 + key) % 26 + 65))
    else:
      encrypted_list.append(char)
    encrypted_message = ''.join(encrypted_list)
  print(encrypted_message)

def get_key():
  while True:
    try: 
      user_key = int(input("Enter a key: "))
      break
    except ValueError:
      print("Please enter a number for the key")
  return user_key

def get_message():
  user_input = input("Enter a message: ")
  return [char for char in user_input]

while True: 
  userMenu_response = show_menu()
  if userMenu_response == 1: 
    encrypt()
  elif userMenu_response == 2: 
    decrypt()
  elif userMenu_response == 3: 
    break