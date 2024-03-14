#Exercise 2: Write a program to prompt for a file name, and then read through
#the file and look for lines of the form:
#X-DSPAM-Confidence: 0.8475
#When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart
#the line to extract the floating-point number on the line. Count these lines and
#then compute the total of the spam confidence values from these lines. When you
#reach the end of the file, print out the average spam confidence.
#Enter the file name: mbox.txt
#Average spam confidence: 0.894128046745
#Enter the file name: mbox-short.txt
#Average spam confidence: 0.750718518519
#Test your file on the mbox.txt and mbox-short.txt files.

# Look for lines that start with x-DSPAM ... get the all the numbers, print the average
name = input('Enter a file name: ')
try:
    fhand = open(name)
except:
    if name == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk'd!')
    print('File can not be opened: ', name)
    quit()

list = []
str = 'X-DSPAM-Confidence:'
for line in fhand:
    if line.startswith(str):
        space = line.find(' ')
        number = float(line[space + 1:])
        list.append(number)

print('Average spam confidence: ', (sum(list) / len(list)))
