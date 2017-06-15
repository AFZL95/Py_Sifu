# tuples are is a term for an ordered set of data.
# in Python, tuples are similar to lists.
# But the difference here is that they're immutable.
# And what that means is they can't be changed.
# So, in other words,attempting to append an item to a tuple
# will actually give you an error.

Seperation = "A seperation ", "Asghar Farhadi", 2011
bedooneTarikh = "No Date, No Sign" "Vahid Jalilvand", 1974
Asheghaneh = "Aasheghaneh", "hooman seyedi", 2017

print(bedooneTarikh)
# Assignment of Tuple elements to separate variables
title, director, year = Seperation
print(title)
print(director)
print(year)


# the expressions on the right hand side of an assignment
# are always evaluated before the left hand side
# to prove that ...
a = b = c = d = 12
print(c)
a, b = 12, 13
print(a, b)

a, b = b, a
print("a is {}".format(a))
print("b is {}".format(b))
