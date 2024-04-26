from random import *
import math 
# import time
from core import *

#Classe Agent

class Agent: 

    def __init__(self, image_bebe:int, esperance_vie, enfant:bool):

        self.alive : bool = True
        self.age = 0
        self.esperance_vie = esperance_vie
        
        # pour deplacement
        self.orientation:int = 0
        self.type : int = image_bebe
        
        self.repos : bool = False
        
        # pour maladie
        self.state : int = 0
        self.cpt : int = 10 
        
        # pour position
        self.x = 0
        self.y = 0
        
        if not enfant:
            self.reset()
        
        self.energie = 100.0 #niveau d'energie 100 par defaut
        return
    
    def reset(self):
        self.x = randint(0,getWorldWidth()-1)
        self.y = randint(0,getWorldWidth()-1)
        while getTerrainAt(self.x,self.y) != 0 or getObjectAt(self.x,self.y) != 0 or getAgentAt(self.x,self.y) != 0:
            self.x = randint(0,getWorldWidth()-1)
            self.y = randint(0,getWorldHeight()-1)
        setAgentAt(self.x,self.y,self.type)
        return

    def getPosition(self):
        return (self.x,self.y)

    def changerImage(self, imageId):
        if self.alive:
            self.type = imageId

    def changerOrientation(self, image_nord:int, image_sud:int, image_est:int, image_ouest:int):
        # changement d'orientation au hasard
        if random() < 0.3: 
            self.orientation = (self.orientation + 1) % 4
        elif random() < 0.1:
            self.orientation = (self.orientation - 1 + 4) % 4

        match self.orientation:
            case 0: # nord
                self.changerImage(image_nord)
            case 1: # est
                self.changerImage(image_est)        
            case 2: # sud
                self.changerImage(image_sud)
            case 3: # ouest
                self.changerImage(image_ouest)
    
    def estAdulte(self):
        # print(self.age>=10)
        return self.age>=20
    
    def move(self, image_bebe:int, nord:int, sud:int, est:int, ouest:int):
        # les morts et les petits ne bougent pas
        if not self.alive :
            setAgentAt(self.x,self.y,noAgentId) # precaution
            return
        elif self.type == image_bebe :
            return

        x_new = self.x
        y_new = self.y

        # changement d'orientation au hasard
        self.changerOrientation(nord, sud, est, ouest)

        # MAJ position de l'agent (depend de l'orientation)
        match self.orientation:
            case 0: # nord	
                y_new = (self.y - 1 + getWorldHeight()) % getWorldHeight()
            case 1: # est
                x_new = (self.x + 1 + getWorldWidth()) % getWorldWidth()        
            case 2: # sud
                y_new = (self.y + 1 + getWorldHeight()) % getWorldHeight()
            case 3: # ouest
                x_new = (self.x - 1 + getWorldWidth()) % getWorldWidth()

        # mouvement si pas d'objet en face
        if getObjectAt(x_new,y_new) == 0: # dont move if collide with object (note that negative values means cell cannot be walked on)
            setAgentAt(self.x,self.y,noAgentId)
            self.x = x_new
            self.y = y_new 
            setAgentAt(self.x,self.y,self.type)
            self.energie -= 1
        
        if verbose == True:
            print ("agent of type ", str(self.type),"located at (",self.x,",",self.y,")")
        # self.energie-=1
        return

    def move2(self, xNew:int, yNew:int): # pour reproduction()
        if not self.alive:
            setAgentAt(self.x,self.y,noAgentId)
            return False
        success = False
        if getObjectAt( (xNew+worldWidth)%worldWidth , (yNew+worldHeight)%worldHeight ) == 0: # dont move if collide with object (note that negative values means cell cannot be walked on)
            setAgentAt(self.x, self.y, noAgentId)
            self.x = ( self.x + xNew + worldWidth ) % worldWidth
            self.y = ( self.y + yNew + worldHeight ) % worldHeight
            setAgentAt( self.x, self.y, self.type)
            success = True

        if verbose == True:
            if success == False:
                print ("agent of type ",str(self.type)," cannot move.")
            else:
                print ("agent of type ",str(self.type)," moved to (",self.x,",",self.y,")")
        return success

    def getType(self):
        return self.type

    def mort_mange(self, coord_pred):
        """retourne -1 si agent mort, 0 sinon"""
        if self.estAdulte() and self.alive and (self.x,self.y) == coord_pred:   
            self.alive=False
            setAgentAt(self.x,self.y,noAgentId)
            # print("mort")
            return -1
        return 0
    
    def mort_nat(self, p):
        """mort naturelle, selon une probabilite qui augmente avec l'age"""
        if self.alive and (self.age * p) > random():
            self.alive = False
            setAgentAt(self.x, self.y, noAgentId)
            return -1
        elif self.alive and (self.energie == 0.0):
            self.alive = False
            setAgentAt(self.x, self.y, noAgentId)
            return -1
        return 0

    def infection(self, nord_s, sud_s, est_s, ouest_s, nord_m, sud_m, est_m, ouest_m, nord_g, sud_g, est_g, ouest_g):
        if not self.estAdulte():
            return
        if (self.state==0 and random() < proba_maladie): # si sain
            self.state=1
            self.changerOrientation(nord_m, sud_m, est_m, ouest_m)
            self.cpt=10 
            # print("un agent infecté\n")
        elif (self.state==1): # si malade 
            if (self.cpt==0):
                self.state=2
                self.changerOrientation(nord_g, sud_g, est_g, ouest_g)
                self.cpt==10
            else:
                self.cpt-=1
        elif (self.state==2): # si "gueri"
            # la maladie fait mourir
            if random() < proba_maladie_mortelle:
                self.mort_mange(self.getPosition())
                return

            # la maladie ne fait pas mourir
            if (self.cpt==0):
                self.state=0
                self.changerOrientation(nord_s, sud_s, est_s, ouest_s)
            else:
                self.cpt-=1

    def infecte(self, coord_malade, nord, sud, est, ouest, nord_m, sud_m, est_m, ouest_m, nord_g, sud_g, est_g, ouest_g):
        if self.alive and self.state==0 and (self.x,self.y) == coord_malade:
            self.infection(nord, sud, est, ouest, nord_m, sud_m, est_m, ouest_m, nord_g, sud_g, est_g, ouest_g)

    def anniversaire(self, image_adulte):
        self.age +=1
        if self.estAdulte():
            self.changerImage(image_adulte)

    def step(self, heure, day, degre, image_bebe:int, nord, sud, est, ouest, nord_m, sud_m, est_m, ouest_m, nord_g, sud_g, est_g, ouest_g):
        """mise a jour : deplacement, infection spontannée, incrementation age et repos"""
        
        self.maj_repos(heure, day, degre)
        
        if not self.alive or self.repos:
            return
        self.anniversaire()
        
        match self.state:
            case 0: # sain
                self.move(image_bebe, nord, sud, est, ouest)
            case 1: # est
                self.move(image_bebe, nord_m, sud_m, est_m, ouest_m)        
            case 2: # sud
                self.move(image_bebe, nord_g, sud_g, est_g, ouest_g)
                
        self.infection(nord, sud, est, ouest, nord_m, sud_m, est_m, ouest_m, nord_g, sud_g, est_g, ouest_g)
        
    def reprod_possible(self):
        # place autour pour un petit ?
        a = getObjectAt((self.x - 1 + getWorldWidth()) % getWorldWidth() , self.y) == 0
        b = getObjectAt((self.x + 1 + getWorldWidth()) % getWorldWidth() , self.y) == 0
        c = getObjectAt(self.x, (self.y - 1 + getWorldHeight()) % getWorldHeight()) == 0 
        d = getObjectAt(self.x, (self.y + 1 + getWorldHeight()) % getWorldHeight()) == 0

        return self.estAdulte() and (a or b or c or d) and random() < 0.01 and self.state!=1 and (not self.repos)
    
    def maj_repos(self, heure, day, degre):
        
        if (heure >= 400) and (day > 1):
            self.repos = False
        elif heure >= 1000 and degre < 50:
            self.repos = True
