#Create a list with pizzas i like and print wach with a loop
#Modify the loop statement to print a message with every element of the list
#Add a line outside of the loop program with how much you love pizza
pizzas = ['Diavola', 'QuatroFormagi', 'QatroCarne', 'Margerita']

for pizza in pizzas:
    print(f"I like {pizza.title()} pizza!")

print("I like pizza very much")

#Make a copy of the list of pizzas, and call it friend_pizzas.
friend_pizzas = pizzas[:]

#Add new pizza to the original list
pizzas.append('Taraneasca')

#Add a different pizza to the friends list
friend_pizzas.append('Capriciosa')

#Print each list through a for loop
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friends favorite pizzas are")
for pizza in friend_pizzas:
    print(pizza.title())