#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
#hourly rate for hours worked above 40 hours.
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

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
