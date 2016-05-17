import sys
import pygame
pygame.init()

size = width, height = 722, 722
surface = pygame.display.set_mode(size)
background = pygame.image.load("chessboard_722.png").convert()
backgroundrect = background.get_rect()
surface.blit(background, backgroundrect)
pygame.display.update(backgroundrect)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   sys.exit()