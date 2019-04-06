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
                for marque_feminin in FEMININ:
                    nb = len(marque_feminin)
                    if j[-nb:] == marque_feminin:
                        fem = True
        if fem == True:
            genre["feminin"] += 1
        else:
            genre["masculin"] += 1
                        
                    
        print(genre)


        


if __name__ == "__main__":


    #entrée = input("texte ?")
    entrée = TEXT
    entrée1 = "je suis très heureuse"

    #opération sur le texte
    apprentissage1 = apprentissage1()
    opé = premiere_opération()


    #methode
    text = opé.trait_texte(entrée1)
    phrases = opé.traitement_phrase(text)
    
    genre = apprentissage1.opération_pour_genre(phrases)
    genre2 = apprentissage1.opération_pour_le_genre2(genre)
    apprentissage1.le_genre(genre2)
    














































