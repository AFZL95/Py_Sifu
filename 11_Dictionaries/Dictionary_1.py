# creating some sweet fruit dictionary
fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# printing all elements of a dictionary
# print(fruit)

# printing the items of the dictionary
# print(fruit.items())

# print one specific element
print(fruit["lemon"])

# add some new fruit to the gruop
fruit["pear"] = "an odd shaped apple"
# print(fruit)

# editing the value of an existing element
fruit["lime"] = "great with tequila"
print(fruit)

# remove some shit from the collection using del() command
# del fruit["lemon"]

# deleting the entire entities of the dictionary
# fruit.clear()
# print(fruit)

# requesting something that doesn't belong to the called dictionary obviously cause an error'
# print(fruit["tomato"])
# print(fruit)

# the values of a dictionary could be anything,
# strings , numbers , or even another dictionary
bike = {"make": "Honda", "model": "250 dream", "colour": "red", "engine_size": 250}
print(bike["engine_size"])
print(bike["colour"])

# sweet example of retrieving dictionary entities using their key
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        #retrieving the description using its key
        description = fruit.get(dict_key)
        print(description)
    else:
        print("we don't have a " + dict_key)