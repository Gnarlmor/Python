#Learning how to use the sort method in Python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#Using the reverse sorting option
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#Sorting a list temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list")
print(cars)

print("\nHere is the sorted list")
print(sorted(cars))

print("\nHere is the original list again\n")
print(cars)

#Printing a list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

