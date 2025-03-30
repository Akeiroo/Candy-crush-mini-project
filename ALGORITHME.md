# Algorithme du Jeu Candy Crush

# Algorithme principal du jeu Candy Crush

## Initialisation

1. **Créer la grille** (génération aléatoire de bonbons)
   - Appel de la fonction : `creer_grille(n)`
   
2. Tant que la **vérification de la grille possible** est fausse :
   - Appel de la fonction : `verification_grille_possible(grille)`
   - Appel de la fonction : `detecte_coordonnees_combinaisons(grille, i, j)`
   - Remplacer les bonbons de la combinaison
     - Appel de la fonction : `remplacement(grille, liste)`
   
3. **Afficher la grille**
   - Appel de la fonction : `affichage_grille(grille, nb_type_bonbons)`
   
4. **Afficher le score du joueur**
   - Appel de la fonction : `maj_score_joueur(score, combinaison)`

---

## Boucle - Tour du joueur

1. Si des **combinaisons sont possibles** :
   - Demander un échange de bonbons au joueur.
   - Vérifier que l'échange est possible :
     - Appel de la fonction : `combinaisons_possible(grille, candy_a, candy_b)`
     - Si l'échange **n'est pas possible** :
       - Demander de nouvelles coordonnées au joueur.
     
     - Si l'échange **est possible** :
       - Permuter les bonbons dans la grille :
         - Appel de la fonction : `executer_changement(grille, candy_a, candy_b)`
       - Afficher la grille mise à jour :
         - Appel de la fonction : `affichage_grille(grille, nb_type_bonbons)`
   
2. **Boucle** tant qu'il y a des **combinaisons à supprimer** :
   - Détecter les 3 bonbons alignés (combinaison de 3) :
     - Appel de la fonction : `detecte_coordonnees_combinaisons(grille, i, j)`
   - Afficher la grille après suppression des bonbons :
     - Appel de la fonction : `affichage_grille(grille, nb_type_bonbons)`
   
3. **Mettre à jour le score du joueur** :
   - Appel de la fonction : `maj_score_joueur(score, combinaison)`

4. **Remplacer les bonbons supprimés par des cases vides** :
   - Appel de la fonction : `remplacement(grille, liste)`
   
5. **Remplir les cases vides avec des bonbons du dessus** :
   - Appel de la fonction : `remplissage(grille)`
   - Afficher la grille après remplissage :
     - Appel de la fonction : `affichage_grille(grille, nb_type_bonbons)`

6. **Remplir les cases vides de manière aléatoire** :
   - Appel de la fonction : `remplissage(grille)`

7. **Détecter les combinaisons de bonbons** :
   - Appel de la fonction : `detecte_coordonnees_combinaisons(grille, i, j)`
   
8. Tant qu'il y a des **combinaisons détectées** :
   - Remplir les cases vides de manière aléatoire :
     - Appel de la fonction : `remplissage(grille)`
   - Détecter les combinaisons de bonbons :
     - Appel de la fonction : `detecte_coordonnees_combinaisons(grille, i, j)`
   - Afficher la grille après chaque mise à jour :
     - Appel de la fonction : `affichage_grille(grille, nb_type_bonbons)`
