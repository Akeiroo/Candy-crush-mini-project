# Algorithme du Jeu Candy Crush

## Initialisation
1. Créer la grille (génération aléatoire de bonbons).
2. Tant que `vérification_grille_possible` est faux :
   - Détecter les coordonnées des combinaisons de 3 bonbons alignés (fonction `detecte_coordonnée_3_combinaisons`).
   - Remplacer les 3 bonbons par des cases vides.

## Affichage Initial
- Afficher la grille.
- Afficher le score du joueur.

---

## Boucle - Tour du joueur

1. Si des combinaisons possibles sont détectées :
   - Demander à l'utilisateur d'échanger deux bonbons.
   - Vérifier que l'échange est possible.
   
2. Si l'échange n'est pas possible :
   - Demander à l'utilisateur d'entrer d'autres coordonnées.
   
3. Sinon :
   - Exécuter l'échange des deux bonbons.
   - Afficher la grille.

4. Tant qu'il y a des combinaisons à supprimer :
   - Détecter une combinaison de 3 bonbons alignés (fonction `detecte_3_combinaison`).
   - Afficher la grille.
   - Mettre à jour le score du joueur.
   - Remplacer les bonbons de la combinaison par des cases vides.

5. Remplir les cases vides avec des bonbons provenant du dessus.

## Vérification et Remplissage
1. Remplir les cases supérieures de manière aléatoire.
2. Détecter si de nouvelles combinaisons de bonbons sont créées après le remplissage.
   
3. Tant que des combinaisons sont détectées :
   - Remplir les cases supérieures de manière aléatoire.
   - Vérifier à nouveau si une combinaison est formée.

## Affichage Final
- Afficher la grille mise à jour.
- Afficher le score final du joueur.
