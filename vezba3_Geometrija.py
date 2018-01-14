import math

class Tacka:
    def __str__(self):
        return ("T{%s,%s}" % (self.x, self.y))
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def x_pomeraj(self,novo_x):
        self.x = float(novo_x)
    def y_pomeraj(self,novo_y):
        self.y = float(novo_y)
    def rastojanjeDo(self,t):
        dx = self.x - t.x
        dy = self.y - t.y
        d = math.sqrt(dx ** 2 + dy ** 2)
        return d

class Duz:
    def __str__(self):
        return ("D: %s-%s" % (self.t_pocetna, self.t_krajnja))
    def __init__(self, t1, t2):
        self.t_pocetna = t1
        self.t_krajnja = t2
    def duzinaDuzi(self):
        duzina = self.t_pocetna.rastojanjeDo(self.t_krajnja)
        return duzina
    def duzInfo(self):
        print("{};\nduzina: {};\n".format(self, self.duzinaDuzi()))