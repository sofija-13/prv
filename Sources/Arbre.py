from core import *

class Arbre:
    
    def __init__(self, imageId, x, y):
        
        self.type = imageId
        self.x = x
        self.y = y
        self.timeburn = 0
        
        setObjectAt(self.x, self.y, imageId)
        pass
    
    def Arbre_rand(imageId): 
        
        """
        Arbe_rand() calcul des coordonnées x, y aléatoirement et fais appel au constructeur Arbre.

        Returns:
            Arbre: renvoie un Arbre au coordonnée x, y tiré aléatoirement.
        """
        
        x = rand.randint(0,getWorldWidth()-1)
        y = rand.randint(0,getWorldHeight()-1)
        
        while (getTerrainAt(x,y) != 0) or (getObjectAt(x,y) != 0):
            x = rand.randint(0,getWorldWidth()-1)
            y = rand.randint(0,getWorldHeight()-1)
        
        return Arbre(imageId, x, y)
    
    #méthode d'instance
    def setFire(self):
        
        """
        setFire() modifie l'état d'un arbre en brûle (état 2 de l'automate)
        """
        if self.type == treeId:
            self.type = burningTreeId
            setObjectAt(self.x, self.y, burningTreeId)
            self.timeburn = 50
        
    def setFire_proba(self, p_burn):
        
        if p_burn > rand.random(): 
            self.setFire()
            return True
        return False
    
    def toString(self):
        
        print("Coordonnée: (", self.x,", ", self.y, "), type: ", self.type, "timeburn: ", self.timeburn)        
    