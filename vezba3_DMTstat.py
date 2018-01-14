import math
import numpy as np

class Tacka:
    br_t = 0
    def __str__(self):
        return "{}, polozaj x:{}m y:{}m, visina {}m".format(self.id, self.x, self.y, self.h)
    def __init__(self, x, y, h, id):
        self.x = x
        self.y = y
        self.h = h
        self.id = "tac" + str(id)
        Tacka.br_t += 1
    def rastojanjeDo(self,t):
        dx = self.x - t.x
        dy = self.y - t.y
        r = math.sqrt(dx ** 2 + dy ** 2)
        return r
    def interpolacija(self,t,r):
        if self.h == t.h:
            return self.h
        d = [0,self.rastojanjeDo(t)]
        h = [self.h,t.h]
        d1 = np.array(d)
        h1 = np.array(h)
        k = np.polyfit(d1, h1, 1)
        fit = np.poly1d(k)
        i = fit(r)
        return i
    def najblizaTacka(self, tacke):
        najbliza = 0
        rmin = 999999
        for t in tacke:
            if self != t and rmin > self.rastojanjeDo(t):
                rmin = self.rastojanjeDo(t)
                najbliza = t
        return najbliza

class Povrs:
    sr_vr_povrsi = 0
    mbb = [[0,0],[0,0]]
    br_tacaka = 0
    def __str__(self):
        return "\nPOVRS \nAnalizu vrsi: {} \nSrednja vrednost: {} m\nMBB: [x: {}-{}];[y: {}-{}]\nBroj tacaka: {}\n".format(self.analiticar, round(self.sr_vr_povrsi,2),self.mbb[0][0],self.mbb[0][1],self.mbb[1][0],self.mbb[1][1],Povrs.br_tacaka)
    def __init__(self, analiticar = "", tacke = list()):
        self.analiticar = analiticar
        self.tacke = tacke
    def dodajTacku(self, t):
        self.tacke.append(t)
        Povrs.br_tacaka = len(self.tacke)
    def srVrednostPovrsi(self):
        sum = 0
        for t in self.tacke:
            sum += t.h
        Povrs.sr_vr_povrsi = sum/len(self.tacke)
        return Povrs.sr_vr_povrsi
    def minBoundingBox(self):
        sum_x = 0
        sum_y = 0
        for t in self.tacke:
            sum_x += t.x
            sum_y += t.y
        #pocetne vrednosti parametara mbb su srednje vrednosti x i y koordinata
        Povrs.mbb[0][0] = sum_x/len(self.tacke)
        Povrs.mbb[0][1] = sum_x/len(self.tacke)
        Povrs.mbb[1][0] = sum_y/len(self.tacke)
        Povrs.mbb[1][1] = sum_y/len(self.tacke)
        for t in self.tacke:
            if t.x < Povrs.mbb[0][0]:
                Povrs.mbb[0][0] = t.x
            if t.x > Povrs.mbb[0][1]:
                Povrs.mbb[0][1] = t.x
            if t.y < Povrs.mbb[1][0]:
                Povrs.mbb[1][0] = t.y
            if t.y > Povrs.mbb[1][1]:
                Povrs.mbb[1][1] = t.y
        return Povrs.mbb
