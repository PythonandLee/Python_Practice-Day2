name = ['davinci', 'turing', 'feynmanm']
print('Welcome ' + name[0].title() + ' to my dinner.')
print('Welcome ' + name[1].title() + ' to my dinner.')
print('Welcome ' + name[2].title() + ' to my dinner.')
print('Now there are ' + str(len(name)) + ' guest(s) is/are coming.')

cant_come = 'turing'
name.remove(cant_come)
new_guest = 'tesla'
name.append(new_guest)
print('Sorry, ' + cant_come.title() + ' cannot make it.')
print('But we have another friend, ' + new_guest.title() +', is coming.\n') 

print('Once again, welcome ' + name[0].title() + ' .')
print('Once again, welcome ' + name[1].title() + ' .')
print('Once again, welcome ' + name[2].title() + ' .')
print('Now there are ' + str(len(name)) + ' guest(s) is/are coming.')

print('\nBecause I just found a larger place, so I am going to invite more friends.')

new_friend1 = 'teresa'
name.insert(0, new_friend1)
new_friend2 = 'lincoln'
name.insert(2, new_friend2)
new_friend3 = 'sherlock'
name.append(new_friend3)

print('Welcome new firend ' + new_friend1.title() + '.')
print('Welcome new firend ' + new_friend2.title() + '.')
print('Welcome new firend ' + new_friend3.title() + '.')
print('Now there are ' + str(len(name)) + ' guest(s) is/are coming.')

print('\nSorry for my mistake, the place I just found\nis not big enough for all people, so I have to\nreduce to two guest. My apology.\n')

cancle_1 = name.pop()
print('Sorry ' + cancle_1.title() + ', hope see you next time.')
cancle_2 = name.pop()
print('Sorry ' + cancle_2.title() + ', hope see you next time.')
cancle_3 = name.pop()
print('Sorry ' + cancle_3.title() + ', hope see you next time.')
cancle_4 = name.pop()
print('Sorry ' + cancle_4.title() + ', hope see you next time.')

print('\n')
print('Welcome ' + name[0].title() + ' to my dinner.')
print('Welcome ' + name[1].title() + ' to my dinner.')
print('Now there are ' + str(len(name)) + ' guest(s) is/are coming.')

del name[0:]
print(name)