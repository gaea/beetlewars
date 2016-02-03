import pygame, sys, os
from pygame.locals import *

pygame.init()
height = 720
width = 1280

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gravity port")

plx = 90
ply = 0
speed_y = 0
speed_x = 20
gravity = 0.8

player = pygame.image.load("pygame-icon.png")
player_rect = player.get_rect()
player.convert()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((4, 6, 3))
    screen.blit(player, (plx, ply))
    ply += speed_y
    plx += speed_x
    speed_y += gravity

    if ply + player_rect.bottom > height:
        speed_y *= -0.95

    if plx + player_rect.left < 0 or plx + player_rect.right > width:
        speed_x *= -0.98

    pygame.display.flip()
    clock.tick(55)

pygame.quit()
