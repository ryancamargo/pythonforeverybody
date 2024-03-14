#Exercise 5: Write a program which prompts the user for a Celsius temperature,
#convert the temperature to Fahrenheit, and print out the converted temperature.

# Celsius to Farenheit converter
celsius = input("Celsius: ")
try:
    farenheit = (9/5 * int(celsius)) + 32
    print("Farenheit: ", farenheit)
except:
    print("Please enter a number")
