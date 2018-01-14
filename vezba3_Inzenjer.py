class Inzenjer:
    broj_inz = 0
    def __init__(self, ime, prezime, jmbg, licenca = "nema"):
        self._ime_inz = ime
        self._prezime_inz = prezime
        self._jmbg = jmbg
        self._licenca = licenca
        Inzenjer.broj_inz+=1
    def getIme(self):
        return self._ime_inz
    def setIme(self, ime):
        self._ime_inz = ime
    def getPrezime(self):
        return self._prezime_inz
    def setPrezime(self, prezime):
        self._prezime_inz = prezime
    def getJmbg(self):
        return self._jmbg
    def setJmbg(self, jmbg):
        self._jmbg = jmbg
    def getLicenca(self):
        return self._licenca
    def setLicenca(self, licenca):
        self._licenca = licenca
    def infoInzenjer(self):
        print("Inzenjer: {} {}, JMBG: {}, Licenca: {}".format(self.getIme(),self.getPrezime(),self.getJmbg(), self.getLicenca()))
    def infoLicenca(self):
        if self.getLicenca() == "nema":
            print("Inzenjer {} {} nema vazecu licencu.".format(self.getIme(), self.getPrezime()))
        else:
            print("Inzenjer {} {} ima licencu - {}.".format(self.getIme(), self.getPrezime(), self.getLicenca()))

print("Test: Inzenjer")
st_st = Inzenjer("Stefan", "Stamenkovic", 1102994, "licencaB")
st_st.infoInzenjer()
print("-----")

class GeodetskiInzenjer(Inzenjer):
    def __init__(self,ime,prezime,jmbg,licenca,staz):
        Inzenjer.__init__(self,ime,prezime,jmbg,licenca)
        self._radni_staz = staz
    def setStaz(self, staz):
        self._radni_staz = staz
    def getStaz(self):
        return self._radni_staz
    def infoGeoInzenjer(self):
        print("{}, Godina staza: {}".format(self.infoInzenjer(), self.getStaz()))
    def infoGeoInzenjer2(self): #Ova metoda radi regularno ali zahteva prekucavanje
        print("Inzenjer: {} {}, JMBG: {}, Licenca: {}, Godina staza: {}".format(self.getIme(), self.getPrezime(), self.getJmbg(), self.getLicenca(), self.getStaz()))

print("Test: Geodetski inzenjer")
ma_ma = GeodetskiInzenjer("Marko", "Markovic", 2203994, "licencaA", 2)
ma_ma.infoGeoInzenjer() #zasto ova metoda printuje inzenjer, pa u novom redu NONE i godine staza ?
ma_ma.infoLicenca()
print("-----")

class ElektrotehnickiInzenjer(Inzenjer):
    def __init__(self,ime,prezime,jmbg,licenca,br_proj):
        Inzenjer.__init__(self,ime,prezime,jmbg,licenca)
        self._broj_projekata = br_proj
    def setProjekti(self, br_proj):
        self._broj_projekata = br_proj
    def getProjekti(self):
        return self._broj_projekata
    def infoEtInzenjer(self):
        print("{}, Broj projekata: {}".format(self.infoInzenjer(),self.getProjekti()))
    def infoEtInzenjer2(self): #ne koristim
        print("Inzenjer: {} {}, JMBG: {}, Licenca: {}, Broj projekata: {}".format(self.getIme(), self.getPrezime(), self.getJmbg(), self.getLicenca(), self.getProjekti()))

print("Test: Elektrotehnicki inzenjer")
pe_jo = ElektrotehnickiInzenjer("Jovan", "Jovanovic", 1505005, "nema", 7)
pe_jo.infoEtInzenjer() #isto kao infoGeoInzenjer
pe_jo.infoLicenca()