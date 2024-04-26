from Agent import *

class Renard(Agent):
    image_bebe : int = 14
    # sain
    nord_s = 15
    sud_s = 16
    est_s = 17
    ouest_s = 18
    # malade
    nord_m = 19
    sud_m = 20
    est_m = 21
    ouest_m = 22
    # gueri (pour l'instant, idem que sain)
    nord_g = 23
    sud_g = 24
    est_g = 25
    ouest_g = 26
    

    def __init__(self, enfant:bool):
        super().__init__(Renard.image_bebe, 0.00004, enfant)
        
        self.chasse : bool = False

    def reproduction(self):
        enfant = Renard(True)
        if not enfant.move2(self.x+1, self.y):
            if not enfant.move2(self.x-1, self.y):
                if not enfant.move2(self.x, self.y+1):
                    enfant.move2(self.x, self.y-1)
        setAgentAt(enfant.x, enfant.y, enfant.type)
        return enfant
    
    def proie_plus_proche(self, l_poule):
        
        """Return la poule la plus proche du renard comme une cible"""
        
        x = l_poule[0].x
        y = l_poule[0].y
        print(x, y)
        dist_min = math.sqrt((x - self.x)**2 + (y - self.y)**2)
        res_poule = l_poule[0]
        
        for p in l_poule[1:]:
            if p.alive == True and math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2) < dist_min:
                x = p.x
                y = p.y
                dist_min = math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)
                res_poule = p
        return p
    
    def mange_chasse(self, poule):
        
        global nbPoule
        
        xp,yp = poule.x, poule.y
        
        if xp == self.x and yp == self.y:
            self.energie += poule.energie % 100
            nbPoule += poule.mort_mange(self.x, self.y)
            if self.energie >= 75:
                self.chasse = False
                return
        elif xp < self.x:
            pass

    def infecte(self, coord_malade):
        if self.alive and self.state==0 and (self.x,self.y) == coord_malade:
            super().infection(Renard.nord_s, Renard.sud_s, Renard.est_s, Renard.ouest_s, Renard.nord_m, Renard.sud_m, Renard.est_m, Renard.ouest_m, Renard.nord_g, Renard.sud_g, Renard.est_g, Renard.ouest_g)

    def anniversaire(self):
        super().anniversaire(Renard.est_s)

    def step(self, heure, day, degre):
        super().step(heure, day, degre, Renard.image_bebe, Renard.nord_s, Renard.sud_s, Renard.est_s, Renard.ouest_s, Renard.nord_m, Renard.sud_m, Renard.est_m, Renard.ouest_m, Renard.nord_g, Renard.sud_g, Renard.est_g, Renard.ouest_g)