#button class
import pygame
class Button(object):
    def __init__(self,upimage,downimage,x,y,sizeX,sizeY):
        self.upimage = upimage
        self.downimage = downimage
        self.x=x;
        self.y=y;
        self.sizeX=sizeX;
        self.sizeY=sizeY;

    #is on it
    def isOn(self):
        posX,posY=pygame.mouse.get_pos() 
        if posX>=self.x and posX<=self.x+self.sizeX and posY>=self.y and posY<=self.y+self.sizeY:
            return True

soider_upimage="resources/soider.png"
soider_downimage="resources/soider.png"
Soider=Button(soider_upimage,soider_downimage,20,620,40,40)

    
