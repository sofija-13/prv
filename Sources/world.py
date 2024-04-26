#from Agent import *
from Poule import *
from Renard import *
from Vipere import *
from Arbre import *
import random as rand
from setup import *

### ### ### ### ### ### ###
###                     ###
###  Initialise world   ###
###                     ###
### ### ### ### ### ### ###

#listes d'agents
poules : list[Poule] = []
renards : list[Renard] = []
viperes : list[Vipere] = []
arbre = []


def initWorld():
    global nbTrees, nbBurningTrees

    x_offset = 3
    y_offset = 3

    building2TerrainMap = [
    [ 0, 4, 4, 4, 4, 4, 0 ],
    [ 0, 4, 4, 4, 4, 4, 0 ],
    [ 0, 4, 4, 4, 4, 4, 0 ],
    [ 0, 4, 4, 4, 4, 4, 0 ],
    [ 0, 4, 4, 4, 4, 4, 0 ],
    [ 0, 4, 4, 4, 4, 4, 0 ],
    [ 0, 4, 4, 4, 4, 4, 0 ],
    [ 0, 4, 4, 4, 4, 4, 0 ],
    [ 0, 4, 4, 4, 4, 4, 0 ]
    ]

    x_offset = randint(0, getWorldWidth())
    y_offset = randint(0, getWorldHeight())
    
    for x in range(len(building2TerrainMap[0])):
        for y in range(len(building2TerrainMap)):
            setTerrainAt( (x+x_offset)%worldWidth, (y+y_offset)%worldHeight, building2TerrainMap[y][x] )
            setObjectAt( (x+x_offset)%worldWidth, (y+y_offset)%worldHeight, -1 ) # add a virtual object: not displayed, but used to forbid agent(s) to come here.

    for _ in range(nbTrees):
        arbre.append(Arbre.Arbre_rand(treeId))
    
### ### ### ### ###

def initAgents():
    
    for i in range(nbPoule):
        poules.append(Poule(False))

    for i in range(nbRenard):
        renards.append(Renard(False))

    for i in range(nbVipere):
        viperes.append(Vipere(False))

    return

### ### ### ### ###

def growingTree(it = 0): #fonction de 'reproduction' des arbres
    
    global nbTrees
    if it % (maxFps/100) == 0:
        for t in arbre:
            for neighbours in ((-1,0),(+1,0),(0,-1),(0,+1),(-1,-1),(-1,1),(1,-1),(1,1)):
                x = (t.x + neighbours[0] + worldWidth) % worldWidth
                y = (t.y + neighbours[1] + worldHeight) % worldHeight
                if (getObjectAt(x, y) == noObjectId) and (rand.random() < p_grow):
                    arbre.append(Arbre(treeId, x, y))
                    nbTrees += 1
              
def climat(heure):
    
    global degre, day
    
    match heure:#
        case 400: # 8 heures
            degre = degre + randint(-10, 10)
            pass
        case 600: # midi
            degre = degre + randint(-10, 10)
            pass
        case 1000: # 20 heures
            degre = degre + randint(-10, 10)
            pass
        case 0: # minuit
            degre = degre + randint(-10, 10)
            day += 1
            pass
        
def maj_heure():
    
    """
    L'heure est fixee avec les ticks horaires du processeur
    100 ticks correspondent à 2 heures
    1 journe vaut 1200 ticks soit environ 24 secondes
    """
    
    global heure
    
    heure = int((pygame.time.get_ticks() / 30) % 1200)
    
    if (heure > 400) and (heure < 800):
        pygame.draw.rect(screen, (179, 230, 255), (0, 0, screenWidth, screenHeight), 0)
    elif (heure > 800) and (heure < 1200):
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, screenWidth, screenHeight), 0)
    elif (heure > 0) and (heure < 400):
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, screenWidth, screenHeight), 0)

def stepWorld( it = 0 ):
    
    global degre, nbTrees, nbBurningTrees, heure, day, arbre
    fichier = open("Graphes/evol_arbre.csv", "a")

                
    for i in range(len(arbre)):
        tree = arbre[i]
        ## Si l'arbre a un voisin en feu, il brûle aussi
        if tree.type == treeId:
            # Selon le voisinage de Newman
            for neighbours in ((-1,0),(+1,0),(0,-1),(0,+1)):
                if getObjectAt((tree.x+neighbours[0]+worldWidth)%worldWidth,(tree.y+neighbours[1]+worldHeight)%worldHeight) == burningTreeId:
                    tree.setFire()
                    nbBurningTrees += 1
                    nbTrees -= 1
                    break
            ## Si il fait trop chaud l'arbre peu prendre feu  
            if degre >= 20:
                if tree.setFire_proba((p_burn)):
                    nbBurningTrees += 1
        ## Si l'arbre est en feu depuis 5 itérations il disparait
        elif tree.type == burningTreeId:
            if tree.timeburn == 0:
                setObjectAt(tree.x, tree.y, 0)
                arbre = arbre[:i] + arbre[i:]
                nbBurningTrees -= 1
            elif tree.timeburn > 0:
                arbre[i].timeburn -= 1
    
    ## Changement de la température 4 fois par jour
    climat(heure) 
    
    ## Apparition de la neige
    if degre < 0:
        for x in range(getWorldHeight()):
            for y in range(getWorldWidth()):
                if getTerrainAt(x, y) == 0:
                    setTerrainAt(x, y, 6) # snow block
                elif getTerrainAt(x, y) == 4: # water block
                    setTerrainAt(x, y, 7) # ice block
    elif degre > 5: # on revient au monde "normal"
        for x in range(getWorldHeight()):
            for y in range(getWorldWidth()):
                if getTerrainAt(x, y) == 6:
                    setTerrainAt(x, y, 0)
                elif getTerrainAt(x, y) == 7:
                    setTerrainAt(x, y, 4)
                    
    ## Point de bascule, la température monte tellement que tous brûle
    if degre >= 50:
        for tree in arbre:
            tree.setFire()
        for x in range(getWorldHeight()):
            for y in range(getWorldWidth()):
                if getTerrainAt(x, y) == 0:
                    setTerrainAt(x, y, 5) # block desert
                elif getTerrainAt(x, y) == 4: # si c'est le lac
                    setHeightAt(x, y, -1) # on descend d'un niveau d'altitude
                    setTerrainAt(x, y, 8) # wet desert block
    growingTree()
            
    # Ecriture dans fichier pour graphes
    fichier.write(str(it)+","+str(nbTrees)+","+str(nbBurningTrees)+"\n")
    fichier.close()
        

