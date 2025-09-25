#!/usr/bin/env python3

import sys
import math
import pygame

fps = 120
width = 1600
height = 1200

origin = (width, height)
scale = min(width, height) * 0.4
dt = 1/fps

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Pendulum")
screen = pygame.display.set_mode(origin)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()