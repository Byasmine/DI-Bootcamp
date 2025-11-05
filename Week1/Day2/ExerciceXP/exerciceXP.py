#Exercice 1:
print("Exercice 1 :")
my_fav_numbers = {5, 7, 3, 15, 9} #creating a set

my_fav_numbers.update([13, 21]) #for adding multiple numbers else use add()
print("Adding two numbers : ", my_fav_numbers)

my_fav_numbers.remove(15) #removing the last number
print("Removing last number : ", my_fav_numbers)

friend_fav_numbers = {4, 8, 12} #another set
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers) #combining both sets
print("Concatinate new set : ", our_fav_numbers)

#Exercice 2:
print("Exercice 2 :")
tuple = (1, 2, 3, 4, 5) # the thing is tuples are immutable
tuple += (6,7,8,)  #adding elements to tuple by concatenation (this is the only way)
print("New tuple : ", tuple)
"""
tuples don't support .append() or extend() methods so we cannot modify a tuple directly
"""
#Exercice 3:
print("Exercice 3 :")
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print("Initial basket : ", basket)
basket.remove("Banana") #removing Banana
print("Removing Banana : ", basket)
basket.remove("Blueberries") #removing Blueberries
print("Removing Blueberries : ", basket)
basket.append("Kiwi") #adding Kiwi at the end
print("Adding Kiwi : ", basket)
basket.insert(0, "Apples") #we use insert to add at a specific index
print("Adding another Apple at the beginning : ", basket) 
count_apples = basket.count("Apples") #counting number of Apples
print("Number of Apples in the basket : ", count_apples)
basket.clear() #emptying the basket
print("Emptying the basket : ", basket)

#Exercice 4:
print("Exercice 4 :")
"""
Float is a data type that represents decimal numbers,
and the difference between flaot and integer is that integers are whole numbers without decimal points.
"""
mixed_list = list()
number = 1.5
while number <= 5:
    mixed_list.append(number)
    number += 0.5

clean_list = [int(num) if num.is_integer() else num for num in mixed_list] #converting float to int if it's whole number
print("List of floats from 1.5 to 5 : ", clean_list)

#or using range
mixed_list2 = []
for i in range(3, 11): #3 to 10
    mixed_list2.append(i / 2) #dividing by 2 to get float values

clean_list2 = [int(num2) if num2.is_integer() else num2 for num2 in mixed_list2] #converting float to int if it's whole number
print("List of floats from 1.5 to 5 : ", clean_list2)

#Exercice 5:
print("Exercice 5 :")
print("Printing numbers from 1 to 20 :")
for i in range(1, 21):
    print(i)#printing numbers from 1 to 20

print("Printing even numbers from 1 to 20 :")
#printing whether the number is even or odd
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

#Exercice 6:
print("Exercice 6 :")
user_name= input("Enter your name: ")
while True:
    if len(user_name)>=3 and not user_name.isdigit() : # we can also use isalpha
        print(f"Thank you, {user_name}!")
        break
    else:
        user_name= input("Give the correct name :")

#Exercice 7:
print("Exercice 7 :")
fruits = input("Enter your favorite fruits (separated by space): ")
fruits_list = fruits.split()  # Creates a list

chosen_fruit = input("Enter the name of any fruit: ")

if chosen_fruit in fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")    

#Exercice 8:
print("Exercice 8 :") #Pizza Toppings
toppings = []
price_per_topping = 2.5
base_price = 10

while True:
    topping = input("Enter a topping (or type 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_price = base_price + len(toppings) * price_per_topping

print("\nYour toppings:", toppings)
print(f"Total cost: ${total_price:.2f}")

#Exercice 9:
print("Exercice 9 :")
ages = []
total_cost = 0

# Ask for number of people
num_people = int(input("How many people want to buy tickets? "))

# Loop to collect ages
for i in range(num_people):
    age = int(input(f"Enter age of person {i+1}: "))
    ages.append(age)

    # Apply pricing rules based on age
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15

    total_cost += cost

print(f"\nTotal ticket cost: ${total_cost}")



