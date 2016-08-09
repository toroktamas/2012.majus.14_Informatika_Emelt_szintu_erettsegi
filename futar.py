#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""2012.majus.14 Informatika emeltszintu erettsegi megoldads Python programozasi nyelvben. """
"""1.feladat adat beolvasas amit en szotarba gondoltam. Ami igy nezne ki:
ut={sorszam{
"Het napja": 1
"kiszallitas szama": 1
"fuvar tavolsag":12
"Fizetendo osszeg":1400ft
 }
}
"""
from operator import itemgetter

def fizetes(uthossza):
    if uthossza in [1,2]:
        fizetendo = 500
    elif uthossza in [3, 4, 5]:
        fizetendo = 700
    elif uthossza in [6, 7, 8, 9, 10]:
        fizetendo = 900
    elif uthossza in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
        fizetendo = 1400
    elif uthossza in [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]:
        fizetendo = 2000
    else:
        fizetendo = "Nem jo adat"
    
    return fizetendo


n = 0
ut = {}
with open("tavok.txt","rt+",encoding="utf-8") as f:
    for s in f:
        sor = s.replace("\n","").split(" ")
        n = (str(sor[0])+" "+str(sor[1]))
        ut[n]={}
        ut[n]["Het napja"] = int(sor[0])
        ut[n]["Kiszallitas szama"] = int(sor[1])
        ut[n]["Fuvar tavolsag"] = int(sor[2])
        ut[n]["Fizetendo osszeg"] = fizetes(int(sor[2]))
#print(ut)
print("2. feladat")
"""Ki kell irni a het elso utjanak hosszat. Figyelni kell ha nincs 1 es az allomanyan akkor 2 est kell kiirni. """
nap = []
for a in ut.values():
    nap.append(int(a["Het napja"]))
for g in ut.values():
    if g['Het napja'] == min(nap) and g['Kiszallitas szama'] == 1:            
        print("A het elso napjanak elos utjanak hossza: {} kilometer".format(g['Fuvar tavolsag']))

print("3. feladat")
"""Kepernyore kiiratni hogy mekkora volt az utolso ut a heten kmerben. """
utolso_ut = []
for e in ut.values():
    if e['Het napja'] == max(nap):
        utolso_ut.append(int(e['Kiszallitas szama']))

for d in ut.values():
    if d["Het napja"] == int(max(nap)) and d['Kiszallitas szama'] == int(max(utolso_ut)):
        print("A het utolso napjanak az utolso szallitasan:{} hosszu volt az ut kilometerben.".format(d["Fuvar tavolsag"]))


print("4. feladat")
""" Ki kell irni a kepernyore hogy a futar melyik nap nem dolgozott."""
het_napjai = list(range(1,8))
for a in het_napjai:
    if a not in nap:
        print("{} napon nem dolgozott a futar.".format(a))

print("5. feladat")
"""Kepernyore kell irni hogy melyik nap volt a legtobb fuvar."""
fuvar_szam = []
for a in ut.values():
    fuvar_szam.append(a['Kiszallitas szama'])
for d in ut.values():
    if d["Kiszallitas szama"] == max(fuvar_szam):
        print("{} napon volt a legtobb kiszallitas.".format(d['Het napja']))

print("6. feladat")
"""Ki kell szamolni hogy egyes napokon hany km-ert kellett tekenie.Ezt ez szotar segjtsegevel gondoltam megoldani.
Ami a kovetkezo keppen nezne ki:
km={
    1:(Megtett km-er)
    2:(Megtett km-er)
}
"""
km = {}
for ad in ut.values():
    napok = ad["Het napja"]
    if napok not in km:
        km[napok] = 0
        km[napok] += ad["Fuvar tavolsag"]
    else:
        km[napok] += ad["Fuvar tavolsag"]

for a in het_napjai:
    if a not in nap:
        km[a] = 0

for k, v in km.items():
    print("{0} nap: {1} km".format(k,v))
    

print("7. feladat")
"""Be kell kerni a felhasznalotol egy tetszoleges ut hosszt es meg kell hatarozni mennyit kell fizetni."""
bekeres = int(input("Kerem adjon meg egy tetszoleges hosszu utat: "))
print("{0} kell fizetni {1} ennyi utert".format(fizetes(bekeres), bekeres))

print("8. feladat")
"""Meg kell hatarozni minden ut ellen erteket.Es ki kell irni a dijazas.txt--fajlba.Sorrendben. """
with open("dijazas.txt","wt",encoding="utf-8") as h:
    for v in sorted(ut.values(), key=lambda v:v["Het napja"]*100+v["Kiszallitas szama"]):   
        h.write("{0}.nap {1}. ut: {2} Ft \n".format(v["Het napja"], v["Kiszallitas szama"], v["Fizetendo osszeg"]))



print("9.feladat")
"""Meg kell hatarozni hogy a futar mennyi penzt kap a munkajaert a heten. """
osszeg = 0
for a in ut.values():
    osszeg+=a["Fizetendo osszeg"]
print("Osszesen:{} ennyi penzt kap a futar a heti kiszallitasokert.".format(osszeg))