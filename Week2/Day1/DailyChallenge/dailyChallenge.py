#Old MacDonald's Farm

class Farm:
    def __init__ (self, farm_name):
        self.farm_name = farm_name
        self.animals= {}

    def add_animal (self,animal_type, count=1):
        if animal_type in self.animals:
            count+=1
            self.animals[animal_type]= (count)
        else:
            self.animals[animal_type]= (count)

    def get_info(self):
        header = f"{self.farm_name}'s farm : \n"
        lines = [f"{animal} \t: {count}" for animal, count in self.animals.items()]
        return header + "\n".join(lines) + "\nE-I-E-I-0!"

    #Bonus
    def get_animal_types(self):
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        animal_list = list(self.animals.keys())

        if len(animal_list) == 1:
            animals_str = animal_list[0]
        else:
            animals_str = ", ".join(animal_list[:-1]) + " and " + animal_list[-1]   
        
        return f"{self.farm_name}'s farm has {animals_str}."


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print(macdonald.get_animal_types())
print (macdonald.get_short_info())
