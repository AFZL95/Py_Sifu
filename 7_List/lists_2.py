#first scenario
list_1 = []
list_2 = list()

print("List 1: {}".format(list_1))
print("List 2: {}".format(list_2))

if list_1 == list_2:
    print("The lists are equal")

# second scenario
# create a list and put every character of the string below in it
print(list("The lists are equal"))

# third scenario
# appending two lists in a list and iterate them 
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]

for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)
