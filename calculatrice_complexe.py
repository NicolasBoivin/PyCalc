import tkinter as tk
from tkinter import ttk
import math
import cmath
from liste_doublement_chainee import ListeDoublementChainee

class CalculatriceComplexe(tk.Tk):
    def __init__(self):
        # Initialise la classe parent (tk.Tk)
        super().__init__()

        # Configuration de la fenêtre
        self.title("Calculatrice")
        self.geometry("580x400")
        self.configure(bg="#343a40")

        # Configuration du style des widgets
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", foreground="#ffffff", background="#495057", padding=5, relief="flat")
        self.style.map("TButton", background=[("active", "#495057")])
        self.style.configure("TEntry", foreground="#ffffff", fieldbackground="#495057", padding=5, relief="flat")
        # Crée une nouvelle liste doublement chainée pour stocker l'historique des calculs
        self.historique = ListeDoublementChainee()

        # Variable pour stocker le résultat courant
        self.resultat = tk.StringVar()

        # Crée les widgets de l'interface
        self.creer_widgets()

    def creer_widgets(self):
        # Crée et positionne l'écran de la calculatrice
        self.ecran = ttk.Entry(self, textvariable=self.resultat, width=50)
        self.ecran.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Liste des boutons à créer avec leurs coordonnées de positionnement
        boutons = [
            ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("+", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("*", 3, 3),
            ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("/", 4, 3),
            ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("√", 5, 3)
        ]

        # Crée et positionne les boutons
        for (text, row, col) in boutons:
            if text.isdigit() or text == ".":
                cmd = lambda t=text: self.ajouter_chiffre(t)
            elif text in "+-*/":
                cmd = lambda t=text: self.ajouter_operation(t)
            elif text == "C":
                cmd = self.clear
            elif text == "=":
                cmd = self.calculer
            elif text in {"sin", "cos", "tan", "√"}:
                cmd = lambda t=text: self.ajouter_fonction(t)

            bouton = ttk.Button(self, text=text, command=cmd)
            bouton.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)

    def ajouter_chiffre(self, chiffre):
        # Ajoute le chiffre à l'affichage de la calculatrice
        self.resultat.set(self.resultat.get() + chiffre)

    def ajouter_operation(self, operation):
        # Ajoute l'opération à l'affichage de la calculatrice
        self.resultat.set(self.resultat.get() + operation)

    def ajouter_fonction(self, fonction):
        # Ajoute la fonction mathématique à l'affichage de la calculatrice
        self.resultat.set(fonction + "(" + self.resultat.get() + ")")

    def clear(self):
        # Efface l'affichage de la calculatrice
        self.resultat.set("")

    def calculer(self):
        try:
            # Récupère l'expression de l'affichage
            expression = self.resultat.get()
            # Remplace les symboles spéciaux par les opérations Python appropriées
            expression = expression.replace("√", "sqrt")
            expression = expression.replace("^", "**")
            # Calcule le résultat de l'expression
            resultat_final = eval(expression, {"__builtins__": None}, {"sin": math.sin, "cos": math.cos, "tan": math.tan, "sqrt": math.sqrt, "pi": math.pi, "e": math.e})
            # Met à jour l'affichage avec le résultat
            self.resultat.set(resultat_final)

             # Ajoute l'expression et le résultat à l'historique
            self.historique.ajouter((expression, resultat_final))

        except Exception as e:
            # Affiche un message d'erreur en cas de problème avec l'expression
            self.resultat.set("Erreur")
