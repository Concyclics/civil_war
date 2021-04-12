#by concyclics
#Area Define

INIT_PEOPLE=100
INIT_brithrate=0.1

class Area:
	people=INIT_PEOPLE
	army=0
	belong=0
	NO=-1
	points=[]
	
	def __init__(self,no,p):
		self.points=p
		self.NO=no
		
	def changeBelong(self,x):
		self.belong=int(x)
		
	def getBelong(self):
		return int(self.belong)
		
	def conscript(self,number):
		if (number>self.people or number<0):
			return True
		else:
			self.army+=number
			self.people-=number
			return False
	
	def population_increase(self,rate=INIT_brithrate):
		self.people+=int(self.people*max(rate,0))
		