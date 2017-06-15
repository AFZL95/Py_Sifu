# a set in Python is an unordered data structure and doesn't contain duplicates
# it look like Bag Data Structure
# unlike a dictionary, items aren't accessed via a key
# In fact, a set is probably more similar to a collection of dictionary keys.
# so every time that a code with Set DS runs , the orders are changed.


# old fashion way to store stuff in Set Data Structure
farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

# make a seperator
print("=" * 40)


# store data in Set Data Structure in another manner
wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

# adding new items to the set
wild_animals.add("horse")
print(wild_animals)

# empty_set = set()
# empty_set_2 = {}
# empty_set.add("a")
# # empty_set_2.add("a")
#
# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print(squares.union(even))
#
# print("-" * 40)
#
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)

even = set(range(0, 40, 2))
print(sorted(even))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares))

print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even")
print(squares.difference(even))
print(squares - even)


