### ### ### ### ###

def regulation():
    """Si un type d'agent dépasse un certain seuil on retire des agents correspondant
       Dans le cas ou les agents sont en dessous d'un certain seuil on ajoute des agents"""
    
    global nbPoule, nbRenard, nbVipere, degre

    if degre >= 50:
        return
    
    i = 0
    
    ## Régulation des renards
    if nbRenard > 20:
        while not renards[i].alive:
            i = randint(0, nbRenard-1)
        # le renard choisi au hasard meurt
        nbRenard += renards[i].mort_mange(renards[i].getPosition())
        
    # magie : s'il ne reste plus qu'un seul renard, on en ajoute 
    elif nbRenard <= 2:
        while nbRenard < 5:
            renards.append(Renard(False))
            nbRenard += 1
            
    ## Régulation des poules
    if nbPoule > 25:
        while not poules[i].alive:
            i = randint(0, nbPoule-1)
        # la poule choisi au hasard meurt
        nbPoule += poules[i].mort_mange(poules[i].getPosition())
        
    # magie : s'il ne reste plus qu'une seule poule, on en ajoute  
    elif nbPoule <= 3:
        while nbPoule < 8:
            poules.append(Poule(False))
            nbPoule += 1
            
    ## Régulation de viperes
    if nbVipere > 15:
        while not viperes[i].alive:
            i = randint(0, nbVipere-1)
        # la vipere choisi au hasard meurt
        nbVipere += viperes[i].mort_mange(viperes[i].getPosition())
        
    # magie : s'il ne reste plus qu'une seule vipère, on en ajoute  
    elif nbVipere <= 1:
        while nbVipere < 5:
            viperes.append(Vipere(False))
            nbVipere += 1

def stepAgents( it = 0 ):
    global nbPoule, nbRenard, nbVipere, heure, day, degre
    fichier = open("Graphes/evol_pop.csv", "a")

    # move agent
    if it % (maxFps/10) == 0:

        shuffle(poules)
        for p in poules:
            # mort des viperes   
            for v in viperes:
                nbVipere += v.mort_mange(p.getPosition())
                    
            # infection des autres agents de la meme espece
            if p.state == 1:
                for pp in poules:
                    pp.infecte(p.getPosition())
			
            # mise a jour (deplacement, infection spontannée etc)
            p.step(heure, day, degre)
            
            # reproduction
            if p.reprod_possible() and degre < 50:
                poules.append(p.reproduction())
                nbPoule +=1

            # mort naturelle poule
            nbPoule += p.mort_nat(p.esperance_vie)
            
            # changement vers l'etat de repos
            if (heure >= 400) and (day >= 1):
                p.repos = False
            elif heure >= 1000 and degre < 50:
                p.repos = True

        shuffle(viperes)
        for v in viperes: 
            # mort des renards 
            for r in renards:
                nbRenard += r.mort_mange(v.getPosition())
                    
            # infection des autres agents de la meme espece
            if v.state == 1:
                for vv in viperes:
                    vv.infecte(v.getPosition())  

            # mise a jour (deplacement, infection spontannée etc)
            v.step(heure, day, degre)
                
            # reproduction
            if v.reprod_possible() and degre < 50:
                viperes.append(v.reproduction())
                nbVipere +=1

            # mort naturelle vipere
            nbVipere += v.mort_nat(v.esperance_vie)
            
            # changement vers l'etat de repos
            if (heure >= 400) and (day > 1): 
                v.repos = False
            elif heure >= 1000 and degre < 50: 
                v.repos = True
                    
        shuffle(renards)
        for r in renards:
            # mort des poules
            for p in poules:
                nbPoule += p.mort_mange(r.getPosition())
            # if r.energie <= 40:
            #     r.chasse = True
            #     r.mange_chasse(r.proie_plus_proche(poules))
                    
            # infection des autres agents de la meme espece
            if r.state == 1:
                for rr in renards:
                    rr.infecte(r.getPosition())
            
            # mise a jour (deplacement, infection spontannée etc)
            r.step(heure, day, degre)
            
            #reproduction
            if r.reprod_possible() and degre < 50:
                renards.append(r.reproduction()) 
                nbRenard +=1     
                
            # mort naturelle renard
            nbRenard += r.mort_nat(r.esperance_vie)

            # changement vers l'etat de repos
            if (heure >= 400) and (day > 1): 
                r.repos = False
            elif heure >= 1000 and degre < 50: 
                r.repos = True

        # regulation du nombre d'agents     
        #regulation()
    
    fichier.write(str(it)+","+str(nbPoule)+","+str(nbRenard)+","+str(nbVipere)+"\n")
    fichier.close()
    
    return