# Définition des fonctions d'opération
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Erreur: division par zéro!")
    return a / b

def resoudre_expression(expression):
    while '(' in expression:
        i = 0
        while i < len(expression):
            if expression[i] == '(':
                j = i
            elif expression[i] == ')':
                sous_expression = expression[j:i+1]
                resultat_sous_expression = str(eval(sous_expression))
                expression = expression.replace(sous_expression, resultat_sous_expression)
                break
            i += 1
    return expression


def calculer(expression):
    # Vérification que l'expression n'est pas vide
    if not expression:
        raise ValueError("Erreur: expression vide!")

    # Suppression des espaces dans l'expression
    expression = expression.replace(' ', '')

    # Vérification que l'expression ne contient pas deux opérateurs consécutifs
    if '--' in expression or '++' in expression or '+-' in expression or '-+' in expression:
        raise SyntaxError("Erreur: opérateurs invalides!")

    # Résolution des expressions entre parenthèses
    while '(' in expression:
        expression = str(resoudre_expression(expression))

    # Parcourir l'expression et exécuter les opérations correspondantes
    if '*' in expression:
        operateur = '*'
        index = expression.index(operateur)
        return multiplication(calculer(expression[:index]), calculer(expression[index + 1:]))
    elif '/' in expression:
        operateur = '/'
        index = expression.index(operateur)
        return division(calculer(expression[:index]), calculer(expression[index + 1:]))
    elif '+' in expression:
        operateur = '+'
        index = expression.index(operateur)
        return addition(calculer(expression[:index]), calculer(expression[index + 1:]))
    elif '-' in expression:
        operateur = '-'
        index = expression.index(operateur)

        # Vérification que le signe '-' n'est pas un opérateur mais un signe négatif
        if index == 0:
            return -calculer(expression[1:])
        else:
            return soustraction(calculer(expression[:index]), calculer(expression[index + 1:]))
    else:
        # Si l'expression ne contient qu'un seul nombre, le renvoyer
        return float(expression)

if __name__ == '__main__':
    # Boucle principale pour demander les entrées et effectuer les opérations
    while True:
        print("Entrez une expression arithmétique (ou tapez 'quitter' pour sortir) :")

        expression = input()

        # Quitter le programme si l'utilisateur le demande
        if expression.lower() == 'quitter':
            break

        try:
            resultat = calculer(expression)
            print(f"{expression} = {resultat}")
        except ValueError as e:
            print(str(e))

