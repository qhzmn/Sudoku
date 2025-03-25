# Sudoku Solver
Résolveur de Sudoku en Python

## Description :

Ce projet propose une implémentation Python pour résoudre un puzzle de Sudoku. La méthode s'appuie sur une analyse logique pour déterminer les valeurs possibles pour chaque case vide en tenant compte des contraintes suivantes :
-  Chaque ligne doit contenir des chiffres uniques de 1 à 9.
-  Chaque colonne doit contenir des chiffres uniques de 1 à 9.
-  Chaque sous-grille 3×3 doit contenir des chiffres uniques de 1 à 9.

## Fonctionnalités principales :
-  Affichage de la grille : Affiche la grille initiale et la grille résolue.
-  Validation des mouvements : Vérifie les valeurs possibles pour une case donnée en fonction des lignes, colonnes, et sous-grilles.
-  Résolution automatique : Remplit la grille de manière logique en excluant les valeurs invalides.

## Améliorations possibles :
-  Interface Graphique : Ajouter une interface graphique pour résoudre les grilles de manière interactive.
-  Algorithme de Backtracking : Implémenter un solveur basé sur la recherche et le retour en arrière pour résoudre des grilles plus complexes.
-  Validation Initiale : Valider la grille avant la résolution pour garantir qu'elle est solvable.
