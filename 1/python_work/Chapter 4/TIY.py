# Use a for loop to print the numbers from 1 to 20 inclusive.
for number in range(1,21):
    print(number)

#Make a list of the numbers from one to one million, and then
#use a for loop to print the numbers

million = list(range(1,10001))
print(million)

#Use min() and max() to check if the list starts at 1 and ends at 10000
#Use sum to see how quick python adds 10000 num.
print(min(million))
print(max(million))
print(sum(million))

#Use the third argument of the range() function to make a list of the 
#odd numbers from 1 to 20. Use a for loop to print each number

odd = list(range(0,21,3))
for num in odd:
    print(num)

#Make a list of the multiples of 3, from 3 to 30. Use a for loop to
#print the numbers in your list.

multiples = [value * 3 for value in range(1,11)]
print(multiples)

#Make a list of the first 10 cubes nd use a for loop to print out
#the value of each cube.

cube = [value **3 for value in range (1,11)]
print(cube)