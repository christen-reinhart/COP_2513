# OO Lab1_Cat
class Cat:
    def __init__(self, name, gender, breed, age):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.age = age
        self.hunger = 50
        self.energy = 50

    def show(self):
        print(f'Cat: {self.name} is a {self.gender} {self.breed}. {self.name} is {self.age} year(s) old.')
        print(f'Energy level: {self.energy}. Hunger level: {self.hunger}.')

    def eat(self):
        self.energy = self.energy + 10
        self.hunger = self.hunger - 5
        print(self.name, 'just ate.')

    def meow(self):
        self.energy = self.energy - 2
        print(self.name, 'says: Meow!')

    def play(self, minutes):
        self.energy = self.energy - (minutes * 2)
        self.hunger = self.hunger + minutes
        print(f'{self.name} just played for {minutes} minutes.')

    def nap(self, minutes):
        self.energy = self.energy + (minutes * 2)
        self.hunger = self.hunger + minutes
        print(f'{self.name} just took a {minutes}-minute nap.')


# main code
garfield = Cat("Garfield", "male", "Tabby", 5)

while True:
    action = input('\nPress I for info, E to eat, M to meow, N to nap, P to play, or Q to quit: ')
    if len(action) > 1:
        action = action[0]
    action = action.upper()

    if action == 'I':
        garfield.show()
    elif action == 'E':
        garfield.eat()
    elif action == 'M':
        garfield.meow()
    elif action == 'N':
        minutes = int(input('How many minutes of nap time? '))
        garfield.nap(minutes)
    elif action == 'P':
        minutes = int(input('How many minutes of play time? '))
        garfield.play(minutes)
    elif action == 'Q':
        break

print('Bye')
