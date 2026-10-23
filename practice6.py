# 1 - Import packages
import pygame, sys, random

# 2 - Define constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
COLOR1 = (0, 0, 0)
COLOR2 = (255, 255, 255)
N_PIXELS_TO_MOVE = 5

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s),  etc.
ballImage = pygame.image.load('images/ball.png')

# 5 - Initialize variables
ballX = 50
ballY = 350
ballRect = pygame.Rect(ballX, ballY, 100, 100)

# 6 - Loop forever
while True:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(580)
                ballY = random.randrange(380)
                ballRect = pygame.Rect(ballX, ballY, 100, 100)

    # 8 - Do any "per frame" actions
    keyPressedTuple = pygame.key.get_pressed()
    if keyPressedTuple[pygame.K_LEFT]:  # moving left
        ballX = ballX - N_PIXELS_TO_MOVE
    elif keyPressedTuple[pygame.K_RIGHT]:  # moving right
        ballX = ballX + N_PIXELS_TO_MOVE
    elif keyPressedTuple[pygame.K_UP]:  # moving up
        ballY = ballY - N_PIXELS_TO_MOVE
    elif keyPressedTuple[pygame.K_DOWN]:  # moving down
        ballY = ballY + N_PIXELS_TO_MOVE            
    ballRect = pygame.Rect(ballX, ballY, 100, 100)
   
    # 9 - Clear the window
    window.fill(COLOR2)
    
    # 10 - Draw all window elements
    pygame.draw.circle(window, COLOR1, (320, 240), 30, 0) # filled   
    pygame.draw.rect(window, COLOR1, (400, 300, 100, 100), 3) # 3 pixel edge
    window.blit(ballImage, (ballX, ballY))
   
    # 11 - Update the window
    pygame.display.update()
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait

