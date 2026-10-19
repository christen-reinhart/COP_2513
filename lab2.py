# Christen Reinhart
# Professor: Hidalgo
# COP-2513 Week 5 lab2 
# Lab 2 - AnimalShelter class will manage a dictionary of Cat objects


class Cat: # Represents a cat with attributes and behaviors
    def __init__(self, name, gender, breed, age): # Initializes a new Cat object
        self.name = name # Sets the cat name
        self.gender = gender # Sets the cat gender
        self.breed = breed # Sets the cat breed
        self.age = age # Sets the cat age
        self.hunger = 50 # Initializes the cat hunger level
        self.energy = 50 # Initializes the cat energy level

    def show(self): # Displays the cat information
        print(f'Cat: {self.name} is a {self.gender} {self.breed}. {self.name} is {self.age} year(s) old.') # Displays the cat basic information
        print(f'Energy level: {self.energy}. Hunger level: {self.hunger}.') # Displays the cat energy and hunger

    def eat(self): # Makes the cat eat, increasing energy and decreasing hunger
        self.energy = self.energy + 10 
        self.hunger = self.hunger - 5
        print(self.name, 'just ate.') 

    def meow(self): # Makes the cat meow, decreasing energy
        self.energy = self.energy - 2
        print(self.name, 'says: Meow!')

    def play(self, minutes): # Makes the cat play decreasing energy and increasing hunger
        self.energy = self.energy - (minutes * 2)
        self.hunger = self.hunger + minutes
        print(f'{self.name} just played for {minutes} minutes.')

    def nap(self, minutes): # Makes the cat nap, increasing energy and hunger
        self.energy = self.energy + (minutes * 2)
        self.hunger = self.hunger + minutes
        print(f'{self.name} just took a {minutes}-minute nap.')


class AnimalShelter: # Represents an animal shelter that manages cats
    def __init__(self): # Initializes AnimalShelter object
        self.animals = {} # Initializes the dictionary to store cats
        self.next_id = 0 # Initializes the next available ID for a new cat

    def add(self, name, gender, breed, age): # Adds a new cat to the shelter and returns its ID
        new_cat = Cat(name, gender, breed, age) # Creates a new Cat object
        animal_id = self.next_id # Cat object and assigns it the next available ID
        self.animals[animal_id] = new_cat # Adds the new cat to the shelter dictionary
        self.next_id = self.next_id + 1 # Increments the next available ID for the next cat
        return animal_id # Return the ID of the newly added animal

    def display(self, aNum): # Displays information for the cat by its ID
        self.animals[aNum].show() 

    def display_all(self): # Loop through every ID in the dictionary and show each cat.
        for animal_id in self.animals: # Loop through each ID in the shelter dictionary
            self.animals[animal_id].show() # Displays the information for each cat in the shelter dictionary
            print() # Prints a blank line between cat information


# main 
shelter = AnimalShelter() # Creates a new AnimalShelter object to manage cats

garfield_id = shelter.add("Garfield", "male", "Tabby", 5) # Adds Garfield to the shelter and stores ID
print(f'Garfield added to the shelter, with ID: {garfield_id}') # Displays message that Garfield was added to the shelter

while True: # Main loop to interact with animal shelter
    action = input('\nPress A to add a cat, I for info about one cat, D for info about all cats, or Q to quit: ') # Prompts the user for an action
    if len(action) > 1: # If the user entered more than one character, take only the first one
        action = action[0] # Takes only the first character of the user's input
    action = action.upper() # Converts the user's input to uppercase to ensure consistent comparison

    if action == 'A': # Adds a new cat to the shelter
        name = input("W hat is the cat's name? ") # Prompts the user for cat name
        gender = input(f"What is {name}'s gender? ") # Prompts user for cat gender
        breed = input(f"What is {name}'s breed? ") # Prompts user for cat breed
        age = int(input(f"How old is {name}? ")) # Prompts user for cat age and converts to integer
        new_id = shelter.add(name, gender, breed, age)  # Adds new cat to shelter and stores ID
        print() # Prints a blank line
        print(f'{name} was added to the shelter, with ID {new_id}') # Displays confirmation message
    

    elif action == 'I': # Displays information about a cat by from its ID
        aNum = int(input("What is the cat's ID? ")) # 
        print()
        shelter.display(aNum)

    elif action == 'D': # Displays information about cats in shelter
        print()
        shelter.display_all()

    elif action == 'Q': # Quits the program
        break

print('Bye') # Displays message 
