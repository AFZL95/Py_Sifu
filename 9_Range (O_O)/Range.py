# create a zero to nine list and print it out
my_list = list(range(10))
print(my_list)

# print out the odd and even numbers between 0 and 1000
even = list(range(0, 1000, 2))
odd = list(range(1, 1000, 2))
print(even)
print(odd)

# function of lists in simple string processing
my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string.index('e'))
print(my_string[4])

# example of indexing stuff
small_decimals = range(0, 10)
print(small_decimals)
print(small_decimals.index(3))

# print value of the 985th odd number
odd = range(1, 10000, 2)
# print(odd)
print(odd[985])

# create an complete application! to guess inputted number is divisible by seven
sevens = range(7, 1000000, 7)
x = int(input("Please enter a positive number less than one million: "))
if x in sevens:
    print("{} is divisible by seven".format(x))
else:
    print("{} is not divisible by seven".format(x))

# example to show how [n:q:m] indexer work
decimals = range(0, 100)
print(decimals)
my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)
# make some seperator with an intelligent way
print('=' * 40)

for i in range(3, 40, 3):
    print(i)

print(my_range == range(3, 40, 3))