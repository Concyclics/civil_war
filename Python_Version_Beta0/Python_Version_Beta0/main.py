#by concyclics
#GUI is here
import init
import sys
import pygame
import random
import Area

#for screen
SCR_W=init.SCR_W
SCR_H=init.SCR_H

#for area
Y_SIZE=init.Y_SIZE
X_SIZE=init.X_SIZE
AREA_DIS=init.AREA_DIS
LINE_WIDTH=init.LINE_WIDTH

#for title
Title='Civil War'

#for color
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)
belongColor=[WHITE,BLUE,RED]

#init
init.Init()

#datas
Areas=init.AreaList
playerArea=[0]
enemyArea=[len(Areas)-1]

#Area belong update
def upadateAreaBelong():
	for x in playerArea:
		Areas[x].changeBelong(1)
	for x in enemyArea:
		Areas[x].changeBelong(2)


#pygame init
pygame.init()
size=width,height=SCR_W,SCR_H
screen=pygame.display.set_mode(size)

pygame.display.set_caption(Title)

clock=pygame.time.Clock()

#background
wargame=pygame.image.load("map.jpg")
wargamerect=wargame.get_rect()

#main flow

upadateAreaBelong()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
	screen.blit(wargame,wargamerect)
	
	for x in Areas:
		pygame.draw.polygon(screen,belongColor[x.getBelong()],x.points,LINE_WIDTH)
		
	pygame.display.flip()
	
pygame.quit()