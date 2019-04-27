"""Classes du jeu de Labyrinthe Donkey Kong"""

import pygame
from pygame.locals import * 
from constantes import *

class Niveau:
    """Classe permettant de créer un niveau"""
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0
    
    
    def generer(self):
        """Méthode permettant de générer le niveau en fonction du fichier.
        On crée une liste générale, contenant une liste par ligne à afficher"""	
        #On ouvre le fichier
        with open(self.fichier, "r") as fichier:
            structure_niveau = []
            #On parcourt les lignes du fichier
            for ligne in fichier:
                ligne_niveau = []
                #On parcourt les sprites (lettres) contenus dans le fichier
                for sprite in ligne:
                    #On ignore les "\n" de fin de ligne
                    if sprite != '\n':
                        #On ajoute le sprite à la liste de la ligne
                        ligne_niveau.append(sprite)
                #On ajoute la ligne à la liste du niveau
                structure_niveau.append(ligne_niveau)
            #On sauvegarde cette structure
            self.structure = structure_niveau
    
    
    def afficher(self, fenetre):
        """Méthode permettant d'afficher le niveau en fonction 
        de la liste de structure renvoyée par generer()"""
        #Chargement des images (seule celle d'arrivée contient de la transparence)
        mur = pygame.image.load(image_mur).convert()
        depart = pygame.image.load(image_depart).convert()
        arrivee = pygame.image.load(image_arrivee).convert_alpha()
        
        #On parcourt la liste du niveau
        num_ligne = 0
        for ligne in self.structure:
            #On parcourt les listes de lignes
            num_case = 0
            for sprite in ligne:
                #On calcule la position réelle en pixels
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if sprite == 'm' or sprite == 'M':		   #m = Mur
                    fenetre.blit(mur, (x,y))
                elif sprite == 'd':		   #d = Départ
                    fenetre.blit(depart, (x,y))
                elif sprite == 'a':		   #a = Arrivée
                    fenetre.blit(arrivee, (x,y))
                num_case += 1
            num_ligne += 1
                    
                    
                    
                    
