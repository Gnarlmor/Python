#Here is shown the concept of slicing a list

players = ['charles', 'martin', 'michael', 'florence', 'eli']
print(players[0:3])

#Looping through a slice
print("Here are the three players on my team:")
for player in players[:3]:
    print(player.title())