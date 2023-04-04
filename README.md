# TU_PYTHON_B3_C2_AYAD_SERRANO_J
Prérequis 
Python 3.8

Commande pour lancer le projet : python main.py


Commande pour lancer les tests BDD : python BDD.py


Commande pour lancer les test TDD : python TDD.py


Voici les tests effectué
Addition :
        expression : 2+3
        result = 5        
        expression : 0+0
        result = 0
        expression : -1 +1
        result = 0
        
Soustraction :
        expression : 5-2
        result = 3
        expression : 0-0
        result = 0
        expression -1 -1 
        result = -2

Multiplication :
        expression : 2x3
        result = 6
        expression : 0x0
        result = 0
        expression : -1 x 1 
        result = -1
        expression : 2,5 x 4 
        result = 10
        expression : 2x4,5
        result = 9
        expression : 2,5 x 4,5
        result = 11,25
        expression : 2x(3+4)
        result = 14

Division :
        expression : 6/3
        result = 2
        expression : 0/5
        result = 0
        expression : 1/0
        result = Erreur
        expression 10 / 4
        result = 2,5
        expression : 12,5 / 2,5
        result = 5
        expression :10/(2+2)
        result = 2,5

Et enfin des tests type TDD

Calculer expression complexe :
        expression : (1+2)x(3-1)/2
        result = 3

Calculer division par zero :
        expression : 1/0
        result = erreur
        
Calculer expression invalide(self):
        expression : 1++2
        result = Erreur
