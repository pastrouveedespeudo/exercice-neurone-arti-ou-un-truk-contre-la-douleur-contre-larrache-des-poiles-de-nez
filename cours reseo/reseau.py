from fonction import sigmoide, tangeante

class Reseau:
    def __init__(self, name='unknown', learn='sigmoide', error=0.001):

        self.name = name

        if 'tangente' == str.lower(learn):
            self.fun_learn = tangeante
            self.name_fun_learn = 'tangeante'

        else:
            self.fun_learn = sigmoide
            self.name_fun_learn = 'sigmoide'

        self.error = error
        self.couche = []
        self.link = []
        self.values = []

        self.control = 0


    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


    def set_erreur(self, nbr):
        if nbr > 0:
            self.error = nbr

    def get_erreur(self):
        return self.error


    def set_fun_learn(self, name):

        if lower(str(name)) == 'tangeante':
            self.fun_learn = tangeante
            self.name_fun_learn = 'tangeante'

        else:
            self.fun_learn = 'sigmoide'
            self.name_fun_learn = 'sigmoide'

    def get_name_fun_learn(self):
        return self.name_fun_learn


    def get_data(self):
        return [self.get_name(), self.get_name_fun_learn(),
                self.get_erreur(), self.get_nbr_couche()]


    def get_nbr_couche(self):
        return len(self.couche)

    def get_last_couche(self):
        return self.values[-1]


    def set_couche(self, value=2):

        if self.control == 0:
            if value>=2:
                for i in range(0, value):
                    self.couche.append(0)
            else:
                print('2 couches')

        else:
            print('déja crée')

    def add_couche(self, pos):

        if self.control == 0:
            if pos >=0 and pos <len(self.couche):
                self.couche.insert(pos, 0)
            else:
                print('nan')
        else:
            print("nan")


    def add_neurone(self, couche, nbr=1):

        if self.control == 0:
            if couche >= 0 and couche <= len(self.couche) -1 and nbr >0:
                self.couche[couche] += nbr

        else:
            print('nan')


    def add_all_neurone(self, tab):

        if self.control == 0:
            if len(tab) == len(self.couche):
                for i in range(0, len(tab)):
                    self.add_neurone(i, tab(i))
            else:
                print('nan')
        else:
            print("nan")



    def creer_reseau(self):

        test = 0
        for j in range(0, len(self.couche)):
            if self.couche[j] <= 0:
                test = 1
        if test != 1:
            if self.control == 0:
                self.control = 1
                for i in range(0, len(self.couche)):
                    add = []
                    add1 = []
                    add_values = []
                    for j in range(0, self.couche[i]):
                        if i != len(self.couche) -1:
                            for k in range(0, self.couche[i+1]):
                                add1.append(0.5)
                            add.append(add1)
                            add1 = []
                            add_values.append(0)
                        if i!= len(self.couche) -1:
                            self.link.append(add)
                        self.values.append(add_values)
            else:
                print("nan")
        else:
            print('nan')
        


    def parcourir(self, tab):
        if self.control == 1:
            if len(tab) == self.couche[0]:
                for i in range(0, len(tab)):
                    self.values[0][i] = tab[i]

                for i in range(1, len(self.values)):
                    for j in range(0, len(self.values[i])):
                        var = 0
                        for k in range(0, len(self.values[i-1])):
                            var += self.values[i-1][k] * self.link[i-1][k][j]

                        self.values[i][j] == self.fun_learn(var)
                    
            else:
                print("nan")
        else:
            print("nan")



    def retopropagation(self, tab):
        if len(tab) == len(self.values[len(self.values)-1]):
            for i in range(0, len(tab)):
                self.values[len(self.values)-1][i] = tab[i] - self.values[len(self.values)-1][i]
                                                                          
            for i in range(len(self.values) -1,0,-1):
                for j in range(0, len(self.values[i-1])):
                    for k in range(0, len(self.link[i-1][j])):
                        somme = 0
                        for l in range(0,len(self.values[i-1])):
                            somme += self.values[i-1][1]*self.link[i-1][l][k]
                        somme = self.fun_learn(somme)

                        self.link[i-1][j][k] -= self.get_erreur() * (-1 * self.values[i][k] * somme * (1-somme) * self.values[i-1][j])
                                                                
            for j in range(0, len(self.values[i])):
                somme = 0
                for k in range(0, len(self.values[i])):                                                
                    somme+= self.values[i][k]*self.link[i-1][j][k]

                self.values[i-1][j] = somme
                                                                

    def learn(self, entree, sortie):
        if self.control == 1:
            if len(entree) == self.couche[0] and len(sortie) == self.couche[len(self)]:
                self.parcourir(entree)
                self.retropropagation(sortie)
            else:
                print('nan')
        else:
            print('nan')
            

    












    

