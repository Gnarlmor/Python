#Introductino so tuples. Python refers to values that cannot change as
#immutable, and an immutable list is called a tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#Looping works the same way for tuples
for dimension in dimensions:
    print(dimension)

#You cant modify a toople but you can assign a new value to a 
# variable that represetns a tuple.

print("Original dimensions")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions")
for dimension in dimensions:
    print(dimension)

#Use tuples for storing values that should not be changed 
#throughout the life of a program.