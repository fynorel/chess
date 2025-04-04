import os
import pygame

WIDTH, HEIGHT = 760, 760
ROWS, COL = 8, 8
SQUARE = WIDTH // ROWS

brown = (87, 16, 16)
white = (255, 255, 255)

Path = "chessGame/chess_images/"

#Black pieces
BlacKnight = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bKN.png")), (SQUARE, SQUARE))
BlackBishop = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bB.png")), (SQUARE, SQUARE))
BlacKing = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bK.png")), (SQUARE, SQUARE))
BlackQueen = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bQ.png")), (SQUARE, SQUARE))
BlackRook = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bR.png")), (SQUARE, SQUARE))
BlackPawn = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bP.png")), (SQUARE, SQUARE))

#White pieces
WhiteKnight = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wKN.png")), (SQUARE, SQUARE))
WhiteBishop = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wB.png")), (SQUARE, SQUARE))
WhiteKing = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wK.png")), (SQUARE, SQUARE))
WhiteQueen = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wQ.png")), (SQUARE, SQUARE))
WhiteRook = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wR.png")), (SQUARE, SQUARE))
WhitePawn = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wP.png")), (SQUARE, SQUARE))
