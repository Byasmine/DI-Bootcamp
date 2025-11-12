#Old MacDonald's Farm

class Farm:
    def __init__ (self, farm_name):
        self.farm_name = farm_name
        self.animals= {}

    # def add_animal (self,animal_type, count=1):
    #     if animal_type in self.animals:
    #         count+=1
    #         self.animals[animal_type]= (count)
    #     else:
    #         self.animals[animal_type]= (count)

    def add_animal(self, **kwargs):
         for animal_type, count in kwargs.items():
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count

    def get_info(self):
        header = f"{self.farm_name}'s farm : \n"
        lines = [f"{animal} \t: {count}" for animal, count in self.animals.items()]
        return header + "\n".join(lines) + "\nE-I-E-I-0!"

    #Bonus
    def get_animal_types(self):
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        # Get sorted animal types
        animal_types = self.get_animal_types()

        # Add "s" if count > 1
        pluralized = [
            animal + "s" if self.animals[animal] > 1 else animal
            for animal in animal_types
        ]

        # Format the list into a readable sentence
        if len(pluralized) == 1:
            animals_str = pluralized[0]
        else:
            animals_str = ", ".join(pluralized[:-1]) + " and " + pluralized[-1]

        # Return final string
        return f"{self.farm_name}'s farm has {animals_str}."

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow', 5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)

macdonald = Farm("McDonald")
macdonald.add_animal(cow=5, sheep=2, goat=12)

print(macdonald.get_info())
print(macdonald.get_animal_types())
print (macdonald.get_short_info())
