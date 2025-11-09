# Exercise 1 : When will i retire ? age and gender
def get_age(year,month,day):
    #hard code the current date
    current_year = 2025
    current_month = 11

    age = current_year - year #calculate age

    return age

def can_retire(gender,date_of_birth):
    split_date = date_of_birth.strip().split("/")
    age=get_age(year=int(split_date[0]),month=int(split_date[1]),day=int(split_date[2]))
    
    #return True or false with the age
    if ((gender in ['men' ,'m'] ) and age >= 67) or ((gender in ['women' , 'f']) and age>= 62):
        return True,age
    else :
        return False,age

gender = input('Enter your gender (women or f / men or m) : ').lower()
date_of_birth = input("Enter you date of birth (yyyy/mm/dd) : ")
retirement_status, age = can_retire(gender,date_of_birth)

if retirement_status :
    print(f"You can retire, you are : {age} years old")
else:
    print(f"You cannot retire yet, you are {age} years old.")

#Exercise 2 : SUM
print("Exercise 2 : ")

from functools import reduce

user_number = int(input('Enter a number : '))

def list_numb(x): #a function that builds a list from one number
    numbers=[]
    for i in range(1,5):
        numbers.append(int(str(x)*i)) # convert to str for repetation and int to be added in the list
    return numbers


total = reduce(lambda x,y : x+y , list_numb(user_number))
print(total)

#Exercise 3: Double Dice
import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    counter = 0
    list_throws = []
    while True:
        dice_1 = throw_dice()
        dice_2 = throw_dice()
        counter += 1
        list_throws.append((dice_1,dice_2))
        if dice_1 == dice_2:
            break
    return counter,list_throws

# Example usage
# throws = throw_until_doubles()
# print(f"It took {throws} throws to get doubles.")

def main():
    results = []  # list to store 100 results

    for i in range(100):
        throws,list_throws = throw_until_doubles()  # how many rolls it took
        results.append(throws)          # save it
        print(f"{i+1}. {tuple(list_throws)}: {throws} throws")
    
    
    total_throws = sum(results)
    average_throws = round(total_throws / len(results), 2)

    print(f"Total throws to get 100 doubles: {total_throws}")
    print(f"Average throws per double: {average_throws}")

main()
        
