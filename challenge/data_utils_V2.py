"""Version 2 des fonctions utilitaires : listes, dictionnaires et conversions."""

def somme_cumulee(liste):
    """Calcule la somme cumulée d'une liste et retourne une liste."""
    running_total = 0
    cumulative_sum = []
    for number in liste:
        running_total += number
        cumulative_sum.append(running_total)
    return cumulative_sum


def compter_occurrences(liste):
    """Retourne un dictionnaire contenant le nombre d'occurrences de chaque élément de la liste."""
    dictionnaire = {}
    for element in liste:
        if element in dictionnaire:
            dictionnaire[element] += 1
        else:
            dictionnaire[element] = 1
    return dictionnaire


def inverser_dict(dictionnaire):
    """Inverse les clés et les valeurs d'un dictionnaire."""
    dict_inverse = {}
    for clé, valeur in dictionnaire.items():
        dict_inverse[valeur] = clé
    return dict_inverse


def filtrer_pairs(liste):
    """Retourne une nouvelle liste contenant uniquement les nombres pairs."""
    nouvelle_liste = []
    for valeur in liste:
        if valeur % 2 == 0:
            nouvelle_liste.append(valeur)
    return nouvelle_liste

def celsius_to_fahrenheit(celcius):
    """Convertit une température de Celcius en Fahrenheit et retourne un nombre."""
    F = (celcius * 9/5) + 32
    return F


def trouver_doublons(liste):
    """Retourne une liste des éléments qui apparaissent plus d'une fois dans la liste d'entrée."""
    liste_doublon = []
    elements = []
    for valeur in liste:
        if valeur in elements and valeur not in liste_doublon:
            liste_doublon.append(valeur)
        else: 
            elements.append(valeur)
    return liste_doublon


def calculer_moyenne_ponderee(valeurs, poids):
    """Calcule la moyenne pondérée d'une liste de valeurs avec 
    une liste de poids correspondante et retourne un nombre."""
    produit_listes = 0
    somme_poids = sum(poids)

    if len(valeurs) != len(poids):
        raise ValueError("Les deux listes doivent avoir la même taille.")
    if somme_poids == 0:
        raise ValueError("La somme des poids ne doit pas être nulle.")

    for value, weight in zip(valeurs, poids):
            produit_listes += value * weight

    return produit_listes / somme_poids    
