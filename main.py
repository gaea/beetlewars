import pygame, sys, os
from pygame.locals import *
import random
import time

pygame.init()
height = 720
width = 1280
fps = 60
execute_game = True
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Beetle Wars")


def clip(val, minval, maxval):
    return min(max(val, minval), maxval)


class Foe(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, image_path):
        self.position_x = position_x
        self.position_y = position_y
        self.image_path = image_path

        self.speed_y = 0
        self.speed_x = 20 * random.choice([1, -1])
        self.gravity = 0.8
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.image.convert()

foe_path_image = "pygame-icon.png"
foes = [Foe(random.randint(0, 900), 0, foe_path_image)]
clock = pygame.time.Clock()
start = time.time()

while execute_game:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((4, 6, 3))

    for foe in foes:
        screen.blit(foe.image, (foe.position_x, foe.position_y))
        foe.position_y += foe.speed_y
        foe.position_x += foe.speed_x
        foe.speed_y += foe.gravity

        if foe.position_y + foe.rect.bottom > height:
            foe.speed_y *= -0.95

        if foe.position_x < 0 or foe.position_x + foe.rect.right > width:
            foe.speed_x *= -1

    if time.time() - start > 3:
        foes.append(Foe(random.randint(0, 900), 0, foe_path_image))
        start = time.time()

    pygame.display.set_caption("[FPS]: %.2f snakes: %i" % (clock.get_fps(), len(foes)))

    pygame.display.flip()
    # clock.tick(40)
    # pygame.time.delay(10)

pygame.quit()
