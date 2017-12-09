#zadatak1
print("Здраво геоинформатичари!")
print("-----")

#zadatak2
x2 = int(input("Unesi neki ceo broj, x:"))
y2 = int(input("Unesi jos jedan ceo broj, y:"))
if y2 != 0:
    print("x =", x2)
    print("y =", y2)
    zbir = x2 + y2
    print("Zbir ova dva broja je " + str(zbir)+".")
    razlika = x2 - y2
    print("Razlika ova dva broja je " + str(razlika)+".")
    proizvod = x2 * y2
    print("Proizvod ova dva broja je " + str(proizvod)+".")
    cdeljenje = x2 // y2
    print("Rezultat celobrojnog deljenja ova dva broja je " + str(cdeljenje)+".")
    odeljenje = x2 % y2
    print("Ostatak deljenja ova dva broja je " + str(odeljenje)+".")
else:
    print("Brojevi x i y moraju biti razliciti od 0!")
print("-----")

#zadatak3
ugao1 = input("Unesi prvi ugao u obliku xx:xx:xx :")
ugao2 = input("Unesi drugi ugao u obliku xx:xx:xx :")
sep = ":"
st1 = int(ugao1.split(sep)[0])
m1 = int(ugao1.split(sep)[1])
se1 = float(ugao1.split(sep)[2])
st2 = int(ugao2.split(sep)[0])
m2 = int(ugao2.split(sep)[1])
se2 = float(ugao2.split(sep)[2])
u1 = st1 + m1/60 + se1/3600
u2 = st2 + m2/60 + se2/3600
if st1 < 360 and m1 < 60 and se1 < 60 and st2 < 360 and m2 < 60 and se2 < 60:
    if u1 > u2:
        razu = u1 - u2
    else:
        razu = u2 - u1
    print("Ugao koji formiraju ovi pravci je " + str(round(razu,4)) + ".")
else:
    print("Nepravilan unos uglova!")
print("-----")

#zadatak4
x4 = int(input("Unesi prvi cetvorocifreni broj:"))
y4 = int(input("Unesi drugi cetvorocifreni broj:"))
if 999<x4<10000 and 999<y4<10000:
    zbiry4 = 0
    zbirx4par = 0
    zbirx4npar = 0
    for i in range(0,4):
        j = i + 1
        locals()["y4" + str(j)] = int(str(y4)[i])
        zbiry4 += locals()["y4" + str(j)]
        locals()["x4" + str(j)] = int(str(x4)[i])
        if j%2 == 1:
            zbirx4npar += locals()["x4" + str(j)]
        else:
            zbirx4par += locals()["x4" + str(j)]
    print("Zbir svih cifara drugog broja je " + str(zbiry4) + ".")
    razlikax4 = zbirx4par - zbirx4npar
    print("Razlika zbira cifara na pozitivnim i negativnim mestima prvog broja je " + str(razlikax4) + ".")
else:
    print("Brojevi nisu cetvorocifreni!")
print("-----")

#zadatak5
x5 = int(input("Unesi petocifreni broj:"))
if 9999<x5<100000:
    max = 0
    for i in range(0, 5):
        a = int(str(x5)[i])
        if max < a:
            max = a
    print("Najveca cifra u ovom broju je " + str(max) + ".")
else:
    print("Broj nije petocifren!")
print("-----")

#zadatak6
import random, string
a6 = string.ascii_uppercase+"1234567890"
i=1
numbers = 0
while i < 6:
    a = random.choice(a6)
    print("Racunar je ucitao " + a + ".")
    if a.isnumeric():
        numbers += 1
    i+=1
print("Broj cifara je " + str(numbers) + ".")
print("-----")

#zadatak7
import math
def dist(x1,y1,x2,y2):
    dist = math.sqrt((x1 - x2)** 2 + (y1 - y2)**2)
    return dist
def area(str1,str2,str3):
    s = (str1+str2+str3)/2
    p = math.sqrt(s*(s-str1)*(s-str2)*(s-str3))
    return p

a = input("Unesi koordinate tacke A u obliku 'x,y':")
ax = float(a.split(",")[0])
ay = float(a.split(",")[1])
b = input("Unesi koordinate tacke B u obliku 'x,y':")
bx = float(b.split(",")[0])
by = float(b.split(",")[1])
c = input("Unesi koordinate tacke C u obliku 'x,y':")
cx = float(c.split(",")[0])
cy = float(c.split(",")[1])
m = input("Unesi koordinate tacke M u obliku 'x,y' i saznaj da li se nalazi u trouglu ABC:")
mx = float(m.split(",")[0])
my = float(m.split(",")[1])

strab = dist(ax,ay,bx,by)
strac = dist(ax,ay,cx,cy)
strbc = dist(bx,by,cx,cy)
stram = dist(ax,ay,mx,my)
strbm = dist(bx,by,mx,my)
strcm = dist(cx,cy,mx,my)
abc = area(strab,strac,strbc)
abm = area(strab,strbm,stram)
acm = area(strac,stram,strcm)
bcm = area(strbc,strbm,strcm)

if (abm+acm+bcm) > abc:
    print("M je van trougla!")
else:
    print("M je u trouglu!")
print("-----")

#zadatak8 - Pogodi broj
random = random.randint(0,100)
pok = 0
ime = input("Unesite svoje ime:")
n8 = int(input("Dobro, da pocnemo! Sta mislis, koji je broj kompjuter 'zamislio'?"))
if n8 == random:
    pok += 1
    print("Bravo! To je bilo fantasticno, iz prvog pokusaja! Kompjuter je zamislio broj",random,".")
else:
    while n8 != random:
        pok += 1
        if n8 < random:
            n8 = int(input("To je bilo blizu... Ipak, trebalo bi da povecas broj."))
        else:
            n8 = int(input("Zamalo! Ovaj put probaj da smanjis broj."))
    pok += 1
    print("Bravo",ime,"! Kompjuter je 'zamislio' broj",random,".")
    print("Trebalo ti je samo" , pok , "pokusaja.")