# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Exercice 1 : Classification Stocks Medicaments
# Utilise les notions de S2 (variables, types, operateurs, f-strings)
# + S3 (if/elif/else, conditions composees)
# ============================================================
# --- DONNEES S2 : Variables medicaments --
# (Reimporter depuis sante_variables.py ou redeclarer ici)
m1_nom            = 'Artemether-Lumefantrine'
m1_stock          = 3200
m1_seuil_rupture  = 2000
m1_cout_unitaire  = 3500.0   # FCFA
m2_nom            = 'Amoxicilline 500mg'
m2_stock          = 950
m2_seuil_rupture  = 800
m2_cout_unitaire  = 850.0
m3_nom            = 'Paracetamol 500mg'
m3_stock          = 12400
m3_seuil_rupture  = 3000
m3_cout_unitaire  = 120.0
m4_nom            = 'SRO (sachets)'
m4_stock          = 4200
m4_seuil_rupture  = 5000
m4_cout_unitaire  = 125.0
m5_nom            = 'Vaccin DTP-HepB-Hib'
m5_stock          = 820
m5_seuil_rupture  = 1000
m5_cout_unitaire  = 8500.0
# --- CLASSIFICATION MEDICAMENT 1 : Artemether-Lumefantrine --
# S3 (nouveau) : if / elif / else
# S2 (reutilise) : operateurs arithmetiques pour calcul des seuils
if m1_stock <= m1_seuil_rupture:
    m1_statut  = 'RUPTURE CRITIQUE'
    m1_couleur = '[ROUGE]'
    m1_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m1_stock <= m1_seuil_rupture * 1.5:
    m1_statut  = ___
    m1_couleur = ___
    m1_action  = ___
elif m1_stock <= m1_seuil_rupture * 2.0:
    m1_statut  = ___
    m1_couleur = ___
    m1_action  = ___
else:
    m1_statut  = ___
    m1_couleur = ___
    m1_action  = ___
# TODO : Reproduire la meme logique pour m2, m3, m4, m5
# (Ne pas copier-coller sans adapter les variables !)
# --- COMPTAGE DES ALERTES --
# S2 (reutilise) : variables numeriques
# S3 (nouveau) : conditions pour compter
nb_ruptures_critiques = 0
nb_alertes_stock      = 0
# TODO : Utiliser des if pour incrementer les compteurs
# Exemple : if m1_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques = 
nb_ruptures_critiques + 1
# --- AFFICHAGE RAPPORT --
# S2 (reutilise) : f-strings structurees
# S3 (nouveau) : statuts et couleurs determines par les conditions
print('=' * 65)
print('  RAPPORT DE STOCK — PHARMACIE NATIONALE D APPROVISIONNEMENT')
print('  Date : 15 janvier 2026')
print('=' * 65)
# TODO : Afficher les 5 medicaments avec leur statut
print(f'  {m1_couleur} {m1_nom}')
print(f'      Stock : {m1_stock} unites | Seuil : {m1_seuil_rupture}')
print(f'      Statut : {m1_statut}')
print(f'      Action : {m1_action}')
print('-' * 65)
# TODO : Afficher le bilan final (compteurs + alerte prioritaire)