

# =====================================================================
# 1. LOGIQUE MÉTIER / ARITHMÉTIQUE
# =====================================================================

def addition(a, b):
    """Effectue l'addition de deux nombres."""
    return a + b


def soustraction(a, b):
    """Effectue la soustraction de deux nombres."""
    return a - b


def multiplication(a, b):
    """Effectue la multiplication de deux nombres."""
    return a * b


def division(a, b):
    """Effectue la division de deux nombres."""
    if b == 0:
        return "Erreur"
    return a / b


# =====================================================================
# 2. SÉCURITÉ ET VÉRIFICATIONS 
# =====================================================================

def est_un_nombre_valide(chaine):
    """Vérifie si la chaîne contient uniquement des chiffres et au maximum un point."""
    if chaine == "":
        return False

    compteur_points = 0
    chiffres_presents = False

    for caractere in chaine:
        if caractere == ".":
            compteur_points = compteur_points + 1
        elif caractere in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            chiffres_presents = True
        else:
            return False

    if compteur_points > 1 or not chiffres_presents:
        return False

    return True


# =====================================================================
# 3. ALGORITHME DE CALCUL 
# =====================================================================

def calculer_expression(texte):
    """Analyse et calcule l'expression mathématique fournie sous forme de chaîne de caractères."""
    if texte == "" or texte == "Erreur":
        return "Erreur"

    # --- ÉTAPE 1 : Nettoyage des signes initiaux  ---
    commence_par_moins = False

    if texte[0] == "-":
        commence_par_moins = True
        texte_a_analyser = texte[1:]
    elif texte[0] == "+":
        texte_a_analyser = texte[1:]
    else:
        texte_a_analyser = texte

    if texte_a_analyser == "":
        return "Erreur"

    # --- ÉTAPE 2 : Recherche de l'opérateur principal (Priorité inversée) ---
    position_operateur = -1
    operateur_trouve = ""

    # Passage 1 : Recherche de + ou - (moins prioritaires, donc découpés en premier)
    for index in range(len(texte_a_analyser) - 1, -1, -1):
        if texte_a_analyser[index] in ["+", "-"]:
            # Sécurité pour éviter de couper sur un signe négatif interne 
            if index > 0 and texte_a_analyser[index - 1] not in ["+", "-", "*", "/"]:
                position_operateur = index
                operateur_trouve = texte_a_analyser[index]
                break

    # Passage 2 : Si pas de + ou -, on cherche * ou /
    if position_operateur == -1:
        for index in range(len(texte_a_analyser) - 1, -1, -1):
            if texte_a_analyser[index] in ["*", "/"]:
                position_operateur = index
                operateur_trouve = texte_a_analyser[index]
                break

    # --- ÉTAPE 3 : Cas où il n'y a pas de calcul à faire ---
    if position_operateur == -1:
        if est_un_nombre_valide(texte_a_analyser):
            if commence_par_moins:
                return -float(texte_a_analyser)
            return float(texte_a_analyser)
        else:
            return "Erreur"

   # --- ÉTAPE 4 : Découpage Récursif ---
    partie_gauche = texte_a_analyser[:position_operateur]
    partie_droite = texte_a_analyser[position_operateur + 1:]

    res_gauche = calculer_expression(partie_gauche)
    res_droite = calculer_expression(partie_droite)

    if res_gauche == "Erreur" or res_droite == "Erreur":
        return "Erreur"

    # --- ÉTAPE 5 : Conversion et Calcul ---
    nbr1 = res_gauche
    if commence_par_moins:
        nbr1 = -nbr1

    nbr2 = res_droite

    if operateur_trouve == "+":
        return addition(nbr1, nbr2)
    elif operateur_trouve == "-":
        return soustraction(nbr1, nbr2)
    elif operateur_trouve == "*":
        return multiplication(nbr1, nbr2)
    elif operateur_trouve == "/":
        return division(nbr1, nbr2)
    