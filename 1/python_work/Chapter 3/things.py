#Create a list of things i like and use every function
# learned in this chapter at least onece.#
things = ['Bouvile', 'Moldova', 'Dog', 'Hungary', 'Cehia', 'Madrid']

things.sort()
things.insert(3, 'Mama')
things[5] = 'Mountains'
things.append('Baile Herculane')
del things[4]
removed = things.pop()
print(removed)
things.remove('Bouvile')
things.reverse()
print(sorted(things))
things.reverse()
length = len(things)
print(length)
