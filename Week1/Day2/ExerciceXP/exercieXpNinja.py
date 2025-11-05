#Exercise 1:
# import math

# print("Exercise 1:") # Fomula
# d_val= input("Enter the value of d: ")

# def calculate_formula(d_val):
#     c = 50
#     h = 30
#     d_values=d_val.split(',')
#     result =[]

#     for d in d_values:
#         q = math.sqrt((2 * c * int(d)) / h)
#         result.append(round(q)) #round to nearest integer
#     return result

# print(calculate_formula(d_val))

#Exercise 2:
print("\nExercise 2:") #List of Integers

# numbers = [[3, 47, 99, -80, 22, 97, 54, -23, 5, 7],
#     [44, 91, 8, 24, -6, 0, 56, 8, 100, 2],
#     [3, 21, 76, 53, 9, -82, -3, 49, 1, 76],
#     [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]]

#Bonus 12
"""
numbers = []
for i in range(10):
    num = []
    for j in range(10):
        user_num = int(input(f'Enter number {j+1} for sublist {i+1}: '))
        num.append(user_num)
    numbers.append(num)
"""
#Bonus 13
import random
numbers = []
for i in range(10):
    num=[]
    for j in range(10):
        random_num = random.randint(-100,100)
        num.append(random_num)
    numbers.append(num)

#Bonus 14
'''import random
numbers = []
count = random.randint(50,100)
for i in range(count):
    num= []
    for j in range(count):
        random_num = random.randint(-100,100)
        num.append(random_num)
    numbers.append(num)
'''

#Bonus 15
"""
Yes, the code works perfectly even when the list contains more or fewer than 10 elements.
All operations are based on dynamic functions like len(), sum(), max(), min(), and for loops, which automatically adapt to any list size.
"""

#for sum nulber of all elements
def sum_elements(numbers):
    summ=0
    for sublist in numbers :
        for n in sublist :
            summ+=n
    return summ

#numbers greater than 50
def greater_than_50(numbers):
    greater_numbers = []
    for sublist in numbers :
        for n in sublist :
            if n > 50 :
                greater_numbers.append(n)
    return greater_numbers

#numbers smallest than 10
def smallest_than_10(numbers):
    small_numbers = []
    for sublist in numbers :
        for n in sublist :
            if n < 10 :
                small_numbers.append(n)
    return small_numbers

#squared numbers value
def squared_values(numbers):
    squared_values_list = []
    for sublist in numbers :
        for n in sublist :
            squared_values_list.append(n**2)
    return squared_values_list

#unique numbers
def unique_numbers(numbers):
    unique_numbers = []
    for sublist in numbers :
        for n in sublist :
            if n in unique_numbers :
                continue
            else :
                unique_numbers.append(n)
    return unique_numbers

def average (numbers):
    average = sum_elements(numbers) / len(numbers)
    return average

def largest_number(numbers):
    largest_num = numbers[0][0]
    for sublist in numbers :
        for n in sublist :
            if n > largest_num :
                largest_num = n
    return largest_num

def smallest_number(numbers):
    smallest_num = numbers[0][0]
    for sublist in numbers :
        for n in sublist :
            if n < smallest_num :
                smallest_num = n
    return smallest_num


print (numbers)
print("Sorted (descending) : ",sorted(numbers, reverse=True))

print("Sum : ", sum_elements(numbers))
print(f'First number is : {numbers[0][0]} and the last number is : {numbers[-1][-1]}')
print("Greater than 50 :   ", greater_than_50(numbers))
print("Smallest than 10 : ", smallest_than_10(numbers))
print("Squaed values : ", squared_values(numbers))
print("Unique numbers : ", unique_numbers(numbers))
print("Average : ", average(numbers))
print("Largest number is : ", largest_number(numbers))
print("Smallest number is : ", smallest_number(numbers))








