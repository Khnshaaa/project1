#Read in a Fahrenheit temperature. Calculate
# and display the equivalent centigrade temperature.
# The following formula is used for the conversion:
# C = (5 / 9) * (F – 32)

def fahrenheit_to_celsius():
    fahrenheit = float(input())  
    celsius = (5 / 9) * (fahrenheit - 32) 
    print(f"TEMPERATURE IN A CELSIUS: {celsius:.2f}") 
    
fahrenheit_to_celsius()
