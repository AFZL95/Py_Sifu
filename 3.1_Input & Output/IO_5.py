'''
so moving on although the pickle module which we just talked about
great for serializing python objects and it really does have a drawback that the
objects all have to be loaded back into memory into the computer's memory that's
fine for many situations but if you're dealing with a really large set of
objects for example a single object very large single object like a large
dictionary for example then loading that in entire thing to memory may not be a
realistic option so you need to look at alternatives now Python's got your
back to their and they have an alternative it and that's to use the shelve module so
the shelve provides a shelve and you can think of it like a dictionary
but its actually stored in a file rather than in memory. now like
a dictionary the shelve holds key value pairs and the values can be anything.
'''


import shelve

# with shelve.open('ShelfTest') as fruit:
fruit = shelve.open('ShelfTest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"

print(fruit["lemon"])
print(fruit["grape"])
fruit.close()

print(fruit)