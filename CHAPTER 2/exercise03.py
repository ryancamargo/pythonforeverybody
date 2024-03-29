#Exercise 3: Write a program to prompt the user for hours and rate per hour to
#compute gross pay.
#Enter Hours: 35
#Enter Rate: 2.75
#Pay: 96.25
#We won’t worry about making sure our pay has exactly two digits after the decimal
#place for now. If you want, you can play with the built-in Python round function
#to properly round the resulting pay to two decimal places.


# Prompt for worked hours and rate/hour to compute gross pay
def computepay(hours, rate):
    if hours > 40:
        return (1.5 * rate) * hours # 1.5x hourly rate when working more than 40 hours
    else:
        return rate * hours


hour = input("Enter Hours: ")
try:
    _hour = int(hour)
except:
    print("Error, please enter numeric input")
    quit()

rate = input("Enter Rate: ")
try:
    _rate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

print("Pay:", computepay(_hour, _rate))
