import sys
import pygame
from pygame.locals import *
import gDraggable
import gScreen
import gChessBoard

test = gScreen.gameScreen(1920, 1080)
test.setBackground(255, 255, 255)

#clock = pygame.time.Clock()

#img = gDraggable.draggable(0, 0, "default_texture.png")

chess = gChessBoard.chess_board(test)

        
QUIT = False


while not QUIT:
        for event in pygame.event.get():
                if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                                QUIT = True
        chess.isClicked()
        test.drawBackground()
        chess.drawBoardandPieces(test.screen)
        chess.isDropped()
        chess.movePiece()
        chess.generateValidMoves()
        chess.checkMove()
        #img.draw(test.screen)
        #img.moveSprite()
        test.update()
        #clock.tick(60)

print("Program closed!")
test.quit()
sys.exit()
