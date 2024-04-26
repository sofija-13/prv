from setup import *

### ### ### ### ### ### ### ### ### ### ### ###
###                                         ###
### CORE/USER: Image management fonctions   ###
###                                         ###
### ### ### ### ### ### ### ### ### ### ### ###


def loadImage(filename):
    global tileTotalWidthOriginal,tileTotalHeightOriginal,scaleMultiplier
    image = pygame.image.load(filename).convert_alpha()
    image = pygame.transform.scale(image, (int(tileTotalWidthOriginal*scaleMultiplier), int(tileTotalHeightOriginal*scaleMultiplier)))
    return image

def loadAllImages():
    global tileType, objectType, agentType

    tileType = []
    objectType = []
    agentType = []

    tileType.append(loadImage('Sources/assets/ext/isometric-blocks/PNG/Voxel tiles/grass_tile.png')) # grass
    tileType.append(loadImage('Sources/assets/ext/isometric-blocks/PNG/Platformer tiles/platformerTile_33.png')) # brick
    tileType.append(loadImage('Sources/assets/ext/isometric-blocks/PNG/Abstract tiles/abstractTile_12.png')) # blue grass (?)
    tileType.append(loadImage('Sources/assets/ext/isometric-blocks/PNG/Abstract tiles/abstractTile_09.png')) # grey brock
    tileType.append(loadImage('Sources/assets/basic111x128/Water.png')) # water block
    tileType.append(loadImage('Sources/assets/ext/isometric-blocks/PNG/Voxel tiles/voxelTile_01.png')) # desert block
    tileType.append(loadImage('Sources/assets/ext/isometric-blocks/PNG/Voxel tiles/voxelTile_02.png')) # snow block
    tileType.append(loadImage('Sources/assets/ext/isometric-blocks/PNG/Voxel tiles/voxelTile_07.png')) # ice block 
    tileType.append(loadImage('Sources/assets/ext/isometric-blocks/PNG/Voxel tiles/voxelTile_53.png')) # wet desert block
    
    objectType.append(None) # default -- never drawn
    objectType.append(loadImage('Sources/assets/test_visuels/chestnut-003.png')) # normal tree
    objectType.append(loadImage('Sources/assets/test_visuels/flametree.png')) # burning tree
    objectType.append(loadImage('Sources/assets/basic111x128/blockHuge_N_ret.png')) # construction block


    agentType.append(None) # default -- never drawn
    ### egg
    agentType.append(loadImage('Sources/assets/animaux/egg.xcf')) # egg 1

    ### ### poule ### ###
    # sain
    agentType.append(loadImage('Sources/assets/animaux/poule/animation/poule_nord.xcf')) # nord 2
    agentType.append(loadImage('Sources/assets/animaux/poule/animation/poule_sud.xcf')) # sud 3
    agentType.append(loadImage('Sources/assets/animaux/poule/animation/poule_est.xcf')) # est 4
    agentType.append(loadImage('Sources/assets/animaux/poule/animation/poule_ouest.xcf')) # ouest 5
    # malade
    agentType.append(loadImage('Sources/assets/animaux/poule/animation/poule_nord_m.xcf')) # nord_m 6
    agentType.append(loadImage('Sources/assets/animaux/poule/animation/poule_sud_m.xcf')) # sud_m 7
    agentType.append(loadImage('Sources/assets/animaux/poule/animation/poule_est_m.xcf')) # est_m 8
    agentType.append(loadImage('Sources/assets/animaux/poule/animation/poule_ouest_m.xcf')) # ouest_m 9
    # gueri (pour l'instant idem que sain)
    agentType.append(loadImage('Sources/assets/animaux/poule/animation/poule_nord.xcf')) # nord_g 10
    agentType.append(loadImage('Sources/assets/animaux/poule/animation/poule_sud.xcf')) # sud_g 11
    agentType.append(loadImage('Sources/assets/animaux/poule/animation/poule_est.xcf')) # est_g 12
    agentType.append(loadImage('Sources/assets/animaux/poule/animation/poule_ouest.xcf')) # ouest_g 13

    ### ### renard ### ###
    agentType.append(loadImage('Sources/assets/animaux/renard/renard_sain.xcf')) # renard_bebe 14
    # sain
    agentType.append(loadImage('Sources/assets/animaux/renard/animation/renard_nord.xcf')) # nord 15
    agentType.append(loadImage('Sources/assets/animaux/renard/animation/renard_sud.xcf')) # sud 16
    agentType.append(loadImage('Sources/assets/animaux/renard/animation/renard_est.xcf')) # est 17
    agentType.append(loadImage('Sources/assets/animaux/renard/animation/renard_ouest.xcf')) # ouest 18
    # malade
    agentType.append(loadImage('Sources/assets/animaux/renard/animation/renard_nord_m.xcf')) # nord_m 19
    agentType.append(loadImage('Sources/assets/animaux/renard/animation/renard_sud_m.xcf')) # sud_m 20
    agentType.append(loadImage('Sources/assets/animaux/renard/animation/renard_est_m.xcf')) # est_m 21
    agentType.append(loadImage('Sources/assets/animaux/renard/animation/renard_ouest_m.xcf')) # ouest_m 22
    # gueri (pour l'instant idem que sain)
    agentType.append(loadImage('Sources/assets/animaux/renard/animation/renard_nord.xcf')) # nord_g 23
    agentType.append(loadImage('Sources/assets/animaux/renard/animation/renard_sud.xcf')) # sud_g 24
    agentType.append(loadImage('Sources/assets/animaux/renard/animation/renard_est.xcf')) # est_g 25
    agentType.append(loadImage('Sources/assets/animaux/renard/animation/renard_ouest.xcf')) # ouest_g 26
    
    ### ### vipere ### ###
    # sain
    agentType.append(loadImage('Sources/assets/animaux/vipere/animation/vipere_nord.xcf')) # nord 27
    agentType.append(loadImage('Sources/assets/animaux/vipere/animation/vipere_sud.xcf')) # sud 28
    agentType.append(loadImage('Sources/assets/animaux/vipere/animation/vipere_est.xcf')) # est 29
    agentType.append(loadImage('Sources/assets/animaux/vipere/animation/vipere_ouest.xcf')) # ouest 30
    # malade
    agentType.append(loadImage('Sources/assets/animaux/vipere/animation/vipere_nord_m.xcf')) # nord_m 31
    agentType.append(loadImage('Sources/assets/animaux/vipere/animation/vipere_sud_m.xcf')) # sud_m 32
    agentType.append(loadImage('Sources/assets/animaux/vipere/animation/vipere_est_m.xcf')) # est_m 33
    agentType.append(loadImage('Sources/assets/animaux/vipere/animation/vipere_ouest_m.xcf')) # ouest_m 34
    # gueri (pour l'instant idem que sain)
    agentType.append(loadImage('Sources/assets/animaux/vipere/animation/vipere_nord.xcf')) # nord_g 35
    agentType.append(loadImage('Sources/assets/animaux/vipere/animation/vipere_sud.xcf')) # sud_g 36
    agentType.append(loadImage('Sources/assets/animaux/vipere/animation/vipere_est.xcf')) # est_g 37
    agentType.append(loadImage('Sources/assets/animaux/vipere/animation/vipere_ouest.xcf')) # ouest_g 38
    

