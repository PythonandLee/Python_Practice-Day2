# Make a list and print.
places = ['india', 'holland', 'peru', 'mexico', 'new zeland']
print(places)

# Use 'sorted()' to sort the list temporary, and the list remains originally.
# Use 'reverse=True' to invert the list.
print(sorted(places))
print(sorted(places, reverse=True))

# Use 'reverse()' to invert the list permanently.
places.reverse()
print(places)

places.reverse()
print(places)

# Use 'sort()' to sort the list permanently.
places.sort()
print(places)
places.sort(reverse=True)
print(places)