import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

from texte import *
from perso import *
from conteneur import *


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
                texte1.append(str("".join(i)))
                texte1.append(j)
                c+=1
            else:
                texte1.append(str("".join(i)))    

        return texte1

    def traitement_phrase(self, texte):
        """ici on a les phrases segmentées par des points"""
        
        self.texte = texte

        liste = [[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[]]

        c = 0
        for i in texte:
         
            if i == ".":
                liste[c].append(i)
                c+=1
            liste[c].append(i)

        liste2 = [i for i in liste if i != []]

        return liste2

    
class poidsPonctuation:
    
    def Ponctuation(self, texte):
        self.texte = texte
        ponctuation = [j for i in self.texte for j in i
                       if j == "?"
                       or j == "!"
                       or j == "."
                       or j == ","
                       or j == ";"]
        
        return ponctuation
        
 

class poidsTexte:
    
    def longueurTexte(self, texte):
        self.texte = texte
        longueur = len(self.texte)

        return longueur

    def type_de_texte(self, texte):
        self.texte = texte

    def structure_phrase(self, texte):
        self.texte = texte

    def impératif(self, texte):
        self.texte = texte

        imperatif = ""
        imperatif1 = ""
        liste = [[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[]]
        c = 0
        for i in self.texte:
            if i[-1] == "!":
                liste[c].append(i)
                c+=1
                
        liste2 = [i for i in liste if i != []]
 
        for i in liste2:
            for j in i[0]:
     
                for pronom in PRONOMS:
                    if j == pronom:
                        imperatif = False
                        
                if imperatif == False:
                    pass
                else:
                    path = "http://www.les-verbes.com/conjuguer.php?verbe={}"
                    path = path.format(j)
                    requete = requests.get(path)
                    page = requete.content
                    
                    soup = BeautifulSoup(page, "html.parser")      
                    propriete = soup.find_all("span", {"class":"arial-12-gris"})
                    verbe = str(propriete).find("VERBE")
                    if verbe >= 0:
                        for conjugai_a_imperatif in IMPERATIF:
                            nb = len(conjugai_a_imperatif)
                            if j[-nb:] == conjugai_a_imperatif:
                                imperatif1 = True
        return imperatif1

class poidsMots:
    
    def Pronom(self, texte):
        self.texte = texte
        
        je = [i for i in self.texte if i == "je" or i == "Je"]
        tu = [i for i in self.texte if i == "tu" or i == "Tu"]
        nbJe = len(je)
        nbTu = len(tu)
        
        return nbJe, nbTu

    def faute(self, texte):
        self.texte = texte

    def adjectif(self, texte):
        self.texte = texte


    










if __name__ == "__main__":

    #on split le texte ect
    premiere_opération = premiere_opération()
    txt = premiere_opération.trait_texte("donne moi ca !")
    text1 = premiere_opération.traitement_phrase(txt)

    poidsTexte = poidsTexte()
    poidsTexte.impératif(text1)