def resetImages():
    global tileTotalWidth, tileTotalHeight, tileTotalWidthOriginal, tileTotalHeightOriginal, scaleMultiplier, heightMultiplier, tileVisibleHeight
    tileTotalWidth = tileTotalWidthOriginal * scaleMultiplier  # width of tile image, as stored in memory
    tileTotalHeight = tileTotalHeightOriginal * scaleMultiplier # height of tile image, as stored in memory
    tileVisibleHeight = tileVisibleHeightOriginal * scaleMultiplier # height "visible" part of the image, as stored in memory
    heightMultiplier = tileTotalHeight/2 # should be less than (or equal to) tileTotalHeight
    loadAllImages()
    return


### ### ### ### ### ### ### ### ###
###                             ###
### core : objects parameters   ###
###                             ###
### ### ### ### ### ### ### ### ###


# spritesheet-specific -- as stored on the disk ==> !!! here, assume 128x111 with 64 pixels upper-surface !!!
# Values will be updated *after* image loading and *before* display starts
tileTotalWidthOriginal : int = 111  # width of tile image
tileTotalHeightOriginal : int = 128 # height of tile image
tileVisibleHeightOriginal : int = 64 # height "visible" part of the image, i.e. top part without subterranean part

###

#tileType = []
# objectType = []
# agentType = []

noObjectId : int = 0
noAgentId : int = 0

grassId : int = 0
desertId : int = 5

treeId : int = 1
burningTreeId : int = 2

blockId : int = 3

###

