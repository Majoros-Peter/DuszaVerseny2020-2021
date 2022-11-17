import os, shutil

def Commit(eleresi_ut):
    mappa = os.listdir(eleresi_ut)
    dusza_mappa = os.listdir(eleresi_ut+"/.dusza/")
    commit = eleresi_ut+"/.dusza/"+Hanyadik(dusza_mappa)+".commit"

    os.mkdir(commit)

    for fajl in mappa:
        if fajl != ".dusza" and os.path.isfile(eleresi_ut+"/"+fajl): shutil.copyfile(eleresi_ut+"/"+fajl, commit+"/"+fajl)
        else: continue

def Hanyadik(mappa):
    szam = 0

    for almappa in mappa:
        if almappa.split(".")[1] == "commit" and int(almappa.split(".")[0]) > szam:
            szam = int(almappa.split(".")[0])

    return str(szam+1)

######################################################################################################
#Józsi
'''
import os
import datetime
import time


def kesleltetes(idokoz=0.5, egysegekszama=5):
    for toltottseg in range(egysegekszama+1):
        print("■" * toltottseg + "□" * (egysegekszama - toltottseg))
        time.sleep(idokoz)

def fajl_beolvasas():
    folder = os.listdir()  # Eltárolja az adott mappában lévő összes fájlt

    for fajl in folder:
        if os.path.exists("commit details.txt"):  # Kitörli a 'commit details' nevű fájlt
            os.remove("commit details.txt")
            kesleltetes()
            print("\nFájl törölve\n")
        if fajl != "commit details.txt" and fajl.split(".")[1] != "py":  # A .py kiterjesztésű fájlokat ignorálja
            fajl_ = open(fajl)
            fajlok.append(Fajl(fajl, [datetime.datetime.fromtimestamp(os.path.getmtime(fajl)),datetime.datetime.fromtimestamp(os.path.getctime(fajl))], fajl_.read(),os.getlogin()))
            # Létrehoz egy objektumot minden fájlra és hozzáadja a fajlok listához


class Fajl:
    def __init__(self, nev, ido, szoveg, szerzo):
        self.nev = nev  # Fájl neve
        self.ido = ido  # Fájl létrehozásának és módosításának ideje
        self.szoveg = szoveg  # Txt fájl tartalma
        self.szerzo = szerzo  # A fájl szerzője
        self.letrehozas_datuma = self.ido_konvertalas(self.ido[1])
        self.modositas_datuma = self.ido_konvertalas(self.ido[0])
        self.commit_details_letrehozas("aaa")

    def ido_konvertalas(self, ido):
        ev = ido.year
        honap = ido.month
        nap = ido.day
        ora = ido.hour
        perc = ido.minute
        masodperc = ido.second
        return f"{ev}.{honap}.{nap} {ora}.{perc}.{masodperc}"

    def commit_details_letrehozas(self, leiras):
        f = open("commit details.txt", "x")
        f.close()
        kesleltetes()
        f = open("commit details.txt", "w")
        f.write(f"Szulo: {self.nev}\nSzerzo: {self.szerzo}\nDatum: {self.letrehozas_datuma}\nCommit leiras: {leiras}")
        f.close()


fajlok = []  # Tárolja az összes fájlt
fajl_beolvasas()

print("\nVÉGE\n")
'''





######################################################################################################
#Misi
