#Exercise 5: Slicing strings
#Take the following Python code that stores a string:
#str = 'X-DSPAM-Confidence: 0.8475'
#Use find and string slicing to extract the portion of the string after the colon
#character and then use the float function to convert the extracted string into a
#floating point number.


# Using find()
str = 'X-DSPAM-Confidence: 0.8475'

pos = str.find(' ')

number = str[pos + 1:]
fnumber = float(number)

print(fnumber)
