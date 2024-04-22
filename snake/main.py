import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
frameRate = 5
block_size = 50



# player
class Player():
    def __init__(self):
        self.x, self.y = 50, 50
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, 50, 50)
        self.body = [pygame.Rect(self.x - 50, self.y, 50, 50)]

    def update(self):
        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
        self.head.x += self.xdir * block_size
        self.head.y += self.ydir * block_size
        self.body.remove(self.head)

def DrawGrid():
    for x in range(0, SCREEN_WIDTH, block_size):
        for y in range(0, SCREEN_HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)

DrawGrid()

horizontalDirection = 0
verticalDirection = 1
horizontalDirectionHasBeenChanged = False
verticalDirectionHasBeenChanged = False

player = Player()

run = True

while run:
    pygame.draw.rect(screen, "green", player.head)

    player.update()
    screen.fill("black")
    DrawGrid()

    for square in player.body:
        pygame.draw.rect(screen, "green", square)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] or key[pygame.K_LEFT] and horizontalDirectionHasBeenChanged:
        player.xdir = -1
        player.ydir = 0
        horizontalDirectionHasBeenChanged = True
        verticalDirectionHasBeenChanged = False
    elif key[pygame.K_d] or key[pygame.K_RIGHT] and horizontalDirectionHasBeenChanged:
        player.xdir = 1
        player.ydir = 0
        horizontalDirectionHasBeenChanged = True
        verticalDirectionHasBeenChanged = False
    elif key[pygame.K_w] or key[pygame.K_UP] and verticalDirectionHasBeenChanged:
        player.xdir = 0
        player.ydir = -1
        horizontalDirectionHasBeenChanged = False
        verticalDirectionHasBeenChanged = True
    elif key[pygame.K_s] or key[pygame.K_DOWN] and verticalDirectionHasBeenChanged:
        player.xdir = 0
        player.ydir = 1
        horizontalDirectionHasBeenChanged = False
        verticalDirectionHasBeenChanged = True


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

    clock.tick(frameRate)

pygame.quit()
