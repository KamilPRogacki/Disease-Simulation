from random import randint

class Animal:
    alive_animals = []  # List to store alive animals
    
    def __init__(self, age, disease_a, disease_b, immunity_a, survival_chance, reproduction_chance):
        self.age = age
        self.disease_a = disease_a
        self.disease_b = disease_b
        self.immunity_a = immunity_a
        self.survival_chance = survival_chance
        self.reproduction_chance = reproduction_chance
        self.alive = True  # Initially all animals are alive
        Animal.alive_animals.append(self)  # Add the new animal to the list of alive animals
        print("New animal born")
        
    def __str__(self):
        return f"Age: {self.age}, Disease A: {self.disease_a}, Disease B: {self.disease_b}, Immunity A: {self.immunity_a}, Survival Chance: {self.survival_chance}, Reproduction Chance: {self.reproduction_chance}"
        
    def turn(self):
        # Display list of animals alive with values of parameters
        print("Animals Alive:")
        for animal in Animal.alive_animals:
            print(animal)
        print()
        
        # Aging process for all animals
        for animal in Animal.alive_animals:
            if animal.age <= 10:
                animal.age += 1
                x = randint(0, 99)
                if not animal.immunity_a and animal.disease_a:
                    a = randint(0, 5)
                    if a >= 4:
                        animal.survival_chance = 15
                if animal.disease_b:
                    animal.survival_chance = 15
                    
                if animal.survival_chance <= x:
                    print("Animal Died")
                    animal.alive = False  # Mark the animal as dead
                    Animal.alive_animals.remove(animal)
                    
                if animal.reproduction_chance >= x:
                    # Make new animal with age 1 and rest of parameters random
                    new_age = 1
                    new_disease_a = bool(randint(0, 1))
                    new_disease_b = bool(randint(0, 1))
                    new_immunity_a = bool(randint(0, 1))
                    new_survival_chance = randint(0, 100)
                    new_reproduction_chance = randint(0, 100)
                    new_animal = Animal(new_age, new_disease_a, new_disease_b, new_immunity_a, new_survival_chance, new_reproduction_chance)
            else:
                # Save information of animals that survived 10 or more turns to a file
                if animal in Animal.alive_animals:
                    if animal.age >= 10:
                        with open("survived_animals.txt", "a") as file:
                            file.write(f"Age: {animal.age}, Disease A: {animal.disease_a}, Disease B: {animal.disease_b}, Immunity A: {animal.immunity_a}, Survival Chance: {animal.survival_chance}, Reproduction Chance: {animal.reproduction_chance}\n")
                    
                    animal.alive = False  
                    print("Animal died")
                    Animal.alive_animals.remove(animal)  # Remove the dead animal from the list of alive animals



# Example usage
animal1 = Animal(2, False, False, False, 90, 100)
for i in range(40):
    animal1.turn()
#print("input any key to close")
#input()