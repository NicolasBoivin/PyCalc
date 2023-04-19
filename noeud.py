class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur    # Stocke la valeur du nœud
        self.precedent = None   # Pointeur vers le nœud précédent dans la liste
        self.suivant = None     # Pointeur vers le nœud suivant dans la liste
