# Christen Reinhart
# Professor: Hidalgo
# Date: 10/23/2026
# COP-2513 Module 10
# Lab 3 - AnimalShelter pygame & widgets GUI 


# 1 - Import packages and define classes
import pygame, pygwidgets, sys
# Do not import other packages without instructor approval.

class Cat():
    def __init__(self, name, gender, breed, age):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.age = age
        self.energy = 50
        self.hunger = 50
    
    def show(self):
        print(f'Cat: {self.name} is a {self.gender} {self.breed}. '\
              f'{self.name} is {self.age} year(s) old.')        
        print(f'Energy level: {self.energy}.'\
              f' Hunger level: {self.hunger}.\n')
    
    def eat(self):
        self.energy += 10
        self.hunger -= 5
        print(self.name, 'just ate.')
        
    def meow(self):
        self.energy -= 2
        print(self.name, 'says: Meow!')
        
    def play(self, minutes):
        self.energy -= (minutes * 2)
        self.hunger += minutes
        print(f'{self.name} just played for {minutes} minutes.') 
        
    def nap(self, minutes):
        self.energy = self.energy + (minutes * 2)
        self.hunger = self.hunger + minutes
        print(f'{self.name} just took a {minutes}-minute nap.') 

class AnimalShelter():
    def __init__(self):
        self.animalDict = {}
        self.nextId = 0

    def add(self, name, gender, breed, age):
        self.animalDict[self.nextId] = Cat(name, gender, breed, age)
        self.nextId += 1
        return self.nextId-1
    
    def display(self, aNum):
        self.animalDict[aNum].show()
        
    def display_all(self):
        for animal in self.animalDict.values():
            animal.show()

# main code

