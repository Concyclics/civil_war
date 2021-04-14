#button class
import pygame
class Button(object):
    def __init__(self,upimage,downimage,x,y,sizeX,sizeY):
        self.upimage = upimage
        self.downimage = downimage
        self.x=int(x);
        self.y=int(y);
        self.sizeX=sizeX;
        self.sizeY=sizeY;

    #is on it
    def isOn(self,posX,posY):
        if posX>=self.x and posX<=self.x+self.sizeX and posY>=self.y and posY<=self.y+self.sizeY:
            return True
        else:
            return False

    #button status
    def ButtonStatus(self,x,y):
        if(self.isOn(x, y)):
            return self.downimage
        else:
            return self.upimage

soider_upimage="resources/soider_button_up.png"
soider_downimage="resources/soider_button_down.png"
Soider=Button(soider_upimage,soider_downimage,20,720,40,40)

    
