#Exercise 1:
print("Exercise 1:") #concatenate Lists
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list1.extend(list2) # or list=[*list1, *list2]
print(list1)

#Exercise 2:
print("\nExercise 2:") #Range of Numbers multiple of 5 and 7 from range 1500 to 2500

multiples = []
for num in range(1500, 2501):
    if num % 5 == 0 and num % 7 == 0:
        multiples.append(num)

print(multiples)

#Exercise 3:
print("\nExercise 3:") #Check the index
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input('Enter your name: ')
for name in names:
    if user_name.lower() == name.lower():
        print(f'your index is: {names.index(name)}') #to reach the index
        break
    else :
        print('your name is not here ')

#Exercise 4:
print("\nExercise 4:") #Greatest Number
numbers = []
for i in range(3):
    user_number = int(input(f'Enter the {i+1} number: '))
    numbers.append(user_number)

greatest_number = max(numbers)

print(f'The greatest number is: {greatest_number}')

#Exercise 5:
print("\nExercise 5:") #The Alphabet
import string
alphabet = list(string.ascii_lowercase) #creates a list of the alphabet
print(alphabet)

for letter in alphabet:
    if letter in ['a', 'e', 'i', 'o', 'u']:
        print(f"{letter} : vowel,")
    else:
        print(f"{letter} : consonant,")

#Exercise 6:
print("\nExercise 6:") #Words and Letters
words = []
for i in range(7):
    words.append(input(f'Enter word {i+1}: '))

letter = input('Enter a letter: ')
for word in words:
    if letter in word:
        print(f"The letter 'letter' is found in the index '{word.index(letter)}' of the word '{word}'.")
    else:
        print(f"The letter '{letter}' is not found in the word '{word}'.")

#Exercice 7:
print("\nExercise 7 :") #Min , Max and Sum

numbers = list(range(1,1000001))

print(f"Minimum number: {min(numbers)}")
print(f"Maximum number: {max(numbers)}")
print(f"Sum of all numbers: {sum(numbers)}")

#Exercice 8:
print("\nExercise 8 :") #List  And Tuple
sequence_number = input("Enter a sequence of numbers separated by commas: ")
split_sequence_number= sequence_number.split(",")
sequence_tuple = tuple(split_sequence_number)
sequence_list = list(split_sequence_number)

print("List:", sequence_list)
print("Tuple:", sequence_tuple)

#Exercice 9:
print("\nExercise 9 :") #Random Number
import random
random_number = random.randint(1, 9)
user_guess = input("Guess a number between 1 and 9: ")

while user_guess.lower() != 'quit':
    if int(user_guess) == random_number:
        print("Winner")
    else:
        print("Better luck next time")

    user_guess = input("Guess a number between 1 and 9 (or type 'quit' to exit): ") #very important line to avoid infinite loop

    
