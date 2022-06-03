def invest(amount, rate, years):
 for year in range(1, years + 1):
  amount = amount + (amount * rate)
  print(f"year {year}: ${amount:,.2f}")
  

amount = float(input("Enter a principal amount: "))
rate = float(input("Enter an anual rate of return: "))
years = int(input("Enter a number of years: "))
invest(amount, rate, years)