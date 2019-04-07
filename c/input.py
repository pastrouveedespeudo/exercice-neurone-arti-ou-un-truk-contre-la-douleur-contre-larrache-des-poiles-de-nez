from traitement import *
from conteneur import *

genre = {"masculin":0, "feminin":0}

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

##
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
##                    if j[-1] == "ée", "ie", "ue":
##                        fem = True

        if fem == True:
            genre["feminin"] += 1
        else:
            genre["masculin"] += 1
                        
                    
        print(genre)


        


if __name__ == "__main__":


    #entrée = input("texte ?")
    liste = [TEXT10, TEXT, TEXT1, TEXT2, TEXT3, TEXT4, TEXT5,TEXT6,
             TEXT7,TEXT8, TEXT9, TEXT11]
    
    apprentissage1 = apprentissage1()
    
    for i in liste:
    
        entrée = i
        entrée1 = "je suis très heureuse"

        #opération sur le texte
        
        opé = premiere_opération()


        #methode
        text = opé.trait_texte(entrée)
        phrases = opé.traitement_phrase(text)

       
        genre = apprentissage1.opération_pour_genre(phrases)
        genre2 = apprentissage1.opération_pour_le_genre2(genre)
        apprentissage1.le_genre(genre2)
            














































