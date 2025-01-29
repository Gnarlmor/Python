#Here I learned how to declare and display a list
bicycles = ['trek','cannondale', 'redline', 'specialized']
print(bicycles)

#Accesing a specific element from a list
#The string methods like "title" can be also used for lists
print(bicycles[0].title())

#Accesing different elements of the list
print(bicycles[1])
print(bicycles[3])

#Python always returns the last item in the list if you ask for the 
#item with the index of -1
#The -2 returns the second last and so forth
print(bicycles[-1].title())

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)