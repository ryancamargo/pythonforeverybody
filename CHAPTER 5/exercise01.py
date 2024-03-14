#Exercise 1: Write a program which repeatedly reads integers until the user enters
#“done”. Once “done” is entered, print out the total, count, and average of the
#integers. If the user enters anything other than a integers, detect their mistake
#using try and except and print an error message and skip to the next integers.
#Enter a number: 4
#Enter a number: 5
#Enter a number: bad data
#Invalid input
#Enter a number: 7
#Enter a number: done
#16 3 5.333333333333333


# Repeatedly reads integer until type 'done' and then print total, count, average of the integers
count = 0
total = 0.0
while True:
    inp = input("Enter a number: ")
    if inp == 'done':
        break
    try:
        finp = float(inp)
        #print(finp)
        count += 1
        total = total + finp
    except:
        print("Invalid input")
    
print(total, count, total/count)
