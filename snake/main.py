import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
frameRate = 60


# player
player = pygame.Rect((275, 275, 50, 50))
isPaused = False
segments = []

# food
blank_object = pygame.Rect(0, 0, 0, 0)
foods = [blank_object]
foodColour = (0, 255, 0)
segmentColour = (0, 0, 255)

horizontalDirection = 0
verticalDirection = 1
horizontalDirectionHasBeenChanged = False
verticalDirectionHasBeenChanged = False

run = True


def spawnFood():
    randomX = random.randint(1, 550)
    randomY = random.randint(1, 550)
    food_prefab = pygame.Rect(randomX, randomY, 50, 50)
    foods.append(food_prefab)

def addSegment():



spawnFood()

while run:
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player)

    for food in foods:
        pygame.draw.rect(screen, foodColour, food)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] and not horizontalDirectionHasBeenChanged:
        horizontalDirection = -1
        verticalDirection = 0
        horizontalDirectionHasBeenChanged = True
        verticalDirectionHasBeenChanged = False
    elif key[pygame.K_d] and not horizontalDirectionHasBeenChanged:
        horizontalDirection = 1
        verticalDirection = 0
        horizontalDirectionHasBeenChanged = True
        verticalDirectionHasBeenChanged = False
    elif key[pygame.K_w] and not verticalDirectionHasBeenChanged:
        verticalDirection = -1
        horizontalDirection = 0
        horizontalDirectionHasBeenChanged = False
        verticalDirectionHasBeenChanged = True
    elif key[pygame.K_s] and not verticalDirectionHasBeenChanged:
        verticalDirection = 1
        horizontalDirection = 0
        horizontalDirectionHasBeenChanged = False
        verticalDirectionHasBeenChanged = True

    player.move_ip(5 * horizontalDirection, 5 * verticalDirection)

    # collision detection
    if player.y == 0 or player.y == 550 or player.x == 0 or player.x == 600:
        run = False

    for food in foods:
        if player.colliderect(food):
            foods.remove(food)
            addSegment()
            spawnFood()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

    clock.tick(frameRate)

pygame.quit()
