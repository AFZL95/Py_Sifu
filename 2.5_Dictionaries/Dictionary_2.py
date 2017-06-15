fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# sort the keys of the dictionary (It Is Important Guys!)
ordered_keys = list(fruit.keys())
ordered_keys.sort()
# another manner to do this
# ordered_keys = sorted(list(fruit.keys()))
for f in ordered_keys:
    print(f + " - " + fruit[f])


# so much nicer approach to do the sorting thing
# for f in sorted(fruit.keys()):
#     print(f  + " - " + fruit[f])
