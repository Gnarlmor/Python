#Here is shown how we cand copy a list or a section of a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food.title())

print("\nMy friends favority foods are:")
for food in friend_foods:
    print(food.title())