# re-scale reference image size -- must be done *after* loading sprites
resetImages()

###

terrainMap = [x[:] for x in [[0] * worldWidth] * worldHeight]
heightMap  = [x[:] for x in [[0] * worldWidth] * worldHeight]
objectMap = [ [ [ 0 for i in range(worldWidth) ] for j in range(worldHeight) ] for k in range(objectMapLevels) ]
agentMap   = [x[:] for x in [[0] * worldWidth] * worldHeight]

###

# set initial position for display on screen
xScreenOffset = screenWidth/2 - tileTotalWidth/2
yScreenOffset = 3*tileTotalHeight # border. Could be 0.


### ### ### ### ### ### ### ### ###
###                             ###
###  CORE: get/set methods      ###
###                             ###
### ### ### ### ### ### ### ### ###

def displayWelcomeMessage():

    print ("=-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-=")
    print ("=-=                Poule Renard Vipere (a.k.a PRV)                  =-=")
    print ("=-=                                                                 =-=")
    print ("=-=                 Sofija GRANET & Nawad KARIHILA                  =-=")
    print ("=-=                                                                 =-=")
    print ("=-=   Heavily inspired by nicolas.bredeche@sorbonne-universite.fr   =-=")
    print ("=-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-=")

def getWorldWidth():
    return worldWidth

def getWorldHeight():
    return worldHeight

def getViewWidth():
    return viewWidth

def getViewHeight():
    return viewHeight

def getTerrainAt(x,y):
    return terrainMap[y][x]

def setTerrainAt(x,y,type):
    terrainMap[y][x] = type

def getHeightAt(x,y):
    return heightMap[y][x]

def setHeightAt(x,y,height):
    heightMap[y][x] = height

def getObjectAt(x,y,level=0):
    if level < objectMapLevels:
        return objectMap[level][y][x]
    else:
        print ("[ERROR] getObjectMap(.) -- Cannot return object. Level does not exist.")
        return 0

def setObjectAt(x,y,type,level=0): # negative values are possible: invisible but tangible objects (ie. no display, collision)
    if level < objectMapLevels:
        objectMap[level][y][x] = type
    else:
        print ("[ERROR] setObjectMap(.) -- Cannot set object. Level does not exist.")
        return 0

def getAgentAt(x,y):
    return agentMap[y][x]

def setAgentAt(x,y,type):
    agentMap[y][x] = type


### ### ### ### ### ### ###
###                     ###
###  CORE: rendering    ###
###                     ###
### ### ### ### ### ### ###

def render( it = 0 ):
    global xViewOffset, yViewOffset
        
    for y in range(getViewHeight()):
        for x in range(getViewWidth()):
            # assume: north-is-upper-right

            xTile = ( xViewOffset + x + getWorldWidth() ) % getWorldWidth()
            yTile = ( yViewOffset + y + getWorldHeight() ) % getWorldHeight()

            heightNoise = 0
            if addNoise == True: # add sinusoidal noise on height positions
                if it%int(math.pi*2*199) < int(math.pi*199):
                    # v1.
                    heightNoise = math.sin(it/23+yTile) * math.sin(it/7+xTile) * heightMultiplier/10 + math.cos(it/17+yTile+xTile) * math.cos(it/31+yTile) * heightMultiplier
                    heightNoise = math.sin(it/199) * heightNoise
                else:
                    # v2.
                    heightNoise = math.sin(it/13+yTile*19) * math.cos(it/17+xTile*41) * heightMultiplier
                    heightNoise = math.sin(it/199) * heightNoise

            height = getHeightAt( xTile , yTile ) * heightMultiplier + heightNoise

            xScreen = xScreenOffset + x * tileTotalWidth / 2 - y * tileTotalWidth / 2
            yScreen = yScreenOffset + y * tileVisibleHeight / 2 + x * tileVisibleHeight / 2 - height

            screen.blit( tileType[ getTerrainAt( xTile , yTile ) ] , (xScreen, yScreen)) # display terrain

            for level in range(objectMapLevels):
                if getObjectAt( xTile , yTile , level)  > 0: # object on terrain?
                    screen.blit( objectType[ getObjectAt( xTile , yTile, level) ] , (xScreen, yScreen - heightMultiplier*(level+1) ))

            if getAgentAt( xTile, yTile ) != 0: # agent on terrain?
                screen.blit( agentType[ getAgentAt( xTile, yTile ) ] , (xScreen, yScreen - heightMultiplier ))

    return
