#Mia Escoto 

#Loop While 
def time_toSeconds():
 hours = int(input("hours: "))
 mins = int(input("minutes: "))
 secs = int(input("seconds: "))
 total_seconds = (mins * 60) + ((hours * 60) * 60) + secs
 print (f"{hours} hours, {mins} minutes, and {secs} seconds is equal to {total_seconds}")

def time_split():
 total_seconds = int(input("total seconds: "))
 hours = (total_seconds // 3600)
 seconds = total_seconds % 3600
 mins = (seconds // 60) 
 seconds %= 60
 print(f"{total_seconds} seconds is equal to {hours} hours {mins} minutes, and {seconds} seconds.")

def coins_toValue():
 quarters = int(input("quarters: "))
 dimes = int(input("dimes: "))
 nickels = int(input("nickels: "))
 pennies = int(input("pennies: "))
 total_value = round((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01), 2)
 print(f"{quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies equals ${total_value}")

def coins_split():
 total_price = float(input("total price : $"))
 quarters = int(total_price / 0.25)
 rem_price = round(total_price % 0.25, 2)
 dimes = int(rem_price / 0.10)
 rem_price %= 0.10
 nickels = int(rem_price / 0.05)
 rem_price %= 0.05
 pennies = int(rem_price)
 print(f"${total_price} is equal to, {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies")

while True:
 try:
  user_choice = int(input("""
  1. combining hours, minutes, and seconds into seconds.
  2. converting seconds into hours, minutes, and seconds.
  3. combining quarters, dimes, nickels, and pennies.
  4. converting a total price into quarters, dimes, nickels and pennies.
  Please input the number of the program you would like to run: """))
 except ValueError:
  print("Please enter a number 1-4")
 if user_choice == 1:
  time_toSeconds()
 if user_choice == 2:
  time_split()
 if user_choice == 3: 
  coins_toValue()
 if user_choice == 4:
  coins_split()
 try: 
  user_choice = int(input("Press any number to continue, press 0 if you would like to stop."))
 except ValueError:
  print("Please enter a number")
 if user_choice == 0:
  break