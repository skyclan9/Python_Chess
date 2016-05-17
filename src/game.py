import sys
import pygame
from game_board import GameBoard
pygame.init()

size = width, height = 722, 722
surface = pygame.display.set_mode(size)

board = GameBoard()
board.fill_tileArray()
board.fill_rectArray()

for i in range(8):
        for k in range(8):
            string = board.tileArray[i][k]
            image = pygame.image.load(string).convert()
            rect = board.rectArray[i][k]
            surface.blit(image, rect)
pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()