
#  Open a text file and search for a specific keyword like "jabberwock" and print the relevant sentence of it !
jabber = open("sample.txt",'r')
for line in jabber:
    # "line.lower" means whatever "jabberwock" is written it converts it to the lower case
    if "jabberwock" in line.lower():
        print(line, end='')
# in "open" method in python we have to close the file for tidy up things
jabber.close()


# there is another way to open a file without worrying about closing the stream
# the "with open" method handles this issue automatically
with open("sample.txt", 'r') as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')
# "with open" method has many other advantages like closing the file whenever an error occurs in reading file
# in other words it got exceptions and error handling option but "open" method is a rudimentary implementation


# diffrence between "readline()" and "readlines()" method

# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# with open("sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')
#


# it shows the complete difference between "readlines()" and "read()" method
# first one reverses the line but second one is reversing the whole characters 
with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')

print("=+"*30)

with open("sample.txt", 'r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end='')
