import numpy as np
import random
from math import *
import matplotlib.pyplot as plt


##fer 18 et 300 ng/ml
##gama gt8-35 u/l
##
##
##1000 ng/ml
##55-100 u/l



def data():

    nombre = 5

    liste = []

    for i in range(nombre):
        liste.append([random.uniform(0.018, 0.31),
                      random.uniform(0.008,0.035)])

    for i in range(nombre):
        liste.append([random.uniform(0.1, 0.2),
                      random.uniform(0.055,0.01)])

    
    entrée = np.asarray(liste)
    cible = np.concatenate((np.zeros(nombre), np.zeros(nombre) + 1))

    return entrée, cible




def init_variable():

    poids = np.random.normal(size=2)
    biais = 0

    return poids, biais


def preactivation(entrée, poids, biais):
    
##  a = (entrée[0][0] * poids[c]) + (entrée[0][1] * poids[c + 1]) + biais
## a = np.array(a) mais c buggué ici apres 1 tour... trouve ici

    return np.dot(entrée, poids) + biais

def activation(z):
    
    return 1 / (1 + np.exp(-z))


def prediction(entrée, poids, biais):

    z = preactivation(entrée, poids, biais)
    y = activation(z)
    

    return np.round(y)


def cost(predictions, cible):
    return np.mean((predictions - cible) **2 )

def pre_activation(z):
    return activation(z) *(1 - activation(z))



def gra_poids(y, cible, z, entrée, mode):
    
    #1/2*(y -t) ** 2
    #1/2 * 2 * (y - t)**1 * 1 ou 1 == a(z)

    
    sig_prime = pre_activation(z)

    print(y)
    out = (y - cible) * sig_prime + entrée

    if mode != 'biais':
        return out
    else:
        out = out - entrée
        print("oui", out)
        return out




    
def entrainement(entrée, cible, poids, biais):

    epoque = 5
    learning_rate = 0.1

    predict = prediction(entrée, poids, biais)
    print("Accuracy de la video de: ", np.mean(predict == cible))
    #les données sont niqué jcrois
    #faut faire avec 3 truks mtn puis 4 pour etre sur
    #et le faire tout seul donc par coeur
    #puis d'autre technique

    
##    plt.scatter(entrée[:, 0], entrée[:, 1], s=40, 
##                c=cible, cmap=plt.cm.Spectral)
##    plt.show()


    for i in range(epoque):

        if i % 10 == 0:
            
            z = preactivation(entrée, poids, biais)
            predictions = activation(z)
            cost1 = cost(predictions, cible)
            print("cost = ", cost1)

        gradient_poids = np.zeros(poids.shape)
        gradient_biais = 0

        for i, j in zip(entrée, cible):
     
            z = preactivation(i, poids, biais)
            y = activation(z)
            erreur_poids = gra_poids(y, j, z, i, 'poids')
            
            erreur_poids_biais = gra_poids(y, j, z, i, 'biais')
            
            gradient_poids += erreur_poids
            gradient_biais += erreur_poids
            print(gradient_biais)
            
        poids = poids - learning_rate * gradient_poids
        biais = biais - learning_rate * erreur_poids_biais


    print(entrée, poids, biais,'iiiiiiiiiiiici')
    predict = prediction(entrée, poids, biais)
    print("Accuracy de la video de: ", np.mean(predict == cible))


if __name__ == "__main__":

    entrée, cible = data()
    poids, biais = init_variable()

    z = preactivation(entrée, poids, biais)
    a = activation(z)


    entrainement(entrée, cible, poids, biais)













    
