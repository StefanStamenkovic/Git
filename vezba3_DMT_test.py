from vezba3_DMTstat import Tacka, Povrs

import random

ids = list(range(1000,10000))
p = Povrs("Stefan S")
#tacke mogu dobiti vrednost ID iz opsega 1000-9999, tako da je maksimalan broj tacaka 8999
n = int(input("Unesi broj tacaka terena:"))
while Tacka.br_t < n:
    #polozajnim koordinatama tacaka se dodeljuju random vrednosti od 0 do 100 m,
    #a visine od 100 do 200 m.
    tx = round(random.uniform(0,100),2)
    ty = round(random.uniform(0,100),2)
    th = round(random.uniform(100, 200),2)
    id = random.choice(ids)
    t = Tacka(tx, ty, th, id)
    ids.remove(id)
    print(t)
    p.dodajTacku(t)
p.srVrednostPovrsi()
p.minBoundingBox()
#podaci o povrsi
print(p)

#rastojanje
t1 = p.tacke[0]
najbliza = t1.najblizaTacka(p.tacke)
d = t1.rastojanjeDo(najbliza)
print("Tacki " + str(t1) + " najbliza je " + str(najbliza) + ".")

dh = t1.h - najbliza.h
print("Rastojanje od " + str(t1.id) + " do " + str(najbliza.id) + " je " + str(round(d,2)) + " metara, visinska razlika " + str(round(dh,2)) +".")
print("Vrsimo interpolaciju izmedju ovih tacaka.")
r = float(input("Unesi na kom rastojanju se nalazi interpolovana tacka od prve tacke (izmedju 0 i " + str(round(d,2)) + "): "))
i = t1.interpolacija(najbliza, r)
print ("Interpolovana vrednost u izabranoj tacki je " + str(round(i,2)) + " metara.")