#exercice 1:
print("Exercice 1: ") #Converting lists into dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionary_list = zip(keys,values)
print(dict(dictionary_list))

#execrice 2:
print("Exercice 2: ") #Cinemax

def total_cost (family):
    total =0
    for name,age in family.items():
        if age <3:
            total+=0
            print(name +"'s ticket price: Free ticket")
        elif age in range(3,13):
            total+=10
            print(name +"'s ticket price: 10$")
        else:
            total+=12
            print(name +"'s ticket price: 12$")

    return print("Total cost is : ",total)

# Collect data
number = int(input("Enter the family member's number: "))
names = []
ages = []

for i in range(number):
    name = input(f"Enter the name of member {i + 1}: ")
    names.append(name)
    age = int(input(f"Enter {name}'s age: "))
    ages.append(age)

family = dict(zip(names, ages))
print("\nFamily data:", family)

total_cost(family)# Compute total

#exercice 3:
print("Exercice 3:")#Zara

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue", 
        "Spain": "red", 
        "US": ["pink", "green"]
    },
}

#change the value of number_stores to 2:
brand["number_stores"] = 2
print ("* number_stores : ",brand["number_stores"] )

#describing Zara clients usinf the type of clothes
type_of_clothes = brand["type_of_clothes"]
print("* Zara clients are:", ", ".join(type_of_clothes[:3]))

#adding new key in the dictionary country_creation with value spain
brand["country_creation"] = "spain"
print("* country_creation : ",brand["country_creation"])

#check if international_cometitors exist
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
print("* List of internation_competitors : ",brand["international_competitors"])

#delet the creation_date key
del brand['creation_date']
print("* Brand Keys are:", list(brand.keys()))

#the last item in international_competitors
print("* The last item in international_competitors :  ",brand["international_competitors"][-1])

#major colors in US
print("* Major color in US :", brand["major_color"]["US"])

#number of keys in a dictionary
print("Number of Keys : ",len(brand.keys()))

#all the keys in the dictionary
print('Keys : ', brand.keys())

#Bonus create another dictionary (more_on_zara)
more_on_zara ={
    "creation_date": 2000,
    "number_stores": 800,
}

merged_dictionaries= brand.copy()
merged_dictionaries.update(more_on_zara)

print("Merged dictionaries : ",merged_dictionaries) # or using brand | more_on_zara

#exercice 4:
print("Exercice 4 :") #Disney Characters

#Character List
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"] 

#Dict 1
dict1 = {name : index for index,name in enumerate(users)}
print("Dictionary 1: ",dict1)

#Dict 2
dict2 = {index: name for index, name in enumerate(users)}
print("Dictionary 2: ", dict2)

#Dict 3
sorted_users= sorted(users)
dict3 = {name : index for index,name in enumerate(sorted_users)}
print("Dictionary 3: ", dict3)


