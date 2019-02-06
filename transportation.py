transportations = ['car', 'train', 'boat']
print(transportations)

# Command .pop() is used for delet element in the list, 
# and can add the position(number) in the function.

popped_transportations = transportations.pop(1)
print(transportations)
print('Today I am going to take a ' + popped_transportations.upper() + '.')

# When want to delet an element permanently, use 'del'
# When want to delet an element and use it afterwards, use '.pop()'

# When want to delet a elememt and only know the value, 
# use command 'remove()'

expensive = 'boat'
transportations.remove(expensive)
print(transportations)
print('A ' + expensive + ' is too expensive.')