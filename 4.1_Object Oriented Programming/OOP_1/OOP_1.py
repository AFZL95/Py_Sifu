class Book(object):

    def __init__(self, author, price):
        self.author = author
        self.price = price
        self.read = False

    def Readed(self):
        self.read =True


Golestan = Book("Golestan E Saadi", 15.99)
print(Golestan.author)
print(str(Golestan.price) + " tomans")

Golestan.price = 12.75
print(str(Golestan.price) + " tomans")

Boostan = Book("Boostan E Saadi", 14.55)

print(Boostan.read)
print("Books : {} = {}, {} = {}".format(Golestan.author, Golestan.price, Boostan.author, Boostan.price))
print("Books : {0.author} = {0.price},{1.author} = {1.author}".format(Golestan,Boostan))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""

print(Golestan.read)
Golestan.Readed()
print(Golestan.read)