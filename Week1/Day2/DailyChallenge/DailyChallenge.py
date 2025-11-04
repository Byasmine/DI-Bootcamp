#Daily Challenge : Lists & Strings
#Date : 2025-11-04

#Challenge 1
print("Challenge 1 :") #Multiples of A Number
list_multiples = []
number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

for i in range(1, length + 1):
    multiple = number * i
    list_multiples.append(multiple)

print("Multiples list:",list_multiples)

#Challenge 2
print("Challenge 2 :") #Remove Consecutive Duplicate Letters

def remove_consecutive_duplicates(s):
    output_string = ""
    for i in range(len(s)):
        if i == 0 or s[i] != s[i - 1]:
            output_string += s[i]
    return output_string

input_string = input("Enter a string: ")

result = remove_consecutive_duplicates(input_string)

print("Output:", result)
        

