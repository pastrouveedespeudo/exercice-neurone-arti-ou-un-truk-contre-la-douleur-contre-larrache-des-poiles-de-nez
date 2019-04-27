#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
"""

import pygame
from pygame.locals import *
import mysql.connector
from classes import *
from constantes import *
from database import *
import random
import os
import requete0
import importlib
import time

def écriture(fichier, liste):
    with open(fichier, 'w') as file:
        file.write('a = ')
        file.write(str(liste))
        
def fichier():
    liste2 = []
    liste = os.listdir()
    for i in liste:
        if i == 'classes.py'\
           or i == 'config.py'\
           or i == 'constantes.py'\
           or i == 'database.py'\
           or i == 'databasedk.py'\
           or i == 'dklabyrinthe.py'\
           or i == 'essais.py'\
           or i == 'images'\
           or i == 'n1'\
           or i == 'n2'\
           or i == '__pycache__':
                pass
        else:
                liste2.append(i)

    nb = liste2[-1][-4]
    nb = int(nb)
    nouvau_nb = nb + 1
    nouveau_file = 'requete' + str(nouvau_nb) + '.py'
    print(nouveau_file)
    return nouveau_file

LISTE_CHOIX  = []
LISTE_CASE = []


class main:
    def main(self):
        pygame.init()
        print(requete0.REQUETE0)
        #Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
        fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
        #Icone
        icone = pygame.image.load(image_icone)
        pygame.display.set_icon(icone)
        #Titre
        pygame.display.set_caption(titre_fenetre)


        FILE = fichier()
        #BOUCLE PRINCIPALE
        continuer = 1
        while continuer:	
            #Chargement et affichage de l'écran d'accueil
            accueil = pygame.image.load(image_accueil).convert()
            fenetre.blit(accueil, (0,0))

            #Rafraichissement
            pygame.display.flip()

            #On remet ces variables à 1 à chaque tour de boucle
            continuer_jeu = 1
            continuer_accueil = 1

            #BOUCLE D'ACCUEIL
            while continuer_accueil:
            
                #Limitation de vitesse de la boucle
                pygame.time.Clock().tick(30)
            
                for event in pygame.event.get():
                
                    #Si l'utilisateur quitte, on met les variables 
                    #de boucle à 0 pour n'en parcourir aucune et fermer
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        continuer_accueil = 0
                        continuer_jeu = 0
                        continuer = 0
                        #Variable de choix du niveau
                        choix = 0
                            
                    elif event.type == KEYDOWN:				
                        #Lancement du niveau 1
                        if event.key == K_F1:
                            continuer_accueil = 0	#On quitte l'accueil
                            choix = 'n1'		#On définit le niveau à charger
                        #Lancement du niveau 2
                        elif event.key == K_F2:
                            continuer_accueil = 0
                            choix = 'n2'
                    
                

            #on vérifie que le joueur a bien fait un choix de niveau
            #pour ne pas charger s'il quitte
            if choix != 0:
                #Chargement du fond
                fond = pygame.image.load(image_fond).convert()

                #Génération d'un niveau à partir d'un fichier
                niveau = Niveau(choix)
                niveau.generer()
                niveau.afficher(fenetre)

                #Création de Donkey Kong
                dk = Perso("images/dk_droite.png", "images/dk_gauche.png", 
                "images/dk_haut.png", "images/dk_bas.png", niveau)

                                    
            #BOUCLE DE JEU
            while continuer_jeu:
            
                #Limitation de vitesse de la boucle
                pygame.time.Clock().tick(30)

                for event in pygame.event.get():
                
                    #Si l'utilisateur quitte, on met la variable qui continue le jeu
                    #ET la variable générale à 0 pour fermer la fenêtre
                    if event.type == QUIT:
                            continuer_jeu = 0
                            continuer = 0
                

                if requete0.REQUETE0 == 5:
                    print("ouiiiiiiiiiiiiiii")
                    a = visualisation_table.visualisation(self)
                    a = str(a)
                    a = a[7:-4]
                    
                    listeeee = []
                    for i in a:

                        if i == "'" or i == ",":
                            pass
                        else:
                            listeeee.append(i)
                    
                    listeeee = "".join(listeeee)
                    listeeee = listeeee.split()
    
                 
                    print(len(listeeee))
                    for i in listeeee:
                        print(i)
                        dep = dk.deplacer(str(i))
                        

                        with open('requete0.py', 'w') as file:
                            file.write('REQUETE0 = ')
                            file.write(str(requete0.REQUETE0 + 1))
                        importlib.reload(requete0)


                    #symbole

                    #INTERDIR LE RETOUR A S

                    #REECRIRE REQUETE - 1
                    




                liste = ['right', 'left', 'top', 'bot']
                choix = random.choice(liste)


                if choix == 'right':
                    a = dk.deplacer('droite')
                    LISTE_CHOIX.append('droite')

                    try:
                        if a[1] == 's':
                            print(a[0])
                            print(len(LISTE_CHOIX))
                            
                            if a[0] >= len(LISTE_CHOIX):
                                print("oui")
                                insertion_table.insertion_climat(self, str(LISTE_CHOIX))
                                continuer_jeu = 0
                                
                            elif a[0] < len(LISTE_CHOIX):
                                continuer_jeu = 0
                                
                            if a[0] == len(LISTE_CHOIX):
                                if REQUETE0 == 5:
                                    pass
                                else:
                                    with open('requete0.py', 'w') as file:
                                        file.write('REQUETE0 = ')
                                        file.write(str(REQUETE0 + 1))
                                    

                    except:
                        pass
                    if a == 'STOP':
                        continuer_jeu = 0
                    if a == 'M':
                        liste1 = ['left', 'top', 'bot']
                        choix = random.choice(liste1)

                        dep = dk.deplacer(choix)
           
                        


                        
                elif choix == 'left':
                    b = dk.deplacer('gauche')
                    LISTE_CHOIX.append('gauche')


                    try:
                        if c[1] == 's':
                            print(b[0])
                            print(len(LISTE_CHOIX))
                            
                            if b[0] >= len(LISTE_CHOIX):
                                print("oui")
                                insertion_table.insertion_climat(self, str(LISTE_CHOIX))
                                continuer_jeu = 0
                                
                            elif a[0] < len(LISTE_CHOIX):
                                continuer_jeu = 0
                                
                            if a[0] == len(LISTE_CHOIX):
                                if REQUETE0 == 5:
                                    pass
                                else:
                                    with open('requete0.py', 'w') as file:
                                        file.write('REQUETE0 = ')
                                        file.write(str(REQUETE0 + 1))
                    except:
                        pass
                    
                    if b == 'STOP':
                        continuer_jeu = 0
                    if b == 'M':
                        liste1 = ['right', 'top', 'bot']
                        choix = random.choice(liste1)
                 
                        dep = dk.deplacer(choix)
              



              
                elif choix == 'top':
                    c = dk.deplacer('haut')
                    LISTE_CHOIX.append('haut')
              
                    try:
                        if c[1] == 's':
                            print(c[0])
                            print(len(LISTE_CHOIX))
                            
                            if c[0] >= len(LISTE_CHOIX):
                                print("oui")
                                insertion_table.insertion_climat(self, str(LISTE_CHOIX))
                                continuer_jeu = 0
                                
                            elif a[0] < len(LISTE_CHOIX):
                                continuer_jeu = 0
                                
                            if a[0] == len(LISTE_CHOIX):
                                if REQUETE0 == 5:
                                    pass
                                else:
                                    with open('requete0.py', 'w') as file:
                                        file.write('REQUETE0 = ')
                                        file.write(str(REQUETE0 + 1))
                    except:
                        pass
                    
                    if c == 'STOP':
                        continuer_jeu = 0
                    if c == 'M':
                       liste1 = ['right','left', 'bot']
                       choix = random.choice(liste1)

                       dep = dk.deplacer(choix)
              
                       
                elif choix == 'bot':
                    d = dk.deplacer('bas')
                    LISTE_CHOIX.append('bas')
          
                    try:
                        if d[1] == 's':
                            print(d[0])
                            print(len(LISTE_CHOIX))
                            if  d[0] >= len(LISTE_CHOIX):
                                print('oui')
                                insertion_table.insertion_climat(self, str(LISTE_CHOIX))
                                continuer_jeu = 0
                                
                            elif a[0] < len(LISTE_CHOIX):
                                continuer_jeu = 0
                                
                            if a[0] == len(LISTE_CHOIX):
                                if REQUETE0 == 5:
                                    pass
                                else:
                                    with open('requete0.py', 'w') as file:
                                        file.write('REQUETE0 = ')
                                        file.write(str(REQUETE0 + 1))
                    except:
                        pass
                        
                    if d == 'STOP':
                        continuer_jeu = 0
                    if d == 'M':
                        liste1 = ['right', 'left', 'top']
                        choix = random.choice(liste1)
                
                        dep = dk.deplacer(choix)
                

                        
                #Affichages aux nouvelles positions
                fenetre.blit(fond, (0,0))
                niveau.afficher(fenetre)
                fenetre.blit(dk.direction, (dk.x, dk.y)) #dk.direction = l'image dans la bonne direction
                pygame.display.flip()

                #Victoire -> Retour à l'accueil
                if niveau.structure[dk.case_y][dk.case_x] == 'a':
                    continuer_jeu = 0
                    print(LISTE_CHOIX)
                    print(LISTE_CASE)
                    #écriture(FILE, str(LISTE))






if __name__ == '__main__':
    
    main = main()
    main.main()





















##
##def longueur():
##    liste = os.listdir()
##    liste2 = []
##    for i in liste:
##        if i == 'classes.py'\
##           or i == 'config.py'\
##           or i == 'constantes.py'\
##           or i == 'database.py'\
##           or i == 'databasedk.py'\
##           or i == 'dklabyrinthe.py'\
##           or i == 'essais.py'\
##           or i == 'images'\
##           or i == 'n1'\
##           or i == 'n2'\
##           or i == '__pycache__':
##                pass
##        else:
##            with open(i, r) as file:
##                liste2.append(file.read)
##        #on enleve les '' et le a =
##        #on split
##        #on fait un len
##        #on compare le min(liste2)
##        #on récupère les info on fait un input "entrainement" ou pas
##        #si pas alors on lui fait faire for i in liste2;
##                                #fait ca
##
##			
##def déplacement():
##        pass
##        #genere le plus petit déplacement


































