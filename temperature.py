def convert_cel_to_far(cel):
 far = cel * (9 / 5) + 32
 return far
def convert_far_to_cel(far):
 cel = (far - 32) * 5 / 9
 return cel 
far = float(input("Enter a temperature in farenheit: "))
cel = convert_far_to_cel(far)
print(f"{far} degrees F = {cel:.2f} degrees C \n")

cel = float(input("Enter a temperature in Celsius: "))
far = convert_cel_to_far(cel)
print(f"{cel} degrees C = {far:.2f} degrees F")

