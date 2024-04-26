from Agent import *

class Poule(Agent):
    image_bebe : int = 1
    # sain
    nord_s = 2
    sud_s = 3
    est_s = 4
    ouest_s = 5
    # malade
    nord_m = 6
    sud_m = 7
    est_m = 8
    ouest_m = 9
    # gueri (pour l'instant, idem que sain)
    nord_g = 10
    sud_g = 11
    est_g = 12
    ouest_g = 13
    
    # nbPoule = 10
    
    def __init__(self, enfant:bool):
        super().__init__(Poule.image_bebe, 0.00002, enfant)

    def reproduction(self):
        enfant = Poule(True)
        if not enfant.move2(self.x+1, self.y):
            if not enfant.move2(self.x-1, self.y):
                if not enfant.move2(self.x, self.y+1):
                    enfant.move2(self.x, self.y-1)
                    
        setAgentAt(enfant.x, enfant.y, enfant.type)
        # Poule.nbPoule += 1
        return enfant

    def infecte(self, coord_malade):
        if self.alive and self.state==0 and (self.x,self.y) == coord_malade:
            super().infection(Poule.nord_s, Poule.sud_s, Poule.est_s, Poule.ouest_s, Poule.nord_m, Poule.sud_m, Poule.est_m, Poule.ouest_m, Poule.nord_g, Poule.sud_g, Poule.est_g, Poule.ouest_g)

    def anniversaire(self):
        super().anniversaire(Poule.est_s)

    def step(self, heure, day, degre):
        super().step(heure, day, degre, Poule.image_bebe, Poule.nord_s, Poule.sud_s, Poule.est_s, Poule.ouest_s, Poule.nord_m, Poule.sud_m, Poule.est_m, Poule.ouest_m, Poule.nord_g, Poule.sud_g, Poule.est_g, Poule.ouest_g)

