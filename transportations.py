# Using X=[] to make a list

transportations = ['car', 'bicycle', 'airplane', 'train', 'bus']

print('I like driving ' + transportations[0] + 's.')
print('I enjoy riding on ' + transportations[1] + '.')
print('I would like to take a ' + transportations[2] + ' to travel.')
print("I don't care to take a " + transportations[3] + '.')
print('For me, taking ' + transportations[4] + ' is quite boring.')

# When want to request a value from a specific position, insert number in the [] 

print(transportations)
transportations[0] = 'taxi'
print(transportations)

transportations.append('motocycle')
print(transportations)

transportations.insert(0, 'cruise')
print(transportations)

# When want to delet a value from a specific position, 
# use 'del' and insert number in the []

del transportations[0]
print(transportations)