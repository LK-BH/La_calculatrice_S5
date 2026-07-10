import tkinter as tk


# =====================================================================
# 1. LOGIQUE MÉTIER / ARITHMÉTIQUE
# =====================================================================

def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Erreur"
    return a / b


# =====================================================================
# 2. SÉCURITÉ ET VÉRIFICATIONS (Uniquement if et for)
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
# 3. ALGORITHME DE PARSING PARFAIT
# =====================================================================

def calculer_expression(texte):
    if texte == "" or texte == "Erreur":
        return "Erreur"

    # --- ÉTAPE 1 : Nettoyage des signes initiaux (+6 ou -6) ---
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

    # --- ÉTAPE 2 : Recherche de l'opérateur principal ---
    position_operateur = -1
    operateur_trouve = ""

    index = 0
    for caractere in texte_a_analyser:
        if caractere in ["+", "-", "*", "/"]:
            position_operateur = index
            operateur_trouve = caractere
        index = index + 1

    # --- ÉTAPE 3 : Cas où il n'y a pas de calcul à faire ---
    if position_operateur == -1:
        if est_un_nombre_valide(texte_a_analyser):
            if commence_par_moins:
                return -float(texte_a_analyser)
            return float(texte_a_analyser)
        else:
            return "Erreur"

    # --- ÉTAPE 4 : Découpage et Validation ---
    partie_gauche = texte_a_analyser[:position_operateur]
    partie_droite = texte_a_analyser[position_operateur + 1:]

    if not est_un_nombre_valide(partie_gauche) or not est_un_nombre_valide(partie_droite):
        return "Erreur"

    # --- ÉTAPE 5 : Conversion et Calcul ---
    nbr1 = float(partie_gauche)
    if commence_par_moins:
        nbr1 = -nbr1

    nbr2 = float(partie_droite)

    if operateur_trouve == "+":
        return addition(nbr1, nbr2)
    elif operateur_trouve == "-":
        return soustraction(nbr1, nbr2)
    elif operateur_trouve == "*":
        return multiplication(nbr1, nbr2)
    elif operateur_trouve == "/":
        return division(nbr1, nbr2)


# =====================================================================
# 4. LOGIQUE DE L'INTERFACE
# =====================================================================

def saisir_caractere(caractere):
    contenu_actuel = ecran.get()

    if "=" in contenu_actuel or "Erreur" in contenu_actuel:
        ecran.delete(0, tk.END)
        contenu_actuel = ""

    ecran.delete(0, tk.END)
    ecran.insert(0, contenu_actuel + str(caractere))


def declencher_calcul():
    expression_complete = ecran.get()

    if "=" in expression_complete or expression_complete == "":
        return

    reponse = calculer_expression(expression_complete)

    # Affichage propre de l'opération et du résultat final
    if reponse == "Erreur":
        affichage_final = "Erreur"
    else:
        affichage_final = expression_complete + " = " + str(reponse)

    ecran.delete(0, tk.END)
    ecran.insert(0, affichage_final)


def effacer():
    ecran.delete(0, tk.END)


# =====================================================================
# 5. INTERFACE GRAPHIQUE
# =====================================================================

fenetre = tk.Tk()
fenetre.title("Calculatrice Robuste")
fenetre.geometry("400x450")
fenetre.configure(bg="#2d3748")
fenetre.resizable(False, False)

ecran = tk.Entry(
    fenetre, font=("Helvetica", 20), justify="right",
    bd=10, width=18, bg="#edf2f7", fg="#1a202c"
)
ecran.pack(pady=20, padx=10, fill="x")

cadre_boutons = tk.Frame(fenetre, bg="#2d3748")
cadre_boutons.pack(fill="both", expand=True, padx=10, pady=10)

for i in range(5):
    cadre_boutons.rowconfigure(i, weight=1)
for j in range(4):
    cadre_boutons.columnconfigure(j, weight=1)

btn_clear = tk.Button(
    cadre_boutons, text="C", font=("Helvetica", 14, "bold"),
    bg="#e53e3e", fg="white", command=effacer
)
btn_clear.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=4, pady=4)

btn_div = tk.Button(
    cadre_boutons, text="÷", font=("Helvetica", 14, "bold"),
    bg="#4a5568", fg="white", command=lambda: saisir_caractere("/")
)
btn_div.grid(row=0, column=3, sticky="nsew", padx=4, pady=4)

touches = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2)
]

for texte, ligne, colonne in touches:
    if texte == '=':
        btn = tk.Button(
            cadre_boutons, text=texte, font=("Helvetica", 14, "bold"),
            bg="#3182ce", fg="white", command=declencher_calcul
        )
        btn.grid(row=ligne, column=colonne, columnspan=2, sticky="nsew", padx=4, pady=4)
    elif texte in ['+', '-', '*']:
        btn = tk.Button(
            cadre_boutons, text=texte if texte != '*' else '×', font=("Helvetica", 14, "bold"),
            bg="#4a5568", fg="white", command=lambda v=texte: saisir_caractere(v)
        )
        btn.grid(row=ligne, column=colonne, sticky="nsew", padx=4, pady=4)
    else:
        btn = tk.Button(
            cadre_boutons, text=texte, font=("Helvetica", 14),
            bg="#718096", fg="white", command=lambda v=texte: saisir_caractere(v)
        )
        btn.grid(row=ligne, column=colonne, sticky="nsew", padx=4, pady=4)

fenetre.mainloop()