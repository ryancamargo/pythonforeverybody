#Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the
#program. The following shows two executions of the program:
#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input
#Enter Hours: forty
#Error, please enter numeric input

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
