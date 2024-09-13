import sys
import pygame
from pygame.locals import *
import gClickable
import gScreen
#import gObj

scr = gScreen.gameScreen(800, 800)
scr.setBackground(255, 255, 255)
playGame = gClickable.clickableObj(800 / 2, 800 / 2, "playGame.png")
quitGame = gClickable.clickableObj(800 / 2, (800 / 2) + 200, "quitGame.png")

stop = False

while not stop:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                stop = True

    print(pygame.mouse.get_pos())

    playGame.isClicked()
    quitGame.isClicked()
    
    scr.drawBackground()

    playGame.draw(scr.screen)
    quitGame.draw(scr.screen)

    if playGame.get_clicked() or quitGame.get_clicked():
        print("Clicking works")
        stop = True

    scr.update()

scr.quit()
sys.exit()
