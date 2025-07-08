# Dictionary 
alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_1['x_position']}")
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
elif alien_1['speed'] == 'fast':
    x_increment = 3
alien_1['x_position'] = alien_1['x_position'] + x_increment
print(f"New position: {alien_1['x_position']}")
print(alien_1)

#del value
del alien_1['y_position']
print(alien_1)

#Empty dictionary
alien2 = {}

alien2['color'] = 'yellow'
alien2['points'] = 21
print(alien2)


# same type object 

favorite_languages = {
    'Jack': 'C',
    'Alex': 'Python',
    'Mike': 'Ruby',
}

print(favorite_languages)

languages = favorite_languages['Mike'].title()
print(f"Mike is favorite languages is {languages}.")


#Method get()
bandit = {'color': 'green', 'x_position': 0}

bandit_points = bandit.get('points', 'No value')


print(bandit_points)






#Dictionary is collection {'key': 'value'} pairs
#                         ordered changeable , no dublicate

capitals = {"USA": "Washington",
     "France": "Paris",
     "Russia": "Moscow",
     "China": "Beijine"}                   

print(capitals)
print(dir(capitals))

print(capitals.get("USA"))
if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesent exists")

capitals.update({"Germany": "Berline"})
capitals.update({"Russia": "St.Peterburg"})
capitals.pop("China")
capitals.popitem()
capitals.clear()
key = capitals.keys()
for key in capitals.keys():
    print(key)

value = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
print(items)

for items in capitals.items():
    print(items)
for key, value in capitals.items():
    print(f"{key} - {value}")
