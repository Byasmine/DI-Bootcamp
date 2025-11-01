#Exercice 1
print("Execrice 1:")
print("The shell finds executables by searching the directories listed in the PATH environment variable, so when python (or python3) is installed in a folder that's in $PATH, you can run it without typing the full path; $PATH tells Linux (or CMD) where to look for those executables.")

#Exercice 2
print("Exercice 2:")
# An alias is a shortcut or nickname for a longer command. It helps to type less and work faster in the terminal.
print("alias lets you create shortcuts for commands. For example alias py='python3' makes py behave like python3.")

#Exercice 3
print("Exercice 3:")
#True
#True
#False
#False
#True
#False / 0

x = (1 == True)        # True
y = (1 == False)       # False
a = True + 4           # 1 + 4 = 5
b = False + 10         # 0 + 10 = 10

print("x is", x)       # x is True
print("y is", y)       # y is False
print("a:", a)         # a: 5
print("b:", b)         # b: 10

#Exercice 4
print("Exercice 4:")
my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum."""

print(len(my_text))

#Exercice 5
print("Exercice 5:")
longest = ""

while True:
    sent = input("Enter a sentence without the letter 'A': ")
    
    if "a" in sent.lower():
        print("Oops! Your sentence contains the letter 'A'. Try again.")
        continue
    
    if len(sent) > len(longest):
        longest = sent
        print("Good job! ^u^")
    else:
        print("Try again to beat your longest sentence!")