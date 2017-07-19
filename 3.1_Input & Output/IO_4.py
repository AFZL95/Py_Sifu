# pickle is the serialization option for creating a efficient bytestream from objects
# so they (python objects) can restored from the ".pickle" file later
import pickle

imelda = ('More Mayhem',
          'IMelda May',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))

# writing area
with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)

# reading the "imelda.pickle" file and restore the object
with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)

print(imelda2)

album, artist, year, track_list = imelda2

print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

# so it all been stored and nicely retrieved
print('=' * 40)


# when we create a pickle file, we can append many data type in it
even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("imelda.pickle", "wb") as pickle_file:
    # in this case we append three different objects in one "imelda.pickle" file
    pickle.dump(even, pickle_file, protocol=0)
    pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(2998302, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
# and loading it back to our workspace...
with open("imelda.pickle", "rb") as imelda_pickled:
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)

for i in even_list:
    print(i)

print('=' * 40)

for i in odd_list:
    print(i)

print('=' * 40)

print(x)

print('=' * 40)












