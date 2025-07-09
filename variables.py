# Variables = a container for a value (int, string, float and booleans)

#string
first_name = "Vladislav"
food = "fish"
email = "qwer123@mail.com"

print(first_name)
print("first_name")
print(f"Hi, {first_name}!")
print(f"You like {food}?")
print(f"Your email is: {email}")


#integer
#age = "26" - string
age = 26
quantity = 0

print(f"You are {age} years old")
print(f"You are buying {quantity} items")

#float

price = 1.99
gpa = 46.7
distance = 30.4

print(f"Your gpa is: {gpa}")
print(f"The price is ${price}")
print(f"You run {distance} m")  


#boolean

is_programmer = False
for_sale = True
is_online = True

print(f"You are a programmer?: {is_programmer}")
if is_programmer:
    print("You are a programmer")
else:
    print("You are not a programmer")    

if for_sale:
    print("That items is for sale")
else:
    print("That items is not available") 

if is_online:
    print("You are online")
else:
    print("You are offline")
