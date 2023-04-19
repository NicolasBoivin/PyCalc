from noeud import Noeud
class ListeDoublementChainee:
    def __init__(self):
        self.tete = None             # Pointeur vers le premier nœud de la liste
        self.queue = None            # Pointeur vers le dernier nœud de la liste

    def ajouter(self, valeur):
        # Crée un nouveau nœud avec la valeur donnée
        nouveau_noeud = Noeud(valeur)
        # Vérifie si la liste est vide
        if not self.tete:
            self.tete = nouveau_noeud
            self.queue = nouveau_noeud
        else:
            # Ajoute le nouveau nœud à la fin de la liste
            nouveau_noeud.precedent = self.queue
            self.queue.suivant = nouveau_noeud
            self.queue = nouveau_noeud

    def afficher(self):
        # Parcours et affichage des nœuds de la liste
        noeud_courant = self.tete
        while noeud_courant:
            print(noeud_courant.valeur, end=" <-> ")
            noeud_courant = noeud_courant.suivant
        print("None")