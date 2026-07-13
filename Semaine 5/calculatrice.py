#==========================================================
# PROJET CALCULATRICE -- AKIENI ACADEMY
#==========================================================
"""
Ce programme est une calculatrice développée en Python qui permet à l'utilisateur d'effectuer quatre opérations mathématiques principales : l'addition, la soustraction, la multiplication et la division.
L'organisation du programme repose sur une fonction principale appelée "calculatrice()" qui contrôle le déroulement général de l'application. Cette fonction affiche le menu des opérations, récupère les choix de l'utilisateur, demande les valeurs nécessaires aux calculs, affiche les résultats et permet de répéter plusieurs calculs grâce à une boucle.
Au-dessus de cette fonction principale, plusieurs sous-fonctions ont été créées : "addition()", "soustraction()", "multiplication()" et "division()". Ces fonctions ont chacune un rôle précis : elles réalisent uniquement le calcul correspondant et retournent le résultat à la fonction principale. Elles sont placées avant "calculatrice()" car Python doit connaître l'existence de ces fonctions avant qu'elles soient appelées dans le programme.
Cette séparation permet d'avoir un code plus clair, mieux organisé et plus facile à modifier. La fonction principale s'occupe de la gestion de l'utilisateur, tandis que les sous-fonctions s'occupent uniquement des opérations mathématiques.
Pour rendre le programme plus accessible, l'utilisateur peut choisir une opération soit en tapant un chiffre (1, 2, 3, 4), soit directement le symbole mathématique correspondant (+, -, *, /).
Plusieurs situations pouvant provoquer des erreurs ont également été prises en compte. Le programme vérifie d'abord que le choix de l'opération est valide afin d'éviter que l'utilisateur sélectionne une option inexistante. Il vérifie aussi que les nombres saisis sont bien des nombres valides avant de les convertir. Il gère également le cas particulier de la division par zéro, qui est une opération impossible en mathématiques. Enfin, une vérification de la réponse de l'utilisateur lors de la question de continuation permet de s'assurer qu'il répond uniquement par "oui" ou "non".
La gestion des erreurs a été réalisée uniquement avec les notions déjà étudiées (conditions, boucles et fonctions), sans utiliser les exceptions Python ("try/except"), car cette notion n'a pas encore été abordée.
"""

# Fonction d'addition
def addition(a, b):
    """
    Additionne deux nombres.

    Paramètres :
        a (float) : le premier nombre
        b (float) : le deuxième nombre

    Retourne :
        float : la somme de a et b
    """
    return a + b

# Fonction de soustraction
def soustraction(a, b):
    """
    Soustrait le deuxième nombre du premier.

    Paramètres :
        a (float) : le nombre duquel on soustrait
        b (float) : le nombre à soustraire

    Retourne :
        float : le résultat de a - b
    """
    return a - b

# Fonction de multiplication
def multiplication(a, b):
    """
    Multiplie deux nombres.

    Paramètres :
        a (float) : le premier nombre
        b (float) : le deuxième nombre

    Retourne :
        float : le produit de a et b
    """
    return a * b

# Fonction de division
def division(a, b):
    """
    Divise le premier nombre par le deuxième.

    Paramètres :
        a (float) : le numérateur
        b (float) : le dénominateur

    Retourne :
        float : le résultat de a / b
        str : un message d'erreur si b est égal à zéro
    """
    if b == 0:
        return "Erreur : impossible de diviser par zéro."
    return a / b

# Fonction qui vérifie si une chaîne de caractères représente bien un nombre
# (entier ou décimal, positif ou négatif) -- sans utiliser try/except
def est_un_nombre(valeur):
    """
    Vérifie si une chaîne de caractères représente un nombre valide
    (entier ou décimal, positif ou négatif), sans utiliser try/except.

    Paramètres :
        valeur (str) : la chaîne de caractères à vérifier

    Retourne :
        bool : True si la chaîne représente un nombre valide, False sinon
    """
    if valeur.startswith("-"):
        valeur = valeur[1:]

    parties = valeur.split(".")

    # Un nombre valide a au maximum un point décimal
    if len(parties) > 2:
        return False

    for partie in parties:
        if partie == "" or not partie.isdigit():
            return False

    return True

# Fonction qui demande un nombre à l'utilisateur et redemande tant que
# la saisie n'est pas valide
def demander_nombre(message):
    """
    Demande un nombre à l'utilisateur et redemande tant que la saisie
    n'est pas un nombre valide.

    Paramètres :
        message (str) : le message affiché pour demander la saisie

    Retourne :
        float : le nombre saisi par l'utilisateur, converti en float
    """
    while True:
        valeur = input(message)
        if est_un_nombre(valeur):
            return float(valeur)
        else:
            print("Erreur : veuillez entrer un nombre valide.")

# Fonction qui convertit le choix de l'utilisateur (chiffre OU symbole)
# en une valeur unique et standard : "1", "2", "3" ou "4"
def normaliser_choix(choix):
    """
    Convertit le choix de l'utilisateur (chiffre ou symbole) en une
    valeur standard utilisable par le reste du programme.

    Paramètres :
        choix (str) : le choix saisi par l'utilisateur ("1", "+", etc.)

    Retourne :
        str : "1", "2", "3" ou "4" si le choix est valide
        None : si le choix ne correspond à aucune opération connue
    """
    if choix == "1" or choix == "+":
        return "1"
    elif choix == "2" or choix == "-":
        return "2"
    elif choix == "3" or choix == "*":
        return "3"
    elif choix == "4" or choix == "/":
        return "4"
    else:
        return None

# Fonction principale
def calculatrice():
    """
    Fonction principale de la calculatrice.

    Affiche le menu des opérations, récupère le choix de l'utilisateur,
    demande les nombres nécessaires au calcul, exécute l'opération choisie,
    affiche le résultat, puis demande à l'utilisateur s'il souhaite
    effectuer un autre calcul. Ne prend aucun paramètre et ne retourne
    aucune valeur : elle gère uniquement le déroulement du programme.
    """
    print("====== CALCULATRICE ======")

    # Boucle qui permet de refaire plusieurs calculs
    while True:
        print("\nChoisissez une opération :")
        print("1 ou + : Addition")
        print("2 ou - : Soustraction")
        print("3 ou * : Multiplication")
        print("4 ou / : Division")

        # Choix de l'utilisateur (chiffre ou symbole accepté)
        choix_brut = input("Votre choix : ")
        choix = normaliser_choix(choix_brut)

        # Vérification du choix de l'utilisateur s'il est valide ou non
        if choix is None:
            print("Choix invalide.")

        # Saisie des deux nombres (avec vérification intégrée)
        else:
            a = demander_nombre("Premier nombre : ")
            b = demander_nombre("Deuxième nombre : ")

            # Exécution de l'opération choisie
            if choix == "1":
                resultat = addition(a, b)
            elif choix == "2":
                resultat = soustraction(a, b)
            elif choix == "3":
                resultat = multiplication(a, b)
            else:
                resultat = division(a, b)

            # Affichage du résultat
            print("Résultat :", resultat)

        # Demande à l'utilisateur s'il veut continuer ou pas,
        # avec vérification de la réponse (on redemande si la réponse est invalide)
        
        continuer = input("\nVoulez-vous effectuer un autre calcul ? (oui/non) : ").lower()
        if continuer == "oui":
            continue
        elif continuer == "non":
            break
        else:
            print("Réponse invalide. Veuillez répondre uniquement par oui ou non.")
            break
    print("Merci d'avoir utilisé la calculatrice !")

# Lancement du programme
calculatrice()