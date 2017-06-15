# How to show the Iterator?
string = '123456789'
my_Iter = iter(string)
# print the first element of the Iterator
print("this is my name :"+ str(my_Iter))

# print the second element of the Iterator
print(next(my_Iter))
# print the third element of the Iterator
print(next(my_Iter))
# ...