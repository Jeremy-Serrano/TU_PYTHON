# TU_PYTHON_B3_C2_AYAD_SERRANO_J
Prérequis 
Python 3.8

Commande pour lancer le projet : python main.py


Commande pour lancer les tests BDD : python BDD.py


Commande pour lancer les test TDD : python TDD.py


Voici les tests effectué<br>
Addition :
        - expression : 2+3 <br>
        - result = 5 <br>        
        - expression : 0+0 <br>
        - result = 0<br>
        - expression : -1 +1<br>
        - result = 0<br>
        
- Soustraction :
        - expression : 5-2<br>
        - result = 3<br>
        - expression : 0-0<br>
        - result = 0<br>
        - expression -1 -1 <br>
        - result = -2<br>

- Multiplication :
       - expression : 2x3<br>
       - result = 6<br>
       - expression : 0x0<br>
       - result = 0<br>
       - expression : -1 x 1 <br>
       - result = -1<br>
       - expression : 2,5 x 4 <br>
       - result = 10<br>
       - expression : 2x4,5<br>
       - result = 9<br>
       - expression : 2,5 x 4,5<br>
       - result = 11,25<br>
       - expression : 2x(3+4)<br>
       - result = 14<br>

- Division :
        - expression : 6/3<br>
        - result = 2<br>
        - expression : 0/5<br>
        - result = 0<br>
        - expression : 1/0<br>
        - result = Erreur<br>
        - expression 10 / 4<br>
        - result = 2,5<br>
        - expression : 12,5 / 2,5<br>
        - result = 5<br>
        - expression :10/(2+2)<br>
        - result = 2,5<br>

Et enfin des tests type TDD<br>

- Calculer expression complexe :<br>
        - expression : (1+2)x(3-1)/2<br>
        - result = 3<br>

- Calculer division par zero :<br>
        - expression : 1/0<br>
        - result = erreur<br>
        
- Calculer expression invalide :<br>
        - expression : 1++2<br>
        - result = Erreur<br>
