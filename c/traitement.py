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
         
            if i == "." or i == "!" or i == "?":
                liste[c].append(i)
                c+=1
            liste[c].append(i)

        liste2 = [i for i in liste if i != []]

        return liste2

    
class poidsPonctuation:
    
    def Ponctuation(self, texte):
        self.texte = texte

        dico = {}
        for i in PONCTUATION:
            dico[i] = 0
    
        liste = []

        
        for i in self.texte:
            for j in i:
                for ponct in PONCTUATION:
                    if j == ponct:
                        dico[j] += 1

        return dico

            
        #return ponctuation



class poidsTexte:

    def type_verbe(self, texte):
        pass
    #transitif ou non

    def longueurTexte(self, texte):
        self.texte = texte

        dico = {"nb_phrase":0, "mot_phrase_max":0}

        liste = [[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[]]

        c = 0
        for i in self.texte:
            compteur = 0
            for j in i:
                compteur += 1
                if j == ".":
                    liste[c].append(compteur)
                    c+=1
            
            
            
        longueur = len(self.texte)
        dico["nb_phrase"] += longueur
        a = max(liste)
        dico["mot_phrase_max"] += a[0]

        return dico


    def structure_phrase(self, texte):
        self.texte = texte
        #on cherche chaque mot (sujet, nom ect)
        #on cherche le verbe avant

        liste = [[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[]]

        c = 0
        for i in self.texte:
            for j in i:
                
                path = "http://www.les-verbes.com/conjuguer.php?verbe={}"
                path = path.format(j.lower())
                requete = requests.get(path)
                page = requete.content

                soup = BeautifulSoup(page, "html.parser")      
                propriete = soup.find_all("span", {"class":"arial-12-gris"})
                verbe = str(propriete).find("VERBE")
                propriete = soup.find_all("span", {"class":"arial-12-gris"})
                if verbe >= 0:
                    liste[c].append("verbe")
                else:
                    path = "https://www.le-dictionnaire.com/definition/{}"
                    path = path.format(j.lower())
                    requete = requests.get(path)
                    page = requete.content
                    soup = BeautifulSoup(page, "html.parser")      
                    propriete = soup.find("div", {"class":"defbox"})
                    
                    pronom_personnel = str(propriete).find("Pronom personnel")
                    nom_commun = str(propriete).find("Nom commun")
                    adjectif = str(propriete).find("Adjectif")
                    conjonction_de_coordination = str(propriete).find("Conjonction de coordination")
                    adverbe = str(propriete).find("Adverbe")
                    adjectif_possessif = str(propriete).find("Adjectif possessif")
                    forme_article_défini = str(propriete).find("Forme d’article défini")
                    Forme_d_article_défini = str(propriete).find("Forme d’article défini")
                    article_défini = str(propriete).find("Article défini")
                    adjectif_numéral = str(propriete).find("Adjectif numéral")
                    forme_de_nom_commun = str(propriete).find("Forme de nom commun")
                    préposition = str(propriete).find("Préposition")
                    conjonction = str(propriete).find("Conjonction")
                    Forme_article_indéfini = str(propriete).find("Forme d’article indéfini")
                    Forme_adjectif_numéral = str(propriete).find("Forme d’adjectif numéral")
                    
                    Aucun_mot_trouvé  = str(propriete).find("Aucun mot trouvé, donc aucune définition")
                    
                    if pronom_personnel >= 0:
                        liste[c].append("pronom_personnel")
                    
                    elif nom_commun >= 0:
                        liste[c].append("nom_commun")
                    
                    elif adjectif >= 0:
                        liste[c].append("adjectif")
                        
                    elif conjonction_de_coordination >= 0:
                        liste[c].append("conjonction_de_coordination")
                
                    elif adverbe >= 0:
                        liste[c].append("adverbe")
                    
                    elif adjectif_possessif >= 0:
                        liste[c].append("adjectif_possessif")
                    
                    elif forme_article_défini >= 0:
                        liste[c].append("forme_article_défini")
                    
                    elif Forme_d_article_défini >= 0:
                        liste[c].append("Forme_d_article_défini")
                    
                    elif article_défini >= 0:
                        liste[c].append("article_défini")
                    
                    elif adjectif_numéral >= 0:
                        liste[c].append("adjectif_numéral")
                    
                    elif forme_de_nom_commun >= 0:
                        liste[c].append("forme_de_nom_commun")
                        
                    elif préposition >= 0:
                        liste[c].append("préposition")
                    
                    elif conjonction >= 0:
                        liste[c].append("conjonction")
                        
                    elif Forme_article_indéfini >= 0 :
                        liste[c].append("Forme_article_indéfini")

                    elif Forme_adjectif_numéral >= 0:
                        liste[c].append("Forme_adjectif_numéral")
                        
                    elif Aucun_mot_trouvé >= 0:
                        liste[c].append("Aucun_mot_trouvé")

                    else:
                        print(j, "mot a chercher !!!")
            
                    

                                    
                                
            c+=1
        return liste



    def impératif(self, texte):
        self.texte = texte

        imperatif = ""
        imperatif1 = ""
        liste_imperatif = []
        
        liste = [[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[]]
        c = 0
        for i in texte:
            #on cherche ! a la fin
            if i[-1] == "!":
                liste[c].append(i)
                c+=1
                
        liste2 = [i for i in liste if i != []]
 
        for i in liste2:
            for j in i[0]:
     
                for pronom in PRONOMS:
                    if j == pronom:
                        #si y'a pronom alors false
                        imperatif = False
                        
                if imperatif == False:
                    pass
                else:
                    #si y'a pas pronom cherche
                    path = "http://www.les-verbes.com/conjuguer.php?verbe={}"
                    path = path.format(j)
                    requete = requests.get(path)
                    page = requete.content
                    
                    soup = BeautifulSoup(page, "html.parser")      
                    propriete = soup.find_all("span", {"class":"arial-12-gris"})
                    verbe = str(propriete).find("VERBE")
                    #si on trouve verbe fais
                    if verbe >= 0:
                        for conjugai_a_imperatif in IMPERATIF:
                            nb = len(conjugai_a_imperatif)
                            if j[-nb:] == conjugai_a_imperatif:
                                #si conjugai 2,4,5 personne alors true
                                liste_imperatif.append((i, True))

                           
        return liste_imperatif

class poidsMots:
    
    def Pronom(self, texte):
        self.texte = texte
        
        je = [j for i in self.texte for j in i if j == "je" or j == "Je"]
        tu = [j for i in self.texte for j in i if j == "tu" or j == "Tu"]
        il = [j for i in self.texte for j in i if j == "il" or j == "Il"]
        elle = [j for i in self.texte for j in i if j == "elle" or j == "Elle"]
        nous = [j for i in self.texte for j in i if j == "nous" or j == "Nous"]
        vous = [j for i in self.texte for j in i if j == "vous" or j == "Vous"]
        ils = [j for i in self.texte for j in i if j == "Ils" or j == "ils"]
        elles = [j for i in self.texte for j in i if j == "Elles" or j == "elles"]
        
        nbJe = len(je)
        nbTu = len(tu)
        nbIl = len(il)
        nbElle = len(elle)
        nbNous = len(nous)
        nbVous = len(vous)
        nbIls = len(ils)
        nbElles = len(elles)
        
        print(nbJe, nbTu, nbIl,nbElle, nbNous, nbVous, nbIls, nbElles)
        return nbJe, nbTu, nbIl,nbElle, nbNous, nbVous, nbIls, nbElles

    
    def faute(self, texte):
        self.texte = texte

    def adjectif(self, texte):
        self.texte = texte
        
        liste = []
      
        for i in self.texte:
            for j in i:
                path = "https://www.le-dictionnaire.com/definition/{}"
                path = path.format(j.lower())
                requete = requests.get(path)
                page = requete.content

                soup = BeautifulSoup(page, "html.parser")      
                propriete = soup.find("div", {"class":"defbox"})
                adjectif = str(propriete).find("Adjectif")
                if adjectif >= 0:
                    liste.append(j)

   
        return liste

    def presence_nom_commun(self, texte):
        self.texte = texte

        liste = []
      
        for i in self.texte:
            for j in i:
                path = "https://www.le-dictionnaire.com/definition/{}"
                path = path.format(j.lower())
                requete = requests.get(path)
                page = requete.content

                soup = BeautifulSoup(page, "html.parser")      
                propriete = soup.find("div", {"class":"defbox"})
                nc = str(propriete).find("Nom commun")
                if nc >= 0:
                    liste.append(j)
     
        return liste
    
    def presence_verbe(self, texte):
        self.texte = texte

        liste = []
        for i in self.texte:
            for j in i:
                path = "http://www.les-verbes.com/conjuguer.php?verbe={}"
                path = path.format(j.lower())
                requete = requests.get(path)
                page = requete.content
                soup = BeautifulSoup(page, "html.parser")      
                propriete = soup.find("span", {"class":"arial-12-gris"})
                verbe = str(propriete).find("VERBE")
                if verbe >= 0:
                    liste.append(j)

                
 
        return liste

