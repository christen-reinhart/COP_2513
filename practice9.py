# Pygame demo text and buttons
# Practice 9 solution: name box, major radio buttons, submit, status/error messages
# Uses Student and Course objects to store each submitted name and major

# 1 - Import packages and define classes
import pygame, sys, pygwidgets  # pygame for the window/events, sys to quit, pygwidgets for text boxes, buttons, labels

class Student:  # blueprint for one student; used by Course.add
    def __init__(self, aName, aMajor):  # runs when Course.add does Student(aName, aMajor)
        self.name = aName  # store the name typed into nameInput
        self.major = aMajor  # store the selected radio nickname (IT, CyS, or other)

    def show(self):  # returns a greeting string; display_all prints this
        return f'Hello {self.name}! Selected major: {self.major}'

class Course:  # manager object; holds a list of Student objects (like AnimalShelter held Cats)
    def __init__(self, aCode):  # runs when main does Course('COP2513')
        self.code = aCode  # course code, COP2513
        self.student_list = []  # empty list that add() will append Student objects to

    def add(self, aName, aMajor):  # called before the loop for Minnie, and again on each valid Submit
        self.student_list.append(Student(aName, aMajor))  # create a Student and put it in the list

    def display_all(self):  # prints every student; not called in this program, but ready to use
        for s in self.student_list:  # loop through each Student object
            print(s.show())  # print that student's greeting

# 2 - Define constants
BLACK = (0, 0, 0)  # RGB black; used by nameLabel
GRAY = (128, 128, 128)  # RGB gray; defined but not used in this file
WHITE = (255, 255, 255)  # RGB white; used as the nameInput background
DARK_BLUE = (51, 51, 151)  # RGB dark blue; used by nameInput text, submit text, and statusMsg
LIGHT_YELLOW = (255, 255, 204)  # RGB light yellow; used by window.fill each frame
RED = (255, 0, 0)  # RGB red; used by nameInput focus border and errorMsg
WINDOW_WIDTH = 640  # window width in pixels; passed to set_mode
WINDOW_HEIGHT = 480  # window height in pixels; passed to set_mode
FRAMES_PER_SECOND = 30  # target loop speed; passed to clock.tick

# 3 - Initialize the world
pygame.init()  # start pygame systems before creating the window or widgets
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # create the surface every widget draws on
pygame.display.set_caption("Pygwidgets Demo")  # set the title bar text
clock = pygame.time.Clock()  # timer used at the bottom of the loop to limit the frame rate

# 4 - Load assets: image(s), sounds,  etc.
# None  # this program has no images or sounds to load

# 5 - Initialize variables

oop = Course('COP2513')  # create the one Course object the rest of the program talks to
oop.add('Minnie Mouse', 'IT')  # put one Student in the list before the user does anything

nameLabel = pygwidgets.DisplayText(window, (20, 50), 'Enter your name: ',
                                   fontSize=36, textColor=BLACK)  # non-editable label left of the text box

nameInput = pygwidgets.InputText(window, (230, 55), '', focusColor=RED,
                                  fontSize=36, textColor=DARK_BLUE, width=320,
                                  backgroundColor=WHITE, initialFocus=True)  # editable name box; cursor starts here
# later: handleEvent for typing, getText on submit, clearText after submit

radioIT = pygwidgets.TextRadioButton(window, (250, 105), 'MajorGroup',
                                           'IT', fontSize=32, nickname='IT')  # radio in MajorGroup; nickname is what getSelectedRadioButton returns
radioCyS = pygwidgets.TextRadioButton(window, (310, 105), 'MajorGroup',
                                            'CyS', fontSize=32, nickname='CyS')  # same group, so only one of IT/CyS/Other can be on
radioOther = pygwidgets.TextRadioButton(window, (390, 105), 'MajorGroup',
                                              'Other', fontSize=32, nickname='other',
                                              value=True)  # same group; value=True means Other starts selected

submitButton = pygwidgets.TextButton(window, (240, 155), 'Submit', fontSize=32,
                                      textColor=DARK_BLUE, enterToActivate=True)  # button; Enter also counts as a click
# later: handleEvent returns True when clicked, which triggers the submit logic

statusMsg = pygwidgets.DisplayText(window, (20, 250),
                                       'Hello!',
                                       fontSize=36, textColor=DARK_BLUE,
                                       justified='center')  # success message; setValue updates it after a valid submit

errorMsg = pygwidgets.DisplayText(window, (20, 250),
                                       'Error.',
                                       fontSize=36, textColor=RED,
                                       justified='center')  # error message; same spot as statusMsg, so only one should be visible
errorMsg.hide()  # start hidden so the Hello status is what the user sees first

# Adding all widgets to a list to make it easier to call draw (using a loop)

widgets = [nameLabel, nameInput, radioIT, radioCyS, radioOther, submitButton, statusMsg, errorMsg]  # draw order; later items cover earlier ones if they overlap

# 6 - Loop forever
while True:  # one pass is one frame; ends only when the user closes the window

    # 7 - Check for and handle events
    for event in pygame.event.get():  # each event since the last frame (close, key, mouse)
        if event.type == pygame.QUIT:  # user clicked the window close button
            pygame.quit()  # shut down pygame
            sys.exit()  # end the program

        nameInput.handleEvent(event)  # let the text box react to typing and clicks
        radioIT.handleEvent(event)  # let this radio react; also keeps the group in sync
        radioCyS.handleEvent(event)  # same for CyS
        radioOther.handleEvent(event)  # same for Other

        if (submitButton.handleEvent(event)):  # True only when Submit is clicked or Enter is pressed
            userText = nameInput.getText()  # read whatever is currently in the name box
            major = radioIT.getSelectedRadioButton()  # nickname of the selected radio in MajorGroup (works from any button in the group)
            if userText == '':  # empty name is invalid
                statusMsg.hide()  # hide the success message so it does not sit under the error
                errorMsg.setValue('Please enter a name.')  # change the error text
                errorMsg.show()  # make the error visible
            else:  # name is not empty
                oop.add(userText, major)  # create a Student and append it to the Course list
                errorMsg.hide()  # hide any previous error
                statusMsg.setValue('Hello ' + userText + '! You selected major: ' + major)  # build the success text
                statusMsg.show()  # make the success message visible
            nameInput.clearText(True)  # clear the box either way; True puts the cursor back in the box

    # 8 - Do any "per frame" actions
    # none in this program; all work happens on events above

    # 9 - Clear the window before drawing it again
    window.fill(LIGHT_YELLOW)  # paint the whole window so old drawings do not leave a trail

    # 10 - Draw the window elements

    for w in widgets:  # draw every widget in the list
        w.draw()  # hidden widgets (errorMsg at the start) draw nothing

    # the above loop makes all these calls to draw:
    # nameLabel.draw()
    # nameInput.draw()
    # radioIT.draw()
    # radioCyS.draw()
    # radioOther.draw()
    # submitButton.draw()
    # statusMsg.draw()
    # errorMsg.draw()

    # 11 - Update the window
    pygame.display.update()  # push the drawn frame to the screen

    # 12 - Slow things down
    clock.tick(FRAMES_PER_SECOND)  # wait so the loop runs about 30 times per second
