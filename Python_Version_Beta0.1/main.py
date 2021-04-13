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
Title=init.GameTitle

#for color
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
belongColor=[WHITE,BLUE,RED]
SelectColor=[GREEN,]

#Area belong update
def upadateAreaBelong():
	for x in playerArea:
		Areas[x].changeBelong(1)
	for x in enemyArea:
		Areas[x].changeBelong(2)


#mouse control
#mouse_cursor = pygame.image.load(init.mouse_image).convert_alpha()
def getMousePos():
	x,y=pygame.mouse.get_pos()
	#x-= mouse_cursor.get_width()/2
	#y-= mouse_cursor.get_height()/2
	return x,y

#Area Select
mouseSelectArea=-1

def Mouse_inArea(x,y):
	for place in Areas:
		if x>=place.points[0][0] and x<=place.points[2][0] and y>=place.points[0][1] and y<=place.points[2][1]:
			return place.NO
	return -1

#in map
def Mouse_inMap(x,y):
	if(x>=0 and x<=SCR_W and y>=0 and y<=SCR_H):
		return True
	else:
		return False

#text display
def AreaReputationDisplay():
	if(mouseSelectArea>=0):
		screen.fill(WHITE)
		if(Areas[mouseSelectArea].belong==1):
			text=font.render("地区编号: "+str(mouseSelectArea)+" 当地人口: "+str(Areas[mouseSelectArea].people)+" 驻地军队: "+str(Areas[mouseSelectArea].army),True,BLACK,WHITE)
		else:
			text=font.render("地区编号: "+str(mouseSelectArea)+" 地区归属: "+str(Areas[mouseSelectArea].belong),True,BLACK,WHITE)
		screen.blit(text,(0,SCR_H))
		
def TotalReputationDisplay():
	reputation=0
	armys=0
	screen.fill(WHITE)
	for place in playerArea:
		reputation+=Areas[place].people
		armys+=Areas[place].army
	text=font.render("玩家拥有地区: "+str(len(playerArea))+" 总计人口: "+str(reputation)+" 总计军队: "+str(armys),True,BLACK,WHITE)
	screen.blit(text,(0,SCR_H))
		
#main flow

#init
init.Init()

#datas
Areas=init.AreaList
playerArea=[0,1,2,3,4,10,11,12,13,20,21,22,30,31,40]
enemyArea=[len(Areas)-1]

#pygame init
pygame.init()
size=width,height=max(init.TEXT_W,SCR_W),SCR_H+init.TEXT_H
screen=pygame.display.set_mode(size)

#background
wargame=pygame.image.load(init.background)
wargamerect=wargame.get_rect()
pygame.display.set_caption(Title)

#reflash
clock=pygame.time.Clock()
clock.tick(60)

#characters
font=pygame.font.Font(init.character,init.charSIZE)

#options
screen.fill(WHITE)
while True:
	for event in pygame.event.get():
		#exit
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y=getMousePos()
			mouseSelectArea=Mouse_inArea(x,y)
			if(mouseSelectArea>=0):
				AreaReputationDisplay()
			elif(Mouse_inMap(x,y)):
				TotalReputationDisplay()
				
	
	#background
	screen.blit(wargame,wargamerect)
	
	#draw areas
	for place in Areas:
		if(place.NO==mouseSelectArea):
			pygame.draw.polygon(screen,SelectColor[0],place.points,LINE_WIDTH)
		else:
			pygame.draw.polygon(screen,belongColor[place.getBelong()],place.points,LINE_WIDTH)
	
	#display mouse
	#screen.blit(mouse_cursor, (x, y))
	upadateAreaBelong()	
	pygame.display.flip()
	
pygame.quit()