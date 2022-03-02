#!/usr/bin/env python3

import pygame
import sys

pygame.init()

winWitdh, winHeight = (400, 400)
gameWin = pygame.display.set_mode((winWitdh, winHeight))
pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(pygame.image.load("gamelogo.png"))

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 90)
            text = font.render(self.text, 1, (255, 255, 255))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False


def redrawWin():
    gameWin.fill((255, 255, 255))
    firstButton.draw(gameWin, (0, 0, 0))
    secondButton.draw(gameWin, (0, 0, 0))
    thirdButton.draw(gameWin, (0, 0, 0))
    fourthButton.draw(gameWin, (0, 0, 0))
    fifthButton.draw(gameWin, (0, 0, 0))
    sixthButton.draw(gameWin, (0, 0, 0))
    seventhButton.draw(gameWin, (0, 0, 0))
    eightButton.draw(gameWin, (0, 0, 0))
    ninthButton.draw(gameWin, (0, 0, 0))



firstButton = button([0, 0, 0], 10, 10, 120, 120, "")
secondButton = button([0, 0, 0], 140, 10, 120, 120, "")
thirdButton = button((0, 0, 0), 270, 10, 120, 120, "")
fourthButton = button((0, 0, 0), 10, 140, 120, 120, "")
fifthButton = button((0, 0, 0), 140, 140, 120, 120, "")
sixthButton = button((0, 0, 0), 270, 140, 120, 120, "")
seventhButton = button((0, 0, 0), 10, 270, 120, 120, "")
eightButton = button((0, 0, 0), 140, 270, 120, 120, "")
ninthButton = button((0, 0, 0), 270, 270, 120, 120, "")

clickCount = int(0)
two = int(2)

while True:
    
    redrawWin()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if clickCount >= 0:
                if firstButton.isOver(pos):
                    if firstButton.text == "":
                        if clickCount%two == 0:
                            firstButton.text = "X"
                        else:
                            firstButton.text = "O"
                        clickCount += 1
                if secondButton.isOver(pos):
                    if secondButton.text == "":
                        if clickCount%two == 0:
                            secondButton.text = "X"
                        else:
                            secondButton.text = "O"
                        clickCount += 1
                if thirdButton.isOver(pos):
                    if thirdButton.text == "":
                        if clickCount%two == 0:
                            thirdButton.text = "X"
                        else:
                            thirdButton.text = "O"
                        clickCount += 1
                if fourthButton.isOver(pos):
                    if fourthButton.text == "":
                        if clickCount%two == 0:
                            fourthButton.text = "X"
                        else:
                            fourthButton.text = "O"
                        clickCount += 1
                if fifthButton.isOver(pos):
                    if fifthButton.text == "":
                        if clickCount%two == 0:
                            fifthButton.text = "X"
                        else:
                            fifthButton.text = "O"
                        clickCount += 1
                if sixthButton.isOver(pos):
                    if sixthButton.text == "":
                        if clickCount%two == 0:
                            sixthButton.text = "X"
                        else:
                            sixthButton.text = "O"
                        clickCount += 1
                if seventhButton.isOver(pos):
                    if seventhButton.text == "":
                        if clickCount%two == 0:
                            seventhButton.text = "X"
                        else:
                            seventhButton.text = "O"
                        clickCount += 1
                if eightButton.isOver(pos):
                    if eightButton.text == "":
                        if clickCount%two == 0:
                            eightButton.text = "X"
                        else:
                            eightButton.text = "O"
                        clickCount += 1
                if ninthButton.isOver(pos):
                    if ninthButton.text == "":
                        if clickCount%two == 0:
                            ninthButton.text = "X"
                        else:
                            ninthButton.text = "O"
                        clickCount += 1
        
    if firstButton.text == secondButton.text == thirdButton.text != "":
        print("Game finished")
        clickCount = -1
    if firstButton.text == fifthButton.text == ninthButton.text != "":
        print("Game finished")
        clickCount = -1
    if firstButton.text == fourthButton.text == seventhButton.text != "":
        print("Game finished")
        clickCount = -1
    if secondButton.text == fifthButton.text == eightButton.text != "":
        print("Game finished")
        clickCount = -1
    if thirdButton.text == sixthButton.text == ninthButton.text != "":
        print("Game finished")
        clickCount = -1
    if thirdButton.text == fifthButton.text == seventhButton.text != "":
        print("Game finished")
        clickCount = -1
    if fourthButton.text == fifthButton.text == sixthButton.text != "":
        print("Game finished")
        clickCount = -1

    pygame.display.flip()