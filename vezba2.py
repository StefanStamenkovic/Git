#zadatak1
niz1 = (1, 5, 3, 8, 4, 9, 2, 4, 6, 5)
def sumEven(niz):
    sumparni = 0
    for i in range(1,len(niz),2):
        sumparni += niz[i]
    print ("Suma parnih elemenata niza "+ str(niz) +" je "+ str(sumparni) + ".")
    return sumparni
sumEven(niz1)
print("-----")

#zadatak2
def sumElements(niz):
    sum = 0
    for i in range(0,len(niz)):
        sum += niz[i]
    print ("Suma elemenata niza "+ str(niz) +" je "+ str(sum) + ".")
    return sum
sumElements(niz1)
print("-----")

#zadatak3
def multElements(niz):
    mult = niz[0]
    for i in range(1,len(niz)):
        mult *= niz[i]
    print("Proizvod elemenata niza " + str(niz) + " je " + str(mult) + ".")
    return niz
multElements(niz1)
print("-----")

#zadatak4
niz2 = (2, 7, 9, 3, 7, 1 ,7, 6, 4, 8)
a4 = input("Korisnice, reci element kog niza da bude prvi? Za niz1 unesi 'p',a za niz2 unesi 'd':")
def mergeLists(a):
    noviniz = []
    if a == "p":
        for i in range(0, len(niz1)):
            noviniz.append(niz1[i])
            noviniz.append(niz2[i])
        print(noviniz)
    elif a == "d":
        for i in range(0, len(niz2)):
            noviniz.append(niz2[i])
            noviniz.append(niz1[i])
        print(noviniz)
    else:
        mergeLists(input("Pokusaj ponovo..."))
mergeLists(a4)
print("-----")

#zadatak5
a5 = input("Unesi recenicu:")
skup5 = set()
for i in range (0,len(a5)):
    s = set(a5[i])
    if s in skup5:
        pass
    else:
        skup5.add(a5[i])
print(skup5)
print("-----")

#zadatak6
import numpy as np
print("Fitovanje polinoma")
br_t = int(input("Unesi broj tacaka:"))
x = []
y = []
while isinstance(br_t, int):
    i = 1
    while i <= br_t:
        x.append(float(input("Unesi x koordinatu tacke " + str(i) + ":")))
        y.append(float(input("Unesi y koordinatu tacke " + str(i) + ":")))
        i+=1
    x1 = np.array(x)
    y1 = np.array(y)
    st_p = int(input("Unesi stepen polinoma:"))
    k = np.polyfit(x1, y1, st_p)
    fit = np.poly1d(k)
    print("Aproksimativna funkcija unetih tacaka: " , fit)
    break
else:
    br_t = int(input("Unesi broj tacaka:"))
print("-----")

#zadatak7
import random #uvoz biblioteke random
spil = list() #globalna promenljiva
#funkcije:
def formirajSpil():
    znak = ["karo", "herc", "tref", "pik"]
    for i in range(2, 15):
        for j in znak:
            n = (str(i) + "_" + j)
            spil.append(n)

def izvuciKartu():
    r = random.randrange(0, len(spil))
    k = spil[r]
    del spil[r]
    return k

def vrednostKarte(k):
    broj = k.split("_")[0]
    if int(broj) < 12:
        vrkarte = int(broj)
    elif 11 < int(broj):
        vrkarte = 10
    return vrkarte

def vrednostA(vr):
    print("Dobio si A (11), a trenutna vrednost tvojih karata je " + str(vr) + ".")
    a = int(input("Da li zelis da se on racuna kao 1 ili kao 11? ('1'/'11'):"))
    while a != 1 and a != 11:
        a = int(input("Da li zelis da se on racuna kao 1 ili kao 11? ('1'/'11'):"))
    if a == 1:
        v = 1
    elif a == 11:
        v = 11
    return v

def novaKarta():
    nk = izvuciKartu()
    vnk = vrednostKarte(nk)
    return vnk

