#Here i learn how to modify elemnts in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#Changing a element of a list
motorcycles[0] = 'ducati'
print(motorcycles)

#Adding elements to a list using the append() method
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

#Inserting elements in a list at any given possition
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0,'ducati')
print(motorcycles)

#Removing Elements from a List
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

#Removing an item using the pop() Method
#It's useful if we want to still work with the item we want to remove
#from the list and for example move to another one
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

#Poping items from any position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop()
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#Removing an item by value
#The remove method tels python to figure out itself where the 
# specific is and remove it.#
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#Remove ca be also used to work with a value that's bieng removed
# from a list.#
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")