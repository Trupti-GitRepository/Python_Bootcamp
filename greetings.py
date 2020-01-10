names = [ 'swati', 'rohini', 'sukhada', 'vijaya', 'chanda']
print(names)
'''
# print a message for each person by accessing each element.
print("Hi! " + names[0].title() + ", How are you? ")
print("Hi! " + names[1].title() + ", How are you? ")
print("Hi! " + names[2].title() + ", How are you? ")
print("Hi! " + names[3].title() + ", How are you? ")
print("Hi! " + names[4].title() + ", How are you? ")
'''

# print message using "for loop." Note : use singular name.title().
for name in names:
    print("Hi! " + name.title() + ", Happy New Year. ")
