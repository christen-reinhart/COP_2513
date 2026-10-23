# 1 - Import packages
import pygame, sys, random

# 2 - Define constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
COLOR1 = (255, 255, 0)
COLOR2 = (0, 255, 0)
COLOR3 = (255, 255, 255)
N_PIXELS_TO_MOVE = 5

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s),  etc.
bounceSound = pygame.mixer.Sound('sounds/boing.wav')
ballImage = pygame.image.load('images/ball.png')

# 5 - Initialize variables
ballX = 50
ballY = 350
circleX = 150
circleY = 50
ballRect = pygame.Rect(ballX, ballY, 100, 100) # a 100x100 square
square = pygame.Rect(400, 300, 100, 100) # a 100x100 square



# 6 - Loop forever
while True:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if square.collidepoint(event.pos):
                circleX = random.randrange(540)
                circleY = random.randrange(380)

            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(540)
                ballY = random.randrange(380)
            

    # 8 - Do any "per frame" actions
    keyPressedTuple = pygame.key.get_pressed()
    if keyPressedTuple[pygame.K_LEFT]:  # moving left
        if ballX <= 0:
            ballX=0

        else:
            ballX = ballX - N_PIXELS_TO_MOVE

    if keyPressedTuple[pygame.K_RIGHT]:  # moving right
        if ballX >= 540:
            ballX=540
        else:    
            ballX = ballX + N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_UP]:  # moving up
        if ballY <= 0:
            ballY=0

        else:
            ballY = ballY - N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_DOWN]:  # moving down
        if ballY >= 380:
            ballY=380

        else:
            ballY = ballY + N_PIXELS_TO_MOVE            
   
    # 9 - Clear the window
    window.fill(COLOR3)
    
    # 10 - Draw all window elements
   
    ballRect = window.blit(ballImage, (ballX, ballY))  
    pygame.draw.circle(window, COLOR1, (circleX, circleY), 30, 0) # filled  
    pygame.draw.rect(window, COLOR2, (400, 300, 100, 100), 3) # 3 pixel edge

    # 11 - Update the window
    pygame.display.update()
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
