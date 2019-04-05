from texte import *
from perso import *

class premiere_opération:
    def trait_texte(self, texte):
        self.texte = texte
        texte = texte.split()

        return texte


    def remplissage_perso(self, perso):
        self.perso = perso
        
        self.dico = {}

        for cle in self.perso:
            self.dico[cle] = 0
            
        print(self.dico)
        return self.dico



class poids:
    def poids1(self, texte):
        self.texte = texte
        longueur = len(texte)

        print(len(longueur))
        return longueur





































if __name__ == "__main__":

    opé = premiere_opération()
    text = opé.trait_texte(TEXT)
    opé.remplissage_perso(PERSO)


    trait_poids = poids()
    trait_poids.poids1(text)




















