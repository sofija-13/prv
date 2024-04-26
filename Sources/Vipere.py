from Agent import *

class Vipere(Agent):
    image_bebe : int = 1
    # sain
    nord_s = 27
    sud_s = 28
    est_s = 29
    ouest_s = 30
    # malade
    nord_m = 31
    sud_m = 32
    est_m = 33
    ouest_m = 34
    # gueri (pour l'instant, idem que sain)
    nord_g = 35
    sud_g = 36
    est_g = 37
    ouest_g = 38
    
    # nbVipere : int = 10
    
    def __init__(self, enfant:bool):
        super().__init__(Vipere.image_bebe, 0.00006, enfant)

    def reproduction(self):
        enfant = Vipere(True)
        if not enfant.move2(self.x+1, self.y):
            if not enfant.move2(self.x-1, self.y):
                if not enfant.move2(self.x, self.y+1):
                    enfant.move2(self.x, self.y-1)

        setAgentAt(enfant.x, enfant.y, enfant.type)
        return enfant

    def infecte(self, coord_malade):
        if self.alive and self.state==0 and (self.x,self.y) == coord_malade:
            super().infection(Vipere.nord_s, Vipere.sud_s, Vipere.est_s, Vipere.ouest_s, Vipere.nord_m, Vipere.sud_m, Vipere.est_m, Vipere.ouest_m, Vipere.nord_g, Vipere.sud_g, Vipere.est_g, Vipere.ouest_g)

    def anniversaire(self):
        super().anniversaire(Vipere.est_s)

    def step(self, heure, day, degre):
        super().step(heure, day, degre, Vipere.image_bebe, Vipere.nord_s, Vipere.sud_s, Vipere.est_s, Vipere.ouest_s, Vipere.nord_m, Vipere.sud_m, Vipere.est_m, Vipere.ouest_m, Vipere.nord_g, Vipere.sud_g, Vipere.est_g, Vipere.ouest_g)