#igra:
def blackJack():
    ime = input("Unesite svoje ime:")
    print("Zdravo, " + str(ime)+ ". Igramo igru Black Jack.")
    #formiranje spila karata
    formirajSpil()
    #izvlacenje karata
    k1 = izvuciKartu()
    #k1 = "11_tref"
    k2 = izvuciKartu()
    #pocetak igre
    print("Dobio si dve karte, to su: " + k1 + " i " +k2)
    #vrednost izvucenih karata
    v1 = vrednostKarte(k1)
    v2 = vrednostKarte(k2)
    #vrednost pocetnih karata u zavisnosti od izvucene kombinacije
    vr = 0
    if v1 != 11 and v2 != 11:
        vr = v1 + v2
    elif (v1 == 11 and v2 == 10) or (v1 == 10 and v2 == 11):
        vr = v1 + v2
        print("Bravo!!! Dobio si BlackJack jer je vrednost podeljenih karata " + str(vr) + "!")
        print("\nK R A J   I G R E")
        return
    elif v1 == 11 and v2 == 11:
        print("Dobio si A A! Obzirom da vrednost karata prelazi granicu, jedan A postaje 1.")
        v2 = 1
        vr = v1 + v2
    elif v1 == 11 or v2 == 11:
        vr = v1 + v2
        if v1 == 11:
            v1 = vrednostA(vr)
        elif v2 == 11:
            v2 = vrednostA(vr)
        vr = v1 + v2
    print("Trenutna vrednost tvojih karata je " + str(vr) + ".")
    a = input("Da li zelis da izvuces jos jednu kartu? ('da'/'ne'):")
    while a != "da" and a != "ne":
        a = input("Da li zelis da izvuces jos jednu kartu? ('da'/'ne'):")
    if a == "da":
        while a == "da":
            nk = izvuciKartu()
            vnk = vrednostKarte(nk)
            print("Dobio si " + str(nk) + ".")
            if vnk == 11:
                v = vrednostA(vr+vnk)
                vr += v
            else:
                vr += vnk
            if vr > 21:
                print("Izgubio siii... Vrednost karata je presla 21.")
                print("\nK R A J   I G R E")
                return
            print("Trenutna vrednost tvojih karata je " + str(vr) + ".")
            a = input("Da li zelis da izvuces jos jednu kartu? ('da'/'ne'):")
    elif a == "ne":
        print("Sledi deljenje karata dileru.")
    dk1 = izvuciKartu()
    dk2 = izvuciKartu()
    print("Diler je dobio karte " + str(dk1) + " i " + str(dk2) + ".")
    dv1 = vrednostKarte(dk1)
    dv2 = vrednostKarte(dk2)
    dvr = dv1 + dv2
    if (dv1 == 11 and dv2 == 10) or (dv1 == 10 and dv2 == 11):
        pass
    elif dv1 == 11 and dv2 == 11:
        dvr = 12
    elif dv1 == 11 or dv2 == 11:
        if dvr < 17 and dv1 == 11:
            dv1 = 1
        elif dvr < 17 and dv2 == 11:
            dv2 = 1
        dvr = dv1 + dv2
    print("Pocetna vrednost dilerovih karata je " + str(dvr) + ".")
    if dvr >= vr and dvr > 16:
        print("Diler je pobedio.")
        print("\nK R A J   I G R E")
        return
    while dvr < 16 or dvr < vr:
        dnk = izvuciKartu()
        dvnk = vrednostKarte(dnk)
        if dvr > 10 and dvnk == 11:
            dvnk = 1
        print("Diler je dobio " + str(dnk) + ".")
        dvr += dvnk
        print("Dilerova ruka je " + str(dvr) + ".")
        if dvr > 21:
            print("Dilerova ruka je presla 21, ti si pobednik!")
            print("\nK R A J   I G R E")
            return
        if dvr >= vr:
            print("Diler je pobedio.")
            print("\nK R A J   I G R E")
            return
    print("\nK R A J   I G R E")
blackJack()