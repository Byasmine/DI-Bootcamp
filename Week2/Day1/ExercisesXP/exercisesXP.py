
#Exercice 1:
print("Exercise 1 : ")
#  Define the Cat class
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Create three cat objects
cat1 = Cat("Milo", 2)
cat2 = Cat("Luna", 5)
cat3 = Cat("Simba", 3)

# Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    if cat2.age > oldest.age:
        oldest = cat2
    if cat3.age > oldest.age:
        oldest = cat3
    return oldest

# Print the oldest cat's details
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

#Exercice 2:
print("Exercise 2 :")  # Dogs

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

#Create Dog Objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

# print Dog Details and Call Methods
print(f"{davids_dog.name} is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

#Compare Dog Sizes
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is taller.")
else:
    print(f"{sarahs_dog.name} is taller.")


#Exercise 3 : 
print (" Exercise 3 : ") #who's the song producer ?

class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for item in self.lyrics:
            print(item)

    
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

#Exercise 4 : 
print("Exercise 4 : ") #Afternoon At the Zoo

class Zoo():
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    
    def add_animal(self,*new_animals):  # Accepts multiple animals
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)

    def get_animals(self):
        print(self.animals)
    
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped = {}

        for animal in sorted_animals:
            first_letter = animal[0]
            if first_letter in grouped:
                grouped[first_letter].append(animal)
            else:
                grouped[first_letter] = [animal]

        return grouped
    
    def get_groups(self):
        grouped = self.sort_animals()
        for letter, animals in grouped.items():
            print(f"{letter} : {animals}")

# Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Add animals
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
# Add multiple animals in one call
brooklyn_safari.add_animal("Cougar", "Cat", "Zebra", "Lion")

# Display current animals
brooklyn_safari.get_animals()

# Sell an animal
brooklyn_safari.sell_animal("Lion")

# Display animals after selling
brooklyn_safari.get_animals()

# Sort and group animals
grouped = brooklyn_safari.sort_animals()
print("Grouped animals:", grouped)

# Print groups nicely
brooklyn_safari.get_groups()
