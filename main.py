import pygame

from chessGame.constants import *

pygame.init()

clock = pygame.time.Clock()

Win = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    run = True
    FPS = 60
    while run:
        clock.tick(FPS)
        Win.blit(WhiteBishop, (50, 50))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()

main()
