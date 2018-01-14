import math
class Sfera:
    broj = 0
    @staticmethod
    def brojSfera():
        print("Broj kreiranih sfera je {}.".format(Sfera.broj))
        return Sfera.broj
    def __init__(self, poluprecnik = 1, x_centar = 0, y_centar = 0, z_centar = 0):
        self.poluprecnik = poluprecnik
        self.xCentar = x_centar
        self.yCentar = y_centar
        self.zCentar = z_centar
        Sfera.broj += 1
    def zapreminaLopte(self):
        v = 4*math.pi*(self.poluprecnik**3)/3
        print("Zapremina sfere je {}.".format(v))
        return v