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

import random
import os


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



pygame.init()

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
        

        liste = ['right', 'left', 'top', 'bot']
        choix = random.choice(liste)

        print(choix)
        if choix == 'right':
            a = dk.deplacer('droite')
            LISTE_CHOIX.append(choix)
            LISTE_CASE.append(a)
            if a == 'STOP':
                continuer_jeu = 0
            if a == 'M':
                print('M')
                liste1 = ['left', 'top', 'bot']
                choix = random.choice(liste1)
                print(choix)
                a = dk.deplacer(choix)


                
        elif choix == 'left':
            b = dk.deplacer('gauche')
            LISTE_CHOIX.append(choix)
            LISTE_CASE.append(b)
            if b == 'STOP':
                continuer_jeu = 0
            if b == 'M':
                print('M')
                liste1 = ['right', 'top', 'bot']
                choix = random.choice(liste1)
                print(choix)
                b = dk.deplacer(choix)
                
        elif choix == 'top':
            c = dk.deplacer('haut')
            LISTE_CHOIX.append(choix)
            LISTE_CASE.append(c)
            if c == 'STOP':
                continuer_jeu = 0
            if c == 'M':
               print('M')
               liste1 = ['right','left', 'bot']
               choix = random.choice(liste1)
               print(choix)
               c = dk.deplacer(choix)
               
        elif choix == 'bot':
            d = dk.deplacer('bas')
            LISTE_CHOIX.append(choix)
            LISTE_CASE.append(d)
            if d == 'STOP':
                continuer_jeu = 0
            if d == 'M':
                print('M')
                liste1 = ['right', 'left', 'top']
                choix = random.choice(liste1)
                print(choix)
                d = dk.deplacer(choix)

                
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


































