import math

class Osoba:
    def __str__(self):
        return "LICNA KARTA \nIme i prezime: %s %s \nDatum rodjenja: %s \nAdresa: %s\n" % (
        self.ime, self.prezime, self.d_rodjenja, self.adresa)
    def __init__(self, ime, prezime, d, m, g, adresa):
        self.ime = ime
        self.prezime = prezime
        self.d_rodjenja = Datum(d,m,g)
        self.adresa = adresa

class Djak(Osoba):
    def __str__(self):
        return "DJACKA KNJIZICA \nIme i prezime: %s %s \nDatum rodjenja: %s \nAdresa: %s \nNaziv skole: %s \nOdeljenje: %s \nGodina upisa: %s\n" \
               % (self.ime, self.prezime, self.d_rodjenja, self.adresa, self.naziv_skole, self.odeljenje, self.god_upisa)
    def __init__(self, ime, prezime, d, m, g, adresa, skola, odeljenje, god_upisa):
        Osoba.__init__(self, ime, prezime, d, m, g, adresa)
        self.naziv_skole = skola
        self.odeljenje = odeljenje
        self.god_upisa = god_upisa #int!
    def razred(self):
        g = 2018 - self.god_upisa #uzima se da je trenutno 2018. godina
        if g <= 8:
            print(self.ime + " ide u " + str(g) + " razred.")
        elif g > 8:
            print(self.ime + " je obnovio godinu " + str(g-8) + " puta.")

class Zaposleni(Osoba):
    def __str__(self):
        return "RADNA KNJIZICA \nIme i prezime: %s %s \nDatum rodjenja: %s \nAdresa: %s \nZaposlen u: %s \nDepartman: %s \nIskustvo: \n%s\n" \
               % (self.ime, self.prezime, self.d_rodjenja, self.adresa, self.kompanija, self.departman, self.radnoIskustvo())
    def __init__(self, ime, prezime, d, m, g, adresa, kompanija, departman, radno_iskustvo = list()):
        Osoba.__init__(self, ime, prezime, d, m, g, adresa)
        self.kompanija = kompanija
        self.departman = departman
        self.radno_iskustvo = radno_iskustvo
    def menjaPosao(self,d1,m1,g1,d2,m2,g2):# 1 - radio od; 2 - radio do
        self.radno_iskustvo.append([self.kompanija,Datum(d1,m1,g1),Datum(d2,m2,g2)])
        a = input("Da li je nasao novi posao? da/ne: ")
        while True == True:
            if a == "da":
                p = input("Unesi naziv nove kompanije i departmana u kojoj je " + self.ime + " zaposlen. kompanija/departman: ")
                self.kompanija = p.split("/")[0]
                self.departman = p.split("/")[1]
                break
            elif a == "ne":
                self.kompanija = "nezaposlen"
                self.departman = "/"
                break
            else:
                a = input("Da li je nasao novi posao? da/ne: ")
    def radnoIskustvo(self):
        i = []
        for red in self.radno_iskustvo:
            i.append(red[0] + ", od " + str(red[1]) + " do " + str(red[2]) + ".")
        return i
    def radniStaz(self):
        sum = 0
        for i in self.radno_iskustvo:
            od = i[1]
            do = i[2]
            od_1900 = (od.godina-1900)*12*30 + od.mesec*30 + od.dan
            do_1900 = (do.godina-1900)*12*30 + do.mesec*30 + do.dan
            raz = do_1900 - od_1900
            sum += raz
        return math.floor(sum/30)

class Datum:
    def __str__(self):
        return "%s.%s.%s" % (self.dan, self.mesec, self.godina)
    def __init__(self, dan, mesec, godina):
        if 0 < dan <= 30 and 0 < mesec <= 12 and 1900 < godina < 2050:
            self.dan = int(dan)
            self.mesec = int(mesec)
            self.godina = int(godina)
        else:
            print("Pogresan unos datuma! {}.{}.{}".format(dan,mesec,godina))