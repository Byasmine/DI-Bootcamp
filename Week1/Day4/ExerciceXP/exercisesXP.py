#Exercise 1: What I learned
print ('Execicse 1 : ')

def display_message(): # define the function 
    print('I am learning about functions in Python. ') #print a message

display_message() #calling the function

#Exercise 2 : What's your fav book
print("Exercise 2 : ")

def favorite_book(title): #define a function 
    return "One of my favorite book is "+ title #concatenation or by using f-string

print(favorite_book("\"Alice in Wonderland\"")) #call the function 

#Exercise 3 : some geography
print("Exercise 3 : ")

def describe_city(city, country = 'Unknown'): #def function
    return print(f'{city} is in {country}') #print a message

describe_city("Reykjavik", "Iceland")
describe_city("Paris")

#Exerecise 4 : Random number
print("Exercice 4 : ")

import random #import random

def compare_random(num): #define function with parameter num 
   randum_number = random.randint(1,100) #geenrate a rundum number
   if num == randum_number: #comparaison
      print("Success!")
   else:
       print(f"Fail ! your number: {num}, random number: {randum_number}")

compare_random(50)

#Exercise 5 : let's create some personalized shirts
print("Exercice 5 : ")

def make_shirt(size = 'large',text ='I Love Python') : #define function with parameters
    print(f"your shirt size is : {size} and {text}") #print a summary message


make_shirt()
make_shirt(size = 'medium')
make_shirt(text= 'it\'s green', size = "XS") #call the function

#Exercise 6 : Magicians
print("Exercice 6 : ")

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_names):
    for index,name in enumerate(magician_names):
        print(f"{index} : {name}")

show_magicians(magician_names)

def make_great(magician_names):
    for index,name in enumerate (magician_names):
        print(f"{index} : {name} the Great ")

make_great(magician_names)

#Exercise 7 :Temperature Advice
print("Exercise 7 : ")

import random

def get_random_temp(season) : #generating random temp
    if season in [12,1,2]:
        return round(random.uniform(-10, 10), 2)
    elif season in [3,4,5]:
        return round(random.uniform(10, 20), 2)
    elif season in [6,7,8]:
        return round(random.uniform(20, 40), 2)
    elif season in [9,10,11]:
        return round(random.uniform(10, 20), 2)
    else:
        return round(random.uniform(-10, 40), 2)  # fallback
    

def main():
    user_month = int(input("Enter the season from month (1-12) : "))

    r_temp = get_random_temp(user_month)
    print(f"The temperature right now is {r_temp:.1f} degrees Celsius.")

    if r_temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif r_temp < 17:
        print("Quite chilly! Don't forget your coat.")
    elif r_temp < 24:
        print("Nice weather.")
    elif r_temp < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")

main()

