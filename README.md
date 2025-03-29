# Candy-crush-mini_project

## Objectif 
Réaliser un jeu candy-crush like

## Cahier des charges du projet
+ La grille de jeu sera représentée par une liste 2D d’entiers. Un bonbon sera donc représenté
  par un entier dans cette grille.
+ Vous devrez choisir un des niveaux de difficulté de la règle du jeu défini dans la section 3
+ Votre code ne devra utiliser aucune autre bibliothèque que la bibliothèque standard de Python
  (pas de Numpy ou Matplotlib par exemple)
+ Votre code ne devra pas faire appel à de la récursivité
+  Votre code devra obligatoirement utiliser les fonctions obligatoires mentionnées dans le fichier **fonctions**


# Définition des Combinaisons et Suppressions

On définit une **combinaison** par au minimum **3 bonbons de même valeur alignés** horizontalement ou verticalement.

La suppression d’une combinaison peut se faire de différentes manières. Nous vous proposons **3 niveaux de difficulté**, tels que :
+ **Niveau 1** : le plus facile à implémenter.
+ **Niveau 3** : le plus difficile à implémenter.

La **Figure 2** illustre les différents niveaux.  
Nous vous conseillons fortement de commencer par **implémenter le niveau 1**, puis de passer aux niveaux supérieurs lorsque les niveaux précédents sont fonctionnels.

---

## 3.1 Niveau 1
Dans ce niveau, on **supprime seulement des combinaisons de 3 bonbons de même valeur** alignés verticalement ou horizontalement.  

➡️ **Si 4 bonbons sont alignés, seulement 3 sont supprimés.**

---

## 3.2 Niveau 2
Dans ce niveau, on **supprime tous les bonbons de même valeur** qui sont alignés horizontalement ou verticalement, avec un minimum de **3 bonbons**.

---

## 3.3 Niveau 3
Dans ce niveau, **si au moins 3 bonbons sont alignés** (verticalement ou horizontalement), alors :  
✅ On supprime **tous les bonbons de même valeur** qui sont **voisins d’un bonbon supprimé** (l’un des 3 bonbons d’origine, ou un voisin de voisin).
