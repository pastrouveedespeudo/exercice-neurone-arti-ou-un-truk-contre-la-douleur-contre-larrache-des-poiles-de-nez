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



class poids:
    
    def longueurTexte(self, texte):
        self.texte = texte
        longueur = len(texte)

        print(longueur)
        return longueur

    def Ponctuation(self, texte):
        ponctuation = [j for i in texte for j in i
                       if j == "?"
                       or j == "!"
                       or j == "."
                       or j == ","
                       or j == ";"]
        
        print(ponctuation)

    def Pronom(self, texte):
        self.texte = texte
        
        je = [i for i in texte if i == "je" or i == "Je"]
        tu = [i for i in texte if i == "tu" or i == "Tu"]
        nbJe = len(je)
        nbTu = len(tu)
        
        return nbJe, nbTu
    
    def poids4(self, texte):
        self.texte = texte
    #impératif ou il faut que tu, tu dois



































if __name__ == "__main__":

    opé = premiere_opération()
    text = opé.trait_texte(TEXT)
    opé.remplissage_perso(PERSO)


    trait_poids = poids()
    trait_poids.longueurTexte(text)
    trait_poids.Ponctuation(text)
    trait_poids.Pronom(text)



















