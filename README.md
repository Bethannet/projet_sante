# Projet Santé Publique — Akieni Academy

Projet data dédié à l'analyse du système de santé publique du Congo (hôpitaux,
médicaments, indicateurs OMS). Le fichier `sante_variables.py` est le module
fondateur : il centralise les constantes métier et les variables de 5 hôpitaux
et 5 médicaments essentiels, réutilisées par tous les scripts du projet. Chaque
semaine apporte de nouvelles fonctionnalités (conditions, fonctions, classes,
puis tables SQL) construites sur cette base commune.

## ⚠️ Fichier cumulatif — pas un fichier par semaine

**`sante_variables.py` est un seul fichier qui s'enrichit chaque semaine.** Il
n'y a pas de fichier "semaine 2" et de fichier "semaine 3" séparés pour ce
module : tout est regroupé au même endroit, et les sections déjà écrites une
semaine ne sont jamais supprimées ni réécrites — on en ajoute simplement de
nouvelles à la suite. Pour savoir quelle semaine a produit quelle partie du
code, voir le tableau ci-dessous.

| Semaine | Sections ajoutées dans `sante_variables.py`  | Repère dans le fichier |
|---------|------------------------------------------------------------------|--------------------------|
| S2      | Constantes nationales, variables des 5 hôpitaux et 5 médicaments, calcul des KPIs, rapport d'inventaire initial | Sections A → E |
| S3      | Classification automatique (statut des stocks, occupation des hôpitaux, couverture vaccinale) et rapport d'état global avec alertes | Sections F → I |

## Exécution

```bash
python sante_variables.py
```

## Mise à jour de ce README

Ce fichier est mis à jour à chaque nouvelle semaine déposée sur le dépôt :
- ajouter une ligne au tableau ci-dessus avec les sections/fichiers de la semaine
- ajouter le nouveau script dans la structure du dépôt si un fichier est créé
- ne jamais supprimer les lignes des semaines précédentes
