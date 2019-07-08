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

    alpahabet = {"a":1,
                "b":2,
                "c":3,
                "d":4,
                "e":5,
                "f":6,
                "g":7,
                "h":8,
                "i":9,
                "j":10,
                "k":11,
                "l":12,
                "m":13,
                "n":14,
                "o":15,
                "p":16,
                "q":17,
                "r":18,
                "s":19,
                "t":20,
                "u":21,
                "v":22,
                "w":23,
                "x":24,
                "y":25,
                "z":26}



    nouvelle_liste = []
    for i in liste:
        
        eph = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,0]

        for j in i[0]:
            for cle, valeur in alpahabet.items():
                if j == cle:
                    eph[valeur - 1] = 1

        eph[26] = i[1]
                    
        nouvelle_liste.append(eph)
            




    


        















  
    

if __name__ == "__main__":

    TEXT = 'prénom.txt'
    
    liste = ouverture(TEXT)
    serialisation(liste)

    































