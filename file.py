class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet('Momo', 'Lemur', ['Glide','Sneak', 'Sit'], health=50, energy=50) #! Why does this work but not using L85?
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        print(f'{self.first_name} takes {self.pet.name} for a walk...')
        print(f" ")
        print(f"{self.pet.name}'s health: {self.pet.health}")
        print(f"{self.pet.name}'s energy: {self.pet.energy}")
        return self

    def feed(self):
        self.pet.eat()
        print(f"{self.pet.name}, Sokka's boomerang is not food...let's get you something to eat.")
        print(f'How about some cactus {self.pet.name}?')
        print(f" ")
        print(f'I think {self.pet.name} had too much cactus juice...')
        print(f" ")
        print(f"{self.pet.name}'s health: {self.pet.health}")
        print(f"{self.pet.name}'s energy: {self.pet.energy}")
        return self


    def bathe(self):
        print(f"Time for a bath {self.pet.name}!")
        self.pet.noise()
        return self
        


# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method


class Pet:
    def __init__(self, name, type, tricks, health=50, energy=50):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 10
        print(f"*{self.name} snores loudly*")
        print(f" ")
        print(f"{self.name}'s health: {self.health}")
        print(f"{self.name}'s energy: {self.energy}")
        return self

    def eat(self):
        self.health += 10
        self.energy += 5
        return self

    def play(self):
        self.energy -= 10
        self.health += 5
        return self

    def noise(self):
        print('Screeeech!')
        return self



#implement __init__( name , type , tricks ):
#implement the following methods:
#sleep() - increases the pets energy by 25
#eat() - increases the pet's energy by 5 & health by 10
#play() - increases the pet's health by 5
#noise() - prints out the pet's sound

#!how can I make the Momo's health and energy work correctly?

ninja = Ninja('Ang', 'The Avater', Pet, 'treats', 'pet_food')
pet = Pet('Momo', 'Lemur', ['Glide','Sneak', 'Sit'], health=50, energy=50)


ninja.walk().feed().bathe()
print(" ")
pet.sleep() 

