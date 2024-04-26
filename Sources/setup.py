import pygame
from pygame.locals import *
import random as rand
import math

### ### ### ### ### ### ### ### 
###                         ###
### PARAMETRES: simulation  ###
###                         ###
### ### ### ### ### ### ### ### 

# all values are for initialisation. May change during runtime.
nbTrees : int = rand.randint(10, 25)
nbBurningTrees : int = 0 #15
heure = 0
degre = 25 #25 #-5 #49
day = 1

nbPoule : int = 12
nbRenard : int = 8
nbVipere : int = 5

# all probabilities variable
proba_maladie = 0.01
proba_maladie_mortelle = 0.3
p_burn : float = 0.0001 
p_grow : float = 0.0001

### ### ### ### ### ### ### ###
###                         ###
### PARAMETRES : rendering  ###
###                         ###
### ### ### ### ### ### ### ### 

# display screen dimensions
screenWidth : int = 1400 #1400 #930
screenHeight : int = 640 #900

# world dimensions (ie. nb of cells in total)
worldWidth : int = 32 #64
worldHeight : int = 32 #64

# set surface of displayed tiles (ie. nb of cells that are rendered) -- must be superior to worldWidth and worldHeight
viewWidth : int = 32 #32
viewHeight : int = 32 #32

scaleMultiplier : int = 0.25 # re-scaling of loaded images

objectMapLevels : int = 8 # number of levels for the objectMap. This determines how many objects you can pile upon one another.

# set scope of displayed tiles
xViewOffset : int = 0
yViewOffset : int = 0

addNoise : bool = False

maxFps : int  = 60 # set up maximum number of frames-per-second

verbose : bool = False # display message in console on/off
verboseFps : bool = True # display FPS every once in a while


### ### ### ### ### ### ### ### 
###                         ###
### Setting up Pygame/SDL   ###
###                         ###
### ### ### ### ### ### ### ### 

pygame.init()
#pygame.key.set_repeat(5,5)
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((screenWidth, screenHeight))#, DOUBLEBUF)
pygame.display.set_caption('PRV')
