#Here i learn what list comprehension is 
#A list comprehension combines the for loop and the 
# creation of new elements into one line, and automatically
#appends each new element.#

#This code does the same thing the code from the square_number file
#file does but uses a list comprehension.

squares = [value ** 2 for value in range(1,11)]
print(squares)