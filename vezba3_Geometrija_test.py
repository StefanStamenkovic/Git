from vezba3_Geometrija import Tacka, Duz

def kreirajDuz(xt1, yt1, xt2, yt2):
    p = Tacka(xt1, yt1)
    k = Tacka(xt2, yt2)
    d = Duz(p, k)
    return d

def isFloat(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

duzi = []
t1 = 0
t2 = 0
p = input("Unesi koordinate pocetne tacke duzi u obliku 'x,y':")
while True==True:
    if len(p.split(","))==2:
        px = p.split(",")[0]
        py = p.split(",")[1]
        if isFloat(px) and isFloat(py) == True:
            t1 = Tacka(float(px), float(py))
            break
        else:
            p = input("Unesi koordinate pocetne tacke duzi u obliku 'x,y':")
    else:
        p = input("Unesi koordinate pocetne tacke duzi u obliku 'x,y':")
k = input("Unesi koordinate krajnje tacke duzi u obliku 'x,y':")
while True==True:
    if len(k.split(","))==2:
        kx = k.split(",")[0]
        ky = k.split(",")[1]
        if isFloat(kx) and isFloat(ky) == True:
            t2 = Tacka(float(kx), float(ky))
            break
        else:
            k = input("Unesi koordinate krajnje tacke duzi u obliku 'x,y':")
    else:
        k = input("Unesi koordinate krajnje tacke duzi u obliku 'x,y':")

duz1 = Duz(t1,t2)
duzi.append(duz1)

duz2 = 0
t = input("Unesi koordinate pocetne i krajnje tacke duzi u obliku 'px,py,kx,ky':")
while True==True:
    if len(t.split(","))==4:
        px, py, kx, ky = t.split(",")[0], t.split(",")[1], t.split(",")[2], t.split(",")[3]
        if isFloat(px) and isFloat(py) and isFloat(kx) and isFloat(ky) == True:
            duz2 = kreirajDuz(float(px),float(py),float(kx),float(ky))
            break
        else:
            t = input("Unesi koordinate pocetne i krajnje tacke duzi u obliku 'px,py,kx,ky':")
    else:
        t = input("Unesi koordinate pocetne i krajnje tacke duzi u obliku 'px,py,kx,ky':")
print("-----")
duzi.append(duz2)
for d in duzi:
    d.duzInfo()

dxk = input("Unesi vrednost za koju zelis izmeniti x koordinatu krajnje tacke prve duzi (dx):")
dyk = input("Unesi vrednost za koju zelis izmeniti y koordinatu krajnje tacke prve duzi (dy):")
while True == True:
    if isFloat(dxk) and isFloat(dyk):
        dxk = float(dxk)
        dyk = float(dyk)
        break
    else:
        dxk = input("Unesi vrednost za koju zelis izmeniti x koordinatu krajnje tacke (dx):")
        dyk = input("Unesi vrednost za koju zelis izmeniti y koordinatu krajnje tacke (dy):")

duz1.t_krajnja.x_pomeraj(duz1.t_krajnja.x+dxk)
duz1.t_krajnja.y_pomeraj(duz1.t_krajnja.y+dyk)
print("-----")
for d in duzi:
    d.duzInfo()