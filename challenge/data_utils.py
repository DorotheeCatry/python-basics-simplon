"""Fonctions utilitaires pour des calculs mathématiques et statistiques."""

import math

PI = math.pi
E = math.e


def carre(x):
    """Retourne le carré de x."""
    return x ** 2


def cube(x):
    """Retourne le cube de x."""
    return x ** 3


def factorielle(n):
    """Retourne la factorielle de l'entier n (n >= 0)."""
    if n < 0:
        raise ValueError("n doit être positif ou nul.")

    result = 1
    factor = n
    while factor > 1:
        result *= factor
        factor -= 1
    return result


def valeur_absolue(x):
    """Fonctions utilitaires pour des calculs mathématiques et statistiques."""
    if x < 0:
        return -x
        return x

def maximum(liste):
    """Retourne le plus grand élément de la liste."""
    maxi = liste[0]

    for item in liste[1:]:
        if item > maxi:
            maxi = item
    return maxi


def minimum(liste):
    """Retourne le plus petit élément de la liste."""
    if not liste:
        raise ValueError("La liste ne doit pas être vide.")

    smallest = liste[0]
    for item in liste[1:]:
        if item < smallest:
            smallest = item
    return smallest


def moyenne(liste):
    """Retourne la moyenne des éléments de la liste."""
    if not liste:
        raise ValueError("La liste ne doit pas être vide.")

    return sum(liste) / len(liste)


def ecart_type(liste):
    """Retourne l'écart type (population) des éléments de la liste."""
    if not liste:
        raise ValueError("La liste ne doit pas être vide.")

    average = moyenne(liste)
    total = 0
    for value in liste:
        total += (value - average) ** 2
    variance = total / len(liste)
    return math.sqrt(variance)

def mediane(liste):
    """Retourne la médiane des éléments de la liste."""
    if not liste:
        raise ValueError("La liste ne doit pas être vide.")

    sorted_list = sorted(liste)

    middle = len(sorted_list) // 2
    if len(sorted_list) % 2 == 1:
        return sorted_list
    return (sorted_list[middle - 1] + sorted_list[middle]) / 2    
