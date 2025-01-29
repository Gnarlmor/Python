#Guest list: Sent at least 3 people invitations for dinner

guests = ['Marcus Aurelius', 'Socrates', 'Seneca']

message_1 = f"\nDistingueshed {guests[0]}, would you care to join me for dinner tonight?"
print(message_1)

message_2 = f"\nDistingueshed {guests[1]}, would you care to join me for dinner tonight?"
print(message_2)

message_3 = f"\nDistingueshed {guests[2]}, would you care to join me for dinner tonight?\n"
print(message_3)

#Changing guest list: Specify wich guest can't come and replace him
print(f"{guests[1]} can't come to dinner.")

guests = ['Marcus Aurelius', 'Aristotel', 'Seneca']

message_1 = f"\nDistingueshed {guests[0]}, would you care to join me for dinner tonight?"
print(message_1)

message_2 = f"\nDistingueshed {guests[1]}, would you care to join me for dinner tonight?"
print(message_2)

message_3 = f"\nDistingueshed {guests[2]}, would you care to join me for dinner tonight?\n"
print(message_3)

#More guests. Using the insert method add 3 more guests to the table
guests.insert(0,'Plato')
guests.insert(3,'Karl Marx')
guests.insert(5,'Epicurus')

message_1 = f"\nDistingueshed {guests[0]}, would you care to join me for dinner tonight?"
print(message_1)

message_2 = f"\nDistingueshed {guests[1]}, would you care to join me for dinner tonight?"
print(message_2)

message_3 = f"\nDistingueshed {guests[2]}, would you care to join me for dinner tonight?"
print(message_3)

message_4 = f"\nDistingueshed {guests[3]}, would you care to join me for dinner tonight?"
print(message_4)

message_5 = f"\nDistingueshed {guests[4]}, would you care to join me for dinner tonight?"
print(message_5)

message_6 = f"\nDistingueshed {guests[5]}, would you care to join me for dinner tonight?\n"
print(message_6)

print("I'm verry sorry but for some unforseen circumstances now i can only invite 2 people to dinner.")

removed_1= guests.pop(5)
print(f"I'm verry sorry {removed_1}, unfortunately I can't invite you to dinner")
removed_2= guests.pop(4)
print(f"I'm verry sorry {removed_2}, unfortunately I can't invite you to dinner")
removed_3= guests.pop(3)
print(f"I'm verry sorry {removed_3}, unfortunately I can't invite you to dinner")
removed_4= guests.pop(2)
print(f"I'm verry sorry {removed_4}, unfortunately I can't invite you to dinner")

message_1 = f"\nDistingueshed {guests[0]}, would you care to join me for dinner tonight?"
print(message_1)

message_2 = f"\nDistingueshed {guests[1]}, would you care to join me for dinner tonight?"
print(message_2)

del guests[1]
del guests[0]

print(guests)

num_guests = len(guests)
print(num_guests)