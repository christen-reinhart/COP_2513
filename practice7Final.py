# Practice 7 Solution

# 1 - Import packages
import pygame, sys, random  # pygame for the window and drawing, sys to quit, random for new positions

# 2 - Define constants
WINDOW_WIDTH = 640  # window width in pixels
WINDOW_HEIGHT = 480  # window height in pixels
FRAMES_PER_SECOND = 30  # how many times the loop should run per second
BLACK = (0, 0, 0)  # RGB black
GREEN = (0, 255, 0)  # RGB green
YELLOW = (255, 255, 0)  # RGB yellow
WHITE = (255, 255, 255)  # RGB white
TEAL = (0, 200, 200)  # RGB teal
N_PIXELS_TO_MOVE = 5  # how far the ball moves per frame when an arrow is held

# 3 - Initialize the world
pygame.init()  # start pygame
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # create the window
clock = pygame.time.Clock()  # timer used to control the frame rate

# 4 - Load assets: image(s), sound(s),  etc.
ballImage = pygame.image.load('images/ball.png')  # load the ball picture
bounceSound = pygame.mixer.Sound('sounds/boing.wav')  # load the bounce sound

# 5 - Initialize variables
bgcolor = WHITE  # starting background color

ballX = 50  # ball's starting left edge
ballY = 350  # ball's starting top edge
maxBallX = WINDOW_WIDTH - 100  # farthest left the ball can go and stay on screen
maxBallY = WINDOW_HEIGHT - 100  # farthest top the ball can go and stay on screen

circleX = 100  # circle center x
circleY = 50  # circle center y
circleRadius = 30  # circle radius
maxCircleX = WINDOW_WIDTH - circleRadius  # farthest right the circle center can go
maxCircleY = WINDOW_HEIGHT - circleRadius  # farthest down the circle center can go

# area that contains the square
rectangleRect = pygame.Rect(400, 300, 100, 100)  # clickable area of the green square

# 6 - Loop forever
while True:  # keep running until the user closes the window

    # 7 - Check for and handle events
    for event in pygame.event.get():  # look at each event since the last frame
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:  # user clicked the window close button
            pygame.quit()  # shut down pygame
            sys.exit()  # end the program

        # See if user clicked
        if event.type == pygame.MOUSEBUTTONDOWN:  # user clicked the mouse
            if ballRect.collidepoint(event.pos):  # click landed on the ball
                ballX = random.randrange(maxBallX)  # pick a new x that keeps the ball on screen
                ballY = random.randrange(maxBallY)  # pick a new y that keeps the ball on screen
            if rectangleRect.collidepoint(event.pos):  # click landed on the square
                circleX = random.randrange(circleRadius, maxCircleX)  # new circle x, fully on screen
                circleY = random.randrange(circleRadius, maxCircleY)  # new circle y, fully on screen
        if event.type == pygame.KEYUP:  # a key was released
            if event.key == pygame.K_c:  # that key was C
                if bgcolor == WHITE:  # if background is white
                    bgcolor = TEAL  # switch it to teal
                else:  # otherwise
                    bgcolor = WHITE  # switch it back to white

    # 8 - Do any "per frame" actions

    # Get pressed keyboard keys
    keyPressedTuple = pygame.key.get_pressed()  # which keys are held down right now

    if keyPressedTuple[pygame.K_LEFT]:  # left arrow is held
        if ballX == 0:  # already at the left edge
            bounceSound.play()  # play bounce, do not move
        elif ballX < N_PIXELS_TO_MOVE:  # close to the left edge
            ballX = 0  # snap to the edge
        else:  # room to move
            ballX = ballX - N_PIXELS_TO_MOVE  # move left 5 pixels

    if keyPressedTuple[pygame.K_RIGHT]:  # right arrow is held
        if ballX == maxBallX:  # already at the right edge
            bounceSound.play()  # play bounce, do not move
        elif ballX > maxBallX - N_PIXELS_TO_MOVE:  # close to the right edge
            ballX = maxBallX  # snap to the edge
        else:  # room to move
            ballX = ballX + N_PIXELS_TO_MOVE  # move right 5 pixels

    if keyPressedTuple[pygame.K_UP]:  # up arrow is held
        if ballY == 0:  # already at the top
            bounceSound.play()  # play bounce, do not move
        elif ballY < N_PIXELS_TO_MOVE:  # close to the top
            ballY = 0  # snap to the top
        else:  # room to move
            ballY = ballY - N_PIXELS_TO_MOVE  # move up 5 pixels (smaller y is higher)

    if keyPressedTuple[pygame.K_DOWN]:  # down arrow is held
        if ballY == maxBallY:  # already at the bottom
            bounceSound.play()  # play bounce, do not move
        elif ballY > maxBallY - N_PIXELS_TO_MOVE:  # close to the bottom
            ballY = maxBallY  # snap to the bottom
        else:  # room to move
            ballY = ballY + N_PIXELS_TO_MOVE  # move down 5 pixels

    # 9 - Clear the window
    window.fill(bgcolor)  # paint the whole window the current background color

    # 10 - Draw all window elements
    ballRect = window.blit(ballImage, (ballX, ballY))  # draw the ball and save its rectangle for clicks
    pygame.draw.circle(window, YELLOW, (circleX, circleY), circleRadius, 0)  # draw a filled yellow circle
    pygame.draw.rect(window, GREEN, (400, 300, 100, 100), 3)  # draw a green square outline, 3 pixels thick

    # 11 - Update the window
    pygame.display.update()  # show the new frame on screen

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # wait so the loop runs about 30 times per second
