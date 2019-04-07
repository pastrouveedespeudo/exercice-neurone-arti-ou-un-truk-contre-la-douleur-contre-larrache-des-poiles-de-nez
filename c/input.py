from traitement import *
from conteneur import *
from methode import *
import os


genre = {"masculin":0, "feminin":0}
A_f = [[],[],[],[],[],[],[],[],[],]
A_m = [[],[],[],[],[],[],[],[],[],]


class apprentissage1:

    def opération_pour_genre(self, texte):
        """découpage de phrase par pronom"""
        
        self.texte = texte
    
        liste = [[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[]]
        
        c = 0
        for phrase in self.texte:
            for mot in phrase:
                mot = mot.lower()
                for pronom in PRONOMS:
                    if mot == pronom:
                        c+=1
                liste[c].append(mot)

        liste2 = [i for i in liste if i != []]
    
        return liste2

    def opération_pour_le_genre2(self, texte):
        self.texte = texte

        liste = [[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[]]

        c = 0
        d = 0
        for phrase in self.texte:
            for mot in self.texte[c]:
                if mot == "je":
                    liste[d].append(self.texte[c])
                    d+=1

            c+=1

        liste2 = [i for i in liste if i != []]

        return liste2  


    def le_genre(self, texte):
        self.texte = texte
        fem = False
        genre = {"feminin":0, "masculin":0}

        for i in self.texte:
            for j in i[0]:
                path = "https://www.le-dictionnaire.com/definition/{}"
                path = path.format(j.lower())
                requete = requests.get(path)
                page = requete.content
                soup = BeautifulSoup(page, "html.parser")      
                propriete = soup.find("div", {"class":"defbox"})
                adjectif = str(propriete).find("Adjectif")
                if adjectif >= 0:
                    for marque_feminin in FEMININ:
                        nb = len(marque_feminin)
                        if j[-nb:] == marque_feminin:
                            fem = True


##                path = "http://www.les-verbes.com/conjuguer.php?verbe={}"
##                path = path.format(j.lower())
##                requete = requests.get(path)
##                page = requete.content
##
##                soup = BeautifulSoup(page, "html.parser")      
##                propriete = soup.find_all("span", {"class":"arial-12-gris"})
##                verbe = str(propriete).find("VERBE")
##                propriete = soup.find_all("span", {"class":"arial-12-gris"})
##                if verbe >= 0:
##                    if j[-1] == "ée" or j[-1] ==  "ie" or j[-1] ==  "ue":
##                        fem = True

        if fem == True:
            genre["feminin"] += 1
        else:
            genre["masculin"] += 1
                        
                    
     

        return genre
        


if __name__ == "__main__":

    #TEXT10, TEXT, TEXT1, TEXT2, TEXT3, TEXT4, TEXT5,TEXT6,
    #         TEXT7,TEXT8, TEXT9,
    #entrée = input("texte ?")
    listeTEXT = [TEXT11,TEXT12,TEXT13,TEXT14,TEXT16]
    
    apprentissage1 = apprentissage1()
    poidsPonctuation = poidsPonctuation()
    ecriture = ecriture()
    poidsTexte = poidsTexte()
    poidsMots = poidsMots()
    
    c = 10
    for i in listeTEXT:
        
        name = "requete{}.py".format(c)

        ecriture.ecriture0("#", name)
        ecriture.ecriture0(("liste numero : {}".format(str(c))), name)
        
        entrée = i
        entrée1 = "je suis très heureuse"

        #opération sur le texte
        
        opé = premiere_opération()


        #methode traitement de texte
        text = opé.trait_texte(entrée)
        phrases = opé.traitement_phrase(text)



        #methode genre
        genre = apprentissage1.opération_pour_genre(phrases)
        genre2 = apprentissage1.opération_pour_le_genre2(genre)
        a = apprentissage1.le_genre(genre2)

        if a["feminin"] == 1:
            A_f[0].append(genre)
        else:
            A_m[0].append(genre)       
        
        
        ecriture.ecriture0("\n", name)
        ecriture.ecriture0("a = ", name)
        ecriture.ecriture0(a, name)
        
        

        
       #ponctuation
        ponctua = poidsPonctuation.Ponctuation(phrases)
        ecriture.ecriture0("\n", name)
        ecriture.ecriture0('b = ', name)
        ecriture.ecriture0(str(ponctua), name)
        
        if a["feminin"] == 1:
            A_f[1].append(ponctua)
        else:
            A_m[1].append(ponctua)

        #longueur_texte
        ecriture.ecriture0("\n", name)
        long = poidsTexte.longueurTexte(phrases)
        ecriture.ecriture0("c = ", name)
        ecriture.ecriture0(long, name)
        
        if a["feminin"] == 1:
            A_f[2].append(long)
        else:
            A_m[2].append(long)

        #structure de phrase
        type_phrase = poidsTexte.structure_phrase(phrases)
        ecriture.ecriture0("\n", name)
        ecriture.ecriture0("d = ", name)
        ecriture.ecriture0(type_phrase, name)
        if a["feminin"] == 1:
            A_f[3].append(type_phrase)
        else:
            A_m[3].append(type_phrase)

            
        #impératif
        imperatif = poidsTexte.impératif(phrases)
        ecriture.ecriture0("\n", name)
        ecriture.ecriture0("e = ", name)
        ecriture.ecriture0(imperatif, name)
        if a["feminin"] == 1:
            A_f[4].append(imperatif)
        else:
            A_m[4].append(imperatif)

        #pronom
        pronom = poidsMots.Pronom(phrases)
        ecriture.ecriture0("\n", name)
        ecriture.ecriture0("f = ", name)
        ecriture.ecriture0(pronom, name)
        if a["feminin"] == 1:
            A_f[5].append(pronom)
        else:
            A_m[5].append(pronom)
        
        #adjectif
        adj = poidsMots.adjectif(phrases)
        ecriture.ecriture0("\n", name)
        ecriture.ecriture0("g = ", name)
        ecriture.ecriture0(adj, name)
        if a["feminin"] == 1:
            A_f[6].append(adj)
        else:
            A_m[6].append(adj)
        
        #nm_comun
        nm = poidsMots.presence_nom_commun(phrases)
        ecriture.ecriture0("\n", name)
        ecriture.ecriture0("h = ", name)
        ecriture.ecriture0(nm, name)
        if a["feminin"] == 1:
            A_f[7].append(nm)
        else:
            A_m[7].append(nm)
        
        #verbe
        verbe = poidsMots.presence_verbe(phrases)
        ecriture.ecriture0("\n", name)
        ecriture.ecriture0("i = ", name)
        ecriture.ecriture0(verbe, name)
        if a["feminin"] == 1:
            A_f[8].append(verbe)
        else:
            A_m[8].append(verbe)

      
        c+=1

    with open("rerequete.py","a") as file:
        if a["feminin"] == 1:
            file.write(str(A_f))
            file.write("\n")

        else:
            file.write(str(A_m))
            file.write("\n")









































