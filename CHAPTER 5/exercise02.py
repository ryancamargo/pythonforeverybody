#Exercise 2: Write another program that prompts for a list of numbers as above
#and at the end prints out both the maximum and minimum of the numbers instead
#of the average.

# Almost the same as before but printing both the maximum and minimum of the numbers
count = 0
total = 0.0
finp = []
while True:
    inp = input("Enter a number: ")
    if inp == 'done':
        break
    try:
        finp.append(float(inp))
        count += 1
        total = total + float(inp)
    except:
        print("Invalid input")
    
print(total, count, max(finp), min(finp))
