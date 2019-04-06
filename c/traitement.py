import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

from texte import *
from perso import *



class premiere_opération:
    def trait_texte(self, texte):
        self.texte = texte
        texte = texte.split()
        print(texte)
        return texte


    def remplissage_perso(self, perso):
        self.perso = perso
        
        self.dico = {}

        for cle in self.perso:
            self.dico[cle] = 0
            
        print(self.dico)
        return self.dico




class poidsPonctuation:
    def Ponctuation(self, texte):
        ponctuation = [j for i in texte for j in i
                       if j == "?"
                       or j == "!"
                       or j == "."
                       or j == ","
                       or j == ";"]
        
        print(ponctuation)


    #def ? ! , <- exité integoré ect





    
class poidsTexte:
    def longueurTexte(self, texte):
        self.texte = texte
        longueur = len(texte)

        print(longueur)
        return longueur







class poidsMots:
    def Pronom(self, texte):
        self.texte = texte
        
        je = [i for i in texte if i == "je" or i == "Je"]
        tu = [i for i in texte if i == "tu" or i == "Tu"]
        nbJe = len(je)
        nbTu = len(tu)
        
        return nbJe, nbTu



    def ordre(self, texte):
        self.texte = texte

        b = ["il faut que","tu dois","vous devez",
             "","","",
             "","","",
             "","",""]
        liste = [j for i in self.texte for j in mot if i == j]
        print(liste)
        
    #impératif ou il faut que tu, tu dois



































if __name__ == "__main__":

    #on split le texte ect
    opé = premiere_opération()
    text = opé.trait_texte(TEXT)
    opé.remplissage_perso(PERSO)


    #la longueur du text
    trait_poids = poidsTexte()
    trait_poids.longueurTexte(text)


    #la ponctuation
    trait_poids1 = poidsPonctuation()
    trait_poids1.Ponctuation(text)

    #les mots
    trait_poids2 = poidsMots()
    trait_poids2.Pronom(text)
    trait_poids2.ordre(text)














