import os

from traitement_image import *




if __name__ == "__main__":

    traitement_caracteristique = traitement_caracteristique()

    
    os.chdir(r'C:\Users\jeanbaptiste\Desktop\reso\d\image')
    liste_image = os.listdir()



    for image in liste_image:
        traitement_caracteristique.reconnaissance_corps_pikachu(image)
