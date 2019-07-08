import numpy as np

def ouverture(text):

    liste = []
    liste1 = []
    
    fichier = open(text, "r", encoding='cp850', errors='ignore')
    liste.append(str(fichier))

    none = ''

    #We clean file
    for i in fichier:
        i = i.split()

        #sometimes only the country is give rase it
        if len(i) <= 1:
            pass
        
        #sometimes only the sexe is give rase it
        elif i[0] == "m" or i[0] == "f":
            pass
        
        #recup only the name and the sexe into a new list
        else:
            if i[1] == "m":
                i[1] = 1
            elif i[1] == "f":
                i[1] = 0
            elif i[1] != "m" or i[1] != "f":
                none = True
            elif i[1] == "m,f":
                i[1] = "f"

            if none != True:
                prenom = [i for i in i[0]]
                liste1.append([prenom, i[1]])
            else:
                none = ''


    return liste1


def serialisation(liste):

    apahabet = {"a":0.1,
                "b":0.2,
                "c":0.3,
                "d":0.4,
                "e":0.5,
                "f":0.6,
                "g":0.7,
                "h":0.8,
                "i":0.9,
                "j":0.10,
                "k":0.11,
                "l":0.12,
                "m":0.13,
                "n":0.14,
                "o":0.15,
                "p":0.16,
                "q":0.17,
                "r":0.18,
                "s":0.19,
                "t":0.20,
                "u":0.21,
                "v":0.22,
                "w":0.23,
                "x":0.24,
                "y":0.25,
                "z":0.26}

    nouvelle_liste = []
    for i in liste:
        liste_ephemere = []
        for j in i[0]:
            for cle, valeur in apahabet.items():
                if j == cle:
                    liste_ephemere.append(valeur)
                    
        liste_ephemere  = sum(liste_ephemere)
        if i[1] == 0:
            liste_ephemere = - liste_ephemere
            
        nouvelle_liste.append(liste_ephemere)


    garcon = []
    fille = []

    for i in nouvelle_liste:
        if i < 0:
            fille.append(i)
        else:
            garcon.append(i)

        
    return garcon, fille


def matrice(garcon, fille):

    features = np.vstack([garcon])
    features1 = np.vstack([fille])

    c = 0
    for i in fille:
        c+=1

    garcon = garcon[:c]


    row = 5
    #row = c

    features = np.vstack([fille, garcon])
    targets = np.concatenate((np.zeros(row), np.zeros(row) + 1))

    print(targets)

    
    

if __name__ == "__main__":

    TEXT = 'prénom.txt'
    
    liste = ouverture(TEXT)
    garcon, fille = serialisation(liste)
    matrice(garcon, fille)
    































