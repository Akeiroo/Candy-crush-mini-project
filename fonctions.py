#Code de toutes les fonctions du programme

# Fonctions Obligatoires

def detecte_coordonnée_combinaisons(grille, i, j):
    """
    Renvoie la liste 2D contenant les coordonnées appartenant à la combinaison du bonbon (i,j).
    """

def affichage_grille(grille, nb_type_bonbons):
    """
    Affiche la grille de jeu "grille" contenant au maximum "nb_type_bonbons" couleurs de bonbons différentes.
    
def detecte_coordonnees_combinaisons(grille, i, j):

Paramètres:
    - grille (list): Liste 2D représentant la grille de jeu (carrée).
    - i (int): L'indice de la ligne du bonbon à vérifier.
    - j (int): L'indice de la colonne du bonbon à vérifier.
    
    Retourne:
    - list: Liste des coordonnées de toutes les combinaisons trouvées.
    """
    nb_ligne = len(grille)
    nb_col = len(grille[0])
   
    bonbon = grille[i][j]  # Bonbon à vérifier
    combinaisons = []  # Liste des combinaisons
   
     # Vérification des combinaisons horizontales (vers la droite)
    if j <= nb_col - 3:  # S'assurer qu'il y a suffisamment de colonnes à droite
        if grille[i][j+1] == bonbon and grille[i][j+2] == bonbon:
            combinaisons.append([(i, j), (i, j+1), (i, j+2)])
    
    # Vérification des combinaisons horizontales (vers la gauche)
    if j >= 2:  # S'assurer qu'il y a suffisamment de colonnes à gauche
        if grille[i][j-1] == bonbon and grille[i][j-2] == bonbon:
            combinaisons.append([(i, j), (i, j-1), (i, j-2)])

    # Vérification des combinaisons verticales (vers le bas)
    if i <= nb_ligne - 3:  # S'assurer qu'il y a suffisamment de lignes en dessous
        if grille[i+1][j] == bonbon and grille[i+2][j] == bonbon:
            combinaisons.append([(i, j), (i+1, j), (i+2, j)])

    # Vérification des combinaisons verticales (vers le haut)
    if i >= 2:  # S'assurer qu'il y a suffisamment de lignes au-dessus
        if grille[i-1][j] == bonbon and grille[i-2][j] == bonbon:
            combinaisons.append([(i, j), (i-1, j), (i-2, j)])
    
    return combinaisons  # Retourne la liste des combinaisons trouvées


def test_detecte_coordonnees_combinaisons():
    """
    Teste la fonction detecte_coordonnée_combinaisons_de_3(grille, i, j).
    Pour chaque cas de test, affiche True si le test passe, False sinon.
    """

# 🛠 Fonctions Supplémentaires

def creer_grille(n):
    """
    Crée une grille carrée de taille n sous forme de liste 2D.
    La fonction remplit cette grille avec des valeurs correspondant aux couleurs des différents bonbons.
    
    Renvoie :
    - (liste 2D) : la grille remplie.
    """

def verification_grille_possible(grille):
    """
    Vérifie si au moins une combinaison est possible dans la grille.
    
    Arguments :
    - grille (liste 2D) : la grille de jeu.
    
    Renvoie :
    - (bool) : True si une combinaison est possible, sinon False.
    """

def maj_score_joueur(score, combinaison):
    """
    Met à jour le score du joueur lorsqu'une combinaison est réalisée.
    
    Arguments :
    - score (int) : le score actuel du joueur.
    - combinaison (bool) : indique si une combinaison a été détectée.
    
    Renvoie :
    - (int) : le score mis à jour.
    """

def executer_changement(grille, candy_a, candy_b):
    """
    Permet de permuter la position de deux bonbons dans la grille.
    
    Arguments :
    - grille (liste 2D) : la grille de jeu.
    - candy_a (liste) : coordonnées du premier bonbon.
    - candy_b (liste) : coordonnées du second bonbon.
    
    Renvoie :
    - (liste 2D) : la grille mise à jour après permutation.
    """

def det_case_vide(grille, i, j):
    """
    Renvoie une liste des coordonnées des cases vides (valeur 0) dans la grille.
    """

def remplacement(grille, liste):
    """
    Remplace les cases vides (détectées via detecte_coordonnee_combinaison) par la valeur 0.
    
    Arguments :
    - grille (liste 2D) : la grille de jeu.
    - liste (liste 2D) : coordonnées des cases vides.
    
    Renvoie :
    - (liste 2D) : la grille mise à jour.
    """

def remplissage(grille):
    """
    Remplace toutes les cases vides par des bonbons générés aléatoirement.
    
    Arguments :
    - grille (liste 2D) : la grille de jeu.
    
    Renvoie :
    - (liste 2D) : la grille mise à jour.
    """

def combinaisons_possible(grille, candy_a, candy_b):
    """
    Vérifie si l’échange entre candy_a et candy_b permet de créer une combinaison.
    
    Arguments :
    - grille (liste 2D) : la grille de jeu.
    - candy_a (liste) : coordonnées du premier bonbon.
    - candy_b (liste) : coordonnées du second bonbon.
    
    Renvoie :
    - (bool) : True si une combinaison est possible après l'échange, sinon False.
    """

