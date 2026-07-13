import tkinter as tk
from livrable_S5_calculatrice import calculer_expression


# =====================================================================
# 4. LOGIQUE DE L'INTERFACE
# =====================================================================

def saisir_caractere(caractere):
    """Ajoute un caractère à l'écran de la calculatrice. 
    Si l'écran contient déjà un résultat ou une erreur, il est effacé avant d'ajouter le nouveau caractère."""
    contenu_actuel = ecran.get()

    if "=" in contenu_actuel or "Erreur" in contenu_actuel:
        ecran.delete(0, tk.END)
        contenu_actuel = ""

    ecran.insert(tk.END, str(caractere))


def declencher_calcul():
    """Déclenche le calcul de l'expression affichée à l'écran. 
    Si l'expression est vide ou contient déjà un résultat, la fonction ne fait rien. Sinon, elle calcule le résultat et l'affiche."""
    expression_complete = ecran.get()

    if "=" in expression_complete or expression_complete == "":
        return

    reponse = calculer_expression(expression_complete)

    # Affichage de l'opération et du résultat final
    if reponse == "Erreur":
        affichage_final = "Erreur"
    else:
        affichage_final = expression_complete + " = " + str(reponse)

    ecran.delete(0, tk.END)
    ecran.insert(0, affichage_final)


def effacer():
    """Efface le contenu de l'écran de la calculatrice."""
    ecran.delete(0, tk.END)


# =====================================================================
# 5. INTERFACE GRAPHIQUE
# =====================================================================

fenetre = tk.Tk()
fenetre.title("Calculatrice")
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