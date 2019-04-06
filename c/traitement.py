import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

from texte import *
from perso import *



class premiere_opération:
    
    def trait_texte(self, texte):
        
        self.texte = texte
        texte = texte.split()
        
        c=0
        texte1 = []
    
        for i in texte:

            if i[-1] == "," or i[-1] == ".":
                j = i[-1]
                i = i[:-1]
                texte1.append(str(i))
                texte1.append(j)
                c+=1
            else:
                texte1.append(str(i))    

        return texte1

    def traitement_phrase(self, texte):
        """ici on a les phrases segmentées par des points"""
        
        self.texte = texte

        liste = [[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[]]

        c = 0
        for i in self.texte:
            if i == ".":
                c+=1
            liste[c].append(i)

        liste2 = [i for i in liste if i != []]

        return liste2

    
class poidsPonctuation:
    
    def Ponctuation(self, texte):
        ponctuation = [j for i in texte for j in i
                       if j == "?"
                       or j == "!"
                       or j == "."
                       or j == ","
                       or j == ";"]

        
 

class poidsTexte:
    
    def longueurTexte(self, texte):
        self.texte = texte
        longueur = len(texte)

        return longueur

    def type_de_texte(self, texte):
        pass

    def structure_phrase(self, texte):
        pass

    def impératif(self, texte):
        pass



class poidsMots:
    
    def Pronom(self, texte):
        self.texte = texte
        
        je = [i for i in texte if i == "je" or i == "Je"]
        tu = [i for i in texte if i == "tu" or i == "Tu"]
        nbJe = len(je)
        nbTu = len(tu)
        
        return nbJe, nbTu

    def faute(self, texte):
        pass

    def adjectif(self, texte):
        pass


    










if __name__ == "__main__":

    #on split le texte ect
    opé = premiere_opération()
    text = opé.trait_texte(TEXT)



    #la longueur du text
    trait_poids = poidsTexte()
    trait_poids.longueurTexte(text)


    #la ponctuation
    trait_poids1 = poidsPonctuation()
    trait_poids1.Ponctuation(text)

    #les mots
    trait_poids2 = poidsMots()
    trait_poids2.Pronom(text)
    trait_poids2.faute(text)
    trait_poids2.adjectif(text)















