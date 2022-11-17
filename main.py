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








######################################################################################################
#Misi
