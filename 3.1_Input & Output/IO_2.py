cities = ["Tehran", "Tabriz", "Darwin", "Melbourne", "Sydney"]
# we create a file named "cities.txt" and write the cities list on it
with open("cities.txt", 'w') as city_file:
    for city in cities:
        # we need no clear spacing assignment for "file=city_file"
        # because it is not an ordinary variable assignment like "a = 5"
        print(city, file=city_file)


# so it's time to re-read our written file
cities = []
with open("cities.txt", 'r') as city_file:
    for city in city_file:
        # using "strip(\n)" function to eliminate spaces in our text
        # what "strip()" does is it removes characters from the beginning
        # or end of a string and only from the beginning or end
        cities.append(city.strip('\n'))

print(cities)
for city in cities:
    print(city)


# imelda = "More Mayhem", "Imelda MAy", "2011", (
#     (1, "Pulling the Rug"), (2,"Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# with open("imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)
#
# with open("imelda3.txt", 'r') as imelda_file:
#     contents = imelda_file.readline()
#
# imelda = eval(contents)
#
# print(imelda)
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
