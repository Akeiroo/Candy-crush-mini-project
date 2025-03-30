# Algorithme du Jeu Candy Crush

# Initialisation

1. **Créer la grille** (génération aléatoire de bonbons)  
   Appel de la fonction : `creer_grille()`  
   
2. Tant que la **vérification de la grille possible** est fausse :  
   - Appel de la fonction : `verification_grille_possible(grille)`
   - Appel de la fonction : `detecte_coordonnees_3_combinaisons(grille)`
   - Appel de la fonction : `remplacer_3_bonbons(grille)`
   
3. **Afficher la grille**  
   Appel de la fonction : `afficher_grille(grille)`
   
4. **Afficher le score du joueur**  
   Appel de la fonction : `afficher_score_joueur()`

---

# Boucle - Tour du joueur

1. Si des combinaisons sont possibles :  
   - Demander un échange de bonbons au joueur.
   - Vérifier que l'échange est possible :  
     Appel de la fonction : `verifier_echange_possible(grille, candy_a, candy_b)`
     
     - Si l'échange est **impossible** :  
       Demander à l'utilisateur d'entrer d'autres coordonnées.
       
     - Si l'échange est **possible** :  
       Appel de la fonction : `executer_changement(grille, candy_a, candy_b)`
       Afficher la grille mise à jour  
       Appel de la fonction : `afficher_grille(grille)`
       
2. Boucle tant qu'il y a des **combinaisons à supprimer** :  
   - Détecter les 3 bonbons alignés (combinaison de 3)  
     Appel de la fonction : `detecte_3_combinaisons(grille)`  
   - Afficher la grille après la suppression des bonbons  
     Appel de la fonction : `afficher_grille(grille)`
   
3. **Mettre à jour le score du joueur**  
   Appel de la fonction : `mise_a_jour_score()`  

4. Remplacer les bonbons supprimés par des **cases vides**  
   Appel de la fonction : `remplacement_bonbons(grille)`
   
5. **Remplir les cases vides avec des bonbons du dessus**  
   Appel de la fonction : `remplir_cases_vides(grille)`  
   Afficher la grille après remplissage  
   Appel de la fonction : `afficher_grille(grille)`

6. **Remplir les cases vides de manière aléatoire**  
   Appel de la fonction : `remplissage_aleatoire(grille)`  

7. **Détecter les combinaisons de bonbons**  
   Appel de la fonction : `detecte_combinaisons(grille)`  
   
8. Tant qu'il y a des **combinaisons détectées** :  
   - Remplir les cases vides de manière aléatoire  
     Appel de la fonction : `remplissage_aleatoire(grille)`
   - Détecter les combinaisons de bonbons  
     Appel de la fonction : `detecte_combinaisons(grille)`  
   - Afficher la grille après chaque mise à jour  
     Appel de la fonction : `afficher_grille(grille)`
