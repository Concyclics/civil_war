#by concyclics
#init for game set

import Area

#for screen
SCR_W=640
SCR_H=640

#for area
Y_SIZE=50
X_SIZE=50
AREA_DIS=10
LINE_WIDTH=4
AreaList=[]

def getPoints(x,y):
	if x>=0 and x<=SCR_W-X_SIZE and y>=0 and y<=SCR_H-Y_SIZE:
		return [(x,y),(x,y+Y_SIZE),(x+X_SIZE,y+Y_SIZE),(x+X_SIZE,y)]

def initArea():
	cnt=0
	for x in range(0,SCR_W-X_SIZE,X_SIZE+AREA_DIS):
		for y in range(0,SCR_H-Y_SIZE,Y_SIZE+AREA_DIS):
			AreaList.append(Area.Area(cnt,getPoints(x,y)))
			cnt+=1
			
def Init():
	initArea()
	