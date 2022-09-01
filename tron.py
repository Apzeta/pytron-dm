import pygame, sys, time
from pygame.locals import *

# CONFIG VARIABLES
FPS = 10
WIDTH = 400
HEIGHT = 400

# Colors

WHITE = (255, 255, 255)
BLACK = ( 0, 0, 0)
GREEN = ( 0, 255, 0)
BLACK_GREEN = ( 0, 155, 0)
RED = (255, 0, 0)


def main():
    global DISPLAYSURF, FPSCLOCK, BASICFONT
    # Start Pygame and Configs
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 20)
    pygame.display.set_caption("PYTHRON")

    while True:
        runGame()


def runGame():
    p1 = player('right', 50)
    p2 = player('left', -50)
    STARTCONT = 0
    pause = False

    while True:

        # Close Game
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Hit detection 1
        if (p1.checkBorder() == True or p2.checkBorder() == True):
            if (p1.checkBorder() == True):
                p1.score += 1
            elif (p2.checkBorder() == True):
                p2.score += 1
            STARTCONT = 0
            restartGame(p1, p2)
            pause = True

        # Hit detection 2
        if (p1.checkPos(p2.step) == True or p2.checkPos(p1.step) == True):
            if (p1.checkPos(p2.step) == True):
                p1.score += 1
            elif (p2.checkPos(p1.step) == True):
                p2.score += 1
            restartGame(p1,p2)
            pause = True

        # Puse for games
        # Checks
        if (pause == False):
            # PLayer 1
            p1.direct(1)
            p1.move()
            p1.drawplayer(RED)

            # PLayer 2
            p2.direct(2)
            p2.move()
            p2.drawplayer(GREEN)
        # If nothing is drawn wiat a bit
        else:
            pausetext = BASICFONT.render("Press Enter to continue...", 2, (WHITE))
            DISPLAYSURF.blit(pausetext, (WIDTH / 5, HEIGHT / 5))
            kys = pygame.key.get_pressed()
            if kys[K_RETURN]:
                DISPLAYSURF.fill(BLACK)
                pause = False


        p1.drawScore(WIDTH / 6, GREEN)
        p2.drawScore(WIDTH / 1.5, RED)

        # FPS checker and Potato
        pygame.display.update()
        FPSCLOCK.tick(FPS)

# Class for player 1, 2
class player():

    # Construction of Bike
    def __init__(self, dir, num):
        self.x = WIDTH / 2 + num
        self.y = HEIGHT / 2
        self.health = 10
        self.damage = 5
        self.speed = 10
        self.direction = dir
        self.score = 0
        self.step = []

    # Method to draw lines & PLayer
    def drawplayer(self, col):
        p1_rect = pygame.Rect(self.x, self.y, 16, 16)
        pygame.draw.rect(DISPLAYSURF, col,p1_rect)

    # Movement check
    def move(self):
        if (self.direction == 'right'):
            self.x += self.speed;
        elif (self.direction == 'left'):
            self.x -= self.speed;
        elif (self.direction == 'up'):
            self.y -= self.speed;
        elif (self.direction == 'down'):
            self.y += self.speed;
        else:
            pass
        # Checks for later
        self.step.append((self.x, self.y))

    # Direction of light bike
    def direct(self, type):
        keys = pygame.key.get_pressed()

        if (type == 1):
            if keys[K_DOWN] and self.direction != 'up':
                self.direction = 'down'
            elif keys[K_UP] and self.direction != 'down':
                self.direction = 'up'
            elif keys[K_RIGHT] and self.direction != 'left':
                self.direction = 'right'
            elif keys[K_LEFT] and self.direction != 'right':
                self.direction = 'left'
        elif(type == 2):
            if keys[K_s] and self.direction != 'up':
                self.direction = 'down'
            elif keys[K_w] and self.direction != 'down':
                self.direction = 'up'
            elif keys[K_d] and self.direction != 'left':
                self.direction = 'right'
            elif keys[K_a] and self.direction != 'right':
                self.direction = 'left'

    # Check for collition
    def checkBorder(self):
        if (self.x == WIDTH):
            return True
        elif (self.x == 0):
            return True
        elif self.y == HEIGHT:
            return True
        elif self.y == 0:
            return True
        else:
            return False

    # Restart
    def restart(self, dir):
        DISPLAYSURF.fill(BLACK)
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.direction = dir

    # Save Data for PLayer 1
    # Save Data for PLayer 2
    def checkPos(self, other):
        for coords in self.step[0:-2]:
            if (self.x, self.y) == coords:
                return True

        if ((self.x, self.y) in other):
            return True
        else:
            return False

    # Draw Score
    def drawScore(self, x, color):
        scoretext = BASICFONT.render("Score: "+str(self.score), 1, (color))
        DISPLAYSURF.blit(scoretext, (x, 10))

# Restart Game
# Calls for Game for restart
def restartGame(p1, p2):
    p1.restart('right')
    p2.restart('left')
    p1.step = []
    p2.step = []

if __name__ == "__main__":
    main()

#Made By Apzeta Aka "Mr.Robot"#
