from vezba3_Osoba import Osoba, Djak, Zaposleni, Datum

osoba = 1
djak = 1
zaposleni = 1
osobe = []
#kreirati MINIMUM jednog djaka i jednog zaposlenog
#test
o1 = Osoba("Marko", "Markovic", 1,1,2000, "Zahumska")
d1 = Djak("Stefan", "Stefanovic", 2,2,2002, "Carina", "Dimitrija Dragovica", "1-1", 2017)
z1 = Zaposleni("Jovan", "Jovanovic", 5,5,1995, "Podina", "Energo-projekt", "geometar")
osobe.append(o1)
osobe.append(d1)
osobe.append(z1)

m = input("Da li zelis da uneses Osobu(o), Djaka(d) ili Zaposlenog(z)? ")
while m == "o" or "d" or "z":
    if m != "o" or "d" or "z":
        dalje = input("Da li zelis da uneses novu osoba? (da/ne): ")
        if dalje == "ne":
            break
        elif dalje == "da":
            m = input("Da li zelis da uneses Osobu(o), Djaka(d) ili Zaposlenog(z)? ")
    i = input("Unesi ime: ")
    p = input("Unesi prezime: ")
    datum = input("Unesi datum rodjenja (d.m.gggg): ")
    while True == True:
        if datum.split(".")[0].isnumeric() and datum.split(".")[1].isnumeric() and datum.split(".")[2].isnumeric():
            dan = int(datum.split(".")[0])
            mes = int(datum.split(".")[1])
            god = int(datum.split(".")[2])
            break
        else:
            datum = input("Unesi datum rodjenja (d.m.gggg): ")
    a = input("Unesi adresu osobe: ")
    if m == "o":
        locals()[m+str(osoba)] = Osoba(i ,p ,dan ,mes, god, a) #promenljiva je o1, o2, o3...
        osobe.append(locals()[m+str(osoba)])
        osoba+=1
    elif m == "d":
        s = input("Unesi naziv osnovne skole: ")
        o = input("Unesi odeljenje: ")
        g = input("Unesi godinu upisa (gggg): ")
        while True == True:
            if g.isnumeric():
                g = int(g)
                break
            else:
                g = input("Unesi godinu upisa (gggg): ")
        locals()[m+str(djak)] = Djak(i ,p ,dan ,mes, god, a, s, o, g) #promenljiva je d1, d2, d3...
        osobe.append(locals()[m+str(djak)])
        djak+=1
    elif m == "z":
        k = input("Unesi naziv kompanije gde zaposleni radi: ")
        d = input("Unesi njegov departman: ")
        locals()[m+str(zaposleni)] = Zaposleni(i ,p ,dan ,mes, god, a, k, d) #promenljiva je z1, z2, z3...
        osobe.append(locals()[m+str(zaposleni)])
        zaposleni+=1
    dalje = input("Da li zelis da uneses novu osoba? (da/ne): ")
    if dalje == "ne":
        break
    elif dalje == "da":
        m = input("Da li zelis da uneses Osobu(o), Djaka(d) ili Zaposlenog(z)? ")
print("----")
for o in osobe:
    print(o)
print("----")
d1.razred()
print("----")
a = "da"
while a == "da":
    d = input(z1.ime + " menja posao. Unesi datume pocetka i kraja radnog odnosa u firmi " + z1.kompanija + ". (d.m.gggg-d.m.gggg): ")
    d1 = int(d.split("-")[0].split(".")[0])
    m1 = int(d.split("-")[0].split(".")[1])
    g1 = int(d.split("-")[0].split(".")[2])
    d2 = int(d.split("-")[1].split(".")[0])
    m2 = int(d.split("-")[1].split(".")[1])
    g2 = int(d.split("-")[1].split(".")[2])
    z1.menjaPosao(d1,m1,g1,d2,m2,g2)
    if z1.kompanija=="nezaposlen":
        print(z1.ime + " je trenutno nezaposlen.")
        break
    else:
        a = input("Da li " + z1.ime + " zeli da menja posao? (da/ne): ")
        if a != "da":
            break
print(z1)
print("----")
rs = z1.radniStaz()
print("Duzina radnog staza osobe " + z1.ime + " je " + str(rs) + " meseca.")