class Perso:
    """Classe permettant de créer un personnage"""
    def __init__(self, droite, gauche, haut, bas, niveau):
        #Sprites du personnage
        self.droite = pygame.image.load(droite).convert_alpha()
        self.gauche = pygame.image.load(gauche).convert_alpha()
        self.haut = pygame.image.load(haut).convert_alpha()
        self.bas = pygame.image.load(bas).convert_alpha()
        #Position du personnage en cases et en pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        #Direction par défaut
        self.direction = self.droite
        #Niveau dans lequel le personnage se trouve 
        self.niveau = niveau
    
    
    def deplacer(self, direction):
        """Methode permettant de déplacer le personnage"""
        LISTE = []

        filee = []

        b = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

        if int(self.x)/30 == 0 and  int(self.y)/30 == 0:
            pass


        if direction == 'droite':

            if self.case_x < (nombre_sprite_cote - 1):
                if self.niveau.structure[self.case_y][self.case_x+1] != 'm'\
                   and self.niveau.structure[self.case_y][self.case_x+1] != 'M':
                                
                    self.case_x += 1
                    LISTE.append((self.x, self.y))
            
                    self.x = self.case_x * taille_sprite
                    if self.niveau.structure[self.case_y][self.case_x+1] == 'm':
                        
                        print('mtn', int(self.x)/30, int(self.y)/30)
                        print('d')
                        x = int(self.x / 30)
                        y = int(self.y / 30)
                        
                        #ouverture
                        with open('n1','r') as file:
                            a = file.read()
                            filee.append(a)
                        #print(filee)
                        filee = " ".join(filee)
                        #recup par grille
                        c = 0
                        for i in filee:
                            if i == "\n":
                                c+=1

                            else:
                                b[c].append(i)
                        #print(b[x+1][y])
                        b[y][x+1] = 'M'
                        
                       
                        c = []

                        for i in b:
                            i = "".join(i)
                            c.append(i)

                        c = "\n".join(c)
                        #print(c)
                        
                        with open('n1','w') as file:
                            file.write(str(c))
                           
                        return 'STOP'
                    
                elif self.niveau.structure[self.case_y][self.case_x+1] == 'M':
                     return 'M'
                    
                #Image dans la bonne direction
                self.direction = self.droite
                return LISTE

            else:
                pass

        #Déplacement vers la gauche
        if direction == 'gauche':
            if self.case_x > 0:
                 if self.niveau.structure[self.case_y][self.case_x-1] != 'm'\
                    and self.niveau.structure[self.case_y][self.case_x-1] != 'M':
                    self.case_x -= 1
                    LISTE.append((self.x, self.y))
                    self.x = self.case_x * taille_sprite
                    if self.niveau.structure[self.case_y][self.case_x-1] == 'm':
                        
                        print('mtn', int(self.x)/30, int(self.y)/30)
                        print('g')
                        x = int(self.x / 30)
                        y = int(self.y / 30)
                        
                        #ouverture
                        with open('n1','r') as file:
                            a = file.read()
                            filee.append(a)

                        filee = " ".join(filee)
                        #recup par grille
                        c = 0
                        for i in filee:
                            if i == "\n":
                                c+=1

                            else:
                                b[c].append(i)

                        b[y][x-1]  = 'M'
                        
                        

                        c = []

                        for i in b:
                            i = "".join(i)
                            c.append(i)

                        c = "\n".join(c)
                        #print(c)
                        
                        with open('n1','w') as file:
                            file.write(str(c))
                        return 'STOP'
                    
                 elif self.niveau.structure[self.case_y][self.case_x-1] == 'M':
                    return 'M'
                    
                 self.direction = self.gauche
                 return LISTE

            else:
                pass

        #Déplacement vers le haut
        if direction == 'haut':
            if self.case_y > 0:

                if self.niveau.structure[self.case_y-1][self.case_x] != 'm'\
                   and self.niveau.structure[self.case_y-1][self.case_x] != 'M':
                    self.case_y -= 1
                    LISTE.append((self.x, self.y))
                    self.y = self.case_y * taille_sprite
                    if self.niveau.structure[self.case_y-1][self.case_x] == 'm':
                      
                        print('mtn', int(self.x)/30, int(self.y)/30)
                        print('h')
                        x = int(self.x / 30)
                        y = int(self.y / 30)
                        
                        #ouverture
                        with open('n1','r') as file:
                            a = file.read()
                            filee.append(a)

                        filee = " ".join(filee)
                        #recup par grille
                        c = 0
         
                        for i in filee:
    
                            if i == "\n":
                                c+=1

                            else:
                                b[c].append(i)

                        b[y-1][x] = 'M'
                 
                     

                        c = []

                        for i in b:
                            i = "".join(i)
                            c.append(i)

                        c = "\n".join(c)
                        print(c)
                        with open('n1','w') as file:
                            file.write(str(c))

                        return 'STOP'

                    
                elif self.niveau.structure[self.case_y-1][self.case_x] == 'M':
                    return 'M'

                    
                self.direction = self.haut
                return LISTE
            else:
                pass
        
        #Déplacement vers le bas
        if direction == 'bas':
            if self.case_y < (nombre_sprite_cote - 1):
                if self.niveau.structure[self.case_y+1][self.case_x] != 'm'\
                   and self.niveau.structure[self.case_y+1][self.case_x] != 'M':
                    self.case_y += 1
                    LISTE.append((self.x, self.y))
                    self.y = self.case_y * taille_sprite
                    if self.niveau.structure[self.case_y+1][self.case_x] == 'm':
                        
                        print('mtn', int(self.x)/30, int(self.y)/30)
                        print('b')
                        x = int(self.x / 30)
                        y = int(self.y / 30)
                        
                        #ouverture
                        with open('n1','r') as file:
                            a = file.read()
                            filee.append(a)

                        filee = " ".join(filee)

                        
                        #recup par grille
                        c = 0
                        for i in filee:
                   
                            if i == "\n":
                                c+=1

                            else:
                                b[c].append(i)
                        print(x,y)
                        b[y+1][x] = 'M'
                        
                        c = []

                        for i in b:
                            i = "".join(i)
                            c.append(i)

                        c = "\n".join(c)
                        print(c)
                        with open('n1','w') as file:
                            file.write(str(c))
                            
                        return 'STOP'
                    
                elif self.niveau.structure[self.case_y+1][self.case_x] == 'M':
                    return 'M'

                    
                self.direction = self.bas
                return LISTE
            else:
                pass

        














			
