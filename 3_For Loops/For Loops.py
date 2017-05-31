#Simple For Loop
for i in range(1,20):
    print("i is now {}".format(i))

#we got some numbers and some symbols
#and we want to print just the numbers

#First Approach
number = "9,223,372,036,854,775***,807"
for i in range(0, len(number)):
    if(number[i] in '0123456789'):
        print(number[i])

#Second Approach
number = "9,223,372,036,854,775,807"
cleanedNumber = ''
for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)

print("The number is {} ".format(newNumber))