# 2 - Define constants
BLACK = (0, 0, 0) 
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
DARK_BLUE = (51, 51, 151)
LIGHT_YELLOW = (255, 255, 204)
RED = (255, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30


# 3 - Initialize the world
pygame.init() # initialize the pygame submodules
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # define the window size
pygame.display.set_caption("Animal Shelter Demo") # define the window title
clock = pygame.time.Clock() # create a clock object to manage the frame rate

# 4 - Load assets: image(s), sound(s),  etc.
# None

# 5 - Initialize variables

# Instantiate the animal shelter object and
# manually add the first cat, Garfield, to the shelter
oAnimalShelter = AnimalShelter() # create an instance of the AnimalShelter class
newId = oAnimalShelter.add('Garfield', 'male', 'Tabby', 5) # add a cat to the shelter and store its ID


# Title DisplayText
titleLabel = pygwidgets.DisplayText(window, (40, 20),'Add a Cat to the Shelter',
                                   fontSize=36, textColor=BLACK) # create a title label for the window using the pygwidgets DisplayText

# Name DisplayText and InputText                                
nameLabel = pygwidgets.DisplayText(window, (40, 80),'Name: ',
                                   fontSize=28, textColor=BLACK) # create a label for the name input field using the pygwidgets DisplayText 

nameInput = pygwidgets.InputText(window, (168, 78), '', focusColor=RED,
                                  fontSize=28, textColor=DARK_BLUE, width=320,
                                  backgroundColor=WHITE, initialFocus=True) # create an input field for the cat's name with specified properties using the pygwidgets InputText

# Gender radio buttons; Unknown starts selected
genderLabel = pygwidgets.DisplayText(window, (40, 130),'Gender: ',
                                   fontSize=28, textColor=BLACK) # create a label for the gender input fields using the pygwidgets DisplayText

radioFemale = pygwidgets.TextRadioButton(window, (160, 132), 'GenderGroup',
                                           'Female', fontSize=24, nickname='Female') # create a radio button for the female gender option using the pygwidgets TextRadioButton

radioMale = pygwidgets.TextRadioButton(window, (280, 132), 'GenderGroup',
                                            'Male', fontSize=24, nickname='Male') # create a radio button for the male gender option using the pygwidgets TextRadioButton

radioUnknown = pygwidgets.TextRadioButton(window, (380, 132), 'GenderGroup',
                                              'Unknown', fontSize=24, nickname='Unknown',
                                              value=True) # create a radio button for the unknown gender option using the pygwidgets TextRadioButton

# Breed DisplayText and InputText
breedLabel = pygwidgets.DisplayText(window, (40, 180),'Breed: ',
                                   fontSize=28, textColor=BLACK) # create a label for the breed input field using the pygwidgets DisplayText

breedInput = pygwidgets.InputText(window, (160, 178), '', focusColor=RED,
                                   fontSize=28, textColor=DARK_BLUE, width=320,
                                   backgroundColor=WHITE) # create an input field for the cat's breed with specified properties using the pygwidgets InputText


# Age DisplayText and InputText
ageLabel = pygwidgets.DisplayText(window, (40, 230), 'Age:',
                                   fontSize=28, textColor=BLACK) # create a label for the age input field using the pygwidgets DisplayText

ageInput = pygwidgets.InputText(window, (160, 228), '', focusColor=RED,
                                 fontSize=28, textColor=DARK_BLUE, width=80,
                                 backgroundColor=WHITE) # create an input field for the cat's age with specified properties using the pygwidgets InputText
 


# Add button 
addButton = pygwidgets.TextButton(window, (270, 290), 'Add', fontSize=28,
                                      textColor=DARK_BLUE, enterToActivate=True) # create a button to add the cat to the shelter with specified properties using the pygwidgets TextButton


# Status and error messages
statusMsg = pygwidgets.DisplayText(window, (40, 360), 'All fields are required.', 
                                       fontSize=28, textColor=DARK_BLUE) # create a status message to display information to the user with specified properties using the pygwidgets DisplayText

errorMsg = pygwidgets.DisplayText(window, (40, 360), 'Error.', 
                                       fontSize=36, textColor=RED) # create an error message to display information to the user with specified properties using the pygwidgets DisplayText  
errorMsg.hide() # hide the error message initially so that it is not displayed until an error occurs

# Show all cats button
showAllButton = pygwidgets.TextButton(window, (360, 410), 'Show all cats (in shell)',
                                       fontSize=22, textColor=DARK_BLUE) # create a button to show all cats in the shelter with specified properties using the pygwidgets TextButton


# Draw list
widgets = [titleLabel, nameLabel, nameInput, genderLabel,
           radioFemale, radioMale, radioUnknown,
           breedLabel, breedInput, ageLabel, ageInput,
           addButton, statusMsg, errorMsg, showAllButton] # create a list of all the widgets to be drawn on the window

# 6 - Loop forever
while True: # start an infinite loop 

    # 7 - Check for and handle events
    for event in pygame.event.get(): # get all events from the event queue
        # Clicked close button, Quit pygame, and end program 
        if event.type == pygame.QUIT: # if the user clicks the close button, quit pygame and exit the program         
            pygame.quit() # quit pygame
            sys.exit() # exit the program          
           
        # Give events to the interactive widgets
        nameInput.handleEvent(event) # handle events for the name input field
        breedInput.handleEvent(event) # handle events for the breed input field
        ageInput.handleEvent(event) # handle events for the age input field
        radioFemale.handleEvent(event) # handle events for the female radio button
        radioMale.handleEvent(event) # handle events for the male radio button
        radioUnknown.handleEvent(event) # handle events for the unknown radio button     

         # Add button: validate, then add the cat
        if addButton.handleEvent(event): # if the add button is clicked, validate the input fields and add the cat to the shelter
            name = nameInput.getText().strip() # get the text from the name input field and remove any leading or trailing whitespace
            breed = breedInput.getText().strip() # get the text from the breed input field and remove any leading or trailing whitespace
            ageText = ageInput.getText().strip() # get the text from the age input field and remove any leading or trailing whitespace
            gender = radioFemale.getSelectedRadioButton() # get the selected radio button for gender

            # Specific error messages; do not clear the form on error
            if name == '': # if the name input field is empty, display an error message
                statusMsg.hide() # hide the status message
                errorMsg.setValue('Name is required.') # set the error message to "Name is required."
                errorMsg.show() # show the error message
            elif breed == '': # if the breed input field is empty, display an error message
                statusMsg.hide() # hide the status message
                errorMsg.setValue('Breed is required.') # set the error message to "Breed is required."
                errorMsg.show() # show the error message
            elif ageText == '': # if the age input field is empty, display an error message
                statusMsg.hide() # hide the status message
                errorMsg.setValue('Age is required.') # set the error message to "Age is required."
                errorMsg.show() # show the error message
            elif not ageText.isdigit(): # if the age input field is not a digit, display an error message
                statusMsg.hide() # hide the status message
                errorMsg.setValue('Age must be an integer.') # set the error message to "Age must be an integer."
                errorMsg.show() # show the error message
            else:
                # All fields are okay: add the cat and show its name and ID
                age = int(ageText) # convert the age input field to an integer
                newId = oAnimalShelter.add(name, gender, breed, age) # add the cat to the shelter and get its ID
                errorMsg.hide() # hide the error message
                statusMsg.setValue(name + ' added to the shelter, with ID: ' + str(newId)) # set the status message to "name added to the shelter, with ID: newId"
                statusMsg.show() # show the status message
                # Clear text fields for the next cat; leave the radio as-is
                nameInput.clearText(True) # clear the name input field and set focus to it
                breedInput.clearText() # clear the breed input field
                ageInput.clearText() # clear the age input field

        # Show all cats prints to the shell, not the window
        if showAllButton.handleEvent(event): # if the show all cats button is clicked, display all cats in the shelter
            oAnimalShelter.display_all() # display all cats in the shelter
    
    
    # 9 - Clear the window
    window.fill(LIGHT_YELLOW) # fill the window with a light yellow color
    
    # 10 - Draw all window elements
    for w in widgets: # loop through all the widgets in the widgets list
        w.draw() # draw each widget on the window


    # 11 - Update the window
    pygame.display.update() # update the window to show the changes made to it

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
